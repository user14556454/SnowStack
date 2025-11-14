import streamlit as st


st.title("SMART SIGNBOARD INTERPRETER")
st.subheader("From the SNOWSTACK team")
st.divider()


user = st.selectbox("How will you upload the image?",["Upload photo","Take image"])

if user == "Upload photo":
    st.subheader("Upload your image (or) Take photo")
    uploaded_files = st.file_uploader("",type=['png','jpg','jpeg'])
    if uploaded_files:
        st.write(f"The photo has been successfully uploaded")
        image_bytes = uploaded_files.read()
        st.image(image_bytes,caption="Captured image", use_column_width=True)
    else:
        st.write("Please upload the photo from above.")

else:
    st.subheader("Take Photo")
    uploaded_camera = st.camera_input("")
    if uploaded_camera:
        image_bytes = uploaded_camera.read()
        st.image(image_bytes, caption="Captured image", use_column_width=True)

# from backend.preprocessing import run_preprocessing

# def preprocessing_preview_section(processed):
#     st.subheader("Preprocessing Output")

#     st.image(processed["original"], caption="Original")
#     st.image(processed["gray"], caption="Grayscale")
#     st.image(processed["binary"], caption="Binarized")
#     st.image(processed["denoised"], caption="Noise Removed")

# from backend.ocr import perform_ocr

# def ocr_section(image_bytes):
#     st.subheader("OCR Result")

#     if st.button("Extract Text"):
#         result = perform_ocr(image_bytes)
#         st.text_area("Extracted Text:", result, height=200)
