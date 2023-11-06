import openai
import os
import re
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

openai.api_key = os.environ.get('API_KEY')

def getRhyme(headline):
    prompt = f"Generate mini Rhyme based on the headline: '{headline}'"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None
    )
    print(response)
    generated_text = response.choices[0].text
    return generated_text