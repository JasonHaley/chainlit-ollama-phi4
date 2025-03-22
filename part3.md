# Create a Chainlit Application to Chat with a PDF File

## Create another chainlit app
In this section you will create another Chainlit app that will allow you to upload a PDF file and interact with it.

1. In the start folder, open the **rag.py** file
2. On line 24, replace the # TODO with the following code:

```
@cl.on_chat_start
async def on_chat_start():
    files = None

    # Wait for the user to upload a file
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a pdf file to begin!",
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]

    msg = cl.Message(content=f"Processing `{file.name}`...")
    await msg.send()
    
    pdf = PyPDF2.PdfReader(file.path)
    pdf_text = ""
    for page in pdf.pages:
        pdf_text += page.extract_text()
        

    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_text(pdf_text)

    # Create a metadata for each chunk
    metadatas = [{"source": f"{i}"} for i in range(len(texts))]

    # Create a Chroma vector store
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    docsearch = await cl.make_async(Chroma.from_texts)(
        texts, embeddings, metadatas=metadatas
    )

    message_history = ChatMessageHistory()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )

    # Create a chain that uses the Chroma vector store
    chain = ConversationalRetrievalChain.from_llm(
        ChatOllama(model="phi4-mini"),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        memory=memory,
        return_source_documents=True,
    )

    # Let the user know that the system is ready
    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()

    cl.user_session.set("chain", chain)
```
As you can see, this on_chat_start handler does more than the last one. This one does the following things:
* takes an uploaded file from the user
* puts a "Publishing" message on the page
* opens the PDF and extracts the text  
* chunks the text into pieces
* loads into a Chroma db and also creates the embeddings for the chunks
* prepares a chain to use when the user enters a message

3. On line 86, paste the following code:

```
@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")  # type: ConversationalRetrievalChain
    cb = cl.AsyncLangchainCallbackHandler()

    res = await chain.ainvoke(message.content, callbacks=[cb])
    answer = res["answer"]
    source_documents = res["source_documents"]  # type: List[Document]

    text_elements = []  # type: List[cl.Text]

    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            # Create the text element referenced in the message
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name, display="side")
            )
        source_names = [text_el.name for text_el in text_elements]

        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"
        else:
            answer += "\nNo sources found"

    await cl.Message(content=answer, elements=text_elements).send()
```
This is the code that runs when a user enters a message, it uses the chain that was initialize earlier when the PDF file was uploaded. This is a RAG chain, it will run a similarity search on the chunks of the PDF and find the relevant pieces to then send to Phi4 with the user's message in order to answer the question.

Next let's run it!

4. In the terminal, type the following in order to have the chainlit application start up:

```
chainlit run rag.py
```

Now you can play with it. There is a pdf in the root of this repo (**phi4-technical-report.pdf**) you can use if you don't have your own PDF to test with.

After loading the file, try asking it some questions about the contents.