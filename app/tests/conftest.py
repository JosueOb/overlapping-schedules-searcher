import pytest
import typing


@pytest.fixture
def get_test_file_path() -> typing.Callable:
    def _get_path(file_name: str) -> str:
        return f"app/tests/data/{file_name}"

    return _get_path


@pytest.fixture
def get_test_file_content(get_test_file_path: typing.Callable) -> typing.Callable:
    def _get_content(file_name: str) -> list[str]:
        file_path = get_test_file_path(file_name)
        with open(file=file_path, mode="r") as file:
            content = file.readlines()
            return [line.replace("\n", "").replace(" ", "") for line in content]

    return _get_content
