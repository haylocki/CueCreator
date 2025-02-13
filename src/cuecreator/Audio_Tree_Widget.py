import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem

from AudioInfoDelegate import AudioInfoDelegate
from Read_Tags import Read_Tags


# Set up icons
app_icon = QIcon("icon.png")
file_icon = QIcon("file.png")
folder_icon = QIcon("folder.png")
song_icon = QIcon("song.png")
time_icon = QIcon("time.png")


class AudioTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.audio_info_delegate = AudioInfoDelegate()
        self.read_tags = Read_Tags
        self.setItemDelegate(self.audio_info_delegate)
        self.setColumnCount(2)
        self.setHeaderLabels(["", "Duration"])

        self.file_icon = file_icon
        self.folder_icon = folder_icon
        self.song_icon = song_icon
        self.time_icon = time_icon

    def setModel(self, model):
        super().setModel(model)
        self.expandAll()

    def add_audio_file(self, file_path):
        audio = self.read_tags.get_audio_info(file_path)
        if audio is None:
            return

        file_item = QTreeWidgetItem([os.path.basename(file_path)])
        file_item.setData(0, Qt.UserRole, file_path)
        file_item.setIcon(0, self.file_icon)

        album_tag = audio.get("album", "")
        album_item = self.add_item(album_tag, self.folder_icon)

        artist_tag = audio.get("artist", "")
        artist_item = self.add_item(artist_tag, self.folder_icon)

        title_tag = audio.get("title", "")
        title_item = self.add_item(title_tag, self.song_icon)

        duration_tag = audio.get("duration", 0)
        duration_item = self.add_item(duration_tag, self.time_icon)

        file_item.addChild(album_item)
        album_item.addChild(artist_item)
        artist_item.addChild(title_item)
        title_item.addChild(duration_item)

        self.insertTopLevelItem(0, file_item)

    def add_item(self, tag, icon):
        item = QTreeWidgetItem([str(tag)])
        item.setData(0, Qt.UserRole, tag)
        item.setIcon(0, icon)

        return item
