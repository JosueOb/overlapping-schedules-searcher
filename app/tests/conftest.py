import pytest
import random
from faker import Faker
from typing import Callable
from app.src.utils import ABBREVIATION_DAYS


@pytest.fixture
def get_test_file_path() -> Callable:
    def _get_path(file_name: str) -> str:
        return f"app/tests/data/{file_name}"

    return _get_path


@pytest.fixture
def get_test_file_content(get_test_file_path: Callable) -> Callable:
    def _get_content(file_name: str) -> list[str]:
        file_path = get_test_file_path(file_name)
        with open(file=file_path, mode="r") as file:
            content = file.readlines()
            return [line.replace("\n", "").replace(" ", "") for line in content]

    return _get_content


@pytest.fixture
def input_schedule_factory(faker: Faker) -> Callable:
    def _factory(n_schedules: int = 3, n_inputs: int = 3) -> list[str]:
        schedules = [
            (
                f"{random.sample(population=ABBREVIATION_DAYS, k=1)[0]}"
                f"{faker.time(pattern='%H:%M')}-{faker.time(pattern='%H:%M')}"
            ) for _ in range(0, n_schedules)
        ]
        return [
            f"{str(faker.first_name()).upper()}={','.join(schedules)}" for _ in range(0, n_inputs)
        ]

    return _factory
