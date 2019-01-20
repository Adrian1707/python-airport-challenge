from airport import Airport, CapacityReachedError, StormyWeather
import pytest
from doubles import allow

a = Airport()
allow(a).weather_is_stormy.and_return(False)

def test_planes():
    assert a.planes == []

def test_capacity_defaults_to_five():
    assert a.capacity == 5

def test_capacity_when_alternative_number_is_passed_in():
    a = Airport(10)

    allow(a).weather_is_stormy.and_return(False)
    assert a.capacity == 10

def test_planes_array_contains_plane_when_landing_happenes():
    allow(a).weather_is_stormy.and_return(False)
    a.land("plane")

    assert a.planes == ["plane"]

def test_planes_array_releases_plane_on_take_off():
    a = Airport()
    allow(a).weather_is_stormy.and_return(False)
    a.land("plane1")
    a.land("plane2")

    a.take_off("plane1")

    assert a.planes == ["plane2"]

def test_does_not_allow_more_planes_than_capacity_allows():
    a = Airport(capacity = 3)
    allow(a).weather_is_stormy.and_return(False)
    a.land("plane1")
    a.land("plane2")
    a.land("plane3")

    with pytest.raises(CapacityReachedError):
        a.land("plane4")

def test_does_not_allow_landing_when_weather_is_stormy():
    a = Airport()
    allow(a).weather_is_stormy.and_return(True)

    with pytest.raises(StormyWeather):
        a.land("plane1")
