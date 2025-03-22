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
2. On line 10, past in the following code:
```
def load_model():
    llm = OllamaLLM(
        model="phi4-mini",
        verbose=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
    return llm
```

## [Next: Create a Chainlit Application to Chat with a PDF File](./part3.md)