import pytest

def get_data():

    return [
        ("trainer@way2automation.com", "gadsgasgdasgasg"),
        ("java@way2automation.com", "gad"),
        ("info@way2automation.com", "afsdfds")
    ]


@pytest.mark.parametrize("username, password", get_data())
def test_do_login(username, password):
    print(f"username: {username}, password: {password}")