"""
This module represents an application that is managing students.
"""

from datetime import datetime
from typing import Tuple


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

    def __str__(self) -> str:
        return self.get_student()

    def __repr__(self) -> str:
        return self.get_student()

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
            birth_date = str(input("Enter student´s birth date (DD.MM.YYYY): "))
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
