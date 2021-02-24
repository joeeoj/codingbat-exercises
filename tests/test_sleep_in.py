import pytest

from warmup.sleep_in import sleep_in


def test_vacation_weekday():
    assert sleep_in(True, True) is True

def test_vacation_weekend():
    assert sleep_in(False, True) is True

def test_weekend_not_vacation():
    assert sleep_in(False, False) is True

def test_weekday_not_vacation():
    assert sleep_in(True, False) is False
