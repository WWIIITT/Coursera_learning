Setting up your development environment
Before we dive into development, let's set up your project environment in the Cloud IDE. This environment is based on Ubuntu 22.04 and provides all the tools you need to build your AI-driven Flask application.

Step 1: Create your project directory
Open the terminal in Cloud IDE and run:
```
mkdir genai_flask_app
cd genai_flask_app
```
This creates a new directory for your project and navigates into it.

Step 2: Set up a Python virtual environment
Initialize a new Python virtual environment:
```
python3.11 -m venv venv
source venv/bin/activate
```

Step 3: Install the ibm-watsonx-ai library
With your virtual environment activated, install ibm-watsonx-ai via:

```
pip install ibm-watsonx-ai

```

Other libraries:
```
pip install Flask langchain-ibm langchain
```

This command installs ibm-watsonx-ai, which has many watsonx.ai features. In this lab, we use this library to help us configure and call our LLMs.

Now that your environment is set up, you're ready to start building your GenAI application!