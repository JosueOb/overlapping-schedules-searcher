import pytest

from typing import Callable
from pytest_mock import MockFixture

from app.src import read_file, FileReaderError


@pytest.mark.reader
def test__read_file__returns_its_content(
    get_test_file_path: Callable,
    get_test_file_content: Callable
):
    file_name = "schedules.txt"
    test_file_path = get_test_file_path(file_name)
    expected_content = get_test_file_content(file_name)

    content = read_file(path=test_file_path)

    assert expected_content == content


@pytest.mark.reader
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


@pytest.mark.reader
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
