import pytest
from fraction import Fraction 


def test_initialization():
    """Verify that numerator and denominator are stored correctly."""
    fraction = Fraction(3, 4)

    assert fraction.numerator == 3
    assert fraction.denominator == 4


@pytest.mark.parametrize("numerator", [-3, 0, 3])
def test_valid_numerator(numerator: int) -> None:
    """Verify that negative, zero, and positive numerators are accepted."""
    fraction = Fraction(numerator, 4)

    assert fraction.numerator == numerator
    assert fraction.denominator == 4


@pytest.mark.parametrize(
    "numerator, denominator",
    [
        (1.5, 4),
        ("3", 4),
        (3, 2.5),
        (3, "4"),
    ],
)
def test_invalid_data_types(numerator, denominator) -> None:
    """Verify that non-integer values raise TypeError."""
    with pytest.raises(TypeError):
        Fraction(numerator, denominator)


@pytest.mark.parametrize("denominator", [0, -1, -4])
def test_invalid_denominator(denominator: int) -> None:
    """Verify that zero and negativ denominators raise ValueError."""
    with pytest.raises(ValueError):
        Fraction(3, denominator)


def test_read_only() -> None:
    """Verify that numerator and denominator are read-only."""
    fraction = Fraction(3, 4)

    with pytest.raises(AttributeError):
        fraction.numerator = 5

    with pytest.raises(AttributeError):
        fraction.denominator = 6


def test_equality() -> None:
    """Verify equality between equivalent fractions."""
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(3, 4) == Fraction(6, 8)
    assert Fraction(-1, 2) == Fraction(-2, 4)
    assert Fraction(0, 2) == Fraction(0, 5)
    assert not (Fraction(1, 2) == Fraction(3, 4))


def test_inequality() -> None:
    """Verify inequality between different fractions."""
    assert Fraction(1, 2) != Fraction(3, 4)
    assert Fraction(-1, 2) != Fraction(1, 2)
    assert Fraction(0, 4) != Fraction(1, 4)
    assert not (Fraction(1, 2) != Fraction(2, 4))


def test_less_than() -> None:
    """Verify the less than comparison between fractions."""
    assert Fraction(1, 2) < Fraction(3, 4)
    assert Fraction(-1, 2) < Fraction(1, 2)
    assert Fraction(0, 4) < Fraction(1, 4)
    assert not (Fraction(1, 2) < Fraction(2, 4))
    assert not (Fraction(3, 4) < Fraction(1, 2))


def test_less_than_or_eqyal() -> None:
    """Verify the less than or equal to comparison."""
    assert Fraction(1, 2) <= Fraction(3, 4)
    assert Fraction(1, 2) <= Fraction(2, 4)
    assert Fraction(-1, 2) <= Fraction(0, 4)
    assert not (Fraction(3, 4) <= Fraction(1, 2))


def test_greater_than() -> None:
    """Verify the greater than comparison between fractions. """
    assert Fraction(3, 4) > Fraction(1, 2)
    assert Fraction(1, 2) > Fraction(-1, 2)
    assert Fraction(1, 4) > Fraction(0, 4)
    assert not (Fraction(1, 2) > Fraction(2, 4))
    assert not (Fraction(1, 2) > Fraction(3, 4))


def test_greater_than_or_equal() -> None:
    """Verify the greater than or equal to comparison."""
    assert Fraction(3, 4) >= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(2, 4)
    assert Fraction(0, 4) >= Fraction(-1, 2)
    assert not (Fraction(1, 2) >= Fraction(3, 4))


def test_str_formatting() -> None:
    """Verify the readable string representation of fractions."""
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(-3, 4)) == "-3/4"
    assert str(Fraction(0, 5)) == "0/5"
    assert str(Fraction(2, 4)) == "2/4"


def test_repr_formatting() -> None:
    """Verify the official string representasjon of fractions."""
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"
    assert repr(Fraction(-3, 4)) == "Fraction(-3, 4)"
    assert repr(Fraction(0, 5)) == "Fraction(0, 5)"
    assert repr(Fraction(2, 4)) == "Fraction(2, 4)"


def test_addition() -> None:
    """Verify addition of fractions."""
    assert Fraction(1, 2) + Fraction(2, 4) == Fraction(1, 1)
    assert Fraction(1, 2) + Fraction(3, 4) == Fraction(5, 4)
    assert Fraction(-1, 2) + Fraction(1, 2) == Fraction(0, 1)
    assert Fraction(0, 4) + Fraction(1, 2) == Fraction(1, 2)


def test_subtraction() -> None:
    """Verify substration of fractions."""
    assert Fraction(1, 2) - Fraction(2, 4) == Fraction(0, 1)
    assert Fraction(1, 2) - Fraction(3, 4) == Fraction(-1, 4)
    assert Fraction(3, 4) - Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(1, 2) - Fraction(0, 4) == Fraction(1, 2)





