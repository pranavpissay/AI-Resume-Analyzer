"""
Education Extractor
"""

EDUCATION_KEYWORDS = [
    "bachelor",
    "master",
    "b.tech",
    "btech",
    "m.tech",
    "mtech",
    "engineering",
    "university",
    "college",
    "school",
    "cgpa",
    "gpa",
    "percentage"
]


def extract_education(sections):
    """
    Extract education details from resume sections.

    Args:
        sections (dict)

    Returns:
        list
    """

    education = []

    education_section = sections.get("Education", [])

    for line in education_section:

        for keyword in EDUCATION_KEYWORDS:

            if keyword.lower() in line.lower():

                education.append(line)

                break

    return education