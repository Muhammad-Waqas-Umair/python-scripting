# Reads a JSON file and extracts names of students with grades above 80.

import json

def filter_top_students(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    top_students = []
    for student in data["students"]:
        if student["grade"] > 80:
            top_students.append({"name": student["name"], "grade": student["grade"]})

    with open(output_file, 'w') as f:
        json.dump({"top_students": top_students}, f, indent=4)

filter_top_students("students.json", "top_students.json")

