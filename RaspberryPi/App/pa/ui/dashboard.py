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

import os
import logging
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QOpenGLWidget
from PyQt5.QtCore import Qt, QPointF, QTimer, QRectF
from PyQt5.QtGui import QPixmap, QPen, QBrush, QStandardItem, QPolygonF, QColor, QSurfaceFormat, QTransform
from model.enums import *
from .polygons_mapping import PolygonsMapping
from typing import Dict, Tuple, Any, List


class Dashboard(QGraphicsView):

    # Parameters

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 480
    INACTIVE_COLOR = QColor('#252525')
    OK_COLOR = Qt.green
    WARNING_COLOR = Qt.yellow
    DANGEROUS_COLOR = Qt.red
    TACHOMETER_GEARS_ARROW_COLOR = Qt.white
    TACHOMETER_GEARS_NUMBER_COLOR = Qt.black
    TACHOMETER_SCALING = 100
    ACCELEROMETER_MIN_ANGEL = 10
    ACCELEROMETER_MAX_ANGEL = 350
    TURN_INDICATOR_FLASH_TIMEOUT = 500

    # Constructor

    def __init__(self, initMode: DriveMode) -> None:
        # Init values
        self.mode = initMode
        self.tachometerEngineRpm = 0  # 0 - 9000
        self.tachometerEngineLevel = DashboardLevel.inactive
        self.tachometerGearboxRpm = 0  # 0 - 9000
        self.tachometerGearboxLevel = DashboardLevel.inactive
        self.tachometerGear1Rpm = 0  # 0 - 9000
        self.tachometerGear2Rpm = 1000  # 0 - 9000
        self.tachometerGear3Rpm = 2000  # 0 - 9000
        self.tachometerGear4Rpm = 3000  # 0 - 9000
        self.tachometerGear5Rpm = 9000  # 0 - 9000
        self.accelerometerAngel = 0  # -180 - +180
        self.accelerometerValue = 0.0  # 0.0 - 1.0
        self.accelerometerLevel = DashboardLevel.inactive
        self.steeringWheelEncoderAngel = 0  # -7 - +7
        self.steeringWheelEncoderLevel = DashboardLevel.inactive
        self.turnIndicatorState = TurnIndication.none
        self.turnIndicatorLevel = DashboardLevel.inactive
        self.oilWarningIndicatorLevel = DashboardLevel.inactive
        self.watterWarningIndicatorLevel = DashboardLevel.inactive
        self.gearNumberValue = 0  # 0 - 5
        self.gearNumberLevel = DashboardLevel.inactive
        self.speedometerValue = 0  # 0 - 999
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
        self.odometerValue = 0  # 0 - 9999
        self.odometerLevel = DashboardLevel.inactive
        # Init UI
        super(Dashboard, self).__init__()
        viewport = QOpenGLWidget()
        viewportFormat = QSurfaceFormat()
        viewportFormat.setSwapInterval(0)  # disable VSync
        viewportFormat.setSamples(2 ** 8)
        viewportFormat.setDefaultFormat(viewportFormat)
        viewport.setFormat(viewportFormat)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setStyleSheet("border: 0px")
        self.setWindowTitle("Dashboard")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.scene = QGraphicsScene(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setScene(self.scene)
        self.setViewport(viewport)
        self.setInteractive(False)
        self.levelPens = {
            DashboardLevel.inactive: QPen(self.INACTIVE_COLOR, 1, Qt.SolidLine),
            DashboardLevel.ok: QPen(self.OK_COLOR, 1, Qt.SolidLine),
            DashboardLevel.warning: QPen(self.WARNING_COLOR, 1, Qt.SolidLine),
            DashboardLevel.dangerous: QPen(self.DANGEROUS_COLOR, 1, Qt.SolidLine)}
        self.levelBrushes = {
            DashboardLevel.inactive: QBrush(self.INACTIVE_COLOR, Qt.SolidPattern),
            DashboardLevel.ok: QBrush(self.OK_COLOR, Qt.SolidPattern),
            DashboardLevel.warning: QBrush(self.WARNING_COLOR, Qt.SolidPattern),
            DashboardLevel.dangerous: QBrush(self.DANGEROUS_COLOR, Qt.SolidPattern)}
        # Helpers
        dirPath = os.path.dirname(os.path.abspath(__file__))
        inactivePen = self.levelPens[DashboardLevel.inactive]
        inactiveBrush = self.levelBrushes[DashboardLevel.inactive]
        def buildPolygonItem(origin: QPointF, polygon: List[QPointF]):
            return self.scene.addPolygon(
                QPolygonF([QPointF(p.x() + origin.x(), p.y() + origin.y()) for p in polygon]),
                inactivePen, inactiveBrush)
        def makeNumberItems(origin: QPointF, polygon: Dict[str, List[QPointF]]):
            return {k: buildPolygonItem(origin, p) for k, p in polygon.items()}
        # Add background
        self.backgroundPixmaps = {
            DriveMode.race: QPixmap(os.path.join(dirPath, "background_race.png"))
                .scaled(self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
            DriveMode.street: QPixmap(os.path.join(dirPath, "background_street.png"))
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
        self.tachometerGearsPens = {
            "A": QPen(self.TACHOMETER_GEARS_ARROW_COLOR, 1, Qt.SolidLine),
            "N": QPen(self.TACHOMETER_GEARS_NUMBER_COLOR, 1, Qt.SolidLine)}
        self.tachometerGearsBrushes = {
            "A": QBrush(self.TACHOMETER_GEARS_ARROW_COLOR, Qt.SolidPattern),
            "N": QBrush(self.TACHOMETER_GEARS_NUMBER_COLOR, Qt.SolidPattern)}
        def makeGearsTransforms(translate: QPointF, rotate: int):
            arrowTrans = QTransform()
            arrowTrans.translate(translate.x(), translate.y())
            arrowTrans.rotate(rotate)
            numberTrans = QTransform()
            numberTrans.translate(translate.x(), translate.y())
            return arrowTrans, numberTrans
        self.tachometerGearsTransforms = \
            {k: makeGearsTransforms(p[0], p[1]) for k, p in PolygonsMapping.TACHOMETER_GEARS["T"].items()}
        def tachometerGearsItem(gearNumber: int):
            (arrowTrans, numberTrans) = self.tachometerGearsTransforms[0]
            arrowItem = self.scene.addPolygon(
                PolygonsMapping.TACHOMETER_GEARS["A"], inactivePen, inactiveBrush)
            arrowItem.setTransform(arrowTrans)
            numberItem = buildPolygonItem(
                PolygonsMapping.TACHOMETER_GEARS["N"]["O"],
                PolygonsMapping.TACHOMETER_GEARS["N"]["P"][gearNumber])
            numberItem.setTransform(numberTrans)
            return arrowItem, numberItem
        self.tachometerGearsItems = {
            1: tachometerGearsItem(1),
            2: tachometerGearsItem(2),
            3: tachometerGearsItem(3),
            4: tachometerGearsItem(4),
            5: tachometerGearsItem(5)}
        # Add accelerometer graphics
        def makeEllipse(points: Tuple[QPointF, QPointF]):
            return self.scene.addEllipse(
                points[0].x(),
                points[0].y(),
                points[1].x() - points[0].x(),
                points[1].y() - points[0].y(),
                inactivePen, inactiveBrush)
        self.accelerometerCenterItem = makeEllipse(PolygonsMapping.ACCELEROMETER["C"])
        self.accelerometerSectorItem = makeEllipse(PolygonsMapping.ACCELEROMETER["S"])
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
        self.renderBackground()
        self.renderTachometerScale(
            self.tachometerEngineItems, self.tachometerEngineRpm, self.tachometerEngineLevel)
        self.renderTachometerScale(
            self.tachometerGearboxItems, self.tachometerGearboxRpm, self.tachometerGearboxLevel)
        self.renderAccelerometer()
        self.renderSteeringWheelEncoder()
        self.renderTurnIndicator()
        self.renderOilWarningIndicator()
        self.renderWatterWarningIndicator()
        self.renderGearNumber()
        self.renderSpeedometer()
        self.renderStopwatch()
        self.renderOilManometer()
        self.renderOilThermometer()
        self.renderWatterThermometer()
        self.renderOdometer()

    # Helpers

    def renderNumberHelper(self, number: int, items: Dict[str, QStandardItem], level: DashboardLevel) -> None:
        def setLevel(p: QStandardItem, l: DashboardLevel):
            p.setPen(self.levelPens[l])
            p.setBrush(self.levelBrushes[l])
        if level != DashboardLevel.inactive:
            for s in PolygonsMapping.NUMBER_TO_SEGMENTS[number][0]:
                setLevel(items[s], level)
            for s in PolygonsMapping.NUMBER_TO_SEGMENTS[number][1]:
                setLevel(items[s], DashboardLevel.inactive)
        else:
            for _, p in items.items():
                setLevel(p, DashboardLevel.inactive)

    def renderTripleNumberHelper(self,
                                 value: int, items001: Dict[str, QStandardItem], items010: Dict[str, QStandardItem],
                                 items100: Dict[str, QStandardItem], level: DashboardLevel) -> None:
        v001 = value % 10
        v010 = (value % 100) // 10
        v100 = value // 100
        self.renderNumberHelper(v001, items001, level)
        self.renderNumberHelper(v010, items010, level if v010 > 0 or v100 > 0 else DashboardLevel.inactive)
        self.renderNumberHelper(v100, items100, level if v100 > 0 else DashboardLevel.inactive)

    # Rendering

    def renderBackground(self) -> None:
        logging.debug(f"[Dashboard.renderBackground] For mode = {self.mode}")
        # Render background pixmap
        self.backgroundItem.setPixmap(self.backgroundPixmaps[self.mode])
        # Re-render all indicators
        self.renderTachometerScale(
            self.tachometerEngineItems, self.tachometerEngineRpm, self.tachometerEngineLevel)
        self.renderTachometerScale(
            self.tachometerGearboxItems, self.tachometerGearboxRpm, self.tachometerGearboxLevel)
        self.renderTachometerGear(1, self.tachometerGear1Rpm)
        self.renderTachometerGear(2, self.tachometerGear2Rpm)
        self.renderTachometerGear(3, self.tachometerGear3Rpm)
        self.renderTachometerGear(4, self.tachometerGear4Rpm)
        self.renderTachometerGear(5, self.tachometerGear5Rpm)
        self.renderAccelerometer()
        self.renderSteeringWheelEncoder()
        self.renderTurnIndicator()
        self.renderOilWarningIndicator()
        self.renderWatterWarningIndicator()
        self.renderGearNumber()
        self.renderSpeedometer()
        self.renderStopwatch()
        self.renderOilManometer()
        self.renderOilThermometer()
        self.renderWatterThermometer()
        self.renderOdometer()

    def renderTachometerScale(self, items: Dict[int, QStandardItem], rpm: int, level: DashboardLevel) -> None:
        segment = round(rpm / self.TACHOMETER_SCALING)
        for k, p in items.items():
            if k <= segment:
                p.setPen(self.levelPens[level])
                p.setBrush(self.levelBrushes[level])
            else:
                p.setPen(self.levelPens[DashboardLevel.inactive])
                p.setBrush(self.levelBrushes[DashboardLevel.inactive])

    def renderTachometerGear(self, gearNumber: int, rpm: int) -> None:
        (arrowItem, numberItem) = self.tachometerGearsItems[gearNumber]
        segment = ((rpm if rpm <= 8600 else 8600) // 200) * 2
        (arrowTrans, numberTrans) = self.tachometerGearsTransforms[segment]
        arrowItem.setTransform(arrowTrans)
        arrowItem.setPen(self.tachometerGearsPens["A"])
        arrowItem.setBrush(self.tachometerGearsBrushes["A"])
        numberItem.setTransform(numberTrans)
        numberItem.setPen(self.tachometerGearsPens["N"])
        numberItem.setBrush(self.tachometerGearsBrushes["N"])

    def renderAccelerometer(self) -> None:
        newPen = self.levelPens[self.accelerometerLevel]
        newBrush = self.levelBrushes[self.accelerometerLevel]
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

    def renderSteeringWheelEncoder(self) -> None:
        angel = self.steeringWheelEncoderAngel
        for k, p in self.steeringWheelEncoderItems.items():
            if (angel == 0 and k == 0) or (abs(k) <= abs(angel) and k != 0 and (k * angel) > 0):
                p.setPen(self.levelPens[self.steeringWheelEncoderLevel])
                p.setBrush(self.levelBrushes[self.steeringWheelEncoderLevel])
            else:
                p.setPen(self.levelPens[DashboardLevel.inactive])
                p.setBrush(self.levelBrushes[DashboardLevel.inactive])

    def renderTurnIndicator(self) -> None:
        newLPen = self.levelPens[DashboardLevel.inactive]
        newRPen = self.levelPens[DashboardLevel.inactive]
        newLBrush = self.levelBrushes[DashboardLevel.inactive]
        newRBrush = self.levelBrushes[DashboardLevel.inactive]
        if self.turnIndicatorIsOn and self.turnIndicatorState != TurnIndication.none:
            if self.turnIndicatorState == TurnIndication.left or self.turnIndicatorState == TurnIndication.both:
                newLPen = self.levelPens[self.turnIndicatorLevel]
                newLBrush = self.levelBrushes[self.turnIndicatorLevel]
            if self.turnIndicatorState == TurnIndication.right or self.turnIndicatorState == TurnIndication.both:
                newRPen = self.levelPens[self.turnIndicatorLevel]
                newRBrush = self.levelBrushes[self.turnIndicatorLevel]
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

    def renderOilWarningIndicator(self) -> None:
        for p in self.oilWarningIndicatorItems:
            p.setPen(self.levelPens[self.oilWarningIndicatorLevel])
            p.setBrush(self.levelBrushes[self.oilWarningIndicatorLevel])

    def renderWatterWarningIndicator(self) -> None:
        for p in self.watterWarningIndicatorItems:
            p.setPen(self.levelPens[self.watterWarningIndicatorLevel])
            p.setBrush(self.levelBrushes[self.watterWarningIndicatorLevel])

    def renderGearNumber(self) -> None:
        for s in PolygonsMapping.GEAR_NUMBER["M"][self.gearNumberValue][0]:
            segment = self.gearNumberItems[s]
            segment.setPen(self.levelPens[self.gearNumberLevel])
            segment.setBrush(self.levelBrushes[self.gearNumberLevel])
        for s in PolygonsMapping.GEAR_NUMBER["M"][self.gearNumberValue][1]:
            segment = self.gearNumberItems[s]
            segment.setPen(self.levelPens[DashboardLevel.inactive])
            segment.setBrush(self.levelBrushes[DashboardLevel.inactive])

    def renderSpeedometer(self) -> None:
        self.renderTripleNumberHelper(self.speedometerValue,
                                      self.speedometer001Items, self.speedometer010Items,self.speedometer100Items,
                                      self.speedometerLevel)

    def renderStopwatch(self) -> None:
        self.renderNumberHelper(self.stopwatchMills % 10, self.stopwatchMS01Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchMills // 10, self.stopwatchMS10Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchSeconds % 10, self.stopwatchS01Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchSeconds // 10, self.stopwatchS10Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchMinutes % 10, self.stopwatchM01Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchMinutes // 10, self.stopwatchM10Items, self.stopwatchLevel)
        self.renderNumberHelper(self.stopwatchHours, self.stopwatchH01Items, self.stopwatchLevel)

    def renderOilManometer(self) -> None:
        intValue = int(self.oilManometerValue * 100)
        self.renderNumberHelper(intValue % 10, self.oilManometer0d01Items, self.oilManometerLevel)
        self.renderNumberHelper((intValue % 100) // 10, self.oilManometer0d10Items, self.oilManometerLevel)
        self.renderNumberHelper(intValue // 100, self.oilManometer1d00Items, self.oilManometerLevel)

    def renderOilThermometer(self) -> None:
        self.renderTripleNumberHelper(self.oilThermometerValue,
                                      self.oilThermometer001Items, self.oilThermometer010Items,
                                      self.oilThermometer100Items, self.oilThermometerLevel)

    def renderWatterThermometer(self) -> None:
        self.renderTripleNumberHelper(self.watterThermometerValue,
                                     self.watterThermometer001Items, self.watterThermometer010Items,
                                     self.watterThermometer100Items, self.watterThermometerLevel)

    def renderOdometer(self) -> None:
        v0001 = (self.odometerValue % 10)
        v0010 = (self.odometerValue % 100) // 10
        v0100 = (self.odometerValue % 1000) // 100
        v1000 = self.odometerValue // 1000
        def level(isActive: bool):
             return self.odometerLevel if isActive > 0 else DashboardLevel.inactive
        self.renderNumberHelper(v0001, self.watterOdometer0001Items, self.odometerLevel)
        self.renderNumberHelper(v0010, self.watterOdometer0010Items, level(v0010 > 0 or v0100 > 0 or v1000 > 0))
        self.renderNumberHelper(v0100, self.watterOdometer0100Items, level(v0100 > 0 or v1000 > 0))
        self.renderNumberHelper(v1000, self.watterOdometer1000Items, level(v1000 > 0))

    # Methods

    def setMode(self, mode: DriveMode) -> None:
        logging.debug(f"[Dashboard.setMode] New mode = {mode}")
        # Store new state
        self.mode = mode
        # Redraw UI
        self.renderBackground()

    def setTachometerEngine(self, rpm: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setTachometerEngine] New rpm = {rpm}, level = {level}")
        # Store new state
        self.tachometerEngineRpm = 0 if rpm < 0 else (9000 if rpm > 9000 else rpm)
        self.tachometerEngineLevel = level
        # Redraw UI
        self.renderTachometerScale(
            self.tachometerEngineItems, self.tachometerEngineRpm, self.tachometerEngineLevel)

    def setTachometerGearbox(self, rpm: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setTachometerGearbox] New rpm = {rpm}, level = {level}")
        # Store new state
        self.tachometerGearboxRpm = 0 if rpm < 0 else (9000 if rpm > 9000 else rpm)
        self.tachometerGearboxLevel = level
        # Redraw UI
        self.renderTachometerScale(
            self.tachometerGearboxItems, self.tachometerGearboxRpm, self.tachometerGearboxLevel)

    def setTachometerGears(self, rpm1: int, rpm2: int, rpm3: int, rpm4: int, rpm5: int) -> None:
            logging.debug(
                f"[Dashboard.setTachometerGears] New rpm1 = {rpm1}, rpm2 = {rpm2}, rpm3 = {rpm3}, "
                f"rpm4 = {rpm4}, rpm5 = {rpm5}")
            # Store new state
            self.tachometerGear1Rpm = 0 if rpm1 < 0 else (9000 if rpm1 > 9000 else rpm1)
            self.tachometerGear2Rpm = 0 if rpm2 < 0 else (9000 if rpm2 > 9000 else rpm2)
            self.tachometerGear3Rpm = 0 if rpm3 < 0 else (9000 if rpm3 > 9000 else rpm3)
            self.tachometerGear4Rpm = 0 if rpm4 < 0 else (9000 if rpm4 > 9000 else rpm4)
            self.tachometerGear5Rpm = 0 if rpm5 < 0 else (9000 if rpm5 > 9000 else rpm5)
            # Redraw UI
            self.renderTachometerGear(1, self.tachometerGear1Rpm)
            self.renderTachometerGear(2, self.tachometerGear2Rpm)
            self.renderTachometerGear(3, self.tachometerGear3Rpm)
            self.renderTachometerGear(4, self.tachometerGear4Rpm)
            self.renderTachometerGear(5, self.tachometerGear5Rpm)

    def setAccelerometer(self, angel: int, value: float, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setAccelerometer] New angel = {angel}, value = {value}, level = {level}")
        # Store new state
        self.accelerometerAngel = -180 if angel < -180 else (180 if angel > 180 else angel)
        self.accelerometerValue = 0.0 if value < 0.0 else (1.0 if value > 1.0 else value)
        self.accelerometerLevel = level
        # Redraw UI
        self.renderAccelerometer()

    def setSteeringWheelEncoder(self, angel: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setSteeringWheelEncoder] New angel = {angel}, level = {level}")
        # Store new state
        self.steeringWheelEncoderAngel = -7 if angel < -7 else (7 if angel > 7 else angel)
        self.steeringWheelEncoderLevel = level
        # Redraw UI
        self.renderSteeringWheelEncoder()

    def setTurnIndicator(self, state: TurnIndication, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setTurnIndicator] New state = {state}, level = {level}")
        # Store new state
        self.turnIndicatorState = state
        self.turnIndicatorLevel = level
        # Redraw UI
        self.renderTurnIndicator()

    def setGearNumber(self, value: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setGearNumber] New value = {value}, level = {level}")
        # Store new state
        self.gearNumberValue = 0 if value < 0 else (5 if value > 5 else value)
        self.gearNumberLevel = level
        # Redraw UI
        self.renderGearNumber()

    def setOilWarningIndicator(self, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setOilWarningIndicator] New level = {level}")
        # Store new state
        self.oilWarningIndicatorLevel = level
        # Redraw UI
        self.renderOilWarningIndicator()

    def setWatterWarningIndicator(self, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setWatterWarningIndicator] New level = {level}")
        # Store new state
        self.watterWarningIndicatorLevel = level
        # Redraw UI
        self.renderWatterWarningIndicator()

    def setSpeedometer(self, value: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setSpeedometer] New value = {value}, level = {level}")
        # Store new state
        self.speedometerValue = 0 if value < 0 else (999 if value > 999 else value)
        self.speedometerLevel = level
        # Redraw UI
        self.renderSpeedometer()

    def setStopwatch(self, mills: int, seconds: int, minutes: int, hours: int, level: DashboardLevel) -> None:
        logging.debug(
            f"[Dashboard.setStopwatch] New mills = {mills}, seconds = {seconds}, minutes = {minutes}, "
            f"hours = {hours}, level = {level}")
        # Store new state
        self.stopwatchMills = 0 if mills < 0 else (99 if mills > 99 else mills)
        self.stopwatchSeconds = 0 if seconds < 0 else (59 if seconds > 59 else seconds)
        self.stopwatchMinutes = 0 if minutes < 0 else (59 if minutes > 59 else minutes)
        self.stopwatchHours = 0 if hours < 0 else (9 if hours > 9 else hours)
        self.stopwatchLevel = level
        # Redraw UI
        self.renderStopwatch()

    def setOilManometer(self, value: float, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setOilManometer] New value = {value}, level = {level}")
        # Store new state
        self.oilManometerValue = 0.0 if value < 0.0 else (9.99 if value > 9.99 else value)
        self.oilManometerLevel = level
        # Redraw UI
        self.renderOilManometer()

    def setOilThermometer(self, value: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setOilThermometer] New value = {value}, level = {level}")
        # Store new state
        self.oilThermometerValue = 0 if value < 0 else (999 if value > 999 else value)
        self.oilThermometerLevel = level
        # Redraw UI
        self.renderOilThermometer()

    def setWatterThermometer(self, value: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setWatterThermometer] New value = {value}, level = {level}")
        # Store new state
        self.watterThermometerValue = 0 if value < 0 else (999 if value > 999 else value)
        self.watterThermometerLevel = level
        # Redraw UI
        self.renderWatterThermometer()

    def setOdometer(self, value: int, level: DashboardLevel) -> None:
        logging.debug(f"[Dashboard.setOdometer] New value = {value}, level = {level}")
        # Store new state
        self.odometerValue = 0 if value < 0 else (9999 if value > 9999 else value)
        self.odometerLevel = level
        # Redraw UI
        self.renderOdometer()
