#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
_____|||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||
_____|||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||
_____     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||
_____     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||     |||||
_____________________     _____     _______              _____       _____ |||||     |||||     |||||     |||||
_____  __ \__(_)__  /_______  /_    ___    |________________(_)________  /______ __________________      |||||
____  /_/ /_  /__  /_  __ \  __/    __  /| |_  ___/_  ___/_  /__  ___/  __/  __ `/_  __ \  ___/  _ \  |||     |||||
___  ____/_  / _  / / /_/ / /_      _  ___ |(__  )_(__  )_  / _(__  )/ /_ / /_/ /_  / / / /__ /  __/  |||     |||||
__/_/     /_/  /_/  \____/\__/      /_/  |_/____/ /____/ /_/  /____/ \__/ \__,_/ /_/ /_/\___/ \___/      |||||

author: CAB
website: github.com/alexcab
created: 2019-11-9
"""

import sys
import os
import logging
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMargins, QCoreApplication
from PyQt5.QtGui import QPainter, QPixmap
from model.enums import DriveMode
from typing import Callable


class Tuning(QMainWindow):

    # Parameters

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    # Constructor

    def __init__(self, onExit: Callable[[], None]):
        # Init
        super(Tuning, self).__init__()
        self.onExit = onExit
        # Init UI
        self.setGeometry(100, 700, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle("PA Tuning")
        # Buttons
        self.raceModeButton = QPushButton('Race mode')
        # self.raceModeButton.clicked.connect(onRaceMode)
        self.streetModeButton = QPushButton('Street mode')
        # self.streetModeButton.clicked.connect(onStreetMode)
        # Layout
        widget = QWidget()
        hBox = QHBoxLayout()
        hBox.setAlignment(Qt.AlignTop)
        hBox.addWidget(self.raceModeButton)
        hBox.addWidget(self.streetModeButton)
        widget.setLayout(hBox)
        self.setCentralWidget(widget)

    # Override methods

    def closeEvent(self, event):
        logging.debug(f"[Tuning.closeEvent] Window close, terminate app")
        self.onExit()

    # Methods

