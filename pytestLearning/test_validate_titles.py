import pytest

def test_validate_titles():

    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is Gmail website"


    # if actual_title == expected_title:
    #     print("Test case pass")
    # else:
    #     print("Test case fail")
    print("Beginning")
    assert expected_title == actual_title, "Titles are not matched"
    assert "Gmails" in title, "Gmail does not contain title"
    assert False, "Forcefully failing the test"
    print("Ending")