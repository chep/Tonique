from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen, QBrush, QColor
from PyQt5.QtCore import QPoint
from PyQt5.Qt import Qt

class Widget(QWidget):
    def __init__(self, parent):
        super(Widget, self).__init__()
        self.pixmap_ = QPixmap("manche.png")
        self.position_ = [(0, 0), (0, 0)]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap_)

        pen = painter.pen();
        pen.setCosmetic(True);
        pen.setWidth(3);
        pen.setColor(QColor(Qt.red));
        painter.setPen(pen);
        brush = painter.brush();
        brush.setStyle(Qt.SolidPattern);
        painter.setBrush(brush);

        if self.position_[0][0] != 0:
            painter.drawEllipse(QPoint(self.position_[0][1] * 10,
                                       self.position_[0][0] * 10),
                                10, 10)
            painter.drawEllipse(QPoint(self.position_[1][1] * 10,
                                       self.position_[1][0] * 10),
                                10, 10)

    def setPosition(self, position):
        self.position_ = position
        self.repaint()
