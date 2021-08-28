import os

from ytpersist.ytpersist import YTPersist

from ytpersist.helper import build_file_name, FileFormat


def create_yt_persist(working: bool = True) -> YTPersist:
    url = "https://www.youtube.com/watch?v=bad-url-Oc1Raa1fAFg"

    if working:
        url = "https://www.youtube.com/watch?v=Oc1Raa1fAFg"

    yt_persist = YTPersist(url)

    return yt_persist


def test_build_mp3_file_name_with_valid_extension():
    file_name = "file.mp3"

    new_file_name = build_file_name(file_name, FileFormat.MP3)

    assert new_file_name == "file.mp3"


def test_build_mp4_file_name_with_valid_extension():
    file_name = "file.mp4"
    new_file_name = build_file_name(file_name, FileFormat.MP4)

    assert new_file_name == "file.mp4"


def test_build_mp3_file_name_with_invalid_extension():
    file_name = "file.ext"
    new_file_name = build_file_name(file_name, FileFormat.MP3)

    assert new_file_name == "file.ext.mp3"


def test_build_mp4_file_name_with_invalid_extension():
    file_name = "file.ext"
    new_file_name = build_file_name(file_name, FileFormat.MP4)

    assert new_file_name == "file.ext.mp4"


def test_build_mp3_file_name_with_no_extension():
    file_name = "file"
    new_file_name = build_file_name(file_name, FileFormat.MP3)

    assert new_file_name == "file.mp3"


def test_build_mp4_file_name_with_no_extension():
    file_name = "file"
    new_file_name = build_file_name(file_name, FileFormat.MP4)

    assert new_file_name == "file.mp4"


def test_video_available():
    yt_persist = create_yt_persist()
    assert yt_persist.is_url_available() == True


def test_video_not_available():
    yt_persist = create_yt_persist(False)
    assert not yt_persist.is_url_available() == True


def test_get_video_title():
    yt_persist = create_yt_persist()
    assert yt_persist.get_title() == "YTPersist - test mp4 file"


def test_download_video_mp4_with_name():
    yt_persist = create_yt_persist()
    file_name = "filename.mp4"
    file_path = yt_persist.download(".", file_name, FileFormat.MP4)

    assert os.stat(file_path).st_size == 52226
    os.remove(file_path)


def test_download_video_mp4_witout_name():
    yt_persist = create_yt_persist()
    file_path = yt_persist.download(dir=".", file_format=FileFormat.MP4)

    assert os.stat(file_path).st_size == 52226
    os.remove(file_path)


def test_download_video_without_format_without_name():
    yt_persist = create_yt_persist()
    file_path = yt_persist.download(dir=".")

    assert os.stat(file_path).st_size == 52226
    os.remove(file_path)


def test_download_with_no_parameters():
    yt_persist = create_yt_persist()
    file_path = yt_persist.download()

    assert os.stat(file_path).st_size == 52226
    os.remove(file_path)


def test_download_to_mp3():
    yt_persist = create_yt_persist()
    file_name = "mp3_format"
    file_path = yt_persist.download(
        file_name=file_name, file_format=FileFormat.MP3)

    assert os.stat(file_path).st_size == 242251
    os.remove(file_path)


def test_download_mp4_no_remove():
    yt_persist = create_yt_persist()
    file_path = yt_persist.download()

    assert os.stat(file_path).st_size == 52226


def test_download_mp3_no_remove():
    yt_persist = create_yt_persist()
    file_path = yt_persist.download(file_format=FileFormat.MP3)

    assert os.stat(file_path).st_size == 242251
