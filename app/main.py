from .src import read_field, validate_content, ValidationError


def search_overlapping_schedules(file_path: str) -> list[str]:
    try:
        file_content = read_field(path=file_path)
        validated_content = validate_content(content=file_content)
        # schedules_by_employee = group_schedules_by_employee()
        return validated_content
    except ValidationError as error:
        print(str(error))
