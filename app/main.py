import streamlit as st
from frontend.styling import apply_custom_styles

from frontend.layout import (
    header_section,
    image_input_section,
    preprocessing_preview_section,
    ocr_section,
    translation_section,
    translation_output_section
)

from backend.preprocessing import run_preprocessing
from backend.ocr import perform_ocr
from backend.translator import translate_text


def main():
    st.set_page_config(layout="wide")
    apply_custom_styles
    header_section()

    image_bytes = image_input_section()

    if image_bytes:
        processed = run_preprocessing(image_bytes)
        preprocessing_preview_section(processed)

        ocr_text = perform_ocr(processed["denoised"])
        st.session_state["ocr_text"] = ocr_text
        ocr_section(ocr_text)

        target_lang = translation_section()
        if target_lang:
            translated_output = translate_text(ocr_text, target_lang)
            translation_output_section(translated_output)


if __name__ == "__main__":
    main()
