from album import Album
from format_time import Format_Time
from track_info import Track_Info


class Load_Tracks:
    def __init__(self):
        self.track_info = Track_Info()
        self.time = Format_Time()

    def update_audio_files_list(
        self, audio_files: list, album: Album, timings: list
    ) -> None:

        album_name = album_artist = genre = date = discid = comment = ""
        for track_count, audio_file in enumerate(audio_files, start=1):
            (
                album_name,
                album_artist,
                genre,
                date,
                discid,
                comment,
            ) = self.track_info.read(album, audio_file, track_count)

            timings.append(self.time.cue_format("0"))

        album.set_name(album_name)
        album.set_album_artist(album_artist)
        album.set_genre(genre)
        album.set_date(date)
        album.set_discid(discid)
        album.set_comment(comment)
        album.tracks.resize()
