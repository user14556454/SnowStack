
import streamlit as st
from frontend.layout import header_section, image_input_section, preprocessing_preview_section, ocr_section
from backend.preprocessing import run_preprocessing

def main():
    header_section()
    image_bytes = image_input_section()   

    if image_bytes:
        st.write("code is runing")
        processed = run_preprocessing(image_bytes)
        preprocessing_preview_section(processed)
        ocr_section(processed["denoised"])

if __name__ == "__main__":
    main()
