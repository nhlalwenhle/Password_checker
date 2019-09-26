import re

from password_checker import*


def test_password_length():
    assert password_is_valid(password) >= 8

def test_password_is_not_null():
	assert password_is_valid(password) != 0