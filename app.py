# Import necessary libraries

import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_contents

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
model="gemini-2.5-flash-lite"

# Function to create messages for the Gemini model
def get_messages(url):
    system_prompt=("You are a helpful assistant that summarizes website content into concise bullet points."
                  "Include relevant links like About, Careers, and Products if found.")
    website_contents=fetch_website_contents(url)
    user_prompt=f"This is the content of the website {website_contents}, summarize into concise bullet points"
    return [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

# Function to stream Gemini model responses
def stream_gemini(url):
    messages=get_messages(url)
    stream=gemini.chat.completions.create(messages=messages, model=model, stream=True)
    result=""
    for chunk in stream:
        result+=chunk.choices[0].delta.content or ""
        yield result

# Gradio interface setup
message_input=gr.Textbox(label="Enter Website URL")
message_output=gr.Markdown(label="Summary")
view=gr.Interface(fn=stream_gemini, inputs=[message_input], outputs=[message_output],
                  title="WebBriefAI", examples=["https://huggingface.co"],
                  flagging_mode="never")


# Entry point for the application
if __name__ == "__main__":
    view.launch(auth=("Krish", "0801"))







