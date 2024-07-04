"""
Module which contains CLI code of StudentDatabase.
"""
import argparse
from typing import List
import json

from studentdatabase import Student
from studentdatabase import to_json
import os


def build_parser() -> argparse.ArgumentParser:
    """
    Build the argparse CLI.

    :return: The fully built CLI parser.
    """
    parser = argparse.ArgumentParser(prog="interactive user input",
                                     description="This module interacts users input.",
                                     epilog="End of the arguments.")

    parser.add_argument("operation", choices=["add", "interactive"],
                        help="Choose an operation: <add> to add a student or <interactive> to see more options.")

    parser.add_argument("-nm", "--name", help="Adds a student into database.")
    parser.add_argument("-bd", "--birthday", help="Adds a student into database.")
    parser.add_argument("-a_y", "--admission-year", help="Adds a student into database.")
    parser.add_argument("-r_b", "--record-book", help="Adds a student into database.")
    parser.add_argument("-gr", "--group", help="Adds a student into database.")
    parser.add_argument("-dp", "--department", help="Adds a student into database.")
    parser.add_argument("-fa", "--faculty", help="Adds a student into database.")
    parser.add_argument("-gd", "--gender", help="Adds a student into database.")
    return parser


def is_student_in_list(students: List[Student], name: str) -> int:
    for student in students:
        if student.name == name:
            return students.index(student)
    return -1


def add_student(list_of_students: List[Student]):
    student = Student()
    student.set_student()
    list_of_students.append(student)


def get_existing_student(list_of_students: List[Student]):
    student_in_the_list = False
    while not student_in_the_list:
        answer = input("Please enter student´s name: ")
        student_index = is_student_in_list(list_of_students, answer)
        if student_index > -1:
            print(list_of_students[student_index].get_student())
            student_in_the_list = True
        else:
            print("Student not found!")


def delete_student(list_of_students: List[Student]):
    student_in_the_list = False
    while not student_in_the_list:
        answer = input("Please enter student´s name: ")
        student_index = is_student_in_list(list_of_students, answer)
        if student_index > -1:
            list_of_students.pop(student_index)
            student_in_the_list = True
        else:
            print("Student not found!")


def interactive_mode():
    list_of_students: List[Student] = []
    users_answer = -1
    while users_answer != 5:
        print("""Hello!
This is student´s database!
What shall we do?

1. Add a student
2. Get an existing student
3. Delete a student
4. Show all students
5. End the program
""")

        users_correct_answer = False
        while not users_correct_answer:
            user = input("Please enter your choice [1-5]: ")
            if user.isdigit() and 0 < int(user) < 6:
                users_correct_answer = True
                users_answer = int(user)
            else:
                print("Not a number between 1 and 5!")

        if users_answer == 1:
            add_student(list_of_students)
            print("""
Student succesfully added! 

/stop to stop the code""")

            user_menu = str(input())
            if user_menu == "/stop":
                print("code stopped.")
                break

        elif users_answer == 2:
            get_existing_student(list_of_students)

        elif users_answer == 3:
            delete_student(list_of_students)

        elif users_answer == 4:
            print(f'''The list of the students:
{list_of_students}''')

        elif users_answer == 5:
            print("Goodbye!")

def main():
    """
    Main entrypoint for the CLI
    """
    parser = build_parser()

    args = parser.parse_args()
    list_of_students: List[Student] = []

    # 1. Check if file exists
    if os.path.exists("students0.json"):
        # 2. use "open" to create file descriptor
        with open("students0.json", encoding="UTF-8") as json_file:
            # 3. Load the file and json in a single line into a variable
            student_json = json.load(json_file)
            # 4. Use a loop to iterate of the variable
            for student in student_json:
                # 5. Load each element and append it to the list_of_students
                list_of_students.append(Student(
                    name=student["name"],
                    birth_date=student["birth_date"],
                    admission_yr=student["admission_yr"],
                    record_book=student["record_book"],
                    group=student["group"],
                    department=student["department"],
                    faculty=student["faculty"],
                    gender=student["gender"],
                ))

    if args.operation == "add":
        new_student = Student(
            name=args.name,
            birth_date=args.birthday,
            admission_yr=args.admission_year,
            record_book=args.record_book,
            group=args.group,
            department=args.department,
            faculty=args.faculty,
            gender=args.gender,
        )
        list_of_students.append(new_student)
        print("Student successfully added!")
        print(list_of_students)

        test = to_json(list_of_students)
        with open("students0.json", "w", encoding="UTF-8") as file:
            file.write(test)

        #
        # with open("students1.json", "w", encoding="UTF-8") as file:
        #     json.dump(list_of_students, file, default=lambda obj: obj.__dict__, indent=2)
        #
        # with open("students2.json", "w", encoding="UTF-8") as file:
        #     file.write(json.dumps(list_of_students, default=lambda obj: obj.__dict__, indent=2))

    if args.operation == "interactive":
        interactive_mode()



