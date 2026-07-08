import streamlit as st
from parser.parser import extract_text_from_pdf

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------
st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and we will analyze it step by step."
)

st.divider()

# -----------------------------------
# Resume Upload
# -----------------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)

# -----------------------------------
# Process Uploaded File
# -----------------------------------
if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    st.subheader("File Details")

    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Type:** {uploaded_file.type}")
    st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")

    st.divider()

    # -------------------------------
    # Extract Resume Text
    # -------------------------------
    if uploaded_file.type == "application/pdf":

        st.subheader("📄 Resume Content")

        resume_text = extract_text_from_pdf(uploaded_file)

        st.text_area(
            "Extracted Text",
            resume_text,
            height=400
        )

    else:
        st.warning("DOCX support will be added in the next version.")