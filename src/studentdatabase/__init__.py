"""
This module represents an application that is managing students.
"""

from datetime import datetime
from typing import Optional


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


    def check_gender(self, gender):
        """
        Represents the check of the correctly written format of the gender.
        :param gender: Ввод пола студента.
        :return:
        """
        gender = str(gender).upper()
        if gender == "M" or gender == "F":
            return gender
        else:
            return 'Wrong format of the gender!'
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
        birth_date = str(input("Enter student´s birth date (YY.GG.XXXX): "))
        try:
            datetime.strptime(birth_date, "%d.%m.%Y")
            self.birth_date = birth_date
        except ValueError:
            raise ValueError('Wrong format of the date!')
        self.birth_date = str(input("Enter student´s birth date (YY.GG.XXXX): "))
        self.admission_yr = str(input("Enter student´s admission year: "))
        self.record_book = str(input("Enter student´s record book: "))
        self.group = str(input("Enter student´s group: "))
        self.department = str(input("Enter student´s department: "))
        self.faculty = str(input("Enter student´s faculty: "))
        self.gender = str(input("Enter student´s gender (M/F): "))

    def get_student(self):
        """
        Returns student´s data.
        :return:
        """
        return (f'{self.name}, {self.birth_date}, {self.admission_yr}, {self.record_book},'
                f' {self.group}, {self.department}, {self.faculty}, {self.gender}')


if __name__ == "__main__":
    print("Hello!")
