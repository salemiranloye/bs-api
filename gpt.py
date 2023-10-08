import os
import openai
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
chat_line ="You are a fake news detector. Please evaluate the following news article, and clearly and separately state sources. please keep it in a formated way with if its true or not first. then check for an apperant biases and try to give a percentage of bias"
        


def get_response(prompt):
    # Set your OpenAI API key here
    openai.api_key = os.getenv("openAI")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": chat_line
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the assistant's response
    response_messages = response['choices'][0]['message']['content']

   

    return response_messages



def linkget_response(prompt):
    r = requests.get(prompt)
    soup = BeautifulSoup(r.text, "html.parser")
    prompt = soup.text

    # Set your OpenAI API key here
    openai.api_key = open('API', 'r').read()
          
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": chat_line
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_messages = response['choices'][0]['message']['content']

    return response_messages



