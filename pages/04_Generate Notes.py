import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key="AIzaSyDzhNYAdbkqaIM9Kfpr3zKUWKNXhTgm5G8")
#genai.configure(api_key="GOOGLE_API_KEY")

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    response = model.generate_content(prompt)
    return response.text


st.title("The Professor's Academy Assistant")
st.header("Send Me Topic Name Along With class and i will create notes for you!")

userprompt = st.text_area("Enter your Topic here:", key="prompt")
submitbtn = st.button("Get Answer")

if submitbtn and userprompt.strip():
    st.info("Notes is getting generated it will take few seconds...")
    response = get_gemini_response(f"Act like professor and create notes on {userprompt} with proper headings and subheadings. Make it easy to understand for students with examples if possible add emojies for intrest also and concise.")
    st.subheader("Your Answer:")
    st.write(response)
