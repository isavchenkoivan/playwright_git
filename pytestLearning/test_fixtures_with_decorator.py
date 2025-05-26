import pytest

@pytest.fixture(scope="module")
def setup():
    print("Creating DB Connection")

    yield
    print("Closing DB Connection")

@pytest.fixture(scope="function")
def before():
    print("Open browser")

    yield
    print("Close browser")


# def test_do_login(setup, before):
#     print("Executing login test:")
#
#
# def test_user_reg(setup, before):
#     print("Executing User registration test:")



@pytest.mark.usefixtures("setup", "before")
def test_do_login():
    print("Executing login test:")

@pytest.mark.usefixtures("setup", "before")
def test_user_reg():
    print("Executing User registration test:")
