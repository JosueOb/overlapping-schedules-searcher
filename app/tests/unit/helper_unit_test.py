import pytest

from typing import Callable
from pytest_mock import MockFixture

from app.src.helpers import read_file, validate_content
from app.src.exceptions import FileReaderError, ValidationError


def test__read_file__returns_a_list_of_strings__if_file_is_valid(
    get_test_file_path: Callable,
    get_test_file_content: Callable
):
    file_name = "schedules.txt"
    test_file_path = get_test_file_path(file_name)
    expected_content = get_test_file_content(file_name)

    content = read_file(path=test_file_path)

    assert expected_content == content


@pytest.mark.parametrize(
    "file_path", ["imaginary_file.txt", "invalid_file.yml"]
)
def test__read_file__raise_an_error__when_file_is_invalid(
    file_path: str,
    get_test_file_path: Callable
):
    test_file_path = get_test_file_path(file_path)

    with pytest.raises(FileReaderError) as error:
        read_file(path=test_file_path)

    assert str(error.value) == f"Make sure that the file {test_file_path} exists and is a .txt file"


def test__read_file__raise_a_error__when_open_file_fails(
    get_test_file_path: Callable,
    get_test_file_content: Callable,
    mocker: MockFixture
):
    file_name = "schedules.txt"
    test_file_path = get_test_file_path(file_name)
    error_message = "Error"
    mock_opener = mocker.mock_open()
    mock_opener.side_effect = Exception(error_message)
    mocker.patch("builtins.open", mock_opener)

    with pytest.raises(FileReaderError) as error:
        read_file(path=test_file_path)

    assert str(error.value) == error_message


def test__validate_content__returns_a_list_of_strings__when_its_content_is_valid(
    input_schedule_factory: Callable
):
    expected_content = input_schedule_factory(n_inputs=5)
    validated_content = validate_content(content=expected_content)

    assert validated_content == expected_content


def test__validate_content__raises_an_error__when_the_content_is_invalid():
    invalid_content = [
        "USER-1:",
        "USER1:MO",
        "USER1:MO07:00",
        "USER1:MO07:00-17:00,SU",
        "USER1:MO07:00-17:00,SU09:00",
        "USER1:MO07:00-17:00,SU09:00-13-00...",
    ]
    expected_error_messages = [
        f"The format of line n# {index + 1} is invalid '{line}'"
        for index, line in enumerate(invalid_content)
    ]
    with pytest.raises(ValidationError) as error:
        validate_content(content=invalid_content)

    assert str(error.value) == "\n".join(expected_error_messages)
