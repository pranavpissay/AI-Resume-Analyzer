import pdfplumber


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file.
    """

    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    return resume_text
