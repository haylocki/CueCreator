import os
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from album import Album
from load_timings_dialog import Load_Timings_dialog
from load_tracks import Load_Tracks
from load_tracks_dialog import Load_Tracks_Dialog
from save_cue_file import Save_Cue_File
from track_number import Track_Number


class Main_Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Audio File Info")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        self.track_dialog = Load_Tracks_Dialog()
        self.timings_dialog = Load_Timings_dialog()
        self.load_tracks = Load_Tracks()
        self.save_cue_file = Save_Cue_File()
        self.track_number = Track_Number()

        self.timings = []
        self.album_name_label = QLabel("Album Name")
        self.album_name = QLineEdit("")
        self.track_directory = os.getcwd()
        main_layout.addWidget(self.album_name_label)
        main_layout.addWidget(self.album_name)

        self.album_artist_label = QLabel("Album Artist")
        self.album_artist = QLineEdit("")
        main_layout.addWidget(self.album_artist_label)
        main_layout.addWidget(self.album_artist)

        self.album = Album(self.album_name, self.album_artist)

        main_layout.addWidget(self.album.tracks.list)

        button_layout = QHBoxLayout()

        self.load_button = QPushButton("Load Directory")
        self.load_button.clicked.connect(self.track_directory_dialog)
        button_layout.addWidget(self.load_button)

        self.load_timings_button = QPushButton("Load Timings")
        self.load_timings_button.clicked.connect(self.load_timings_dialog)
        button_layout.addWidget(self.load_timings_button)

        self.save_button = QPushButton("Save Cue File")
        self.save_button.clicked.connect(self.save_to_file)
        button_layout.addWidget(self.save_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.track_directory = self.track_directory_dialog()

    def track_directory_dialog(self) -> str:
        self.track_directory = self.track_dialog.track_directory_dialog(
            self.album, self.timings, self.track_directory
        )
        return self.track_directory

    def load_timings_dialog(self) -> None:
        self.timings_dialog.timings_dialog(
            self.album, self.timings, self.track_directory
        )

    def save_to_file(self) -> None:
        self.save_cue_file.save(self.album, self.timings, self.track_directory)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_Window()
    window.show()

    sys.exit(app.exec())
