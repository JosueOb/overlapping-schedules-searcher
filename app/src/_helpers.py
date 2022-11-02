import re
from ._exceptions import ValidationError


def read_field(path: str) -> list:
    with open(file=path, mode='r', encoding='utf-8') as line:
        lines = line.readlines()
        return _format_content(content=lines)


def validate_content(content: list[str]) -> list[str]:
    valid_content = []
    error_messages = []
    for index, line in enumerate(content):
        if not _is_the_line_valid(line):
            error_messages.append(f"The format of line n# {index + 1} is invalid.")

        valid_content.append(line)

    if error_messages:
        raise ValidationError("\n".join(error_messages))

    return valid_content


def _format_content(content: list[str]) -> list[str]:
    return [line.replace("\n", "").replace(" ", "") for line in content]


def _is_the_line_valid(line: str) -> bool:
    # regex = r"^\w+=((MO|TU|WE|TH|FR|SA|SU)$(0-9))+$"
    regex = r"^\w"
    return bool(re.search(pattern=regex, string=line))
