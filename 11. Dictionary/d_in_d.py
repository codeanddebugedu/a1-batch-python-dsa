"""
anirudh has scored 252 marks
nihar has scored
"""

student_details = {
    "anirudh": {
        "age": 66,
        "gender": "Male",
        "address": "Surat",
        "phone": 100,
        "physics": 98,
        "chemistry": 87,
        "maths": 11,
    },
    "nihar": {
        "phone": 3213421,
        "gender": "Male",
        "address": "Delhi",
        "age": 16,
        "physics": 54,
        "chemistry": 71,
        "maths": 91,
    },
    "anusha": {
        "phone": 585652,
        "gender": "Female",
        "address": "Agra",
        "age": 52,
        "physics": 14,
        "chemistry": 64,
        "maths": 71,
    },
}

# ....

for name, details in student_details.items():
    total = (
        details.get("physics", 0)
        + details.get("chemistry", 0)
        + details.get("maths", 0)
    )
    details["total_marks"] = total

print(student_details)
