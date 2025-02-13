import os

from PyQt5.QtWidgets import QFileDialog

from Album import Album
from Format_Time import Format_Time
from Track_Info import Track_Info

FILENAME_COLUMN = 4


class Load_Timings_dialog:
    def __init__(self):
        self.time = Format_Time()
        self.track_info = Track_Info()

    def timings_dialog(self, album: Album, timings: list) -> None:
        timings_file, _ = QFileDialog.getOpenFileName(
            None, "Select File", os.getcwd(), "Text Files (*.txt);;All Files (*)"
        )

        if timings_file:
            timings.clear()

            with open(timings_file, "r") as file:
                first_track = album.tracks.list.topLevelItem(0)
                filename = first_track.text(FILENAME_COLUMN)
                album.tracks.clear()

                track_count = 0
                for line in file:
                    track_count += 1
                    time = line.split("\t")
                    timings.append(self.time.cue_format(float(time[0])))

                    (
                        album_name,
                        album_artist,
                        genre,
                        date,
                        discid,
                        comment,
                    ) = self.track_info.read(album, filename, track_count)

                album.set_name(album_name)
                album.set_album_artist(album_artist)
                album.set_genre(genre)
                album.set_date(date)
                album.set_discid(discid)
                album.set_comment(comment)
                album.tracks.resize()
