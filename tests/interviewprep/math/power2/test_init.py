from __future__ import annotations

from interviewprep.math.power2 import (
    is_power_of_2,
    next_power_of_2_left,
    next_power_of_2_right,
)


def test_is_power_of_2_ints():
    assert is_power_of_2(1) is True
    assert is_power_of_2(2) is True
    assert is_power_of_2(4) is True
    assert is_power_of_2(8) is True
    assert is_power_of_2(16) is True
    assert is_power_of_2(5) is False
    assert is_power_of_2(6) is False
    assert is_power_of_2(7) is False
    assert is_power_of_2(9) is False
    assert is_power_of_2(10) is False


def test_next_power_of_2_left():
    assert next_power_of_2_left(0) == 1
    assert next_power_of_2_left(-1) == 1
    assert next_power_of_2_left(1) == 1
    assert next_power_of_2_left(2) == 2
    assert next_power_of_2_left(3) == 4
    assert next_power_of_2_left(4) == 4
    assert next_power_of_2_left(5) == 8
    assert next_power_of_2_left(6) == 8
    assert next_power_of_2_left(7) == 8
    assert next_power_of_2_left(8) == 8
    assert next_power_of_2_left(9) == 16

def test_next_power_of_2_right():
    assert next_power_of_2_right(0) == 1
    assert next_power_of_2_right(-1) == 1
    assert next_power_of_2_right(1) == 2
    assert next_power_of_2_right(2) == 4
    assert next_power_of_2_right(3) == 4
    assert next_power_of_2_right(4) == 8
    assert next_power_of_2_right(5) == 8
    assert next_power_of_2_right(6) == 8
    assert next_power_of_2_right(7) == 8
    assert next_power_of_2_right(8) == 16
    assert next_power_of_2_right(9) == 16
