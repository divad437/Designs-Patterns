from structural.adapter import RoundHole, RoundPeg, SquarePeg, SquarePegAdapter


class TestAdapter:
    def test_create_round_peg(self) -> None:
        round_peg = RoundPeg(5)
        assert round_peg.get_radius() == 5

    def test_create_round_hole(self) -> None:
        round_hole = RoundHole(5)
        assert round_hole.get_radius() == 5

    def test_round_peg_fits_round_hole(self) -> None:
        round_hole = RoundHole(5)
        round_peg = RoundPeg(5)
        assert round_hole.fits(round_peg) is True

    def test_create_square_peg(self) -> None:
        square_peg = SquarePeg(5)
        assert square_peg.get_width() == 5

    def test_create_square_peg_adapter(self) -> None:
        square_peg = SquarePeg(5)
        square_peg_adapter = SquarePegAdapter(square_peg)
        assert square_peg_adapter.get_radius() == 5 * 2**0.5 / 2

    def test_square_peg_adapter_fits_round_hole(self) -> None:
        round_hole = RoundHole(5)
        square_peg_adapter = SquarePegAdapter(SquarePeg(5))
        assert round_hole.fits(square_peg_adapter) is True

    def test_square_peg_big_adapter_not_fits_round_hole(self) -> None:
        round_hole = RoundHole(5)
        square_peg_big_adapter = SquarePegAdapter(SquarePeg(10))
        assert round_hole.fits(square_peg_big_adapter) is False
