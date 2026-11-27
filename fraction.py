class Fraction:
    """Represent a fraction with an integer numerator and a positive intiger denominator.
    """

    def __init__(self, numerator, denominator):
        """Initialize a fraction and validate its input values."""
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer")

        if not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer")

        if denominator <= 0:
            raise ValueError("Denominator must be greater than 0")

        self._numerator = numerator
        self._denominator = denominator


    @property
    def numerator(self) -> int:
        """Return the numerator of the fraction."""
        return self._numerator


    @property
    def denominator(self) -> int:
        """Return the denominator of the fraction."""
        return self._denominator


    def __eq__(self, other: "Fraction") -> bool:
        """Check whether twe fractions are equal."""
        return (
            self.numerator * other._denominator
            == other._numerator * self._denominator
        )

    def __ne__(self, other: "Fraction") -> bool:
        """Check whether two fractions are not equal."""
        return not self == other 

    def __lt__(self, other: "Fraction") -> bool:
        """CHeck whether the first fraction is less than the second."""
        return (
            self._numerator * other._denominator
            < other._numerator * self._denominator
        )

    def __le__(self, other: "Fraction") -> bool:
        """Check whether the first fraction is less than or equal to the secound."""
        return self < other or self == other

    def __gt__(self, other: "Fraction") -> bool:
        """Check whether the first fraction is greater than the secund."""
        return other < self

    def __ge__(self, other: "Fraction") -> bool:
        """Check whether the first fraction is greater than or equal to the second."""
        return self > other or self == other

    def __str__(self) -> str:
        """Return a readable string representation of the fraction."""
        return f"{self.numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Return the official string representation of the fraction."""
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other: "Fraction") -> "Fraction":
        """Add two fractions and return a new Fraction object."""
        numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        denominator = self._denominator * other._denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Subtract two fractions and return a new Fraction object."""
        numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        denominator = self._denominator * other._denominator
        return Fraction(numerator, denominator)


fraction = Fraction(3, 4)
print(fraction.numerator)
print(fraction.denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(2, 4)
fraction3 = Fraction(3, 4)


print(fraction1 == fraction2)
print(fraction1 == fraction3)
print(fraction1 != fraction2)
print(fraction1 != fraction3)
print(fraction1 < fraction2)
print(fraction1 < fraction3)
print(fraction1 <= fraction2)
print(fraction1 <= fraction3)
print(fraction3 <= fraction1)
print(fraction1 > fraction2)
print(fraction1 > fraction3)
print(fraction3 > fraction1)
print(fraction1 >= fraction2)
print(fraction1 >= fraction3)
print(fraction3 >= fraction1)
print(fraction1)
print(fraction2)
print(fraction3)
print(repr(fraction1))
print(repr(fraction2))
print(repr(fraction3))
print(fraction1 + fraction2)
print(fraction1 + fraction3)
print(fraction1 - fraction2)
print(fraction1 - fraction3)
print(fraction3 - fraction1)


