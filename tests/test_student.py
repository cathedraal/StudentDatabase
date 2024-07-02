from studentdatabase import Student, is_student_in_list


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


def test_is_student_in_list():
    # Arrange
    student = Student("Roman Mallindine")
    list_of_student = [student]

    # Act
    result = is_student_in_list(list_of_student, "Roman Mallindine")

    # Assert
    assert result == 0
