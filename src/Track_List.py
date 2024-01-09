import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QAbstractItemView, QTreeWidgetItem

from Album_Tree_Widget import Album_Tree_Widget
from Track_Item_Delegate import Track_Item_Delegate

FIRST_ROW = 0
TRACK_NUMBER_COLUMN = 0
ARTIST_NAME_COLUMN = 1
TITLE_COLUMN = 2
FILENAME_COLUMN = 4


class Track_List:
    def __init__(self):
        self.list = Album_Tree_Widget()
        self.list.setEditTriggers(
            QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked
        )
        self.list.setItemDelegate(Track_Item_Delegate(self.list))
        self.list.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def get_tracks(self) -> Album_Tree_Widget:
        return self.list

    def clear(self) -> None:
        self.list.clear()

    def add_track(
        self, track_num: str, artist: str, title: str, track_time: str, audio_file: str
    ) -> None:
        item = QTreeWidgetItem(self.list)
        self.add_item(item, 0, track_num, "#CCCCCC")
        self.add_item(item, 1, artist, "#E0E0E0")
        self.add_item(item, 2, title, "#CCCCCC")
        self.add_item(item, 3, track_time, "#E0E0E0")
        self.add_item(item, 4, audio_file, "#CCCCCC")

    def add_item(
        self, item: QTreeWidgetItem, column: int, text: str, colour: str
    ) -> None:
        item.setText(column, f"{text}")
        item.setBackground(column, QBrush(QColor(colour)))
        item.setFlags(item.flags() | Qt.ItemIsEditable)

    def number_of_tracks(self) -> int:
        return self.list.topLevelItemCount()

    def get_track_number(self, index: int) -> str:
        item = self.list.topLevelItem(index)
        return item.text(TRACK_NUMBER_COLUMN)

    def get_track_title(self, index: int) -> str:
        item = self.list.topLevelItem(index)
        return item.text(TITLE_COLUMN)

    def get_filename(self, index: int) -> str:
        item = self.list.topLevelItem(index)
        filename = item.text(FILENAME_COLUMN)
        return filename

    def get_extn(self, index: int) -> str:
        item = self.list.topLevelItem(index)
        filename = item.text(FILENAME_COLUMN)
        _, extn = os.path.splitext(filename)
        extn = extn.upper()[1:]
        
        if extn != "MP3":
            extn = "WAVE"
        
        return extn

    def resize(self) -> None:
        self.list.setCurrentItem(self.list.topLevelItem(0))

        for col in range(self.list.columnCount()):
            self.list.resizeColumnToContents(col)
