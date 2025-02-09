import pytest
from .main import check_password

@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("123456789", False),
        ("abc1234567", False),
        ("password@123", False),
        ("A1@123456789012345", False),
        ("Password@!", False),
        ("A1@abcd", False),
        ("Password123", False),
        ("Pass@word1", True),
    ],
    ids=[
        "Password_contains_only_numbers",
        "Password_without_uppercase_letter",
        "Password_without_uppercase_but_with_special_and_digit",
        "Password_more_than_16_symbols",
        "Password_without_digit",
        "Password_less_than_8_symbols",
        "Password_without_special_character",
        "Correct_password_case",
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    result = check_password(password)
    assert result is expected_result
