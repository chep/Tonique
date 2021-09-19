#!/usr/bin/python3

# Copyright (c) 2021, Cédric Chépied. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2.0, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License, version 2.0, for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA

from PyQt5.QtWidgets import QApplication

import mainwindow


# Application Qt
app = QApplication([])
mainWindow = mainwindow.MainWindow()
mainWindow.show()
app.exec_()
mainWindow.destructeur()
