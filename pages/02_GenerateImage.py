import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from io import BytesIO
from PIL import Image
import streamlit as st

load_dotenv()

os.environ["GOOGLE_API_KEY"] = "AIzaSyDzhNYAdbkqaIM9Kfpr3zKUWKNXhTgm5G8"
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

st.title("The Professor's Academy Assistant")
st.header("Give Me Detail. i will create an image for you!")
prompt = st.text_area("Enter your question here:", key="prompt")
#prompt="boy enjoying evening with fathr at beach, sunset, father and son, happy, warm colors, realistic style, high detail, 4k resolution"
submitbtn = st.button("Get Answer")

if submitbtn and prompt.strip():
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",  # Updated model name
        contents=prompt,  # Changed from 'content' to 'contents'
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"]  # Fixed parameter name and values
        )
    )

    for idx, part in enumerate(response.candidates[0].content.parts):
        if part.text:
            st.write(part.text)
        elif part.inline_data and part.inline_data.data:
            image_bytes = part.inline_data.data
            image = Image.open(BytesIO(image_bytes))
            outfile = f"generated_image_{idx}.png"
            image.save(outfile)
            st.image(outfile, caption=f"Generated Image {idx + 1}")
            #image.show()  # Uncomment if you want to display the image in a separate window
    
   




    # # if not api_key:
    # #     raiese ValueError("GOOGLE_API_KEY is not set in the environment variables.")

    # client =genai.Client(api_key=api_key)
    # prompt = st.text_area("Enter your question here:", key="prompt")

    # response = client.models.generate_content(
    #     model="gemini-2.0-flash-preview-image-generation",
    #     content=prompt,
    #     config=types.GenerationConfig( 
    #         response_modality = ["Text", "Image"],
    #     ),
    
    # )


    # for idx, part in enumerate(response.candidates[0].content.parts):
    #     if part.text:
    #         print("text",part.text)
    #     elif part.inline_data and part.inline_data.data:
    #         image_bytes = part.inline_data.data
    #         image = Image.open(BytesIO(image_bytes))
    #         outfile = f"generated_image_{idx}.png"
    #         image.save(outfile)
    #         st.image(outfile, caption=f"Generated Image {idx + 1}")
    #         image.show()