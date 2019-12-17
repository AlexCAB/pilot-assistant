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
import time

from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal, QThread

from Worker import Worker
from com.cabin import CabinCom
from com.engine import EngineCom
from model.logic_config import LogicConfig
from ui.dashboard import Dashboard
from model.enums import *
import traceback


class LogicSignals(QObject):
    outMode                   = pyqtSignal(DriveMode)  # (mode)
    outTachometerEngine       = pyqtSignal(int, DashboardLevel)  # (rpm, level)
    outTachometerGearbox      = pyqtSignal(int, DashboardLevel)  # (rpm, level)
    outTachometerGears        = pyqtSignal(int, int, int, int, int)  # (rpm1, rpm2, rpm3, rpm4, rpm5)
    outAccelerometer          = pyqtSignal(int, float, DashboardLevel)  # (angel, value, level)
    outSteeringWheelEncoder   = pyqtSignal(int, DashboardLevel)  # (angel, level)
    outTurnIndicator          = pyqtSignal(TurnIndication, DashboardLevel)  # (state, level)
    outGearNumber             = pyqtSignal(int, DashboardLevel)  # (value, level)
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
        self.signals = LogicSignals()
        self.worker = Worker()





        #
        # if config.getboolean(section="DASHBOARD", option="FullScreen"):
        #     dashboard.showFullScreen()
        # else:
        #     dashboard.show()

        # self.dashboard = dashboard
        #
        # self.testLevel = DashboardLevel.ok
        #
        # self.tachometerEngineValueRpm = 0  # 0 - 9000
        # self.tachometerGearboxValueRpm = 0  # 0 - 9000
        # self.tachometerGear1Rpm = 0  # 0 - 9000
        # self.tachometerGear2Rpm = 0  # 0 - 9000
        # self.tachometerGear3Rpm = 0  # 0 - 9000
        # self.tachometerGear4Rpm = 0  # 0 - 9000
        # self.tachometerGear5Rpm = 0  # 0 - 9000
        # self.accelerometerAngel = 0  # -180 - +180
        # self.accelerometerValue = 0.0  # 0.0 - 1.0
        # self.steeringWheelEncoderAngel = 0  # -7 - +7
        # self.turnIndicatorState = TurnIndication.none
        # self.gearNumberValue = 0  # 0 - 5
        # self.speedometerValue = 0  # 0 - 999
        # self.stopwatchMills = 0  # 0 - 99
        # self.stopwatchSeconds = 0  # 0 - 59
        # self.stopwatchMinutes = 0  # 0 - 59
        # self.stopwatchHours = 0  # 0 - 9
        # self.oilManometerValue = 0.0  # 0.0 - 9.99
        # self.oilThermometerValue = 0  # 0 - 999
        # self.watterThermometerValue = 0  # 0 - 999
        # self.odometerValue = 0  # 0 - 9999






    # # Worker
    #
    # @pyqtSlot()
    # def run(self) -> None:
    #     logging.debug(f"[Logic.run] Start processing")
    #     # while self.doWork:
    #     #     print("RRRRRRRRRRRRRRRRRRRRR3")



    # Input

    @pyqtSlot(float)
    def inEngineRpm(self, rpm: float) -> None:
        logging.debug(f"[Logic.inEngineRpm] New rpm = ${rpm}")

    @pyqtSlot(float)
    def inGearboxInRpm(self, rpm: float) -> None:
        logging.debug(f"[Logic.inGearboxInRpm] New rpm = ${rpm}")

    @pyqtSlot(float)
    def inGearboxOutRpm(self, rpm: float) -> None:
        logging.debug(f"[Logic.inGearboxOutRpm] New rpm = ${rpm}")

    @pyqtSlot(int)
    def inGearNumber(self, number: int) -> None:
        logging.debug(f"[Logic.inGearNumber] New number = ${number}")

    @pyqtSlot(float)
    def inOilPressure(self, value: float) -> None:
        logging.debug(f"[Logic.inOilPressure] New value = ${value}")

    @pyqtSlot(float)
    def inOilTemperature(self, value: float) -> None:
        logging.debug(f"[Logic.inOilTemperature] New value = ${value}")

    @pyqtSlot(float)
    def inWatterTemperature(self, value: float) -> None:
        logging.debug(f"[Logic.inWatterTemperature] New value = ${value}")

    @pyqtSlot(bool)
    def inRaceModeIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inRaceModeIsOn] New isOn = ${isOn}")

    @pyqtSlot(bool)
    def inStopwatchButtonIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inStopwatchButtonIsOn] New isOn = ${isOn}")

    @pyqtSlot(bool)
    def inOdometerButtonIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inOdometerButtonIsOn] New isOn = ${isOn}")

    @pyqtSlot(bool)
    def inTurnLeftSignalIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inTurnLeftSignalIsOn] New isOn = ${isOn}")

    @pyqtSlot(bool)
    def inTurnRightSignalIsOn(self, isOn: bool) -> None:
        logging.debug(f"[Logic.inTurnRightSignalIsOn] New isOn = ${isOn}")

    @pyqtSlot(int)
    def inSteeringWhilePosition(self, value: int) -> None:
        logging.debug(f"[Logic.inSteeringWhilePosition] New value = ${value}")

    @pyqtSlot(float, float, float)
    def inAccelerometer(self, x: float, y: float, z: float) -> None:
        logging.debug(f"[Logic.inAccelerometer] New x = ${x}, y = ${y}, z = ${z}")

    @pyqtSlot()
    def inStop(self) -> None:
        logging.debug(f"[CabinCom.inStop] Stop processing")
        self.worker.stop()










            # self.signals.test.emit(1, "2")
        #
        # print("FFFFFFFFFFFFFFFF1")
        #
        # time.sleep(2)
        # print("FFFFFFFFFFFFFFFF2")

        # try:
        #     pass
        #
        #     #
        #     # if self.testLevel == DashboardLevel.ok:
        #     #     self.testLevel = DashboardLevel.warning
        #     # elif self.testLevel == DashboardLevel.warning:
        #     #     self.testLevel = DashboardLevel.dangerous
        #     # else:
        #     #     self.testLevel = DashboardLevel.ok
        #
        #     # self.tachometerEngineValueRpm += 10
        #     # if self.tachometerEngineValueRpm > 9000: self.tachometerEngineValueRpm = 0  # 0 - 9000
        #     # self.tachometerGearboxValueRpm += 20
        #     # if self.tachometerGearboxValueRpm > 9000: self.tachometerGearboxValueRpm = 0  # 0 - 9000
        #     #
        #     # self.tachometerGear1Rpm += 10  # 0 - 9000
        #     # if self.tachometerGear1Rpm > 9000: self.tachometerGear1Rpm = 0  # 0 - 9000
        #     #
        #     # self.tachometerGear2Rpm += 20  # 0 - 9000
        #     # if self.tachometerGear2Rpm > 9000: self.tachometerGear2Rpm = 0  # 0 - 9000
        #     #
        #     # self.tachometerGear3Rpm += 30  # 0 - 9000
        #     # if self.tachometerGear3Rpm > 9000: self.tachometerGear3Rpm = 0  # 0 - 9000
        #     #
        #     # self.tachometerGear4Rpm += 40  # 0 - 9000
        #     # if self.tachometerGear4Rpm > 9000: self.tachometerGear4Rpm = 0  # 0 - 9000
        #     #
        #     # self.tachometerGear5Rpm += 50  # 0 - 9000
        #     # if self.tachometerGear5Rpm > 9000: self.tachometerGear5Rpm = 0  # 0 - 9000
        #     #
        #     # self.accelerometerAngel += 10
        #     # if self.accelerometerAngel > 180: self.accelerometerAngel = -180  # -180 - +180
        #     # self.accelerometerValue += 0.1
        #     # if self.accelerometerValue > 1.0: self.accelerometerValue = 0.0  # 0.0 - 1.0
        #     # self.steeringWheelEncoderAngel += 1
        #     # if self.steeringWheelEncoderAngel > 7: self.steeringWheelEncoderAngel = -7  # -7 - +7
        #     # if self.turnIndicatorState == TurnIndication.none:
        #     #     self.turnIndicatorState = TurnIndication.left
        #     # elif self.turnIndicatorState == TurnIndication.left:
        #     #     self.turnIndicatorState = TurnIndication.right
        #     # elif self.turnIndicatorState == TurnIndication.right:
        #     #     self.turnIndicatorState = TurnIndication.both
        #     # else:
        #     #     self.turnIndicatorState = TurnIndication.none
        #     # self.gearNumberValue += 1
        #     # if self.gearNumberValue > 5: self.gearNumberValue = 0  # 0 - 5
        #     # self.speedometerValue += 1
        #     # if self.speedometerValue > 999:  self.speedometerValue = 0  # 0 - 999
        #     # self.stopwatchMills += 1
        #     # if self.stopwatchMills > 99: self.stopwatchMills = 0  # 0 - 99
        #     # self.stopwatchSeconds += 1
        #     # if self.stopwatchSeconds > 59: self.stopwatchSeconds = 0  # 0 - 59
        #     # self.stopwatchMinutes += 1
        #     # if self.stopwatchMinutes > 59: self.stopwatchMinutes = 0  # 0 - 59
        #     # self.stopwatchHours += 1
        #     # if self.stopwatchHours > 9: self.stopwatchHours = 0  # 0 - 9
        #     # self.oilManometerValue += 0.01
        #     # if self.oilManometerValue > 9.99: self.oilManometerValue = 0.0  # 0.0 - 9.99
        #     # self.oilThermometerValue += 1
        #     # if self.oilThermometerValue > 999: self.oilThermometerValue = 0  # 0 - 999
        #     # self.watterThermometerValue += 1
        #     # if self.watterThermometerValue > 999: self.watterThermometerValue = 0  # 0 - 999
        #     # self.odometerValue += 1
        #     # if self.odometerValue > 9999: self.odometerValue = 0  # 0 - 9999
        #     # self.dashboard.setTachometerEngine(self.tachometerEngineValueRpm, self.testLevel)
        #     # self.dashboard.setTachometerGearbox(self.tachometerGearboxValueRpm, self.testLevel)
        #     # self.dashboard.setTachometerGears(
        #     #     self.tachometerGear1Rpm,
        #     #     self.tachometerGear2Rpm,
        #     #     self.tachometerGear3Rpm,
        #     #     self.tachometerGear4Rpm,
        #     #     self.tachometerGear5Rpm)
        #     # self.dashboard.setAccelerometer(self.accelerometerAngel, self.accelerometerValue, self.testLevel)
        #     # self.dashboard.setSteeringWheelEncoder(self.steeringWheelEncoderAngel, self.testLevel)
        #     # self.dashboard.setTurnIndicator(self.turnIndicatorState, self.testLevel)
        #     # self.dashboard.setGearNumber(self.gearNumberValue, self.testLevel)
        #     # self.dashboard.setOilWarningIndicator(self.testLevel)
        #     # self.dashboard.setWatterWarningIndicator(self.testLevel)
        #     # self.dashboard.setSpeedometer(self.speedometerValue, self.testLevel)
        #     # self.dashboard.setStopwatch(self.stopwatchMills, self.stopwatchSeconds, self.stopwatchMinutes,
        #     #                             self.stopwatchHours, self.testLevel)
        #     # self.dashboard.setOilManometer(self.oilManometerValue, self.testLevel)
        #     # self.dashboard.setOilThermometer(self.oilThermometerValue, self.testLevel)
        #     # self.dashboard.setWatterThermometer(self.watterThermometerValue, self.testLevel)
        #     # self.dashboard.setOdometer(self.odometerValue, self.testLevel)
        #
        # except Exception as err:
        #     traceback.print_exc()
        #
        #     print("FFFFFFFFFFFFFFFFFFFF err" + str(err.args))
         
