from utils import check_type, check_full_name


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        super().__init__()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        check_type("name", value, str)
        check_full_name("name", value)
        self.__name = value

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, value) -> None:
        check_type("surname", value, str)
        check_full_name("surname", value)
        self.__surname = value
