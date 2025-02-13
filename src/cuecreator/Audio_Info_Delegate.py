from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QStyledItemDelegate


class AudioInfoDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == 1:
            value = index.model().data(index, Qt.DisplayRole)
            if value.isNull():
                text = ""
            else:
                text = value.toString()

            painter.save()

            font = painter.font()
            font.setBold(True)
            painter.setFont(font)

            brush = QBrush(Qt.black)
            painter.setPen(Qt.black)
            painter.setBrush(brush)

            painter.drawText(option.rect, Qt.AlignCenter, text)

            painter.restore()
        else:
            super().paint(painter, option, index)

    def setModelData(self, editor, model, index):
        if index.column() == 1:
            model.setData(index, editor.text(), Qt.DisplayRole)
        else:
            super().setModelData(editor, model, index)
