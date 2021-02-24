import pytest

from warmup.sum_double import sum_double


def test_diff_values():
    assert sum_double(5, 6) == 11

def test_same_values():
    assert sum_double(5, 5) == 20

def test_zero():
    assert sum_double(0, 0) == 0

def test_negative():
    assert sum_double(10, -20) == -10
