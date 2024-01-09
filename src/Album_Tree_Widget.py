from PyQt5.QtWidgets import QTreeWidget


class Album_Tree_Widget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(5)
        self.setHeaderLabels(["Track", "Track Artist", "Title", "Time", "Filename"])
        self.setRootIsDecorated(False)
        self.setIndentation(0)
