#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

  TODO

author: CAB
website: github.com/alexcab
last edited: 2019-11-9
"""

import os
import logging
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QStandardItem, QPolygonF
from model.enums import *
from .polygons_mapping import PolygonsMapping
from typing import Dict, Tuple, Any


class Dashboard(QGraphicsView):

    # Parameters

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 480
    INACTIVE_COLOR = Qt.darkGray
    OK_COLOR = Qt.green
    WARNING_COLOR = Qt.yellow
    DANGEROUS_COLOR = Qt.red
    TACHOMETER_SCALING = 100
    ACCELEROMETER_MIN_ANGEL = 10
    ACCELEROMETER_MAX_ANGEL = 350

    # Constructor

    def __init__(self, initMode: DashboardMode):
        # Init values
        self.mode = initMode
        self.tachometerEngineValueRpm = 0  # 0 - 9000
        self.tachometerEngineValueLevel = DashboardLevel.inactive
        self.tachometerGearboxValueRpm = 0  # 0 - 9000
        self.tachometerGearboxValueLevel = DashboardLevel.inactive
        self.accelerometerAngel = 0  # -180 - +180
        self.accelerometerValue = 0.0  # 0.0 - 1.0
        self.accelerometerLevel = DashboardLevel.inactive
        self.steeringWheelEncoderAngel = 0  # -7 - +7
        self.steeringWheelEncoderLevel = DashboardLevel.inactive
        # Init UI
        super(Dashboard, self).__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setGeometry(100, 100, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)                        # TODO 100, 100 -> 0, 0
        self.setStyleSheet("border: 0px")
        self.setWindowTitle("Dashboard")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.scene = QGraphicsScene(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setScene(self.scene)
        self.pens = {
            DashboardLevel.inactive: QPen(self.INACTIVE_COLOR, 2, Qt.SolidLine),
            DashboardLevel.ok: QPen(self.OK_COLOR, 2, Qt.SolidLine),
            DashboardLevel.warning: QPen(self.WARNING_COLOR, 2, Qt.SolidLine),
            DashboardLevel.dangerous: QPen(self.DANGEROUS_COLOR, 2, Qt.SolidLine)}
        self.brushes = {
            DashboardLevel.inactive: QBrush(self.INACTIVE_COLOR, Qt.SolidPattern),
            DashboardLevel.ok: QBrush(self.OK_COLOR, Qt.SolidPattern),
            DashboardLevel.warning: QBrush(self.WARNING_COLOR, Qt.SolidPattern),
            DashboardLevel.dangerous: QBrush(self.DANGEROUS_COLOR, Qt.SolidPattern)}
        # Add background
        dirPath = os.path.dirname(os.path.abspath(__file__))
        inactivePen = self.pens[DashboardLevel.inactive]
        inactiveBrush = self.brushes[DashboardLevel.inactive]
        self.backgroundPixmaps = {
            DashboardMode.race: QPixmap(os.path.join(dirPath, "background_race.png"))
                .scaled(self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
            DashboardMode.street: QPixmap(os.path.join(dirPath, "background_street.png"))
                .scaled(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)}
        logging.debug(
            f"[Dashboard.__init__] Loaded: backgroundPixmaps = {self.backgroundPixmaps}, initMode = {initMode}")
        self.backgroundItem = QGraphicsPixmapItem()
        self.backgroundItem.setZValue(-1)
        self.scene.addItem(self.backgroundItem)
        # Add tachometer graphics
        self.tachometerEngineItems = \
            {k: self.scene.addPolygon(p, inactivePen, inactiveBrush)
             for k, p in PolygonsMapping.TACHOMETER_ENGINE.items()}
        self.tachometerGearboxItems = \
            {k: self.scene.addPolygon(p, inactivePen, inactiveBrush)
             for k, p in PolygonsMapping.TACHOMETER_GEARBOX.items()}
        # Add accelerometer graphics
        def makeEllipse(points: Tuple[QPointF, QPointF]):
            return self.scene.addEllipse(
                points[0].x(),
                points[0].y(),
                points[1].x() - points[0].x(),
                points[1].y() - points[0].y(),
                inactivePen, inactiveBrush)
        self.accelerometerCenterItem = makeEllipse(PolygonsMapping.ACCELEROMETER["C"])
        self.accelerometerSectorItem = makeEllipse( PolygonsMapping.ACCELEROMETER["S"])
        self.accelerometerSectorItem.setStartAngle(int((270 - (self.ACCELEROMETER_MIN_ANGEL / 2))) * 16)
        self.accelerometerSectorItem.setSpanAngle(self.ACCELEROMETER_MIN_ANGEL * 16)
        # Add steering wheel encoder graphics
        self.steeringWheelEncoderItems = \
            {k: self.scene.addPolygon(p, inactivePen, inactiveBrush)
             for k, p in PolygonsMapping.STEERING_WHEEL_ENCODER.items()}
        # Add turn indicators graphics
        def movePolygon(initCoordinates: Dict[str, Any]):
            origin: QPointF = initCoordinates["C"]
            return QPolygonF([QPointF(p.x() + origin.x(), p.y() + origin.y()) for p in initCoordinates["P"]])
        self.turnIndicatorLeftItem = self.scene.addPolygon(
            movePolygon(PolygonsMapping.TURN_INDICATOR["L"]), inactivePen, inactiveBrush)
        self.turnIndicatorRightItem = self.scene.addPolygon(
            movePolygon(PolygonsMapping.TURN_INDICATOR["R"]), inactivePen, inactiveBrush)


        # Initial rendering
        # self.renderBackground()
        self.renderTachometerEngine(
            self.tachometerEngineItems, self.tachometerEngineValueRpm, self.tachometerEngineValueLevel)
        self.renderTachometerEngine(
            self.tachometerGearboxItems, self.tachometerGearboxValueRpm, self.tachometerGearboxValueLevel)
        self.renderAccelerometer()
        self.renderSteeringWheelEncoder()

    # Rendering

    def renderBackground(self):
        logging.debug(f"[Dashboard.renderBackground] For mode = {self.mode}")
        self.backgroundItem.setPixmap(self.backgroundPixmaps[self.mode])

    def renderTachometerEngine(self, items: Dict[int, QStandardItem], rpm: int, level: DashboardLevel):
        segment = round(rpm / self.TACHOMETER_SCALING)
        for k, p in items.items():
            if k <= segment:
                p.setPen(self.pens[level])
                p.setBrush(self.brushes[level])
            else:
                p.setPen(self.pens[DashboardLevel.inactive])
                p.setBrush(self.brushes[DashboardLevel.inactive])

    def renderAccelerometer(self):
        newPen = self.pens[self.accelerometerLevel]
        newBrush = self.brushes[self.accelerometerLevel]
        self.accelerometerCenterItem.setPen(newPen)
        self.accelerometerCenterItem.setBrush(newBrush)
        self.accelerometerSectorItem.setPen(newPen)
        self.accelerometerSectorItem.setBrush(newBrush)
        span = ((self.ACCELEROMETER_MAX_ANGEL - self.ACCELEROMETER_MIN_ANGEL) * self.accelerometerValue)\
            + self.ACCELEROMETER_MIN_ANGEL
        startAngel = self.accelerometerAngel - (span / 2)
        correctedAngel = ((startAngel - 90) if startAngel >= 90 else (270 + startAngel))
        self.accelerometerSectorItem.setStartAngle(int(correctedAngel) * 16)
        self.accelerometerSectorItem.setSpanAngle(int(span) * 16)

    def renderSteeringWheelEncoder(self):
        angel = self.steeringWheelEncoderAngel
        for k, p in self.steeringWheelEncoderItems.items():
            if (angel == 0 and k == 0) or (abs(k) <= abs(angel) and k != 0 and (k * angel) > 0):
                p.setPen(self.pens[self.steeringWheelEncoderLevel])
                p.setBrush(self.brushes[self.steeringWheelEncoderLevel])
            else:
                p.setPen(self.pens[DashboardLevel.inactive])
                p.setBrush(self.brushes[DashboardLevel.inactive])

    # Methods

    def setMode(self, mode: DashboardMode):
        logging.debug(f"[Dashboard.setMode] New mode = {mode}")
        # Store new state
        self.mode = mode
        # Redraw UI
        self.renderBackground()

    def setTachometerEngine(self, rpm: int, level: DashboardLevel):
        logging.debug(f"[Dashboard.setTachometerEngine] New rpm = {rpm}, level = {level}")
        # Store new state
        self.tachometerEngineValueRpm = 0 if rpm < 0 else (9000 if rpm > 9000 else rpm)
        self.tachometerEngineValueLevel = level
        # Redraw UI
        self.renderTachometerEngine(
            self.tachometerEngineItems, self.tachometerEngineValueRpm, self.tachometerEngineValueLevel)

    def setGearboxEngine(self, rpm: int, level: DashboardLevel):
        logging.debug(f"[Dashboard.setGearboxEngine] New rpm = {rpm}, level = {level}")
        # Store new state
        self.tachometerGearboxValueRpm = 0 if rpm < 0 else (9000 if rpm > 9000 else rpm)
        self.tachometerGearboxValueLevel = level
        # Redraw UI
        self.renderTachometerEngine(
            self.tachometerGearboxItems, self.tachometerGearboxValueRpm, self.tachometerGearboxValueLevel)

    def setAccelerometer(self, angel: int, value: float, level: DashboardLevel):
        logging.debug(f"[Dashboard.setAccelerometer] New angel = {angel}, value = {value}, level = {level}")
        # Store new state
        self.accelerometerAngel = -180 if angel < -180 else (180 if angel > 180 else angel)
        self.accelerometerValue = 0.0 if value < 0.0 else (1.0 if value > 1.0 else value)
        self.accelerometerLevel = level
        # Redraw UI
        self.renderAccelerometer()

    def setSteeringWheelEncoder(self, angel: int, level: DashboardLevel):
        logging.debug(f"[Dashboard.setSteeringWheelEncoder] New angel = {angel}, level = {level}")
        # Store new state
        self.steeringWheelEncoderAngel = -7 if angel < -7 else (7 if angel > 7 else angel)
        self.accelerometerLevel = level
        # Redraw UI
        self.renderSteeringWheelEncoder()

