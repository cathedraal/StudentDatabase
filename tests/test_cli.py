from studentdatabase import Student
from studentdatabase.cli import is_student_in_list


def test_is_student_in_list():
    # Arrange
    student = Student("Roman Mallindine")
    list_of_student = [student]

    # Act
    result = is_student_in_list(list_of_student, "Roman Mallindine")

    # Assert
    assert result == 0
