from models.mentor import Mentor
from models.student import Student
from utils import check_type, check_course, check_grade


class Reviewer(Mentor):
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade) -> None:
        check_type("student", student, Student)
        check_type("course", course, str)
        check_course(self, student, course)
        check_type("grade", grade, int)
        check_grade(grade)
        student.add_grade(course, grade)
