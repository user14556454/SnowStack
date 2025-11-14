import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.preprocessing import run_preprocessing
from backend.ocr import perform_ocr

def header_section():
    st.title("SMART SIGNBOARD INTERPRETER")
    st.subheader("From the SNOWSTACK team")
    st.divider()

def image_input_section():
    image_bytes = None
    user = st.selectbox("How will you upload the image?", ["Upload photo", "Take image"])

    if user == "Upload photo":
        st.subheader("Upload your image")
        uploaded_file = st.file_uploader("", type=['png','jpg','jpeg'])
        if uploaded_file:
            image_bytes = uploaded_file.read()
            st.image(image_bytes, caption="Uploaded image", use_column_width=True)
    else:
        st.subheader("Take Photo")
        uploaded_camera = st.camera_input("")
        if uploaded_camera:
            image_bytes = uploaded_camera.read()
            st.image(image_bytes, caption="Captured image", use_column_width=True)

    return image_bytes


def preprocessing_preview_section(processed):
    st.subheader("Preprocessing Output")

    st.image(processed["original"], caption="Original")
    st.image(processed["gray"], caption="Grayscale")
    st.image(processed["binary"], caption="Binarized")
    st.image(processed["denoised"], caption="Noise Removed")



def ocr_section(image_bytes):
    st.subheader("OCR Result")

    if st.button("Extract Text"):
        result = perform_ocr(image_bytes)
        st.text_area("Extracted Text:", result, height=200)

def translation_section(extracted_text):
    std