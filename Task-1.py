# Student Marks Lookup Program

def main():
    # Dictionary storing student names and their corresponding marks
    student_marks = {
        "Alice": 85,
        "Billie": 78,
        "Caroline": 92,
        "Derek": 74,
        "Erik": 88
    }

    # Prompt user for input
    student_name = input("Enter the student's name: ").strip().title()

    # Check if the student's name exists in the dictionary
    if student_name in student_marks:
        print(f"{student_name}'s marks: {student_marks[student_name]}")
    else:
        print(f"Student '{student_name}' not found.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()