# List of known skills
SKILLS_DATABASE = [
    "python",
    "sql",
    "power bi",
    "excel",
    "c",
    "c++",
    "java",
    "matlab",
    "streamlit",
    "git",
    "github",
    "arduino",
    "esp32",
    "stm32",
    "machine learning",
    "deep learning",
    "numpy",
    "pandas",
    "tensorflow",
    "pytorch",
    "opencv"
]


def extract_skills(resume_text):
    """
    Extract skills from resume text.
    """

    detected_skills = []

    resume_text = resume_text.lower()

    for skill in SKILLS_DATABASE:

        if skill.lower() in resume_text:

            detected_skills.append(skill.title())

    return sorted(detected_skills)