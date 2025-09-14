from functools import total_ordering
from inspect import stack
from itertools import chain
from math import isclose


@total_ordering
class Grade:
    def __init__(self) -> None:
        self.__grades: dict[str, list[int]] = {}
        self.__average_grade: float = 0.0

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return isclose(self.average_grade, other.average_grade, abs_tol=0.01)

    def __lt__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return not self == other and self.average_grade < other.average_grade

    @property
    def grades(self) -> dict[str, list[int]]:
        return self.__grades

    @grades.setter
    def grades(self, _) -> None:
        raise AttributeError

    @property
    def average_grade(self) -> float:
        return self.__average_grade

    @average_grade.setter
    def average_grade(self, _) -> None:
        raise AttributeError

    def add_grade(self, course: str, grade: int) -> None:
        if stack()[1].function not in ("rate_lecture", "rate_hw"):
            raise AttributeError
        self.__grades.setdefault(course, []).append(grade)
        grades = list(chain.from_iterable(self.__grades.values()))
        self.__average_grade = sum(grades) / len(grades)
