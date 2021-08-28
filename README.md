# YouTube Persist
This library is a wrapper combining both ``pytube`` and ``moviepy`` that can be used for simplified YouTube video downloads and converting them to mp3 format.

## Requirements
```
pytest==6.2.4
moviepy==1.0.3
pytube==11.0.1
```

## Usage
```python
from ytpersist.ytpersist import YTPersist
from ytpersist.helper import FileFormat

yt_persist = YTPersist("<youtube_url>")
yt_persist.download("<local_directory>", "<file_name>", FileFormat.MP3)
```