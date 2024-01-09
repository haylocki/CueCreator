import sys

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
)

from Album import Album
from Load_Timings_Dialog import Load_Timings_dialog
from Load_Tracks import Load_Tracks
from Load_Tracks_Dialog import Load_Tracks_Dialog
from Save_Cue_File import Save_Cue_File
from Track_Number import Track_Number


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
        self.load_button.clicked.connect(self.directory_dialog)
        button_layout.addWidget(self.load_button)

        self.load_timings_button = QPushButton("Load Timings")
        self.load_timings_button.clicked.connect(self.load_timings_dialog)
        button_layout.addWidget(self.load_timings_button)

        self.save_button = QPushButton("Save Cue File")
        self.save_button.clicked.connect(self.save_to_file)
        button_layout.addWidget(self.save_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.directory_dialog()

    def directory_dialog(self) -> None:
        self.track_dialog.directory_dialog(self.album, self.timings)

    def load_timings_dialog(self) -> None:
        self.timings_dialog.timings_dialog(self.album, self.timings)

    def save_to_file(self) -> None:
        self.save_cue_file.save(self.album, self.timings)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_Window()
    window.show()

    sys.exit(app.exec_())
