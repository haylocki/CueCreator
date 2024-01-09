from PyQt5.QtWidgets import QLineEdit

from Track_List import Track_List


class Album:
    def __init__(self, album_name: QLineEdit, album_artist: QLineEdit):
        self.album_name_edit = album_name
        self.album_artist_edit = album_artist
        self.tracks = Track_List()
        self.genre = ""
        self.date = ""
        self.discid = ""
        self.comment = ""

    def set_name(self, title: str):
        self.album_name_edit.setText(title)

    def get_name(self) -> str:
        return self.album_name_edit.text()

    def set_album_artist(self, artist: str):
        self.album_artist_edit.setText(artist)

    def get_album_artist(self) -> str:
        return self.album_artist_edit.text()

    def set_genre(self, genre: str):
        self.genre = genre

    def get_genre(self) -> str:
        return self.genre

    def set_date(self, date: str):
        self.date = date

    def get_date(self) -> str:
        return self.date

    def set_discid(self, discid: str):
        self.discid = discid

    def get_discid(self) -> str:
        return self.discid

    def get_comment(self) -> str:
        return self.comment

    def set_comment(self, comment: str):
        self.comment = comment
