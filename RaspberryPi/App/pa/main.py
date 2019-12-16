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

from configparser import ConfigParser
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from model.logic_config import LogicConfig
from model.main_config import MainConfig
from ui.dashboard import Dashboard
from ui.tuning import Tuning
from com.cabin import CabinCom
from com.engine import EngineCom
from logic import Logic
from model.enums import *
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
    engineCom = EngineCom()
    cabinCom = CabinCom()
    dashboard = Dashboard(mainConfig.initDriveMode)
    logic = Logic(logicConfig, mainConfig.initDriveMode, engineCom, cabinCom)
    tuning = Tuning()
    # Connect logic to UI


    # Show UI
    if mainConfig.dashboardFullScreen:
        dashboard.showFullScreen()
    else:
        dashboard.show()
    # Create and show tuning UI
    if mainConfig.showTuningUi:
        tuning.show()
    #






    timer = QTimer()
    timer.timeout.connect(logic.tick)
    timer.start(2)





    app.exec_()


if __name__ == '__main__':
    main()
