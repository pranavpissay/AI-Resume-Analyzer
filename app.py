import streamlit as st

from core.parser.pdf_parser import extract_text_from_pdf
from core.extractor.contact import extract_contact_info
from core.extractor.skills import extract_skills
from core.extractor.sections import detect_sections
from core.extractor.education import extract_education

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

    # -----------------------------------
    # File Details
    # -----------------------------------
    st.subheader("📁 File Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("File Name", uploaded_file.name)

    with col2:
        st.metric("File Type", uploaded_file.type)

    with col3:
        st.metric("File Size", f"{uploaded_file.size / 1024:.2f} KB")

    st.divider()

    # -----------------------------------
    # PDF Processing
    # -----------------------------------
    if uploaded_file.type == "application/pdf":

        # Extract Resume Text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Run Extractors
        contact_info = extract_contact_info(resume_text)
        detected_skills = extract_skills(resume_text)
        sections = detect_sections(resume_text)
        education = extract_education(sections) 
        # -----------------------------------
        # Candidate Profile
        # -----------------------------------
        st.subheader("👤 Candidate Profile")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Name:** {contact_info.get('Name', 'Not Found')}")
            st.write(f"**Email:** {contact_info.get('Email', 'Not Found')}")
            st.write(f"**Phone:** {contact_info.get('Phone', 'Not Found')}")

        with col2:
            st.write(f"**LinkedIn:** {contact_info.get('LinkedIn', 'Not Found')}")
            st.write(f"**GitHub:** {contact_info.get('GitHub', 'Not Found')}")

        st.divider()

        # -----------------------------------
        # Resume Content
        # -----------------------------------
        st.subheader("📄 Resume Content")

        st.text_area(
            "Extracted Text",
            resume_text,
            height=350
        )

        st.divider()

        # -----------------------------------
        # Detected Skills
        # -----------------------------------
        st.subheader("🎯 Detected Skills")

        if detected_skills:

            cols = st.columns(4)

            for index, skill in enumerate(detected_skills):
                cols[index % 4].success(skill)

        else:

            st.warning("No skills detected.")

        st.divider()
        
        # -----------------------------------
        # Education
        # -----------------------------------
        st.divider()

        st.subheader("🎓 Education")

        if education:
            for item in education:
                st.info(item)
            else:
                st.warning("Education details not found.")
        
        # -----------------------------------
        # Resume Sections
        # -----------------------------------
        st.header("📂 Resume Sections")

        for section, content in sections.items():

            with st.expander(section, expanded=False):

                if content:

                    for line in content:
                        st.write(line)

                else:

                    st.write("No content found.")

    else:

        st.warning("⚠ DOCX support will be added in the next version.")