import pytest

@pytest.mark.functional
def test_login():
    print("Executing login test")
@pytest.mark.regression
def test_user_reg():
    print("Executing User reg test")

@pytest.mark.functional
def test_compose_email():
    print("Executing compose email test")

@pytest.mark.skip
def test_skip():
    print("skipping test")