from models.person import Person
from utils import check_type


class Mentor(Person):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.__courses_attached: set[str] = set()

    @property
    def courses_attached(self) -> set[str]:
        return self.__courses_attached

    @courses_attached.setter
    def courses_attached(self, _) -> None:
        raise AttributeError

    def add_course(self, course: str) -> None:
        check_type("course", course, str)
        self.__courses_attached.add(course)
