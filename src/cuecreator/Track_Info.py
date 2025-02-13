import mutagen

from Album import Album
from Format_Time import Format_Time
from Track_Number import Track_Number


class Track_Info:
    def __init__(self):
        self.time = Format_Time()
        self.track = Track_Number()

    def read(self, album: Album, audio_file: str, track_count: int) -> str:
        audio_file_info = mutagen.File(audio_file, easy=True)

        track_number = self.track.format(audio_file_info.get("tracknumber", ["0"])[0])
        artist = audio_file_info.get("artist", ["Unknown"])[0]
        title = audio_file_info.get("title", ["Unknown"])[0]
        track_time = self.time.track_format(audio_file_info.info.length)
        genre = audio_file_info.get("genre", [""])[0]
        date = audio_file_info.get("date", [""])[0]
        discid = audio_file_info.get("discid", [""])[0]
        comment = audio_file_info.get("comment", [""])[0]
        album_name = audio_file_info.get("album", ["Unknown"])[0]
        album_artist = audio_file_info.get("albumartist", [artist])[0]
        
        if track_number == 0:
            track_number = track_count

        album.tracks.add_track(track_number, artist, title, track_time, audio_file)

        return album_name, album_artist, genre, date, discid, comment
