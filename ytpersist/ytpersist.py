import os
import tempfile

from moviepy.editor import VideoFileClip as vfc
from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube as YT

from .helper import FileFormat, build_file_name, TEMPORARY_DIRECTORY


class YTPersist():
    __url: str
    __yt: YT

    def __init__(self, url: str):
        """
        Constructor with one string parameter being the url to the YouTube video
        """
        self.__url = url
        self.__yt = YT(url)  # Creates a pytube object

    def is_url_available(self) -> bool:
        """
        Simplified method of checking whether a video is available for download.
        """
        try:
            # This rises a number of different exceptions but we only care
            # about whether we can download a video or not
            self.__yt.check_availability()
        except:
            return False

        return True

    def get_title(self) -> str:
        """
        Returns the video title.
        """
        return self.__yt.title

    def get_url(self) -> str:
        """
        Returns the video url.
        """
        return self.__url

    def download(self, dir: str = ".", file_name: str = None, file_format: FileFormat = FileFormat.MP4) -> str:
        """
        Downloads the video and saves if in a defined directory with specific file name.
        The directory by default is set to current folder. If the file name is not passed, the video title is used instead. 
        If the format is MP3, the downloaded video is converted. 
        The final file name is renamed taking into account the format MP3 or MP4.
        If a file with the final name exists at the specified location, it will be overwritten.
        """
        # Generate a temporary file name.
        tmp_file_name = tempfile.NamedTemporaryFile().name

        # If temporary directory doesn't exist, create it.
        if not os.path.exists(TEMPORARY_DIRECTORY):
            os.mkdir(TEMPORARY_DIRECTORY)

        # Download the video to a temporary directory with a temporary name
        # and return it.
        tmp_abs_path = self.__yt.streams.first().download(
            output_path=TEMPORARY_DIRECTORY, filename=tmp_file_name)

        # If for some reasons the file doesn't exist, return None here.
        if not tmp_abs_path:
            # TODO: Log here that the file doesn't exist.
            return None

        # If the target file name is not passed or empty, use the video title.
        if not file_name or file_name == "":
            file_name = self.get_title()

        # Generate the target file name and absolute path.
        file_name = build_file_name(file_name, file_format)
        abs_path = os.path.join(os.path.abspath(dir), file_name)

        # For MP4, just rename file to target location.
        # For MP3, convert it and save in target location.
        if file_format == FileFormat.MP4:
            os.rename(tmp_abs_path, abs_path)
        elif file_format == FileFormat.MP3:
            video = VideoFileClip(tmp_abs_path)
            video.audio.write_audiofile(abs_path)
            os.remove(tmp_abs_path)

        # If for some reasons the target file is not created, return None here.
        if not os.path.exists(abs_path):
            return None

        return abs_path
