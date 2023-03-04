import openai
import os

openai.api_key = os.environ['API_KEY']

def gpt_response(user_question):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_question}
        ]
    )
    return response.choices[0].message.content