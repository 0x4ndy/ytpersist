from enum import Enum

TEMPORARY_DIRECTORY: str = "tmp"


class FileFormat(Enum):
    MP3 = ".mp3"
    MP4 = ".mp4"


def build_file_name(file_name: str, file_format: FileFormat) -> str:
    new_file_name = file_name
    if not file_name.lower().endswith(file_format.value):
        new_file_name += file_format.value

    return new_file_name
