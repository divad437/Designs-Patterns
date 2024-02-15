class RoundHole:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self) -> int:
        return self.__radius

    def fits(self, peg) -> bool:
        return self.get_radius() >= peg.get_radius()


class RoundPeg:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self) -> int:
        return self.__radius


class SquarePeg:
    def __init__(self, width):
        self.__width = width

    def get_width(self) -> int:
        return self.__width


class SquarePegAdapter:
    def __init__(self, peg):
        self.__peg = peg

    def get_radius(self) -> int:
        return (self.__peg.get_width() * 2**0.5) / 2


class Application:
    def main(self):
        round_hole = RoundHole(5)
        round_peg = RoundPeg(5)
        if round_hole.fits(round_peg):
            print("Round peg with radius 5 fits round hole with radius 5.")
        square_peg = SquarePeg(5)
        square_peg_adapter = SquarePegAdapter(square_peg)
        square_peg_big_adapter = SquarePegAdapter(SquarePeg(20))
        if not round_hole.fits(square_peg_big_adapter):
            print("Square peg with width 10 not fits round hole with radius 5.")
        if round_hole.fits(square_peg_adapter):
            print("Square peg with width 5 fits round hole with radius 5.")
        return 0


app = Application()
app.main()
