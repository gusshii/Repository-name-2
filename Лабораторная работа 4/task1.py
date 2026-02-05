from __future__ import annotations


class Vehicle:
    """
    Базовый класс транспортного средства.

    Атрибуты:
        brand: марка (не пустая строка)
        model: модель (не пустая строка)
        fuel_liters: топливо в баке (float, >= 0)

    Некоторые поля сделаны "непубличными" (с _), чтобы менять их только через методы класса.
    """

    def __init__(self, brand: str, model: str, fuel_liters: float) -> None:
        """
        Создание объекта транспортного средства.

        :param brand: марка
        :param model: модель
        :param fuel_liters: количество топлива в литрах

        :raise TypeError: если типы аргументов неверные
        :raise ValueError: если значения аргументов недопустимы
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not brand.strip():
            raise ValueError("brand не может быть пустым")

        if not isinstance(model, str):
            raise TypeError("model должен быть строкой")
        if not model.strip():
            raise ValueError("model не может быть пустым")

        if not isinstance(fuel_liters, (int, float)):
            raise TypeError("fuel_liters должен быть int или float")
        fuel_liters = float(fuel_liters)
        if fuel_liters < 0:
            raise ValueError("fuel_liters не может быть отрицательным")

        self._brand: str = brand
        self._model: str = model
        self._fuel_liters: float = fuel_liters

    @property
    def brand(self) -> str:
        """Марка (только чтение)."""
        return self._brand

    @property
    def model(self) -> str:
        """Модель (только чтение)."""
        return self._model

    @property
    def fuel_liters(self) -> float:
        """Топливо в баке (только чтение)."""
        return self._fuel_liters

    def __str__(self) -> str:
        """
        Читаемое представление объекта для пользователя.

        :return: строка вида 'Vehicle: Brand Model, fuel=...L'
        """
        return f"Vehicle: {self.brand} {self.model}, fuel={self.fuel_liters:.1f}L"

    def __repr__(self) -> str:
        """
        Техническое представление объекта.

        :return: строка, по которой можно воссоздать объект
        """
        return (
            f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
            f"fuel_liters={self.fuel_liters!r})"
        )

    def refuel(self, liters: float) -> None:
        """
        Заправить транспорт.

        :param liters: сколько литров добавить ( > 0 )
        :return: None

        :raise TypeError: если liters не число
        :raise ValueError: если liters <= 0
        """
        if not isinstance(liters, (int, float)):
            raise TypeError("liters должен быть int или float")
        liters = float(liters)
        if liters <= 0:
            raise ValueError("liters должен быть положительным")
        self._fuel_liters += liters

    def estimate_range_km(self) -> float:
        """
        Оценка запаса хода в км.
        В базовом классе используем условный усредненный расход.

        :return: запас хода в км (float)
        """
        # условно: 8 л на 100 км
        return (self.fuel_liters / 8.0) * 100.0


class Car(Vehicle):
    """
    Легковой автомобиль.

    Доп. атрибут:
        seats: количество мест (int, >= 1)
    """

    def __init__(self, brand: str, model: str, fuel_liters: float, seats: int) -> None:
        """
        Создание легкового автомобиля.

        :param brand: марка
        :param model: модель
        :param fuel_liters: топливо
        :param seats: количество мест

        :raise TypeError/ValueError: при некорректных аргументах
        """
        super().__init__(brand=brand, model=model, fuel_liters=fuel_liters)

        if not isinstance(seats, int):
            raise TypeError("seats должен быть int")
        if seats < 1:
            raise ValueError("seats должен быть >= 1")
        self._seats: int = seats

    @property
    def seats(self) -> int:
        """Количество мест (только чтение)."""
        return self._seats

    def estimate_range_km(self) -> float:
        """
        Перегружаем метод оценки запаса хода.

        Причина перегрузки:
        у легкового автомобиля обычно расход меньше, чем у усредненного транспорта,
        поэтому логично переопределить расчет в дочернем классе.

        :return: запас хода в км (float)
        """
        # условно: 6.5 л на 100 км
        return (self.fuel_liters / 6.5) * 100.0


class Truck(Vehicle):
    """
    Грузовой автомобиль.

    Доп. атрибут:
        max_load_kg: максимальная грузоподъёмность (float, > 0)
    """

    def __init__(self, brand: str, model: str, fuel_liters: float, max_load_kg: float) -> None:
        """
        Создание грузового автомобиля.

        :param brand: марка
        :param model: модель
        :param fuel_liters: топливо
        :param max_load_kg: грузоподъёмность

        :raise TypeError/ValueError: при некорректных аргументах
        """
        super().__init__(brand=brand, model=model, fuel_liters=fuel_liters)

        if not isinstance(max_load_kg, (int, float)):
            raise TypeError("max_load_kg должен быть int или float")
        max_load_kg = float(max_load_kg)
        if max_load_kg <= 0:
            raise ValueError("max_load_kg должен быть > 0")
        self._max_load_kg: float = max_load_kg

    @property
    def max_load_kg(self) -> float:
        """Максимальная грузоподъёмность (только чтение)."""
        return self._max_load_kg

    def estimate_range_km(self) -> float:
        """
        Перегружаем метод оценки запаса хода.

        Причина перегрузки:
        у грузовика расход топлива обычно выше, поэтому базовая оценка будет неверной.

        :return: запас хода в км (float)
        """
        # условно: 22 л на 100 км
        return (self.fuel_liters / 22.0) * 100.0


if __name__ == "__main__":
    # Write your solution here

    car = Car(brand="Toyota", model="Corolla", fuel_liters=30, seats=5)
    truck = Truck(brand="Volvo", model="FH", fuel_liters=120, max_load_kg=18000)

    print(car)                 # проверяем __str__
    print(repr(car))           # проверяем __repr__
    print(car.estimate_range_km())

    print(truck)
    print(repr(truck))
    print(truck.estimate_range_km())

    car.refuel(10)
    print(car.fuel_liters)
