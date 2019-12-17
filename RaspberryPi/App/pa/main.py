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
created: 2019-12-16
"""

import sys
from configparser import ConfigParser
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QThreadPool

from model.logic_config import LogicConfig
from model.main_config import MainConfig
from ui.dashboard import Dashboard
from ui.tuning import Tuning
from com.cabin import CabinCom
from com.engine import EngineCom
from logic import Logic
import logging


def main():
    # Logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Application starting...")
    # Read config
    config = ConfigParser()
    config.read("app.ini", encoding="UTF-8")
    mainConfig = MainConfig(config)
    logicConfig = LogicConfig(config)
    # Create components
    app = QApplication([])
    threadPool = QThreadPool()
    engineCom = EngineCom()
    cabinCom = CabinCom()
    dashboard = Dashboard(mainConfig.initDriveMode)
    logic = Logic(logicConfig, mainConfig.initDriveMode)
    tuning = Tuning(onExit=lambda: app.quit())
    # Connect components
    engineCom.signals.outEngineRpm.connect(logic.inEngineRpm)
    engineCom.signals.outGearboxInRpm.connect(logic.inGearboxInRpm)
    engineCom.signals.outGearboxOutRpm.connect(logic.inGearboxOutRpm)
    engineCom.signals.outGearNumber.connect(logic.inGearNumber)
    engineCom.signals.outOilPressure.connect(logic.inOilPressure)
    engineCom.signals.outOilTemperature.connect(logic.inOilTemperature)
    engineCom.signals.outWatterTemperature.connect(logic.inWatterTemperature)
    cabinCom.signals.outRaceModeIsOn.connect(logic.inRaceModeIsOn)
    cabinCom.signals.outStopwatchButtonIsOn.connect(logic.inStopwatchButtonIsOn)
    cabinCom.signals.outOdometerButtonIsOn.connect(logic.inOdometerButtonIsOn)
    cabinCom.signals.outTurnLeftSignalIsOn.connect(logic.inTurnLeftSignalIsOn)
    cabinCom.signals.outTurnRightSignalIsOn.connect(logic.inTurnRightSignalIsOn)
    cabinCom.signals.outSteeringWhilePosition.connect(logic.inSteeringWhilePosition)
    cabinCom.signals.outAccelerometer.connect(logic.inAccelerometer)
    logic.signals.outMode.connect(dashboard.inMode)
    logic.signals.outTachometerEngine.connect(dashboard.inTachometerEngine)
    logic.signals.outTachometerGearbox.connect(dashboard.inTachometerGearbox)
    logic.signals.outTachometerGears.connect(dashboard.inTachometerGears)
    logic.signals.outAccelerometer.connect(dashboard.inAccelerometer)
    logic.signals.outSteeringWheelEncoder.connect(dashboard.inSteeringWheelEncoder)
    logic.signals.outTurnIndicator.connect(dashboard.inTurnIndicator)
    logic.signals.outGearNumber.connect(dashboard.inGearNumber)
    logic.signals.outOilWarningIndicator.connect(dashboard.inOilWarningIndicator)
    logic.signals.outWatterWarningIndicator.connect(dashboard.inWatterWarningIndicator)
    logic.signals.outSpeedometer.connect(dashboard.inSpeedometer)
    logic.signals.outStopwatch.connect(dashboard.inStopwatch)
    logic.signals.outOilManometer.connect(dashboard.inOilManometer)
    logic.signals.outOilThermometer.connect(dashboard.inOilThermometer)
    logic.signals.outWatterThermometer.connect(dashboard.inWatterThermometer)
    logic.signals.outOdometer.connect(dashboard.inOdometer)
    app.aboutToQuit.connect(logic.inStop)
    app.aboutToQuit.connect(cabinCom.inStop)
    app.aboutToQuit.connect(engineCom.inStop)
    # Show UI
    if mainConfig.dashboardFullScreen:
        dashboard.showFullScreen()
    else:
        dashboard.show()
    if mainConfig.showTuningUi:
        tuning.show()
    # Run processing
    threadPool.start(logic.worker)
    threadPool.start(cabinCom.worker)
    threadPool.start(engineCom.worker)
    # Start events loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
