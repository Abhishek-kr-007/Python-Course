TASK-1

Student Marks Lookup Program

Overview

The Student Marks Lookup Program is a simple Python script that allows users to retrieve student marks by entering a student's name. If the student's name exists in the predefined dictionary, their marks are displayed; otherwise, the program notifies the user that the student is not found.

Features

Case-insensitive student name lookup

Allows multiple queries until the user exits

Provides a friendly prompt for user interaction


Prerequisites

Python 3.x installed on your system


How to Run

1. Download or clone this repository.


2. Navigate to the directory containing the script.


3. Run the script using the following command:

python student_marks.py


4. Enter a student's name when prompted.


5. Type exit to quit the program.



Code Explanation

The script stores student names and marks in a dictionary.

The user is prompted to enter a student's name.

The program converts the input to lowercase to allow case-insensitive searches.

If a match is found, the student's marks are displayed.

If no match is found, an error message is displayed.

The program runs in a loop, allowing multiple searches until the user types exit.


Example Usage

Enter the student's name (or type 'exit' to quit): Alice
Alice's marks: 85

Enter the student's name (or type 'exit' to quit): john
Student 'john' not found. Please try again.

Enter the student's name (or type 'exit' to quit): exit
Exiting program. Goodbye!

Future Improvements

Add a feature to allow users to add new students dynamically.

Enable fuzzy search for partial name matching.

Store student marks in an external file or database for persistence.


License

This project is open-source and free to use.
