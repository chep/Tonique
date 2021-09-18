import random
from threading import Timer
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from PyQt5.QtGui import QColor, QPalette
from PyQt5.Qt import Qt

from ui_mainWindow import Ui_MainWindow
import widget

NOTES = [("Do", 2),
         ("Ré", 2),
         ("Mi", 1),
         ("Fa", 2),
         ("Sol", 2),
         ("La", 2),
          ("Si", 1)]
CORDES = ["Mi", "Si", "Sol", "Ré", "La", "Mi"]

POSITIONS = {6: [(3, -3), (4, +2)],
             5: [(3, +2), (2, -2)],
             4: [(2, +3), (1, -2)],
             3: [(1, +4)]}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.start_ = True
        self.uneFois.clicked.connect(self.click1fois)
        self.startStop.clicked.connect(self.clickStart)
        self.widget_ = widget.Widget(self.frameDessin)
        self.horizontalLayout_2.addWidget(self.widget_)
        self.NOMBRES_ = [self.un, self.deux, self.trois, self.quatre]
        self.temps_ = 0
        self.demarre_ = False
        self.mesure_ = 0
        random.seed()

    def destructeur(self):
        self.timer_.cancel()

    def click1fois(self):
        tonique = self.note.currentText()
        while True:
            corde = random.randint(3, 6)
            liste = POSITIONS[corde]
            pos = random.randrange(0, len(liste))

            avide = CORDES[corde - 1]
            depart = 0

            for i in range(len(NOTES)):
                if NOTES[i][0] == avide:
                    depart = i
                    break

            case = 0
            index = depart
            while NOTES[index][0] != tonique:
                case += NOTES[index][1]
                index = (index + 1) % len(NOTES)

            if case + 12 < 20:
                case = case + (12 * random.randint(0, 1))

            deuxiemeCorde = liste[pos][0]
            deuxiemeCase = case + liste[pos][1]

            if deuxiemeCase >= 0:
                break

        self.widget_.setPosition([(corde, case),
                                  (deuxiemeCorde, deuxiemeCase)])

    def tempsSuivant(self):
        self.changeCouleurNombre(self.NOMBRES_[self.temps_], Qt.white)
        self.temps_ = (self.temps_ + 1) % len(self.NOMBRES_)
        self.changeCouleurNombre(self.NOMBRES_[self.temps_], Qt.red)
        if self.temps_ == 0:
            self.mesure_ += 1
            if self.mesure_ > self.nbMesures.value():
                self.click1fois()
                self.mesure_ = 1
            self.mesure.display(self.mesure_)
        self.timer_ = Timer(60 / self.tempo.value(),
                            self.tempsSuivant)
        self.timer_.start()

    def changeCouleurNombre(self, nombre, couleur):
        pal = nombre.palette()
        pal.setColor(pal.WindowText, QColor(couleur))
        nombre.setPalette(pal)

    def clickStart(self):
        if self.demarre_:
            self.startStop.setText("Start")
            self.demarre_ = False
            self.timer_.cancel()
            for i in self.NOMBRES_:
                self.changeCouleurNombre(i, Qt.white)
            self.mesure.display(0)
        else:
            self.demarre_ = True
            self.startStop.setText("Stop")
            for i in self.NOMBRES_:
                self.changeCouleurNombre(i, Qt.white)
            self.temps_ = 0
            self.mesure_ = 1
            self.mesure.display(1)
            self.changeCouleurNombre(self.NOMBRES_[0], Qt.red)
            self.click1fois()
            self.timer_ = Timer(60 / self.tempo.value(),
                                self.tempsSuivant)
            self.timer_.start()
