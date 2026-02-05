class Book:
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if not name.strip():
            raise ValueError("name не может быть пустым")

        if not isinstance(author, str):
            raise TypeError("author должен быть строкой")
        if not author.strip():
            raise ValueError("author не может быть пустым")

        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def _repr_extra(self) -> str:
        return ""

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}(name={self.name!r}, author={self.author!r}{self._repr_extra()})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("pages должен быть int")
        if value <= 0:
            raise ValueError("pages должен быть положительным числом")
        self._pages = value

    def _repr_extra(self) -> str:
        return f", pages={self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration
    @property
    def duration(self) -> float:
        return self._duration
    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("duration должен быть int или float")
        value = float(value)
        if value <= 0:
            raise ValueError("duration должен быть положительным числом")
        self._duration = value

    def _repr_extra(self) -> str:
        return f", duration={self.duration}"