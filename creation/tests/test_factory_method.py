from creation.fabrique import Car, CarFactory, Motorcycle, MotorcycleFactory


class TestCodeUnderTest:
    def test_car_creation(self) -> None:
        car_factory = CarFactory()
        car = car_factory.create_vehicle()
        assert isinstance(car, Car)

    def test_motorcycle_creation(self):
        motorcycle_factory = MotorcycleFactory()
        motorcycle = motorcycle_factory.create_vehicle()
        assert isinstance(motorcycle, Motorcycle)

    def test_car_drive(self):
        car_factory = CarFactory()
        car = car_factory.create_vehicle()
        assert car.drive() == "The car drives on the road"

    def test_car_factory_create(self):
        car_factory = CarFactory()
        car = car_factory.create_vehicle()
        assert isinstance(car, Car)
