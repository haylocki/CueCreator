import os

from PyQt6.QtWidgets import QFileDialog

from album import Album
from load_tracks import Load_Tracks
from track_number import Track_Number


class Load_Tracks_Dialog:
    def __init__(self, parent=None):
        self.parent = parent
        self.load_tracks = Load_Tracks()
        self.track_number = Track_Number()
        self.directory = os.getcwd()

    def track_directory_dialog(self, album: Album, timings: list, directory: str) -> str:
        selected_directory = QFileDialog.getExistingDirectory(
            self.parent, "Select Directory", directory
        )

        if selected_directory:
            self.directory = selected_directory

            timings.clear()
            self.audio_files = self.read_audio_files(self.directory)

            if self.audio_files:
                album.tracks.clear()
                self.load_tracks.update_audio_files_list(
                    self.audio_files, album, timings
                )

        return self.directory

    def read_audio_files(self, directory: str) -> list:
        audio_files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.endswith((".mp3", ".flac", ".wav"))
        ]

        return sorted(audio_files, key=self.track_number.get)
