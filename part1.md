# Setup your machine

In this part we will get the things you need to run models installed.

## Install Ollama

This section walks through getting the Ollama service downloaded and installed on you machine in order to run the models locally.

1. In a browser, navigate to: [https://ollama.com/download](https://ollama.com/download) and click the operating system you have and then the Download button.
2. Next once the installer is downloaded (be patient we have several people doing this at one time - it may not be fast), run the installer.

Now we need to verify it is installed and running.

3. Open a command line (if you don't already have one open) and run the following command:

```
ollama list
```

You should see some headings but an empty list.

## Download Phi 4 Mini

This section walks through getting the Phi 4 Mini model downloaded to use with Chainlit later.

1. Open a command line (if you don't already have one open)
2. Type the following in the command line:

```
ollama run phi4-mini 
```
> NOTE: once the model has been run once, you can just use the serve command to make it available next time you want to use it

## Download Nomic Embed Text

[nomic-embed-text]( https://ollama.com/library/nomic-embed-text) is a high-performing open embedding model with a large token context window (8,192). [Introducing Nomic Embed: A Truly Open Embedding Model](https://www.nomic.ai/blog/posts/nomic-embed-text-v1) is a good explanation of the motivations behind the model and its details.

This section walks through getting an embedding model downloaded to use in the RAG exercise later.

1. Open a command line (if you don't already have one open)
2. Type the following in the command line:

```
ollama pull nomic-embed-text 
```

> NOTE: with embedding models you use the command pull instead of run

## [Next: Create a Chainlit Application to Chat with Phi 4](./part2.md)