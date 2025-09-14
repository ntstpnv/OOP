from models.mentor import Mentor
from models.grade import Grade


class Lecturer(Mentor, Grade):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)

    def __str__(self) -> str:
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade:.1f}"
        )
