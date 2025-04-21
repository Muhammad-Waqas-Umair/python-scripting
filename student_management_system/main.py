import re

MAX_RECORDS = 10
student_records = []

# Menu display
def show_menu():
    print("\n--- Student Record Management ---")
    print("1. Display all records")
    print("2. Add a new record")
    print("3. Delete a record")
    print("0. Exit")

# Add a new record with validation
def add_record():
    if len(student_records) >= MAX_RECORDS:
        print("⚠️ Maximum record limit reached.")
        return

    # Validate student ID (two-digit integer)
    while True:
        try:
            student_id = int(input("Enter student ID (two-digit): "))
            if 10 <= student_id <= 99:
                break
            else:
                print("❌ ID must be a two-digit number between 10 and 99.")
        except ValueError:
            print("❌ Invalid ID. It should be a two-digit number.")

    # Check if ID exists
    if any(student['id'] == student_id for student in student_records):
        print("⚠️ Student ID already exists.")
        return

    # Validate batch year (between 2015 and 2025)
    while True:
        try:
            batch_year = int(input("Enter batch year (2015-2025): "))
            if 2015 <= batch_year <= 2025:
                break
            else:
                print("❌ Batch year must be between 2015 and 2025.")
        except ValueError:
            print("❌ Invalid year. Please enter a valid number.")

    # Validate date of birth format (MM/DD/YYYY)
    while True:
        dob = input("Enter birth date (mm/dd/yyyy): ")
        if re.match(r"\d{2}/\d{2}/\d{4}", dob):
            break
        else:
            print("❌ Invalid date format. Please use MM/DD/YYYY.")

    # Validate department and name (alphabetical characters only)
    while True:
        department = input("Enter department (letters only): ")
        if department.isalpha():
            break
        else:
            print("❌ Department should only contain letters.")

    while True:
        name = input("Enter name (letters only): ")
        if name.isalpha():
            break
        else:
            print("❌ Name should only contain letters.")

    student = {
        "id": student_id,
        "batchYear": batch_year,
        "birthDate": dob,
        "department": department,
        "name": name
    }

    student_records.append(student)
    print("✅ Student record added.")

# Display all records
def display_records():
    if not student_records:
        print("📭 No records found.")
        return

    print("\n📋 All Student Records:")
    for student in student_records:
        print("---------------")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Department: {student['department']}")
        print(f"Birth Date: {student['birthDate']}")
        print(f"Batch Year: {student['batchYear']}")

# Delete a record by ID
def delete_record():
    try:
        student_id = int(input("Enter the student ID to delete: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    for i, student in enumerate(student_records):
        if student['id'] == student_id:
            del student_records[i]
            print("🗑️ Record deleted.")
            return

    print("❌ Record not found.")

# Main loop
def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        if choice == 1:
            display_records()
        elif choice == 2:
            add_record()
        elif choice == 3:
            delete_record()
        elif choice == 0:
            print("👋 Exiting the application.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
