import streamlit as st
import requests
import streamlit.components.v1 as components

GENERATE_CODE_URL = "http://localhost:8000/generate-code"

st.title("Screenshot to Code")

# Initialize session state variables if not already set
if 'generated_code' not in st.session_state:
    st.session_state.generated_code = ""
if 'output_html' not in st.session_state:
    st.session_state.output_html = ""
if 'status' not in st.session_state:
    st.session_state.status = ""
if 'error' not in st.session_state:
    st.session_state.error = ""

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if st.button("Generate Code") and uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(GENERATE_CODE_URL, files=files)
    if response.status_code == 200:
        result_data = response.json()
        st.session_state.generated_code = result_data.get("generated_code", "")
        st.session_state.output_html = result_data.get("output_html", "")
        st.session_state.status = "Code generation complete."
        st.session_state.error = ""
    else:
        st.session_state.error = "Failed to generate code. Please try again."
        st.session_state.status = ""

if st.session_state.generated_code:
    st.subheader("Generated Code")
    st.code(st.session_state.generated_code, language="html")

if st.session_state.output_html:
    st.subheader("Rendered Output")
    components.html(st.session_state.output_html, height=600)

if st.session_state.status:
    st.success(st.session_state.status)
if st.session_state.error:
    st.error(st.session_state.error)
