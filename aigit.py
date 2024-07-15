
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
import json
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]



def generate_html_from_json(response_dict):
    #command_explain = response_dict.get('explanation', 'No Explanation')

    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
            }}
            .title {{
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }}
            .explanation {{
                font-size: 18px;
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .explanation h3 {{
                font-size: 24px;
                margin-top: 20px;
            }}
            .explanation ul {{
                margin: 0;
                padding-left: 20px;
            }}
            .explanation li {{
                margin-bottom: 10px;
            }}
            .explanation code {{
                background-color: #eee;
                padding: 2px 4px;
                border-radius: 4px;
                font-size: 16px;
            }}
            .explanation .section {{
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="explanation">
                <div class="section">
                    {command_explain}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content



llm = OpenAI(temperature=0.9) 


template = PromptTemplate(
    input_variables = ['command'],
    template = "give an explinatiom of this git command: {command}"
  )

llm_chain = template | llm

commandinput = st.text_input("Insert command")

if 'outputs' not in st.session_state:
    st.session_state['outputs'] = []

def buttonTrue(commandinput):
    res = llm_chain.invoke({"command": commandinput})
    st.session_state.outputs.append((commandinput, res))
    st.write(res)


if st.button('Run!'):
    if commandinput: 
        st.write(f"command: {commandinput}")
        buttonTrue(commandinput)


if st.session_state['outputs']:
    st.write("### Previous Outputs")
    for idx, (command, output) in enumerate(st.session_state.outputs):
        st.write(f"**Command {idx + 1}:** `{command}`")
        st.write(f"**Explanation:** {output}")
