import doctest


class Lamp:
    def __init__(self, power_watts: float, is_on: bool, location: str):
        """
        Создание и подготовка к работе объекта "Лампа"

        :param power_watts: Мощность лампы (Вт)
        :param is_on: Включена ли лампа
        :param location: Место установки лампы

        Примеры:
        >>> lamp = Lamp(60, False, "Kitchen")
        """
        if not isinstance(power_watts, (int, float)):
            raise TypeError("Мощность должна быть типа int или float")
        if power_watts <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power_watts = float(power_watts)

        if not isinstance(is_on, bool):
            raise TypeError("is_on должен быть типа bool")
        self.is_on = is_on

        if not isinstance(location, str):
            raise TypeError("Локация должна быть строкой")
        if not location.strip():
            raise ValueError("Локация не может быть пустой")
        self.location = location

    def switch_on(self) -> None:
        """
        Включить лампу.

        :return: None

        Примеры:
        >>> lamp = Lamp(60, False, "Kitchen")
        >>> lamp.switch_on()
        """
        ...

    def switch_off(self) -> None:
        """
        Выключить лампу.

        :return: None

        Примеры:
        >>> lamp = Lamp(60, True, "Kitchen")
        >>> lamp.switch_off()
        """
        ...

    def relocate(self, new_location: str) -> None:
        """
        Переместить лампу в другое место.

        :param new_location: Новая локация
        :return: None

        :raise ValueError: если новая локация пустая

        Примеры:
        >>> lamp = Lamp(60, False, "Kitchen")
        >>> lamp.relocate("Hall")
        """
        if not isinstance(new_location, str):
            raise TypeError("Новая локация должна быть строкой")
        if not new_location.strip():
            raise ValueError("Новая локация не может быть пустой")
        ...


class EventTicket:
    def __init__(self, event_name: str, price: float, seat_number: int):
        """
        Создание и подготовка к работе объекта "Билет на мероприятие"

        :param event_name: Название мероприятия
        :param price: Стоимость билета
        :param seat_number: Номер места

        Примеры:
        >>> ticket = EventTicket("Concert", 1500, 12)
        """
        if not isinstance(event_name, str):
            raise TypeError("Название мероприятия должно быть строкой")
        if not event_name.strip():
            raise ValueError("Название мероприятия не может быть пустым")
        self.event_name = event_name

        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = float(price)

        if not isinstance(seat_number, int):
            raise TypeError("Номер места должен быть типа int")
        if seat_number <= 0:
            raise ValueError("Номер места должен быть положительным числом")
        self.seat_number = seat_number

    def validate_entry(self, user_name: str) -> bool:
        """
        Проверка допуска по билету.

        :param user_name: Имя владельца билета
        :return: Допущен ли пользователь (True/False)

        Примеры:
        >>> ticket = EventTicket("Concert", 1500, 12)
        >>> ticket.validate_entry("Alex")
        """
        if not isinstance(user_name, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not user_name.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        ...

    def refund(self, reason: str) -> float:
        """
        Оформить возврат билета.

        :param reason: Причина возврата
        :return: Сумма возврата

        :raise ValueError: если причина пустая

        Примеры:
        >>> ticket = EventTicket("Concert", 1500, 12)
        >>> ticket.refund("Can't go")
        """
        if not isinstance(reason, str):
            raise TypeError("Причина должна быть строкой")
        if not reason.strip():
            raise ValueError("Причина не может быть пустой")
        ...

    def change_seat(self, new_seat_number: int) -> None:
        """
        Сменить место в билете.

        :param new_seat_number: Новый номер места
        :return: None

        :raise ValueError: если номер места некорректный

        Примеры:
        >>> ticket = EventTicket("Concert", 1500, 12)
        >>> ticket.change_seat(30)
        """
        if not isinstance(new_seat_number, int):
            raise TypeError("Новый номер места должен быть типа int")
        if new_seat_number <= 0:
            raise ValueError("Новый номер места должен быть положительным числом")
        ...


class SimpleStack:
    def __init__(self, capacity: int, current_size: int):
        """
        Создание и подготовка к работе объекта "Стек"

        :param capacity: Максимальная емкость стека
        :param current_size: Текущее количество элементов

        Примеры:
        >>> st = SimpleStack(5, 0)
        """
        if not isinstance(capacity, int):
            raise TypeError("Емкость должна быть типа int")
        if capacity <= 0:
            raise ValueError("Емкость должна быть положительным числом")
        self.capacity = capacity

        if not isinstance(current_size, int):
            raise TypeError("Текущий размер должен быть типа int")
        if current_size < 0:
            raise ValueError("Текущий размер не может быть отрицательным")
        if current_size > capacity:
            raise ValueError("Текущий размер не может превышать емкость")
        self.current_size = current_size

    def is_empty(self) -> bool:
        """
        Проверка: пуст ли стек.

        :return: True если стек пуст, иначе False

        Примеры:
        >>> st = SimpleStack(5, 0)
        >>> st.is_empty()
        """
        ...

    def push(self, items_count: int) -> None:
        """
        Добавить элементы в стек.

        :param items_count: Количество добавляемых элементов
        :return: None

        :raise ValueError: если добавление превысит емкость

        Примеры:
        >>> st = SimpleStack(5, 0)
        >>> st.push(3)
        """
        if not isinstance(items_count, int):
            raise TypeError("Количество добавляемых элементов должно быть типа int")
        if items_count < 0:
            raise ValueError("Количество добавляемых элементов не может быть отрицательным")
        ...

    def pop(self, items_count: int) -> int:
        """
        Извлечь элементы из стека.

        :param items_count: Количество извлекаемых элементов
        :return: Реально извлеченное количество элементов

        :raise ValueError: если пытаемся извлечь больше, чем есть

        Примеры:
        >>> st = SimpleStack(5, 5)
        >>> st.pop(2)
        """
        if not isinstance(items_count, int):
            raise TypeError("Количество извлекаемых элементов должно быть типа int")
        if items_count < 0:
            raise ValueError("Количество извлекаемых элементов не может быть отрицательным")
        ...


if __name__ == "__main__":
    doctest.testmod()
