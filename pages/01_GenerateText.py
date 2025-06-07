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
st.header("Ask me anything I Will help you with your studies!")

userprompt = st.text_area("Enter your question here:", key="prompt")
submitbtn = st.button("Get Answer")

if submitbtn and userprompt.strip():
    response = get_gemini_response(userprompt)
    st.subheader("Your Answer:")
    st.write(response)
