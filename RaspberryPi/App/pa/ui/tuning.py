#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

  TODO

author: CAB
website: github.com/alexcab
last edited: 2019-11-9
"""

import sys
import os
import logging
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QPainter, QPixmap
from model.enums import DashboardMode
from typing import Callable


class Tuning(QMainWindow):

    # Parameters

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    # Constructor

    def __init__(self, onRaceMode: Callable[[], None], onStreetMode: Callable[[], None]):
        # Init
        super(Tuning, self).__init__()
        # Init UI
        self.setGeometry(100, 700, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle("PA Tuning")
        # Buttons
        self.raceModeButton = QPushButton('Race mode')
        self.raceModeButton.clicked.connect(onRaceMode)
        self.streetModeButton = QPushButton('Street mode')
        self.streetModeButton.clicked.connect(onStreetMode)
        # Layout
        widget = QWidget()
        hBox = QHBoxLayout()
        hBox.setAlignment(Qt.AlignTop)
        hBox.addWidget(self.raceModeButton)
        hBox.addWidget(self.streetModeButton)
        widget.setLayout(hBox)
        self.setCentralWidget(widget)


    # Methods

