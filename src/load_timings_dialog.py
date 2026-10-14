from mutagen import File  # pyright: ignore[reportPrivateImportUsage]
from PyQt6.QtWidgets import QFileDialog

from album import Album
from format_time import Format_Time
from track_info import Track_Info

FILENAME_COLUMN = 4


class Load_Timings_dialog:
    def __init__(self):
        self.time = Format_Time()
        self.track_info = Track_Info()

    def timings_dialog(self, album: Album, timings: list, directory: str) -> None:
        timings_file, _ = QFileDialog.getOpenFileName(
            None, "Select File", directory, "Text Files (*.txt);;All Files (*)"
        )

        if not timings_file:
            return

        first_track = album.tracks.list.topLevelItem(0)
        if first_track is None:
            return

        filename = first_track.text(FILENAME_COLUMN)

        with open(timings_file, "r") as file:
            start_times = [float(line.split("\t")[0]) for line in file if line.strip()]

        audio_metadata = File(filename, easy=True)
        if audio_metadata is None:
            return

        audio_duration = audio_metadata.info.length

        timings.clear()
        album.tracks.clear()

        album_name = album_artist = genre = date = discid = comment = ""

        for track_count, start_time in enumerate(start_times, start=1):
            if track_count < len(start_times):
                track_duration = start_times[track_count] - start_time
            else:
                track_duration = audio_duration - start_time

            formatted_duration = self.time.track_format(str(track_duration))
            timings.append(self.time.cue_format(str(start_time)))

            (
                album_name,
                album_artist,
                genre,
                date,
                discid,
                comment,
            ) = self.track_info.read(album, filename, track_count, formatted_duration)

        album.set_name(album_name)
        album.set_album_artist(album_artist)
        album.set_genre(genre)
        album.set_date(date)
        album.set_discid(discid)
        album.set_comment(comment)
        album.tracks.resize()
