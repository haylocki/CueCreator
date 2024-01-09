from PyQt5.QtWidgets import QStyledItemDelegate


class Track_Item_Delegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
