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
created: 2019-12-13
"""

import logging
import time

from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal, QThread

from worker import Worker


class CabinComSignals(QObject):
    outRaceModeIsOn          = pyqtSignal(bool)
    outStopwatchButtonIsOn   = pyqtSignal(bool)
    outOdometerButtonIsOn    = pyqtSignal(bool)
    outTurnLeftSignalIsOn    = pyqtSignal(bool)
    outTurnRightSignalIsOn   = pyqtSignal(bool)
    outSteeringWhilePosition = pyqtSignal(int)
    outAccelerometer         = pyqtSignal(float, float, float)


class CabinCom(QObject):

    # Constructor

    def __init__(self) -> None:
        # Init
        super(CabinCom, self).__init__()
        self.signals = CabinComSignals()
        self.worker = Worker(timeout=0.1, job=self.job)
        self.raceModeIsOn = False
        self.stopwatchButtonIsOn = False
        self.odometerButtonIsOn = False
        self.turnLeftSignalIsOn = False
        self.turnRightSignalIsOn = False
        self.steeringWhilePosition = 0  # -7 - +7
        self.accelerometerX = 0.0
        self.accelerometerY = 0.0
        self.accelerometerZ = 0.0

    # Worker job

    def job(self) -> None:
        logging.debug(f"[CabinCom.job] Start processing")

    # Methods

    def getRaceModeIsOn(self) -> bool:

        # TODO Get real value

        return self.raceModeIsOn

    def getStopwatchButtonIsOn(self) -> bool:

        # TODO Get real value

        return self.stopwatchButtonIsOn

    def getOdometerButtonIsOn(self) -> bool:

        # TODO Get real value

        return self.odometerButtonIsOn

    def getTurnLeftSignalIsOn(self) -> bool:

        # TODO Get real value

        return self.turnLeftSignalIsOn

    def getTurnRightSignalIsOn(self) -> bool:

        # TODO Get real value

        return self.turnRightSignalIsOn

    def getSteeringWhilePosition(self) -> int:

        # TODO Get real value

        return self.steeringWhilePosition

    def getAccelerometer(self) -> (float, float, float):  # Returns: (x, y, z)

        # TODO Get real value

        return self.accelerometerX, self.accelerometerY, self.accelerometerZ
