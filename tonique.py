#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication

import mainwindow


# Application Qt
app = QApplication([])
mainWindow = mainwindow.MainWindow()
mainWindow.show()
app.exec_()
mainWindow.destructeur()
