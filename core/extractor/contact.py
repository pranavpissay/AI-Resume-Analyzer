"""
Contact Information Extractor
"""

import re


def extract_contact_info(resume_text):
    """
    Extract contact information from resume text.

    Returns:
        dict
    """

    contact = {}

    # ------------------------
    # Name
    # ------------------------
    lines = resume_text.splitlines()

    for line in lines:

        if line.strip():

            contact["Name"] = line.strip()

            break

    # ------------------------
    # Email
    # ------------------------
    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    if email:

        contact["Email"] = email.group()

    # ------------------------
    # Phone
    # ------------------------
    phone = re.search(
        r"(\+91[\-\s]?)?[6-9]\d{9}",
        resume_text
    )

    if phone:

        contact["Phone"] = phone.group()

    # ------------------------
    # LinkedIn
    # ------------------------
    linkedin = re.search(
        r"(https?://)?(www\.)?linkedin\.com/[^\s]+",
        resume_text
    )

    if linkedin:

        contact["LinkedIn"] = linkedin.group()

    # ------------------------
    # GitHub
    # ------------------------
    github = re.search(
        r"(https?://)?(www\.)?github\.com/[^\s]+",
        resume_text
    )

    if github:

        contact["GitHub"] = github.group()

    return contact