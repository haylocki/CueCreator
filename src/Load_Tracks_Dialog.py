import os

from PyQt5.QtWidgets import QFileDialog

from Album import Album
from Load_Tracks import Load_Tracks
from Track_Number import Track_Number


class Load_Tracks_Dialog:
    def __init__(self, parent=None):
        self.parent = parent
        self.load_tracks = Load_Tracks()
        self.track_number = Track_Number()

    def directory_dialog(self, album: Album, timings: list) -> None:
        directory = QFileDialog.getExistingDirectory(
            self.parent, "Select Directory", os.getcwd()
        )

        if directory:
            timings.clear()
            self.audio_files = self.read_audio_files(directory)

            if self.audio_files:
                album.tracks.clear()
                self.load_tracks.update_audio_files_list(
                    self.audio_files, album, timings
                )

    def read_audio_files(self, directory: QFileDialog) -> list:
        audio_files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.endswith((".mp3", ".flac", ".wav"))
        ]

        return sorted(audio_files, key=self.track_number.get)
