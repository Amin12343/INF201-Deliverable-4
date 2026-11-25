class Temperature:
    """Represents a temperature in Celsius ("C"), Fahrenheit ("F") or Kelvin ("K")."""

    VALID_UNITS: tuple[str, str, str] = ("C", "F", "K")  # the only units that are allowed
    TOLERANCE: float = 1e-9  # tolerance used when floating-point values are compared

    def __init__(self, value: int | float, unit: str = "C") -> None:
        """
        Initialise the Temperature.

        Args:
            value: The temperature value.
            unit: The unit "C", "F" or "K", not case-sensitive (default = "C").

        Raises:
            ValueError: If the unit is not valid, or if the temperature is below absolute zero (0 K).
        """
        unit = unit.upper()  # "c" and "C" are treated as the same unit
        if unit not in self.VALID_UNITS:  # stop if the unit is unknown
            raise ValueError(f"Invalid unit '{unit}'. Use 'C', 'F' or 'K'.")

        self._value = float(value)  # protected, so it can only be read through the property
        self._unit = unit  # protected, so it can only be read through the property

        if self.to_kelvin() < -self.TOLERANCE:  # below 0 K, with tolerance for rounding errors
            raise ValueError(f"{value} {unit} is below absolute zero.")

    @property
    def value (self) -> float: 
        """Public read-only property to inspect the temperature value."""
        return self._value
    

    @property
    def unit(self) -> str:
        """Public read-only property to inspect the temperature unit. """
        return self._unit
    

    def to_celsius(self) -> float:
        """
        Convert the temperature to Celsius 

        Returns: 
            The temperature in Celsius 
        """
        if self._unit == "K": #from Kelvin 
            return self._value - 273.15
        if self._unit == "F": #from Fahrenheit 
            return (self._value - 32) * 5 / 9 
        return self._value #already in Celsius 


    def to_fahrenheit(self) -> float: 
        """
        Convert the temperature to Fahrenheit 

        Returns: 
            The temperature in Fahrenheit 
        """
        if self._unit == "C": #From celsius 
            return self._value * 9 / 5 + 32 
        if self._unit == "K": #from kelvin
            return (self._value - 273.15) * 9 / 5 + 32 
        return self._value #already in fahrenheit 


    def to_kelvin(self) -> float:
        """
        convert the temperature to kelvin 

        Returns: 
            the temperature in Kelvin 
        """
        if self._unit == "C": #from celsius 
            return self._value + 273.15
        if self._unit == "F": #from fahrenheit 
            return (self._value - 32) * 5 / 9 +273.15
        return self._value #already in Kelvin 


    def convert_to (self, target_unit: str) -> "Temperature": 
        """
        Create a new Temperature converted to another unit. 

        Args: 
            target_unit: the unit to convert to, "C", "F", or "K"

        Returns: 
            A new Temperature instance in the target unit 

        Raises: 
            ValueError: if target_unit is not valid. 
        """
        target_unit = target_unit.upper() #"f" and "F" are treated as the same unit 
        if target_unit == "C": #convert to celsius 
            return Temperature(self.to_celsius(), "C")
        if target_unit == "F": #Convert to fahrenheit 
            return Temperature(self.to_fahrenheit(), "F")
        if target_unit == "K": #cinvert to Kelvin 
            return Temperature(self.to_kelvin(), "K")
        raise ValueError(f"invalid unit '{target_unit}'. use 'C', 'F' or 'K'.")
    
    
    def __repr__(self) -> str:
        """Unambiguous representation of the temperature, e.g. Temperature(25.0, 'C')."""
        return f"Temperature({self._value}, '{self._unit}')"

    def __str__(self) -> str:
        """Human-readable string with two decimals, e.g. 25.00 °C (Kelvin is written without °)."""
        if self._unit == "K":  # Kelvin is an absolute scale and has no degree sign
            return f"{self._value:.2f} K"
        return f"{self._value:.2f} °{self._unit}"

    def _kelvin_difference(self, other: "Temperature") -> float:
        """
        Find the difference between two temperatures, measured in Kelvin.

        Args:
            other: The temperature to compare with.

        Returns:
            self minus other, in Kelvin.
        """
        return self.to_kelvin() - other.to_kelvin()

    def __eq__(self, other: object) -> bool:
        """Return True if the temperatures are equal within the tolerance, also across units."""
        if not isinstance(other, Temperature):  # only temperatures can be compared
            return NotImplemented
        return abs(self._kelvin_difference(other)) <= self.TOLERANCE

    def __ne__(self, other: object) -> bool:
        """Return True if the temperatures differ by more than the tolerance."""
        if not isinstance(other, Temperature):  # only temperatures can be compared
            return NotImplemented
        return abs(self._kelvin_difference(other)) > self.TOLERANCE

    def __lt__(self, other: object) -> bool:
        """Return True if self is colder than other by more than the tolerance."""
        if not isinstance(other, Temperature):  # only temperatures can be compared
            return NotImplemented
        return self._kelvin_difference(other) < -self.TOLERANCE

    def __le__(self, other: object) -> bool:
        """Return True if self is colder than or equal to other, within the tolerance."""
        if not isinstance(other, Temperature):  # only temperatures can be compared
            return NotImplemented
        return self._kelvin_difference(other) <= self.TOLERANCE

    def __gt__(self, other: object) -> bool:
        """Return True if self is warmer than other by more than the tolerance."""
        if not isinstance(other, Temperature):  # only temperatures can be compared
            return NotImplemented
        return self._kelvin_difference(other) > self.TOLERANCE

    def __ge__(self, other: object) -> bool:
        """Return True if self is warmer than or equal to other, within the tolerance."""
        if not isinstance(other, Temperature):  # only temperatures can be compared
            return NotImplemented
        return self._kelvin_difference(other) >= -self.TOLERANCE