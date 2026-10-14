from PyQt6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import (
    QLineEdit,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QWidget,
)


class AudioInfoDelegate(QStyledItemDelegate):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def paint(
        self,
        painter: QPainter | None,
        option: QStyleOptionViewItem,
        index: QModelIndex,
    ) -> None:
        assert painter is not None

        if index.column() == 1:
            model = index.model()
            assert model is not None

            value = model.data(index, Qt.ItemDataRole.DisplayRole)
            text = "" if value is None else str(value)

            painter.save()
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)
            painter.setPen(Qt.GlobalColor.black)
            painter.drawText(option.rect, Qt.AlignmentFlag.AlignCenter, text)
            painter.restore()
        else:
            super().paint(painter, option, index)

    def setModelData(
        self,
        editor: QWidget | None,
        model: QAbstractItemModel | None,
        index: QModelIndex,
    ) -> None:
        assert editor is not None
        assert model is not None

        if index.column() == 1:
            assert isinstance(editor, QLineEdit)
            model.setData(index, editor.text(), Qt.ItemDataRole.DisplayRole)
        else:
            super().setModelData(editor, model, index)
