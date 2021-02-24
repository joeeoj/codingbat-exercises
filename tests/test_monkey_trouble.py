import pytest

from warmup.monkey_trouble import monkey_trouble


def test_both_smiling():
    assert monkey_trouble(True, True) is True

def test_both_not_smiling():
    assert monkey_trouble(False, False) is True

def test_first_not_smiling():
    assert monkey_trouble(False, True) is False

def test_second_not_smiling():
    assert monkey_trouble(True, False) is False
