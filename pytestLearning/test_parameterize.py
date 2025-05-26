import pytest
import allure
from allure_commons.types import AttachmentType


def get_data():

    return [
        ("trainer@way2automation.com", "gadsgasgdasgasg"),
        ("java@way2automation.com", "gad"),
        ("info@way2automation.com", "afsdfds")
    ]

@allure.feature("Login Test")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username, password", get_data())
def test_do_login(page, username, password):
    with allure.step(f"Enter username and password {username}, and {password}"):
        page.fill("#email", username)
        page.fill("#pass", password)
        print(f"username: {username}, password: {password}")
        # assert 1 == 2
    #allure.attach(page.screenshot(path="screenshot/fullpage.png"), name="dologin", attachment_type=AttachmentType.PNG)