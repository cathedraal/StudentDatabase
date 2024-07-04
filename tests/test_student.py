from studentdatabase import Student, to_json


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


def test_student_gender_check_v2():
    # Arrange
    student = Student(name="Roman")

    # Act
    result = student.check_gender_v2("M")

    # Assert
    assert result == (True, "M")


def test_to_json():
    # Arrange
    student = Student(name="Roman")

    # Act
    result = to_json(student)

    # Assert
    assert len(result.splitlines()) == 10
