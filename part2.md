# Create a Chainlit Application to Chat with Phi 4

## Get the code

In this section we will get the starter code from GitHub and create the first Chainlit app to interact with the Phi 4 model.

1. If you haven't already cloned the repository, go to the GitHub repo [https://github.com/JasonHaley/chainlit-ollama-phi4](https://github.com/JasonHaley/chainlit-ollama-phi4), click on the **Code dropdown** button and click **copy url to clipboard** button.
2. On your machine, you'll need a directory to put the code in. Open a console window and navigate to where you want to put the code. The run the following command:

```
git clone https://github.com/JasonHaley/chainlit-ollama-phi4.git
```

3. Once the code has downloaded, run the following in order to open it in VS Code:
```
cd chainlit-ollama-phi4
code .
```
This will open VS Code with the directory loaded. Look open the **/start** folder.

4. Once you have opened the **start** folder, go to the **Terminal menu** -> **New Terminal** 

5. Create a virtual environment, by running the following command:

```
python -m venv venv
```

Once that completes you will need to activate it by running:

On windows:
```
.\venv\scripts\activate
```

Linux/Mac
```
source ./venv/bin/activate
```

6. Next you need to install the requirements, by running the following:

```
pip install -r requirements.txt
```
This will take a few minutes, be patient.

## Create and run the code

In this section you will add the code to the main.py file to create the Chainlit application and see how easy it is to get it running with Phi 4.

1. In the start folder, open the **main.py** file
2. On line 10, replace the # TODO with the following code:
```
def load_model():
    llm = OllamaLLM(
        model="phi4-mini",
        verbose=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
    return llm
```
This code is a utlity method that initializes the code needed to interact with Phi 4 mini using Ollama.

3. On line 18, replace the # TODO line with the following code:
```
@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Learning Generative AI",
            message="Can you help me create a personalized learning plan to learn Generative AI? Start by asking me about my current knowledge and experience.",
            ),

        cl.Starter(
            label="Explain Generative AI",
            message="Explain Generative AI like I am a high school student.",
            ),
        cl.Starter(
            label="Python script for daily AI topics email",
            message="Write a script to automate sending daily email reports about AI in Python, and walk me through how I would set it up."
            ),
        ]
```
This is a list of default prompts that will show as buttons on the page when we run the application. Feel free to change the prompts to something you want to use instead of using these.

Chainlit applications are python application and are driven by a few event handlers.

4. On line 36, replace the # TODO line with the following code:
```
@cl.on_chat_start
async def on_chat_start():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a helpful assistant who provides accurate and eloquent answers to questions.",
            ),
            ("human", "{question}"),
        ]
    )
    model = load_model()
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)
```
This is the logic that is going to run when the chat starts up. As you can see, it initializes the prompt template that will be use when the user types a message.

5. On line 51, replace the # TODO line with the following code:

```
@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")

    msg = cl.Message(content="")

    for chunk in await cl.make_async(runnable.stream)(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
```
This is the code that will use the prompt template that was initialized in the on_chat_start and use the user's message to pass off to the Ollama/Phi 4 model and then stream the results out to the UI.

Next let's run it!

6. In the terminal, type the following in order to have the chainlit application start up:

```
chainlit run main.py
```

Now play with the Chainlit application and ask Phi 4 questions. You may want to start with the starter buttons, but feel free to come up with your own questions.

## [Next: Create a Chainlit Application to Chat with a PDF File](./part3.md)