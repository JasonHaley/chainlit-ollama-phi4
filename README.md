# Build a Chainlit App using Ollama and Phi 4

This short hands on lab explores how to quickly create a web application to interact with a LLM using [Chainlit](https://docs.chainlit.io/get-started/overview). Instead of using OpenAI or Azure AI Foundry, we will use [Ollama](https://ollama.com/) to serve [Phi 4-mini](https://techcommunity.microsoft.com/blog/educatordeveloperblog/welcome-to-the-new-phi-4-models---microsoft-phi-4-mini--phi-4-multimodal/4386037) locally.

## Running Models Locally

If you have used [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/) or [Gemini](https://gemini.google.com/app), you are accessing the LLM over the internet which is running in a data center some where in the world on another company's hardware - which is under their control. When you **run (or host) a model locally** you are running it on your hardware. That hardware is in your control, it could be your laptop or it could be your own data center (or Azure tenant).

Like with Cloud computing's spectrum of control, we now have a new one for hosting AI models (from least control to most):

 * **External Service/Website/API hosted by the model created** - OpenAI's Chat GPT is an an example of this
 * **Models hosted by third parties** - Azure OpenAI is an example of this
 * **Models as a service** - Azure AI Foundry will provide you many models as a service
 * **Models hosted or controlled by you** - This is what we are going to focus on

### Ollama

[Ollama](https://ollama.com/) is an [open-source tool](https://github.com/ollama/ollama) designed to run AI models locally on your machine. For those of you familiar with using [docker](https://www.docker.com/) for running services locally, using Ollama to run (or serve) models will feel familiar. It can be run on macOS, Linux and Windows.

### Phi 4 

The [Phi 4 models](https://azure.microsoft.com/en-us/products/phi/) are a family of Small Language Models (SLMs) designed to deliver high performance inference that is lightweight and resource-efficient. One differentiation of the models are how they have been trained on a curated dataset. The data was more textbook-like material to help the models learn complex language and understanding - which is a different approach than the LLMs that were trained on all the scraped data they could get from the internet. The latest releases of the Phi 4 family were the [Phi 4 multimodal and Phi-4-mini](https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/)

### Chainlit

[Chainlit](https://github.com/Chainlit/chainlit) is an open source python conversational AI web application framework. It allows you to create a web application that can interact with an LLM in a mater of minutes.

## Prerequisites
* Experience with Python is helpful
* Modern hardware (performance of the models will depend on your memory and CPU)
* Ability to install services on your machine

## What you will need
* VS Code
* Python and pip (can have use the VS Code extension)
* Git installed


## Learning Objectives
1. Install the necessary tools to run AI models locally
2. Create a web application to interact with a locally running SLM
3. Create a Chainlit application to chat with a PDF document

## [Next: Setup your local machine](./part1.md)