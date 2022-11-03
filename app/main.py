from .src.helpers import read_file, validate_content
from .src.exceptions import ValidationError, FileReaderError, OverlappingSchedulesError


def overlapping_schedules_searcher(file_path: str) -> list[str]:
    try:
        file_content = read_file(path=file_path)
        validated_file_content = validate_content(content=file_content)

        return validated_file_content

    except (FileReaderError, ValidationError) as error:
        raise OverlappingSchedulesError(str(error)) from error
