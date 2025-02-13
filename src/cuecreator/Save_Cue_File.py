import os

from io import TextIOBase
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Album import Album
from Track_Number import Track_Number

TRACK_NUMBER_COLUMN = 0
ARTIST_NAME_COLUMN = 1
TITLE_COLUMN = 2
FILENAME_COLUMN = 4


class Save_Cue_File:
    def __init__(self):
        self.track_number = Track_Number()

    def save(self, album: Album, timings: list) -> None:
        filename, _ = QFileDialog.getSaveFileName(
            None, "Save File", os.getcwd(), "Cue Files (*.cue)"
        )

        if filename:
            file = open(filename, "w")
            self.write_header(file, album)
            self.write_tracks(file, album, timings)

            QMessageBox.information(None, "Save", "Cue file saved successfully.")

    def write_header(self, file: TextIOBase, album: Album) -> None:
        file.write(f"REM GENRE {album.get_genre()}\n")
        file.write(f"REM DATE {album.get_date()}\n")
        file.write(f"REM DISCID {album.get_discid()}\n")
        file.write(f"REM COMMENT {album.get_comment()}\n")
        file.write(f"REM PERFORMER {album.get_album_artist()}\n")
        file.write(f"REM TITLE {album.get_name()}\n")

    def write_tracks(self, file: TextIOBase, album: Album, timings: list) -> None:
        for index in range(len(timings)):
            item = album.tracks.list.topLevelItem(index)
            track_num = item.text(TRACK_NUMBER_COLUMN)
            artist = item.text(ARTIST_NAME_COLUMN)
            title = item.text(TITLE_COLUMN)
            filename = os.path.basename(item.text(FILENAME_COLUMN))
            extn = album.tracks.get_extn(index)

            file.write(f'FILE "{filename}" {extn}\n')
            file.write(f"  Track {int(track_num):02d} AUDIO\n")
            file.write(f'    TITLE "{title}"\n')
            file.write(f'    PERFORMER "{artist}"\n')
            file.write(f"    INDEX 01 {timings[index]}\n")
