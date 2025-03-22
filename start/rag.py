from langchain_ollama import ChatOllama, OllamaLLM, OllamaEmbeddings
from langchain.callbacks.manager import CallbackManager
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import (
    ConversationalRetrievalChain,
)
from typing import cast
import PyPDF2
import chainlit as cl

def load_model():
    llm = OllamaLLM(
        model="phi4-mini",
        verbose=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
    return llm

# TODO: create the chat start handler

# TODO: create the on message handler
