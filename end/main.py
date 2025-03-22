from langchain_ollama import ChatOllama, OllamaLLM
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
import chainlit as cl

def load_model():
    llm = OllamaLLM(
        model="phi4-mini",
        verbose=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
    return llm

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