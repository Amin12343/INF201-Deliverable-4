import pytest 
from temperature import Temperature 

def test_default_unit():
    """Test that the default unit is Celsius when no unit is specified."""
    temp = Temperature(25)
    assert temp.unit == "C"
    assert temp.value == 25


@pytest.mark.parametrize("unit, expected",
                         [("c", "C"),
                          ("f", "F"),
                          ("k", "K"),
                          ("C", "C"),
                          ("F", "F"),
                          ("K", "K")])
def test_case_insensitive_units(unit, expected):
    """Test that units are case-insensitive. """
    temp = Temperature(25, unit)
    assert temp.unit == expected


def test_read_only():
    """Test that value and unit are read-only. """
    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"


def test_invalid_unit():
    """Test that an invalid unit raises a ValueError. """
    with pytest.raises(ValueError):
        Temperature(25, "X")


@pytest.mark.parametrize("value, unit",
                         [(-300, "C"),
                          (-500, "F"),
                          (-1, "K")])
def test_below_absolute_zero(value, unit):
    """Test that temperatures below absolute zero raise a ValueError."""
    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize("celsius, fahrenheit, kelvin",
                         [(-273.15, -459.67, 0),
                          (-40, -40, 233.15),
                          (0, 32, 273.15),
                          (37, 98.6, 310.15),
                          (100, 212, 373.15)])
def test_celsius_conversions(celsius, fahrenheit, kelvin):
    """Test conversions from Celsius to Fathrenheit and Kelvin."""
    temp = Temperature(celsius, "C")
    assert temp.to_fahrenheit() == pytest.approx(fahrenheit, abs=1e-9, rel=0)
    assert temp.to_celsius() == pytest.approx(celsius, abs=1e-9, rel=0)
    assert temp.to_kelvin() == pytest.approx(kelvin, abs=1e-9, rel=0)


@pytest.mark.parametrize("celsius, fahrenheit, kelvin",
                         [(-273.15, -459.67, 0),
                          (-40, -40, 233.15),
                          (0, 32, 273.15),
                          (37, 98.6, 310.15),
                          (100, 212, 373.15)])
def test_fahrenheit_conversions(celsius, fahrenheit, kelvin):
    """Test conversions from Fathrenheit to Calsius and Kelvin."""
    temp = Temperature(fahrenheit, "F")
    assert temp.to_celsius() == pytest.approx(celsius, abs=1e-9, rel=0)
    assert temp.to_fahrenheit() == pytest.approx(fahrenheit, abs=1e-9, rel=0)
    assert temp.to_kelvin() == pytest.approx(kelvin, abs=1e-9, rel=0)


@pytest.mark.parametrize("celsius, fahrenheit, kelvin",
                         [(-273.15, -459.67, 0),
                          (-40, -40, 233.15),
                          (0, 32, 273.15),
                          (37, 98.6, 310.15),
                          (100, 212, 373.15)])
def test_kelvin_conversions(celsius, fahrenheit, kelvin):
    """Test conversions from Kelvin to Celsius and Fahrenheit."""
    temp = Temperature(kelvin, "K")
    assert temp.to_celsius() == pytest.approx(celsius, abs=1e-9, rel=0)
    assert temp.to_fahrenheit() == pytest.approx(fahrenheit, abs=1e-9, rel=0)
    assert temp.to_kelvin() == pytest.approx(kelvin, abs=1e-9, rel=0)

                
@pytest.mark.parametrize("value", [-273.15, -40, 0, 37, 100])
def test_round_trip_conversions(value):
    """Test round-trip conversions from C to F to K and back to C."""
    original = Temperature(value, "C")
    fahrenheit = original.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    result = kelvin.convert_to("C")
    assert result.value == pytest.approx(original.value, abs=1e-9, rel=0)
    assert result.unit == original.unit

    
def test_cross_unit_equality():
    """Test equality across different temperature units."""
    celsius = Temperature(0, "C")
    fahrenheit = Temperature(32, "F")
    kelvin = Temperature(273.15, "K")

    assert celsius == fahrenheit
    assert celsius == kelvin
    assert fahrenheit == kelvin


def test_cross_unit_inequality():
    """Test inequality across different temperature units."""
    celsius = Temperature(0, "C")
    fahrenheit = Temperature(98.6, "F")
    kelvin = Temperature(373.15, "K")

    assert celsius != fahrenheit
    assert celsius != kelvin
    assert fahrenheit != kelvin


def test_cross_unit_ordering():
    """Test ordning across different temperature units."""
    cold = Temperature(0, "C")
    warm = Temperature(98.6, "F")
    hot = Temperature(373.15, "K")

    assert cold < warm
    assert warm < hot
    assert cold <= warm
    assert hot >= warm 
    assert hot > warm
    assert cold <= Temperature(32, "F")
    assert cold >= Temperature(32, "F")


def test_str_formatting():
    """Test the string representations of temperatures."""
    celsius = Temperature(25, "C")
    fahrenheit = Temperature(98.6, "F")
    kelvin = Temperature(273.15, "K")

    assert str(celsius) == "25.00 °C"
    assert str(fahrenheit) == "98.60 °F"
    assert str(kelvin) == "273.15 K"


def test_repr_formatting():
    """Test the repr representation of temperatures."""
    celsius = Temperature(25, "C")
    fahrenheit = Temperature(98.6, "F")
    kelvin = Temperature(273.15, "K")

    assert repr(celsius) == "Temperature(25.0, 'C')"
    assert repr(fahrenheit) == "Temperature(98.6, 'F')"
    assert repr(kelvin) == "Temperature(273.15, 'K')"


