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
created: 2019-12-4
"""

import logging
import math
import time

from PyQt5.QtCore import  pyqtSlot, QObject, pyqtSignal

from worker import Worker
from model.logic_config import LogicConfig
from model.enums import *


class LogicSignals(QObject):
    outMode                   = pyqtSignal(DriveMode)  # (mode)
    outTachometerEngine       = pyqtSignal(int, DashboardLevel)  # (rpm, level)
    outTachometerGearbox      = pyqtSignal(int, DashboardLevel)  # (rpm, level)
    outTachometerGears        = pyqtSignal(int, int, int, int, int)  # (rpm1, rpm2, rpm3, rpm4, rpm5)
    outAccelerometer          = pyqtSignal(int, float, DashboardLevel)  # (angel, value, level)
    outSteeringWheelEncoder   = pyqtSignal(int, DashboardLevel)  # (angel, level)
    outTurnLeftIndicator      = pyqtSignal(DashboardLevel)  # (level)
    outTurnRightIndicator     = pyqtSignal(DashboardLevel)  # (level)
    outGearNumber             = pyqtSignal(int)  # (value, level)
    outOilWarningIndicator    = pyqtSignal(DashboardLevel)  # (level)
    outWatterWarningIndicator = pyqtSignal(DashboardLevel)  # (level)
    outSpeedometer            = pyqtSignal(int, DashboardLevel)  # (value, level)
    outStopwatch              = pyqtSignal(int, int, int, int, DashboardLevel)  # (mills, seconds, minutes, hours,level)
    outOilManometer           = pyqtSignal(float, DashboardLevel)  # (value, level)
    outOilThermometer         = pyqtSignal(int, DashboardLevel)  # (value, level)
    outWatterThermometer      = pyqtSignal(int, DashboardLevel)  # (value, level)
    outOdometer               = pyqtSignal(int, DashboardLevel)  # (value, level)


class Logic(QObject):

    # Constructor

    def __init__(self, config: LogicConfig, initMode: DriveMode) -> None:
        # Init
        super(Logic, self).__init__()
        self.config = config
        self.driveMode = initMode
        self.signals = LogicSignals()
        self.worker = Worker(timeout=0.1, job=self.job)
        self.engineRpm = 0
        self.oilPressureLevel = DashboardLevel.ok
        self.oilTemperatureLevel = DashboardLevel.ok
        self.oilWarningIndicator = DashboardLevel.inactive
        self.watterWarningIndicator = DashboardLevel.inactive
        self.distance = 0
        self.odometerLevel = DashboardLevel.ok
        self.timeCountIsReset = True
        self.timeCountIsStarted = False
        self.startTime = 0  # in mills

    # Helpers

    def getTimeMills(self) -> int:
        return int(round(time.time() * 1000))

    def setOilWarningIndicator(self) -> None:
        newLevel = DashboardLevel.inactive
        if self.oilPressureLevel == DashboardLevel.dangerous or self.oilTemperatureLevel == DashboardLevel.dangerous:
            newLevel = DashboardLevel.dangerous
        elif self.oilPressureLevel == DashboardLevel.warning or self.oilTemperatureLevel == DashboardLevel.warning:
            newLevel = DashboardLevel.warning
        if self.oilWarningIndicator != newLevel:
            self.signals.outOilWarningIndicator.emit(newLevel)
            self.oilWarningIndicator = newLevel

    def setStopwatch(self, level: DashboardLevel) -> None:
        period = self.getTimeMills() - self.startTime
        mills = (period // 10) % 100
        seconds = (period // 1000) % 60
        minutes = (period // (60 * 1000)) % 60
        hours = (period // (60 * 60 * 1000)) % 10
        self.signals.outStopwatch.emit(mills, seconds, minutes, hours, level)

    # Worker job

    def job(self) -> None:
        logging.debug(f"[Logic.job] Start processing")
        # Update stopwatch
        if self.timeCountIsStarted:
            self.setStopwatch(DashboardLevel.dangerous)

    # Input

    @pyqtSlot(float, int)
    def inEngineTachometer(self, period: float, count: int) -> None:
        logging.debug(f"[Logic.inEngineTachometer] New period = ${period}, count = {count}")
        self.engineRpm = int(period * count * self.config.tachometerEngineScale)
        level = DashboardLevel.ok
        if self.driveMode == DriveMode.race:
            if self.engineRpm <= self.config.tachometerEngineRaceMinWarning \
                    or self.engineRpm >= self.config.tachometerEngineRaceMaxWarning:
                level = DashboardLevel.warning
            if self.engineRpm <= self.config.tachometerEngineRaceMinDangerous \
                    or self.engineRpm >= self.config.tachometerEngineRaceMaxDangerous:
                level = DashboardLevel.dangerous
        else:
            if self.engineRpm <= self.config.tachometerEngineStreetMinWarning \
                    or self.engineRpm >= self.config.tachometerEngineStreetMaxWarning:
                level = DashboardLevel.warning
            if self.engineRpm <= self.config.tachometerEngineStreetMinDangerous \
                    or self.engineRpm >= self.config.tachometerEngineStreetMaxDangerous:
                level = DashboardLevel.dangerous
        self.signals.outTachometerEngine.emit(self.engineRpm, level)

    @pyqtSlot(float, int)
    def inGearboxInTachometer(self, period: float, count: int) -> None:
        logging.debug(f"[Logic.inGearboxInTachometer] New period = ${period}, count = {count}")
        gearboxInRpm = int(period * count * self.config.tachometerGearboxScale)
        rpmDef = abs(self.engineRpm - gearboxInRpm)
        level = DashboardLevel.ok
        if rpmDef >= self.config.tachometerGearboxDeviationDangerous:
            level = DashboardLevel.dangerous
        elif rpmDef >= self.config.tachometerGearboxDeviationWarning:
            level = DashboardLevel.warning
        self.signals.outTachometerGearbox.emit(gearboxInRpm, level)

    @pyqtSlot(float, int)
    def inGearboxOutTachometer(self, period: float, count: int) -> None:
        logging.debug(f"[Logic.inGearboxOutTachometer] New period = ${period}, count = {count}")
        rpm = (period * count * self.config.speedometerRpmScale)
        speed = int(rpm * self.config.speedometerSpeedScale)
        level = DashboardLevel.ok
        if self.driveMode == DriveMode.street:
            level = DashboardLevel.dangerous
            i = 0
            while i < len(self.config.speedometerStreetMinWarning) and level == DashboardLevel.dangerous:
                if self.config.speedometerStreetMinDangerous[i] <= speed \
                        < self.config.speedometerStreetMinWarning[i] \
                        or self.config.speedometerStreetMaxWarning[i] <= speed \
                        < self.config.speedometerStreetMaxDangerous[i]:
                    level = DashboardLevel.warning
                elif self.config.speedometerStreetMinWarning[i] <= speed \
                        < self.config.speedometerStreetMaxWarning[i]:
                    level = DashboardLevel.ok
                i += 1
        self.signals.outSpeedometer.emit(speed, level)
        self.signals.outTachometerGears.emit(
            int(rpm / self.config.tachometerGear1Ratio),
            int(rpm / self.config.tachometerGear2Ratio),
            int(rpm / self.config.tachometerGear3Ratio),
            int(rpm / self.config.tachometerGear4Ratio),
            int(rpm / self.config.tachometerGear5Ratio))
        if self.odometerLevel == DashboardLevel.ok:
            self.distance += int(count * self.config.odometerDistanceScale)
            if self.distance >= 9999 and self.driveMode == DriveMode.race:
                self.odometerLevel = DashboardLevel.dangerous
                self.distance = 9999
            elif self.distance > 9999:
                self.distance = 0
            self.signals.outOdometer.emit(self.distance, self.odometerLevel)

    @pyqtSlot(int)
    def inGearNumber(self, number: int) -> None:
        logging.debug(f"[Logic.inGearNumber] New number = ${number}")
        self.signals.outGearNumber.emit(number)

    @pyqtSlot(float)
    def inOilPressure(self, value: float) -> None:
        logging.debug(f"[Logic.inOilPressure] New value = ${value}")
        pressure = int(value * self.config.oilManometerScale * 100) / 100
        level = DashboardLevel.ok
        if pressure <= self.config.oilManometerMinWarning or pressure >= self.config.oilManometerMaxWarning:
            level = DashboardLevel.warning
        if pressure <= self.config.oilManometerMinDangerous or pressure >= self.config.oilManometerMaxDangerous:
            level = DashboardLevel.dangerous
        self.signals.outOilManometer.emit(pressure, level)
        self.oilPressureLevel = level
        self.setOilWarningIndicator()

    @pyqtSlot(float)
    def inOilTemperature(self, value: float) -> None:
        logging.debug(f"[Logic.inOilTemperature] New value = ${value}")
        temperature = int(value * self.config.oilThermometerScale)
        level = DashboardLevel.ok
        if temperature <= self.config.oilThermometerMinWarning \
                or temperature >= self.config.oilThermometerMaxWarning:
            level = DashboardLevel.warning
        if temperature <= self.config.oilThermometerMinDangerous \
                or temperature >= self.config.oilThermometerMaxDangerous:
            level = DashboardLevel.dangerous
        self.signals.outOilThermometer.emit(temperature, level)
        self.oilTemperatureLevel = level
        self.setOilWarningIndicator()

    @pyqtSlot(float)
    def inWatterTemperature(self, value: float) -> None:
        logging.debug(f"[Logic.inWatterTemperature] New value = ${value}")
        temperature = int(value * self.config.watterThermometerScale)
        level = DashboardLevel.ok
        if temperature <= self.config.watterThermometerMinWarning \
                or temperature >= self.config.watterThermometerMaxWarning:
            level = DashboardLevel.warning
        if temperature <= self.config.watterThermometerMinDangerous \
                or temperature >= self.config.watterThermometerMaxDangerous:
            level = DashboardLevel.dangerous
        self.signals.outWatterThermometer.emit(temperature, level)
        if self.watterWarningIndicator != level:
            self.signals.outWatterWarningIndicator.emit(DashboardLevel.inactive if level == DashboardLevel.ok else level)
            self.watterWarningIndicator = level

    @pyqtSlot(bool)
    def inRaceModeIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inRaceModeIsOn] New isOn = ${isOn}")
        self.driveMode = DriveMode.race if isOn else DriveMode.street
        self.distance = 0
        self.odometerLevel = DashboardLevel.ok
        self.signals.outMode.emit(self.driveMode)

    @pyqtSlot(bool)
    def inStopwatchButtonIsOn(self, isOn: bool) -> None:
        logging.debug(
            f"[Logic.inStopwatchButtonIsOn] New isOn = ${isOn}, self.timeCountIsReset = {self.timeCountIsReset}, "
            f"self.timeCountIsStarted = {self.timeCountIsStarted}, self.startTime = {self.startTime}")
        if isOn and self.timeCountIsReset and not self.timeCountIsStarted:
            self.timeCountIsReset = False
            self.timeCountIsStarted = True
            self.startTime = self.getTimeMills()
            self.setStopwatch(DashboardLevel.dangerous)
        elif isOn and not self.timeCountIsReset and self.timeCountIsStarted:
            self.timeCountIsStarted = False
            self.setStopwatch(DashboardLevel.warning)
        elif not isOn and not self.timeCountIsReset and not self.timeCountIsStarted:
            self.timeCountIsReset = True
            self.signals.outStopwatch.emit(0, 0, 0, 0, DashboardLevel.ok)

    @pyqtSlot(bool)
    def inOdometerButtonIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inOdometerButtonIsOn] New isOn = ${isOn}")
        if isOn:
            self.odometerLevel = DashboardLevel.warning
        else:
            self.distance = 0
            self.odometerLevel = DashboardLevel.ok
        self.signals.outOdometer.emit(self.distance, self.odometerLevel)

    @pyqtSlot(bool)
    def inTurnLeftSignalIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inTurnLeftSignalIsOn] New isOn = ${isOn}")
        self.signals.outTurnLeftIndicator.emit(
            DashboardLevel.ok if isOn else DashboardLevel.inactive)

    @pyqtSlot(bool)
    def inTurnRightSignalIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inTurnRightSignalIsOn] New isOn = ${isOn}")
        self.signals.outTurnRightIndicator.emit(
            DashboardLevel.ok if isOn else DashboardLevel.inactive)

    @pyqtSlot(int)
    def inSteeringWhilePosition(self, value: int) -> None:
        logging.debug(f"[Logic.inSteeringWhilePosition] New value = ${value}")
        level = DashboardLevel.ok
        if abs(value) >= self.config.steeringWheelEncoderWarning:
            level = DashboardLevel.warning
        if abs(value) >= self.config.steeringWheelEncoderDangerous:
            level = DashboardLevel.dangerous
        self.signals.outSteeringWheelEncoder.emit(value, level)

    @pyqtSlot(float, float, float)
    def inAccelerometer(self, x: float, y: float, z: float) -> None:
        logging.debug(f"[Logic.inAccelerometer] New x = ${x}, y = ${y}, z = ${z}")
        angel = math.degrees(math.atan(y / abs(x))) if x != 0.0 else 0.0
        if x < 0 and y < 0:
            angel += -90
        elif x < 0:
            angel += 90
        value = math.sqrt((x * x) + (y * y)) * self.config.accelerometerScale
        level = DashboardLevel.ok
        if self.driveMode == DriveMode.race:
            if value <= self.config.accelerometerRaceMinWarning \
                    or value >= self.config.accelerometerRaceMaxWarning:
                level = DashboardLevel.warning
            if value <= self.config.accelerometerRaceMinDangerous \
                    or value >= self.config.accelerometerRaceMaxDangerous:
                level = DashboardLevel.dangerous
        else:
            if value >= self.config.accelerometerStreetMaxWarning:
                level = DashboardLevel.warning
            if value >= self.config.accelerometerStreetMaxDangerous:
                level = DashboardLevel.dangerous
        self.signals.outAccelerometer.emit(angel, value, level)
