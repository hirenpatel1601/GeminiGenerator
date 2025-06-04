import streamlit as st 
import google.generativeai as genai 
from dotenv import load_dotenv 
load_dotenv()
genai.configure(api_key="GOOGLE_API_KEY")

st.title("The Professor's Academy Assistant")
st.header("Give Me Detail. i will create an image for you!")