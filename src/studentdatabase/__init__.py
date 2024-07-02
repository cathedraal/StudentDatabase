"""
This module represents an application that is managing students.
"""

from datetime import datetime
from typing import Optional, Tuple, List


class Student:
    def __init__(self, name=None, birth_date=None, admission_yr=None, record_book=None,
                 group=None, department=None, faculty=None, gender=None):
        """
        Initialization of the student.

        :param name: Name of the student.
        :param birth_date: Date birth of the student.
        :param admission_yr: Student´s admission year.
        :param record_book: Student´s record book.
        :param group: Student´s group.
        :param department: Student´s department.
        :param faculty: Student´´s faculty.
        :param gender: Student´s gender.
        """
        self.name = name
        self.birth_date = birth_date
        self.admission_yr = admission_yr
        self.record_book = record_book
        self.group = group
        self.department = department
        self.faculty = faculty
        self.gender = gender

    def check_date(self, date):
        """
        Represents the check if the date is written correctly.

        :param date: Date.
        :return:
        """
        try:
            datetime.strptime(date, "%d.%m.%Y")
            return date
        except ValueError:
            return 'Wrong format of the date!'

    def check_gender(self, gender: str) -> str:
        """
        Represents the check of the correctly written format of the gender.
        :param gender: Ввод пола студента.
        :return:
        """
        gender = str(gender).upper()
        if gender == "M" or gender == "F":
            return gender
        else:
            raise ValueError("Incorrect gender!")

    def is_valid_gender(self, gender: str) -> bool:
        gender = str(gender).upper()
        if gender == "M" or gender == "F":
            return True
        return False

    def check_gender_v2(self, gender: str) -> Tuple[bool, str]:
        gender = str(gender).upper()
        if gender == "M" or gender == "F":
            return True, gender
        else:
            return False, ""

    def check_admissionYR(self, admission_yr):
        """
        Checks of the format of the admission year is written correctly.
        :param admission_yr: Admission year.
        :return:
        """

        if str(admission_yr).isdigit() and len(admission_yr) == 4:
            return admission_yr
        else:
            return 'The format is wrong!'

    def set_student(self):
        """
        Sets the student´s data.
        :return:
        """

        self.name = str(input('Enter surname and lastname: '))
        date_correctly_entered = False
        while not date_correctly_entered:
            birth_date = str(input("Enter student´s birth date (YY.GG.XXXX): "))
            try:
                datetime.strptime(birth_date, "%d.%m.%Y")
                self.birth_date = birth_date
                date_correctly_entered = True
            except ValueError:
                print("Incorrect date entered! Please try again!")
        admission_yr_correctly_entered = False
        while not admission_yr_correctly_entered:
            admission_yr = str(input("Enter student´s admission year: "))
            if str(admission_yr).isdigit() and len(admission_yr) == 4:
                self.admission_yr = admission_yr
                admission_yr_correctly_entered = True
            else:
                print("Incorrect format of admission year entered! Please try again!")
                admission_yr_correctly_entered = False
        self.record_book = str(input("Enter student´s record book: "))
        self.group = str(input("Enter student´s group: "))
        self.department = str(input("Enter student´s department: "))
        self.faculty = str(input("Enter student´s faculty: "))
        gender_successfully_validate = False
        while not gender_successfully_validate:
            gender = str(input("Enter student´s gender (M/F): "))
            gender_successfully_validate, self.gender = self.check_gender_v2(gender)
            if not gender_successfully_validate:
                print("Incorrect gender entered! Please try again!")

    def get_student(self):
        """
        Returns student´s data.
        :return:
        """
        return (f'{self.name}, {self.birth_date}, {self.admission_yr}, {self.record_book},'
                f' {self.group}, {self.department}, {self.faculty}, {self.gender}')


def is_student_in_list(students: List[Student], name: str) -> int:
    for student in students:
        if student.name == name:
            return students.index(student)
    return -1


def add_student(list_of_students: List[Student]):
    student = Student()
    student.set_student()
    list_of_students.append(student)
    print("Student successfully added!")


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


def main():
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

        elif users_answer == 2:
            get_existing_student(list_of_students)

        elif users_answer == 3:
            delete_student(list_of_students)

        elif users_answer == 4:
            print(f'''The list of the students:
{list_of_students}''')

        elif users_answer == 5:
            print("Goodbye!")


if __name__ == "__main__":
    main()
