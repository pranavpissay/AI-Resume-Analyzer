"""
Resume Section Detection Engine
"""

import re

# Different names that resumes may use
SECTION_PATTERNS = {
    "Education": [
        "education",
        "academic background",
        "qualification",
        "qualifications"
    ],

    "Skills": [
        "skills",
        "technical skills",
        "core competencies"
    ],

    "Projects": [
        "projects",
        "academic projects",
        "personal projects"
    ],

    "Experience": [
        "experience",
        "work experience",
        "employment history",
        "professional experience"
    ],

    "Certifications": [
        "certifications",
        "certificates"
    ]
}


def detect_sections(resume_text):
    """
    Detect common resume sections.

    Returns:
        dict
    """

    sections = {}

    current_section = "General"

    sections[current_section] = []

    lines = resume_text.splitlines()

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        found = False

        for section, headers in SECTION_PATTERNS.items():

            if clean_line.lower() in headers:

                current_section = section

                sections[current_section] = []

                found = True

                break

        if not found:

            sections[current_section].append(clean_line)

    return sections