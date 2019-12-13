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
from configparser import ConfigParser
from com.cabin import CabinCom
from com.engine import EngineCom
from ui.dashboard import Dashboard
from model.enums import *
import traceback


class Logic:

    # Constructor

    def __init__(self, config: ConfigParser, engineCom: EngineCom, cabinCom: CabinCom, dashboard: Dashboard) -> None:
        # Init
        self.engineCom = engineCom
        self.cabinCom = cabinCom
        self.dashboard = dashboard






        if config.getboolean(section="DASHBOARD", option="FullScreen"):
            dashboard.showFullScreen()
        else:
            dashboard.show()

        self.dashboard = dashboard

        self.testLevel = DashboardLevel.ok

        self.tachometerEngineValueRpm = 0  # 0 - 9000
        self.tachometerGearboxValueRpm = 0  # 0 - 9000
        self.tachometerGear1Rpm = 0  # 0 - 9000
        self.tachometerGear2Rpm = 0  # 0 - 9000
        self.tachometerGear3Rpm = 0  # 0 - 9000
        self.tachometerGear4Rpm = 0  # 0 - 9000
        self.tachometerGear5Rpm = 0  # 0 - 9000
        self.accelerometerAngel = 0  # -180 - +180
        self.accelerometerValue = 0.0  # 0.0 - 1.0
        self.steeringWheelEncoderAngel = 0  # -7 - +7
        self.turnIndicatorState = TurnIndication.none
        self.gearNumberValue = 0  # 0 - 5
        self.speedometerValue = 0  # 0 - 999
        self.stopwatchMills = 0  # 0 - 99
        self.stopwatchSeconds = 0  # 0 - 59
        self.stopwatchMinutes = 0  # 0 - 59
        self.stopwatchHours = 0  # 0 - 9
        self.oilManometerValue = 0.0  # 0.0 - 9.99
        self.oilThermometerValue = 0  # 0 - 999
        self.watterThermometerValue = 0  # 0 - 999
        self.odometerValue = 0  # 0 - 9999






    # Methods

    def tick(self) -> None:





        logging.debug(f"[Logic.tick] Start update")

        try:

            #
            # if self.testLevel == DashboardLevel.ok:
            #     self.testLevel = DashboardLevel.warning
            # elif self.testLevel == DashboardLevel.warning:
            #     self.testLevel = DashboardLevel.dangerous
            # else:
            #     self.testLevel = DashboardLevel.ok

            self.tachometerEngineValueRpm += 10
            if self.tachometerEngineValueRpm > 9000: self.tachometerEngineValueRpm = 0  # 0 - 9000
            self.tachometerGearboxValueRpm += 20
            if self.tachometerGearboxValueRpm > 9000: self.tachometerGearboxValueRpm = 0  # 0 - 9000

            self.tachometerGear1Rpm += 10  # 0 - 9000
            if self.tachometerGear1Rpm > 9000: self.tachometerGear1Rpm = 0  # 0 - 9000

            self.tachometerGear2Rpm += 20  # 0 - 9000
            if self.tachometerGear2Rpm > 9000: self.tachometerGear2Rpm = 0  # 0 - 9000

            self.tachometerGear3Rpm += 30  # 0 - 9000
            if self.tachometerGear3Rpm > 9000: self.tachometerGear3Rpm = 0  # 0 - 9000

            self.tachometerGear4Rpm += 40  # 0 - 9000
            if self.tachometerGear4Rpm > 9000: self.tachometerGear4Rpm = 0  # 0 - 9000

            self.tachometerGear5Rpm += 50  # 0 - 9000
            if self.tachometerGear5Rpm > 9000: self.tachometerGear5Rpm = 0  # 0 - 9000













            self.accelerometerAngel += 10
            if self.accelerometerAngel > 180: self.accelerometerAngel = -180  # -180 - +180
            self.accelerometerValue += 0.1
            if self.accelerometerValue > 1.0: self.accelerometerValue = 0.0  # 0.0 - 1.0
            self.steeringWheelEncoderAngel += 1
            if self.steeringWheelEncoderAngel > 7: self.steeringWheelEncoderAngel = -7  # -7 - +7
            if self.turnIndicatorState == TurnIndication.none:
                self.turnIndicatorState = TurnIndication.left
            elif self.turnIndicatorState == TurnIndication.left:
                self.turnIndicatorState = TurnIndication.right
            elif self.turnIndicatorState == TurnIndication.right:
                self.turnIndicatorState = TurnIndication.both
            else:
                self.turnIndicatorState = TurnIndication.none
            self.gearNumberValue += 1
            if self.gearNumberValue > 5: self.gearNumberValue = 0  # 0 - 5
            self.speedometerValue += 1
            if self.speedometerValue > 999:  self.speedometerValue = 0  # 0 - 999
            self.stopwatchMills += 1
            if self.stopwatchMills > 99: self.stopwatchMills = 0  # 0 - 99
            self.stopwatchSeconds += 1
            if self.stopwatchSeconds > 59: self.stopwatchSeconds = 0  # 0 - 59
            self.stopwatchMinutes += 1
            if self.stopwatchMinutes > 59: self.stopwatchMinutes = 0  # 0 - 59
            self.stopwatchHours += 1
            if self.stopwatchHours > 9: self.stopwatchHours = 0  # 0 - 9
            self.oilManometerValue += 0.01
            if self.oilManometerValue > 9.99: self.oilManometerValue = 0.0  # 0.0 - 9.99
            self.oilThermometerValue += 1
            if self.oilThermometerValue > 999: self.oilThermometerValue = 0  # 0 - 999
            self.watterThermometerValue += 1
            if self.watterThermometerValue > 999: self.watterThermometerValue = 0  # 0 - 999
            self.odometerValue += 1
            if self.odometerValue > 9999: self.odometerValue = 0  # 0 - 9999
            self.dashboard.setTachometerEngine(self.tachometerEngineValueRpm, self.testLevel)
            self.dashboard.setTachometerGearbox(self.tachometerGearboxValueRpm, self.testLevel)
            self.dashboard.setTachometerGears(
                self.tachometerGear1Rpm,
                self.tachometerGear2Rpm,
                self.tachometerGear3Rpm,
                self.tachometerGear4Rpm,
                self.tachometerGear5Rpm)
            self.dashboard.setAccelerometer(self.accelerometerAngel, self.accelerometerValue, self.testLevel)
            self.dashboard.setSteeringWheelEncoder(self.steeringWheelEncoderAngel, self.testLevel)
            self.dashboard.setTurnIndicator(self.turnIndicatorState, self.testLevel)
            self.dashboard.setGearNumber(self.gearNumberValue, self.testLevel)
            self.dashboard.setOilWarningIndicator(self.testLevel)
            self.dashboard.setWatterWarningIndicator(self.testLevel)
            self.dashboard.setSpeedometer(self.speedometerValue, self.testLevel)
            self.dashboard.setStopwatch(self.stopwatchMills, self.stopwatchSeconds, self.stopwatchMinutes,
                                        self.stopwatchHours, self.testLevel)
            self.dashboard.setOilManometer(self.oilManometerValue, self.testLevel)
            self.dashboard.setOilThermometer(self.oilThermometerValue, self.testLevel)
            self.dashboard.setWatterThermometer(self.watterThermometerValue, self.testLevel)
            self.dashboard.setOdometer(self.odometerValue, self.testLevel)

        except Exception as err:
            traceback.print_exc()

            print("FFFFFFFFFFFFFFFFFFFF err" + str(err.args))
         
