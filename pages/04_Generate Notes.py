import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()
genai.configure(api_key="AIzaSyDzhNYAdbkqaIM9Kfpr3zKUWKNXhTgm5G8")
#genai.configure(api_key="GOOGLE_API_KEY")

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    response = model.generate_content(prompt)
    return response.text


st.title("The Professor's Academy Assistant")
st.header("Send me topic name and i will create notes for you!")
st.info("like Semiconductor physics for class 12 maharshtra board, or Computer science for class 10 cbse board, etc. Be specific with your topic and class to get better results.")
#st.info("like Semiconductor physics for class 12 maharshtra board, or Computer science for class 10 cbse board, etc. Be specific with your topic and class to get better results.")

userprompt = st.text_area("Enter your Topic here:", key="prompt")
submitbtn = st.button("Get Answer")

if submitbtn and userprompt.strip():
    st.info("Notes is getting generated it will take few seconds...")
    response = get_gemini_response(f"Act like professor and create notes on {userprompt} with proper headings must have notes from The Professor's Academy  and subheadings. Make it easy to understand for students with examples if possible add emojies for intrest also and concise. and create 5-10 important questions at the end of notes for students to practice. Make it easy to understand for students with examples if possible add emojies for intrest also and concise.")
   

    


    st.subheader("Your Answer:")
    
    st.write(response)
