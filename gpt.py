import os
import openai

def get_response(prompt):
# Set your OpenAI API key here
    openai.api_key = "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"
    chat_line ="You are a fake news detector. Please evaluate the following news article, and clearly and separately state sources."
        
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

    # Print the assistant's response
    responeMain = response['choices'][0]['message']['content']
    return responeMain
