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
from PyQt5.QtCore import Qt, QPointF, QTimer
from PyQt5.QtGui import QPixmap, QPen, QBrush, QStandardItem, QPolygonF
from model.enums import *
from .polygons_mapping import PolygonsMapping
from typing import Dict, Tuple, Any, List


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
    TURN_INDICATOR_FLASH_TIMEOUT = 500

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
        self.turnIndicatorState = TurnIndication.none
        self.turnIndicatorLevel = DashboardLevel.inactive
        self.oilWarningIndicatorLevel = DashboardLevel.inactive
        self.watterWarningIndicatorLevel = DashboardLevel.inactive
        self.gearNumberValue = 1  # 0 - 5
        self.gearNumberLevel = DashboardLevel.inactive
        self.speedometerValue = 789  # 0 - 999
        self.speedometerLevel = DashboardLevel.inactive
        self.stopwatchMills = 0  # 0 - 99
        self.stopwatchSeconds = 0  # 0 - 59
        self.stopwatchMinutes = 0  # 0 - 59
        self.stopwatchHours = 0  # 0 - 9
        self.stopwatchLevel = DashboardLevel.inactive

        self.oilManometerValue = 0.0  # 0.0 - 9.99
        self.oilManometerLevel = DashboardLevel.inactive

        self.oilThermometerValue = 0  # 0 - 999
        self.oilThermometerLevel = DashboardLevel.inactive

        self.watterThermometerValue = 0  # 0 - 999
        self.watterThermometerLevel = DashboardLevel.inactive

        self.odometerThermometerValue = 0  # 0 - 9999
        self.odometerThermometerLevel = DashboardLevel.inactive


        # TODO Add more






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
            DashboardLevel.inactive: QPen(self.INACTIVE_COLOR, 1, Qt.SolidLine),
            DashboardLevel.ok: QPen(self.OK_COLOR, 1, Qt.SolidLine),
            DashboardLevel.warning: QPen(self.WARNING_COLOR, 1, Qt.SolidLine),
            DashboardLevel.dangerous: QPen(self.DANGEROUS_COLOR, 1, Qt.SolidLine)}
        self.brushes = {
            DashboardLevel.inactive: QBrush(self.INACTIVE_COLOR, Qt.SolidPattern),
            DashboardLevel.ok: QBrush(self.OK_COLOR, Qt.SolidPattern),
            DashboardLevel.warning: QBrush(self.WARNING_COLOR, Qt.SolidPattern),
            DashboardLevel.dangerous: QBrush(self.DANGEROUS_COLOR, Qt.SolidPattern)}
        # Helpers
        dirPath = os.path.dirname(os.path.abspath(__file__))
        inactivePen = self.pens[DashboardLevel.inactive]
        inactiveBrush = self.brushes[DashboardLevel.inactive]
        def buildPolygonItem(origin: QPointF, polygon: List[QPointF]):
            return self.scene.addPolygon(
                QPolygonF([QPointF(p.x() + origin.x(), p.y() + origin.y()) for p in polygon]),
                inactivePen,
                inactiveBrush)
        def makeNumberItems(origin: QPointF, polygon: Dict[str, List[QPointF]]):
            return {k: buildPolygonItem(origin, p) for k, p in polygon.items()}
        # Add background
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
        # Add turn indicator graphics
        def makeTurnIndicatorItem(initCoordinates: Dict[str, Any]):
            return buildPolygonItem(initCoordinates["C"], initCoordinates["P"])
        self.turnIndicatorLeftItem = makeTurnIndicatorItem(PolygonsMapping.TURN_INDICATOR["L"])
        self.turnIndicatorRightItem = makeTurnIndicatorItem(PolygonsMapping.TURN_INDICATOR["R"])
        self.turnIndicatorTimer = QTimer(self)
        self.turnIndicatorTimer.timeout.connect(self.renderTurnIndicator)
        self.turnIndicatorIsOn = True
        # Add warning indicators graphics
        def makeWarningIndicatorItems(initCoordinates: Dict[str, Any]):
            return [buildPolygonItem(initCoordinates["C"], p) for p in initCoordinates["P"]]
        self.oilWarningIndicatorItems = makeWarningIndicatorItems(PolygonsMapping.WARNING_INDICATORS["OIL"])
        self.watterWarningIndicatorItems = makeWarningIndicatorItems(PolygonsMapping.WARNING_INDICATORS["WATTER"])
        # Add gear number graphics
        self.gearNumberItems = makeNumberItems(PolygonsMapping.GEAR_NUMBER["C"], PolygonsMapping.GEAR_NUMBER["P"])
        # Add speedometer graphics
        self.speedometer001Items = makeNumberItems(PolygonsMapping.SPEEDOMETER[1], PolygonsMapping.SPEED_NUMBERS)
        self.speedometer010Items = makeNumberItems(PolygonsMapping.SPEEDOMETER[10], PolygonsMapping.SPEED_NUMBERS)
        self.speedometer100Items = makeNumberItems(PolygonsMapping.SPEEDOMETER[100], PolygonsMapping.SPEED_NUMBERS)
        # Add stopwatch graphics
        self.stopwatchMS01Items = makeNumberItems(PolygonsMapping.STOPWATCH["MS01"], PolygonsMapping.STANDARD_NUMBERS)
        self.stopwatchMS10Items = makeNumberItems(PolygonsMapping.STOPWATCH["MS10"], PolygonsMapping.STANDARD_NUMBERS)
        self.stopwatchS01Items = makeNumberItems(PolygonsMapping.STOPWATCH["S01"], PolygonsMapping.STANDARD_NUMBERS)
        self.stopwatchS10Items = makeNumberItems(PolygonsMapping.STOPWATCH["S10"], PolygonsMapping.STANDARD_NUMBERS)
        self.stopwatchM01Items = makeNumberItems(PolygonsMapping.STOPWATCH["M01"], PolygonsMapping.STANDARD_NUMBERS)
        self.stopwatchM10Items = makeNumberItems(PolygonsMapping.STOPWATCH["M10"], PolygonsMapping.STANDARD_NUMBERS)
        self.stopwatchH01Items = makeNumberItems(PolygonsMapping.STOPWATCH["H01"], PolygonsMapping.STANDARD_NUMBERS)
        # Add oil manometer graphics
        self.oilManometer0d01Items = makeNumberItems(
            PolygonsMapping.OIL_MANOMETER[0.01], PolygonsMapping.STANDARD_NUMBERS)
        self.oilManometer0d10Items = makeNumberItems(
            PolygonsMapping.OIL_MANOMETER[0.1], PolygonsMapping.STANDARD_NUMBERS)
        self.oilManometer1d00Items = makeNumberItems(
            PolygonsMapping.OIL_MANOMETER[1], PolygonsMapping.STANDARD_NUMBERS)
        # Add oil thermometer graphics
        self.oilThermometer001Items = makeNumberItems(
            PolygonsMapping.OIL_THERMOMETER[1], PolygonsMapping.STANDARD_NUMBERS)
        self.oilThermometer010Items = makeNumberItems(
            PolygonsMapping.OIL_THERMOMETER[10], PolygonsMapping.STANDARD_NUMBERS)
        self.oilThermometer100Items = makeNumberItems(
            PolygonsMapping.OIL_THERMOMETER[100], PolygonsMapping.STANDARD_NUMBERS)
        # Add watter thermometer graphics
        self.watterThermometer001Items = makeNumberItems(
            PolygonsMapping.WATTER_THERMOMETER[1], PolygonsMapping.STANDARD_NUMBERS)
        self.watterThermometer010Items = makeNumberItems(
            PolygonsMapping.WATTER_THERMOMETER[10], PolygonsMapping.STANDARD_NUMBERS)
        self.watterThermometer100Items = makeNumberItems(
            PolygonsMapping.WATTER_THERMOMETER[100], PolygonsMapping.STANDARD_NUMBERS)
        # Add odometer graphics
        self.watterOdometer0001Items = makeNumberItems(PolygonsMapping.ODOMETER[1], PolygonsMapping.STANDARD_NUMBERS)
        self.watterOdometer0010Items = makeNumberItems(PolygonsMapping.ODOMETER[10], PolygonsMapping.STANDARD_NUMBERS)
        self.watterOdometer0100Items = makeNumberItems(PolygonsMapping.ODOMETER[100], PolygonsMapping.STANDARD_NUMBERS)
        self.watterOdometer1000Items = makeNumberItems(PolygonsMapping.ODOMETER[1000], PolygonsMapping.STANDARD_NUMBERS)
        # Initial rendering
#        self.renderBackground()
        self.renderTachometerEngine(
            self.tachometerEngineItems, self.tachometerEngineValueRpm, self.tachometerEngineValueLevel)
        self.renderTachometerEngine(
            self.tachometerGearboxItems, self.tachometerGearboxValueRpm, self.tachometerGearboxValueLevel)
        self.renderAccelerometer()
        self.renderSteeringWheelEncoder()
        self.renderTurnIndicator()
        self.renderOilWarningIndicator()
        self.renderWatterWarningIndicator()
        self.renderGearNumber()
        self.renderSpeedometer()
        self.renderStopwatch()

        # TODO Add more

    # Helpers

    def renderNumberHelper(self, number: int, items: Dict[str, QStandardItem], level: DashboardLevel):
        def setLevel(p: QStandardItem, l: DashboardLevel):
            p.setPen(self.pens[l])
            p.setBrush(self.brushes[l])
        if level != DashboardLevel.inactive:
            for s in PolygonsMapping.NUMBER_TO_SEGMENTS[number][0]:
                setLevel(items[s], level)
            for s in PolygonsMapping.NUMBER_TO_SEGMENTS[number][1]:
                setLevel(items[s], DashboardLevel.inactive)
        else:
            for _, p in items.items():
                setLevel(p, DashboardLevel.inactive)

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

    def renderTurnIndicator(self):
        newLPen = self.pens[DashboardLevel.inactive]
        newRPen = self.pens[DashboardLevel.inactive]
        newLBrush = self.brushes[DashboardLevel.inactive]
        newRBrush = self.brushes[DashboardLevel.inactive]
        if self.turnIndicatorIsOn and self.turnIndicatorState != TurnIndication.none:
            if self.turnIndicatorState == TurnIndication.left or self.turnIndicatorState == TurnIndication.both:
                newLPen = self.pens[self.turnIndicatorLevel]
                newLBrush = self.brushes[self.turnIndicatorLevel]
            if self.turnIndicatorState == TurnIndication.right or self.turnIndicatorState == TurnIndication.both:
                newRPen = self.pens[self.turnIndicatorLevel]
                newRBrush = self.brushes[self.turnIndicatorLevel]
        self.turnIndicatorLeftItem.setPen(newLPen)
        self.turnIndicatorLeftItem.setBrush(newLBrush)
        self.turnIndicatorRightItem.setPen(newRPen)
        self.turnIndicatorRightItem.setBrush(newRBrush)
        if self.turnIndicatorState != TurnIndication.none:
            self.turnIndicatorIsOn = not self.turnIndicatorIsOn
            self.turnIndicatorTimer.start(self.TURN_INDICATOR_FLASH_TIMEOUT)
        else:
            self.turnIndicatorIsOn = True
            self.turnIndicatorTimer.stop()

    def renderOilWarningIndicator(self):
        for p in self.oilWarningIndicatorItems:
            p.setPen(self.pens[self.oilWarningIndicatorLevel])
            p.setBrush(self.brushes[self.oilWarningIndicatorLevel])

    def renderWatterWarningIndicator(self):
        for p in self.watterWarningIndicatorItems:
            p.setPen(self.pens[self.watterWarningIndicatorLevel])
            p.setBrush(self.brushes[self.watterWarningIndicatorLevel])

    def renderGearNumber(self):
        for s in PolygonsMapping.GEAR_NUMBER["M"][self.gearNumberValue][0]:
            segment = self.gearNumberItems[s]
            segment.setPen(self.pens[self.gearNumberLevel])
            segment.setBrush(self.brushes[self.gearNumberLevel])
        for s in PolygonsMapping.GEAR_NUMBER["M"][self.gearNumberValue][1]:
            segment = self.gearNumberItems[s]
            segment.setPen(self.pens[DashboardLevel.inactive])
            segment.setBrush(self.brushes[DashboardLevel.inactive])

    def renderSpeedometer(self):
        value100 = self.speedometerValue // 100
        value010 = (self.speedometerValue % 100) // 10
        value001 = (self.speedometerValue % 100) % 10
        level = self.speedometerLevel
        self.renderNumberHelper(
            value100, self.speedometer100Items, level if value100 > 0 else DashboardLevel.inactive)
        self.renderNumberHelper(
            value010, self.speedometer010Items, level if value010 > 0 or value100 > 0 else DashboardLevel.inactive)
        self.renderNumberHelper(
            value001, self.speedometer001Items, level)

    def renderStopwatch(self):
        self.renderNumberHelper(self.stopwatchMills % 10, self.stopwatchMS01Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchMills // 10, self.stopwatchMS10Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchSeconds % 10, self.stopwatchS01Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchSeconds // 10, self.stopwatchS10Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchMinutes % 10, self.stopwatchM01Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchMinutes // 10, self.stopwatchM10Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchHours, self.stopwatchH01Items, self.stopwatchLevel)







    # TODO Add more


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

    def setTurnIndicator(self, state: TurnIndication, level: DashboardLevel):
        logging.debug(f"[Dashboard.setTurnIndicator] New state = {state}, level = {level}")
        # Store new state
        self.turnIndicatorState = state
        self.turnIndicatorLevel = level
        # Redraw UI
        self.renderTurnIndicator()

    def setSpeedometer(self, value: int, level: DashboardLevel):
        logging.debug(f"[Dashboard.setSpeedometer] New value = {value}, level = {level}")
        # Store new state
        self.speedometerValue = 0 if value < 0 else (999 if value > 999 else value)
        self.speedometerLevel = level
        # Redraw UI
        self.renderSpeedometer()

    def setStopwatch(self, mills: int, seconds: int, minutes: int, hours: int, level: DashboardLevel):
        logging.debug(
            f"[Dashboard.setStopwatch] New mills = {mills}, seconds = {seconds}, minutes = {minutes}, "
            f"hours = {hours}, level = {level}")
        # Store new state
        self.stopwatchMills = 0 if mills < 0 else (99 if mills > 99 else mills)  # 0 - 99
        self.stopwatchSeconds = 0 if seconds < 0 else (59 if seconds > 59 else seconds)  # 0 - 59
        self.stopwatchMinutes = 0 if minutes < 0 else (59 if minutes > 59 else minutes)  # 0 - 59
        self.stopwatchHours = 0 if hours < 0 else (9 if hours > 9 else hours)  # 0 - 9
        self.stopwatchLevel = level
        # Redraw UI
        self.renderStopwatch()





    # TODO Add more
