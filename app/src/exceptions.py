class ValidationError(Exception):
    """
    This exception is used when the line format is invalid.
    """
    pass


class FileReaderError(Exception):
    """
        This exception is used when reading a file fails.
    """
    pass


class OverlappingSchedulesError(Exception):
    """
        This exception is used when the schedule overlap search fails.
    """
    pass
