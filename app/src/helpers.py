import re
import pathlib
from .exceptions import ValidationError, FileReaderError
from .utils import ABBREVIATION_DAYS


def read_file(path: str) -> list[str]:
    if not _is_file_valid(path):
        raise FileReaderError(f"Make sure that the file {path} exists and is a .txt file")
    try:
        with open(file=path, mode='r', encoding='utf-8') as line:
            lines = line.readlines()
            return _format_content(content=lines)
    except Exception as error:
        raise FileReaderError(str(error)) from error


def validate_content(content: list[str]) -> list[str]:
    error_messages = []
    for index, line in enumerate(content):
        if not _is_the_line_valid(line):
            error_messages.append(f"The format of line n# {index + 1} is invalid '{line}'")

    if error_messages:
        raise ValidationError("\n".join(error_messages))

    return content


def _is_file_valid(file_path: str, allowed_extension: str = ".txt") -> bool:
    file = pathlib.Path(file_path)
    return True if file.exists() and file.suffix == allowed_extension else False


def _format_content(content: list[str]) -> list[str]:
    return [line.replace("\n", "").replace(" ", "").rstrip(",") for line in content]


def _is_the_line_valid(line: str) -> bool:
    regex = (
        r"^(\w+)=("
        rf"({'|'.join(ABBREVIATION_DAYS)})"
        r"(0[0-9]|1[0-9]|2[0-3])"
        r":([0-5][0-9])"
        r"-(0[0-9]|1[0-9]|2[0-3])"
        r":([0-5][0-9]),?"
        r")*?$"
    )
    return bool(re.search(pattern=regex, string=line))
