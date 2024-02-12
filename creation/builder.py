from abc import ABC, abstractmethod


class Car:
    def __init__(self) -> None:
        self.seats = 0
        self.engine = ""
        self.trip_computer = False
        self.gps = False

    def __str__(self) -> str:
        return (
            f"Car with {self.seats} seats, "
            f"{self.engine} engine, trip computer"
            f"{self.trip_computer} and gps {self.gps}"
        )


class Builder(ABC):
    """
    The Builder pattern is a creational design
    pattern that lets you construct complex objects step by step.
    """

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_seats(self, number: int) -> None:
        pass

    @abstractmethod
    def set_engine(self, engine: str) -> None:
        pass

    @abstractmethod
    def set_trip_computer(self, value: bool) -> None:
        pass

    @abstractmethod
    def set_gps(self, value: bool) -> None:
        pass


class CarBuider(Builder):
    def reset(self) -> None:
        self.__car = Car()

    def set_seats(self, number: int) -> None:
        self.__car.seats = number

    def set_engine(self, engine: str) -> None:
        self.__car.engine = engine

    def set_trip_computer(self, value: bool) -> None:
        self.__car.trip_computer = value

    def set_gps(self, value: bool) -> None:
        self.__car.gps = value

    def get_product(self) -> Car:
        final_product = self.__car
        self.reset()
        return final_product


class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def construct_sports_car(self) -> None:
        self.builder.reset()
        self.builder.set_seats(2)
        self.builder.set_engine("Sport Engine")
        self.builder.set_trip_computer(True)
        self.builder.set_gps(False)
        car: Car = self.builder.get_product()
        print(car)

    def construct_suv(self) -> None:
        self.builder.reset()
        self.builder.set_seats(4)
        self.builder.set_engine("SUV Engine")
        self.builder.set_trip_computer(True)
        self.builder.set_gps(True)
        car: Car = self.builder.get_product()
        print(car)


if __name__ == "__main__":
    builder = CarBuider()
    director = Director(builder)
    director.construct_sports_car()
    director.construct_suv()
