import pytest

def setup_module(module):
    print("Creating DB Connection")

def teardown_module(module):
    print("Closing DB Connection")

def setup_function(function):
    print("launching browser")

def teardown_function(function):
    print("closing browser")


def test_do_login():
    print("Executing login test:")


def test_user_reg():
    print("Executing User regestration test:")
