#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src\main.py
# Project: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src
# Created Date: Thursday, November 28th 2024, 1:25:50 am
# Author: GUI Cheng
# -----
# Last Modified: Fri Nov 29 2024
# Modified By: GUI Cheng
# -----
# It's a great pelasure to have the life running on the world.
# Be patient and kind to yourself.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###



import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 400, 1600, 2400)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('resources/DSP.png'))        

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources/DSP.png'))
    ex = Example()
    sys.exit(app.exec_())