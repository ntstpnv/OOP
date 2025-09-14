from re import fullmatch


def check_type(arg_name: str, value, expected_type) -> None:
    if not isinstance(value, expected_type):
        e = f"{arg_name} не может быть типа {type(value).__name__}"
        raise TypeError(e)


def check_full_name(arg_name: str, value: str) -> None:
    if not fullmatch(r"(?i)[a-zа-яё -]+", value):
        e = f"{arg_name} содержит недопустимые символы"
        raise ValueError(e)


def check_course(mentor, student, course: str) -> None:
    if course not in mentor.courses_attached:
        e = f"{mentor.name} {mentor.surname} не ведет курс {course}"
        raise ValueError(e)
    if course not in student.courses_in_progress:
        e = f"{student.name} {student.surname} не обучается на курсе {course}"
        raise ValueError(e)


def check_grade(value: int) -> None:
    if not value in range(11):
        e = f"grade не может принимать значение {value}"
        raise ValueError(e)
