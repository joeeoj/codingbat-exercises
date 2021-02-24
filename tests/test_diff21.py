import pytest

from warmup.diff21 import diff21


def test_one():
    assert diff21(1) == 20

def test_zero():
    assert diff21(0) == 21

def test_over_21():
    assert diff21(26) == 10

def test_negative():
    assert diff21(-21) == 42
