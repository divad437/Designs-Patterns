# import pytest

from creation.fabrique import Car, CarFactory, Motorcycle, MotorcycleFactory


class TestCodeUnderTest:
    def test_car_creation(self) -> None:
        car_factory = CarFactory()
        car = car_factory.create_vehicle()
        assert isinstance(car, Car)

    def test_motorcycle_creation(self) -> None:
        motorcycle_factory = MotorcycleFactory()
        motorcycle = motorcycle_factory.create_vehicle()
        assert isinstance(motorcycle, Motorcycle)

    def test_car_drive(self) -> None:
        car_factory = CarFactory(self)
        car = car_factory.create_vehicle(self)
        assert car.drive() == "The car drives on the road"

    # def test_vehicle_instantiation() -> None:
    #     with pytest.raises(TypeError):
    #         Vehicle()

    # def test_vehicle_factory_instantiation() -> None:
    #     with pytest.raises(TypeError):
    #         VehicleFactory()

    def test_car_factory_create(self) -> None:
        car_factory = CarFactory()
        car = car_factory.create_vehicle()
        assert isinstance(car, Car)
