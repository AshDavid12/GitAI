# Git Command Explainer

This project provides a Streamlit web application that explains Git commands using OpenAI's language model. Users can input a Git command, and the application will generate a detailed explanation of the command.

## Features

**Input Git Commands**: Users can input any Git command to get an explanation.  
**Generated Explanations**: The application uses OpenAI's language model to generate comprehensive explanations.  
**History of Commands**: The application keeps track of previously entered commands and their explanations.  


## Main Components
**Environment Setup**: Loads the OpenAI API key from Streamlit secrets or a .env file.  
**Streamlit Application**: Provides a web interface for inputting commands and displaying explanations.  
**LangChain Integration**: Uses the LangChain library to create a prompt template and generate explanations from the OpenAI model.  


## Installation

To run this project locally, follow these steps:  

### Clone the repository:  
```
git clone https://github.com/yourusername/GitAI.git  
cd GitAI
```  
### Install Poetry: 

If you don't have Poetry installed, you can install it by following the instructions here.  
Install the dependencies:`poetry install`  
### Set up environment variables:  
Create a .env file in the root directory of the project and add your OpenAI API key:
```OPENAI_API_KEY=your_openai_api_key```  
### Run the application:  
```poetry run streamlit run app.py```
