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
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QPainter, QPixmap
from model.enums import DashboardMode


class Dashboard(QGraphicsView):

    # Parameters

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 480

    # Constructor

    def __init__(self, initMode: DashboardMode):
        # Init
        self.mode = initMode
        super(Dashboard, self).__init__()
        # Load background images
        dirPath = os.path.dirname(os.path.abspath(__file__))
        self.backgroundPixmaps = {
            DashboardMode.race: QPixmap(os.path.join(dirPath, "background_race.png"))
                .scaled(self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
            DashboardMode.street: QPixmap(os.path.join(dirPath, "background_street.png"))
                .scaled(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)}
        logging.debug(
            f"[Dashboard.__init__] Loaded: backgroundPixmaps = {self.backgroundPixmaps}, initMode = {initMode}")
        # Init UI
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setStyleSheet("border: 0px")
        self.setWindowTitle("Dashboard")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.backgroundItem = QGraphicsPixmapItem()
        self.backgroundItem.setZValue(-1)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.backgroundItem)
        self.setScene(self.scene)
        # Initial rendering
        self.renderBackground()

    # Rendering

    def renderBackground(self):
        logging.debug(f"[Dashboard.renderBackground] For mode = {self.mode}")
        self.backgroundItem.setPixmap(self.backgroundPixmaps[self.mode])

    # Methods

    def setMode(self, mode: DashboardMode):
        logging.debug(f"[Dashboard.setMode] New mode = {mode}")
        # Init
        self.mode = mode
        # Redraw UI
        self.renderBackground()


