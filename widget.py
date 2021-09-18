from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen, QBrush, QColor
from PyQt5.QtCore import QPoint, QLine
from PyQt5.Qt import Qt

OFFSET_CORDES = 10
INTERVALE_CORDES = 20
POSITIONS_FRETS = [11, 90, 167, 242, 316, 387, 455, 522, 587, 650, 710, 771, 827, 882, 936, 987, 1036, 1082, 1127, 1170, 1211, 1250, 1287, 1322]


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
            self.affichePosition(self.position_[0], painter)
            self.affichePosition(self.position_[1], painter)

    def affichePosition(self, position, painter):
        case = position[1]
        if case > 0:
            x = (POSITIONS_FRETS[case - 1] + POSITIONS_FRETS[case]) / 2
            y = 10 + (position[0] - 1) * 20
            painter.drawEllipse(QPoint(x, y), 10, 10)
        else:
            painter.drawLine(QLine(POSITIONS_FRETS[0], 10 + (position[0] - 1) * 20,
                                   POSITIONS_FRETS[-1], 10 + (position[0] - 1) * 20))

    def setPosition(self, position):
        self.position_ = position
        self.repaint()
