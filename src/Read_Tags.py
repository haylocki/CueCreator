import mutagen

from mutagen.id3 import ID3
from mutagen.mp3 import MP3


class Read_Tags:
    def get_audio_info(self, file_path: str) -> str:
        audio = mutagen.File(file_path, easy=True)
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

    def read_tag(tag_name: str, audio: mutagen) -> str:
        value = None

        if isinstance(tag_name, dict) or isinstance(tag_name, ID3):
            value = audio.get(tag_name, [b""])[0].decode("utf-8", "ignore")

        elif isinstance(tag_name, MP3):
            if audio != "TLEN":
                value = audio.get(tag_name, [b""])[0].decode("utf-8", "ignore")
            else:
                value = audio.info.length

        return value
