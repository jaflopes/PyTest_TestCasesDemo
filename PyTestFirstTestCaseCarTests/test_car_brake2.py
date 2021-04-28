import pytest

from TestCasesDemo.PyTestFirstTestCaseCar.car import Car

# speed_data = {45}
speed_data = {45, 50, 55, 100}


@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake2(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake
