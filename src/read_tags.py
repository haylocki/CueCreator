from typing import Any

from mutagen import File  # pyright: ignore[reportPrivateImportUsage]
from mutagen.id3 import ID3
from mutagen.mp3 import MP3


class Read_Tags:
    def get_audio_info(self, file_path: str) -> dict[str, Any] | None:
        audio = File(file_path, easy=True)
        if not audio:
            return None

        title = self.read_tag("TIT2", audio)
        artist = self.read_tag("TPE1", audio)
        album = self.read_tag("TALB", audio)
        track_number = self.read_tag("TRCK", audio)
        genre = self.read_tag("TCON", audio)
        year = self.read_tag("TYER", audio)
        duration = self.read_tag("TLEN", audio)

        return {
            "title": title,
            "artist": artist,
            "album": album,
            "track_number": track_number,
            "genre": genre,
            "year": year,
            "duration": duration,
        }

    def read_tag(self, tag_name: str, audio: Any) -> str | float | None:
        if isinstance(audio, (dict, ID3)):
            value = audio.get(tag_name, [b""])
            if not value:
                return None
            return value[0].decode("utf-8", "ignore")

        if isinstance(audio, MP3):
            if tag_name == "TLEN":
                return audio.info.length
            value = audio.get(tag_name, [b""])
            if not value:
                return None
            return value[0].decode("utf-8", "ignore")

        return None
