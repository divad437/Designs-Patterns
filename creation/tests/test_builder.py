from creation.builder import CarBuider, Director


class TestCodeUnderTest:
    def test_build_sports_car(self):
        builder = CarBuider()
        director = Director(builder)
        director.construct_sports_car()
        car = builder.get_product()
        assert car.seats == 2
        assert car.engine == "Sport Engine"
        assert car.trip_computer is True
        assert car.gps is False

    def test_build_suv_car(self):
        builder = CarBuider()
        director = Director(builder)
        director.construct_suv()
        car = builder.get_product()
        assert car.seats == 4
        assert car.engine == "SUV Engine"
        assert car.trip_computer is True
        assert car.gps is True
