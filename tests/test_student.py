from studentdatabase import Student


def test_student_creation():
    # Arrange, Act
    student = Student()

    # Assert
    assert isinstance(student, Student)


def test_student_creation_with_name():
    # Arrange, Act
    student = Student(name="Roman")

    # Assert
    assert student.name == "Roman"
