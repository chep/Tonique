import random
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget

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
             3: [(1, +4), (2, -4)]}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.start_ = True
        self.uneFois.clicked.connect(self.click1fois)
        self.widget_ = widget.Widget(self.frameDessin)
        self.horizontalLayout_2.addWidget(self.widget_)
        random.seed()
        #                exit(0)

    def click1fois(self):
        tonique = "La"#self.note.currentText()
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
