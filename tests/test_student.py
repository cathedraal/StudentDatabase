from studentdatabase import Student


def test_student_creation():
    # Arrange, Act
    student = Student()

    # Assert
    assert isinstance(student, Student)
