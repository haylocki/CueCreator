import os
from io import TextIOBase

from PyQt6.QtWidgets import QFileDialog, QMessageBox

from album import Album
from track_number import Track_Number

TRACK_NUMBER_COLUMN = 0
ARTIST_NAME_COLUMN = 1
TITLE_COLUMN = 2
FILENAME_COLUMN = 4


class Save_Cue_File:
    def __init__(self):
        self.track_number = Track_Number()

    def save(self, album: Album, timings: list, directory) -> None:
        filename, _ = QFileDialog.getSaveFileName(
            None, "Save File", directory, "Cue Files (*.cue)"
        )

        if filename:
            with open(filename, "w") as file:
                self.write_header(file, album)
                self.write_tracks(file, album, timings)

            QMessageBox.information(None, "Save", "Cue file saved successfully.")

    def write_header(self, file: TextIOBase, album: Album) -> None:
        file.write(f"REM GENRE {album.get_genre()}\n")
        file.write(f"REM DATE {album.get_date()}\n")
        file.write(f"REM DISCID {album.get_discid()}\n")
        file.write(f"REM COMMENT {album.get_comment()}\n")
        file.write(f"PERFORMER {album.get_album_artist()}\n")
        file.write(f"TITLE {album.get_name()}\n")

    def write_tracks(self, file: TextIOBase, album: Album, timings: list) -> None:
        previous_filename = ""

        for index in range(len(timings)):
            track = album.tracks.list.topLevelItem(index)
            if track is not None:
                track_num = track.text(TRACK_NUMBER_COLUMN)
                artist = track.text(ARTIST_NAME_COLUMN)
                title = track.text(TITLE_COLUMN)
                filename = os.path.basename(track.text(FILENAME_COLUMN))
                extn = album.tracks.get_extn(index)

                if filename != previous_filename:
                    file.write(f'FILE "{filename}" {extn}\n')
                    previous_filename = filename

                file.write(f"  TRACK {int(track_num):02d} AUDIO\n")
                file.write(f'    TITLE "{title}"\n')
                file.write(f'    PERFORMER "{artist}"\n')
                file.write(f"    INDEX 01 {timings[index]}\n")
