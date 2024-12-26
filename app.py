from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define helper functions
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Define input prompt
input_prompt = """
You are an expert nutritionist. Analyze the food items from the image
and calculate the total calories. Also, provide the calories for each food item in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories
---
---
"""

# Streamlit setup
st.set_page_config(page_title="AI Nutritionist App")
st.header("AI Nutritionist App")

# User inputs
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to trigger processing
submit = st.button("Tell me the total calories")

if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input_text)
        st.subheader("The Response is")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")
