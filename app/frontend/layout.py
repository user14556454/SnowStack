import streamlit as st

def header_section():
    st.title("SMART SIGNBOARD INTERPRETER")
    st.subheader("From the SNOWSTACK team")
    st.divider()


def image_input_section():
    st.subheader("Image Input")

    method = st.selectbox("Choose input method:", ["Upload photo", "Take image"])

    image_bytes = None

    if method == "Upload photo":
        uploaded = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
        if uploaded:
            image_bytes = uploaded.read()
            st.image(image_bytes, caption="Uploaded Image", use_column_width=True)

    else:
        cam = st.camera_input("Take a photo")
        if cam:
            image_bytes = cam.read()
            st.image(image_bytes, caption="Captured Image", use_column_width=True)

    return image_bytes


def preprocessing_preview_section(processed):
    st.subheader("Preprocessing Result")

    st.image(processed["original"], caption="Original")
    st.image(processed["gray"], caption="Grayscale")
    st.image(processed["binary"], caption="Binarized")
    st.image(processed["denoised"], caption="Noise Removed")


def ocr_section(ocr_text):
    st.subheader("OCR Result")

    st.text_area("Extracted Text:", ocr_text, height=150, key="ocr_text_box")


def translation_section():
    st.subheader("Translation")

    target_language = st.selectbox(
        "Select Target Language",
        ["en", "hi", "mr", "ta", "te", "ml", "gu", "bn", "kn", "pa", "ur", "fr", "es", "de", "zh-cn"],
        index=0,
        key="language_selector"
    )

    if st.button("Translate"):
        return target_language

    return None


def translation_output_section(translated_text):
    st.text_area("Translated Output", translated_text, height=150, key="translated_text_box")
