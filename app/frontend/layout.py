import streamlit as st

def header_section():
    st.title("SMART SIGNBOARD INTERPRETER")
    st.subheader("From the SNOWSTACK team")
    st.divider()

def image_input_section():
    user = st.selectbox("How will you upload the image?",["Upload photo","Take image"])

    if user == "Upload photo":
        st.subheader("Upload your image (or) Take photo")
        uploaded_files = st.file_uploader("",type=['png','jpg','jpeg'])
        if uploaded_files:
            st.write(f"The photo has been successfully uploaded")
        else:
            st.write("Please upload the photo from above.")

    else:
        st.subheader("Take Photo")
        uploaded_camera = st.camera_input("")
        if uploaded_camera:
            st.image(uploaded_camera, caption="Captured image", use_column_width=True)


