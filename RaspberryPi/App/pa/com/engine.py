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
created: 2019-12-12
"""

import logging
import time

from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal, QThread, QMutex

from Worker import Worker


class EngineComSignals(QObject):
    outEngineRpm         = pyqtSignal(float)
    outGearboxInRpm      = pyqtSignal(float)
    outGearboxOutRpm     = pyqtSignal(float)
    outGearNumber        = pyqtSignal(int)
    outOilPressure       = pyqtSignal(float)
    outOilTemperature    = pyqtSignal(float)
    outWatterTemperature = pyqtSignal(float)
        

class EngineCom(QObject):

    # Constructor

    def __init__(self) -> None:
        # Init
        super(EngineCom, self).__init__()
        self.signals = EngineComSignals()
        self.worker = Worker()
        self.engineRpm = 0.0
        self.gearboxInRpm = 0.0
        self.gearboxOutRpm = 0.0
        self.gearNumber = 0  # 0 - 5
        self.oilPressure = 0.0
        self.oilTemperature = 0.0
        self.watterTemperature = 0.0

    #
    # # Worker
    #
    # @pyqtSlot()
    # def run(self) -> None:
    #     logging.debug(f"[CabinCom.run] Start processing")
    #     while self.doWork:
    #         print("RRRRRRRRRRRRRRRRRRRRR1")


    # Methods

    def getEngineRpm(self) -> float:

        # TODO Get real value

        return self.engineRpm

    def getGearboxInRpm(self) -> float:

        # TODO Get real value

        return self.gearboxInRpm

    def getGearboxOutRpm(self) -> float:

        # TODO Get real value

        return self.gearboxOutRpm

    def getGearNumber(self) -> int:

        # TODO Get real value

        return self.gearNumber

    def getOilPressure(self) -> float:

        # TODO Get real value

        return self.oilPressure

    def getOilTemperature(self) -> float:

        # TODO Get real value

        return self.oilTemperature

    def getWatterTemperature(self) -> float:

        # TODO Get real value

        return self.watterTemperature

   # Input

    @pyqtSlot()
    def inStop(self) -> None:
        logging.debug(f"[CabinCom.inStop] Stop processing")
        self.worker.stop()
