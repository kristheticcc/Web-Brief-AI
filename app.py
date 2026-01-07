# Import necessary libraries

import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_contents
from IPython.display import display, Markdown

# Load environment variables, and Api key setup
load_dotenv(override=True)
google_key=os.getenv("GOOGLE_API_KEY")

# Check if the API key is loaded
if not google_key:
    raise ValueError("GOOGLE_API_KEY not found!!!")
elif not google_key.startswith("AIzaSy"):
    raise ValueError("GOOGLE_API_KEY does not seem to be valid!!!")
else:
    print("GOOGLE_API_KEY loaded successfully.")

# Setting up the client
base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
gemini=OpenAI(base_url=base_url, api_key=google_key)

def get_messages(url):
    system_prompt=("You are a helpful assistant that summarizes website content into concise bullet points."
                  "You also generates a list of relevant links such as About, Careers, and Product or Service pages"
                  "if available.")
    website_contents=fetch_website_contents(url)
    user_prompt="This is the content of the website I want you to summarize into concise bullet points: {website_contents}"
    return [{"system": system_prompt}, {"user": user_prompt}]





