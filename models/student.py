from models.person import Person
from models.grade import Grade
from models.lecturer import Lecturer

from utils import check_type, check_course, check_grade


class Student(Person, Grade):
    def __init__(self, name: str, surname: str, sex: str) -> None:
        super().__init__(name, surname)
        self.sex = sex
        self.__courses_in_progress: set[str] = set()
        self.__finished_courses: set[str] = set()

    def __str__(self) -> str:
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_grade:.1f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, value: str) -> None:
        check_type("sex", value, str)
        self.__sex = value

    @property
    def courses_in_progress(self) -> set[str]:
        return self.__courses_in_progress

    @courses_in_progress.setter
    def courses_in_progress(self, _) -> None:
        raise AttributeError

    @property
    def finished_courses(self) -> set[str]:
        return self.__finished_courses

    @finished_courses.setter
    def finished_courses(self, _) -> None:
        raise AttributeError

    def start_course(self, course: str) -> None:
        check_type("course", course, str)
        if course in self.finished_courses:
            e = f"{course} уже завершен"
            raise TypeError(e)
        self.__courses_in_progress.add(course)

    def finish_course(self, course: str) -> None:
        check_type("course", course, str)
        if course not in self.courses_in_progress:
            e = f"{course} еще не начат"
            raise TypeError(e)
        self.__courses_in_progress.remove(course)
        self.__finished_courses.add(course)

    def rate_lecture(self, lecturer, course, grade) -> None:
        check_type("lecturer", lecturer, Lecturer)
        check_type("course", course, str)
        check_course(lecturer, self, course)
        check_type("grade", grade, int)
        check_grade(grade)
        lecturer.add_grade(course, grade)
