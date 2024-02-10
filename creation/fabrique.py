from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass

    @property
    @abstractmethod
    def protect_from_sun(self) -> bool:
        pass


class Car(Vehicle):
    def __init__(self):
        self._protect_from_sun = True

    def drive(self) -> str:
        return "The car drives on the road"

    @property
    def protect_from_sun(self) -> bool:
        return self._protect_from_sun


class Motorcycle(Vehicle):
    def __init__(self):
        self._protect_from_sun = False

    def drive(self) -> str:
        return "The motorcycle drives on the road"

    @property
    def protect_from_sun(self) -> bool:
        return self._protect_from_sun


class VehicleFactory(ABC):

    """
    The factory method pattern is a creational pattern
    that uses factory methods to deal with the problem of creating
    objects without having to specify the exact class of the
    object that will be created.

    """

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Motorcycle()


if __name__ == "__main__":
    car_factory = CarFactory()
    car = car_factory.create_vehicle()
    print(car.drive())
    print(car.protect_from_sun)

    motor_cyle = MotorcycleFactory()
    moto = motor_cyle.create_vehicle()
    print(moto.drive())
    print(moto.protect_from_sun)
