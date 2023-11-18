from abc import ABC


class Transport(ABC):
    def __init__(self, coordinates, speed, brand, year, number):
        self.__coordinates = coordinates
        self.__speed = speed
        self.__brand = brand
        self.__year = year
        self.__number = number

    def __str__(self):
        return f'Координаты: {self.__coordinates}\nСкорость: {self.__speed}\nМарка: {self.__brand}\nГод: {self.__year}\nНомер: {self.__number}'

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        else:
            self.__speed = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1:
            raise ValueError("Значение не может быть отрицательным")
        if isinstance(value, float):
            raise ValueError("Значение должно являться целым числом")
        else:
            self.__year = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        else:
            self.__number = value

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        if 0 <= pos_x <= width and 0 <= pos_y <= length:
            return True
        return False


class Passenger(ABC):
    def __init__(self, capacity, number):
        self.__passengers_capacity = capacity
        self.__number_of_passengers = number

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if passengers_capacity < 0:
            raise ValueError("Значение не может быть отрицательным")
        else:
            self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if number_of_passengers < 0:
            raise ValueError("Значение не может быть отрицательным")
        if isinstance(number_of_passengers, float):
            raise ValueError("Значение должно являться целым числом")
        else:
            self.__number_of_passengers = number_of_passengers


class Cargo(ABC):
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if carrying < 0:
            raise ValueError("Значение не может быть отрицательным")


class Plane(Transport):
    def __init__(self, height, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        else:
            self.__height = value


class Auto(Transport):
    def __init__(self, name, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Значение должно являться строкой")


class Ship(Transport):
    def __init__(self, port, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self.__port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        if isinstance(value, str):
            self.__port = value
        else:
            raise ValueError("Значение должно являться строкой")

# Машины
class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass

# Лодки
class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass

# Самолеты
class Airplane(Plane):
    pass


class PassengerPlane(Plane, Passenger):
    pass


class CargoPlane(Plane, Cargo):
    pass


class Seaplane(Plane, Ship):
    pass
