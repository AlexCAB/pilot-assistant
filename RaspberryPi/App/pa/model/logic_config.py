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
from dataclasses import dataclass
from typing import List
import json


@dataclass
class LogicConfig:

    # Tachometer engine
    tachometerEngineScale: float
    tachometerEngineRaceMinDangerous: int
    tachometerEngineRaceMinWarning: int
    tachometerEngineRaceMaxWarning: int
    tachometerEngineRaceMaxDangerous: int
    tachometerEngineStreetMinDangerous: int
    tachometerEngineStreetMinWarning: int
    tachometerEngineStreetMaxWarning: int
    tachometerEngineStreetMaxDangerous: int
    # Tachometer gearbox
    tachometerGearboxScale: float
    tachometerGearboxDeviationWarning: int
    tachometerGearboxDeviationDangerous: int
    # Tachometer gears
    tachometerGear1Ratio: float
    tachometerGear2Ratio: float
    tachometerGear3Ratio: float
    tachometerGear4Ratio: float
    tachometerGear5Ratio: float
    # Accelerometer
    accelerometerScale: float
    accelerometerRaceMinDangerous: float
    accelerometerRaceMinWarning: float
    accelerometerRaceMaxWarning: float
    accelerometerRaceMaxDangerous: float
    accelerometerStreetMaxWarning: float
    accelerometerStreetMaxDangerous: float
    # Steering wheel encoder
    steeringWheelEncoderWarning: int
    steeringWheelEncoderDangerous: int
    # Speedometer
    speedometerRpmScale: float
    speedometerSpeedScale: float
    speedometerStreetMinDangerous: List[int]
    speedometerStreetMinWarning: List[int]
    speedometerStreetMaxWarning: List[int]
    speedometerStreetMaxDangerous: List[int]
    # Oil manometer
    oilManometerScale: float
    oilManometerMinDangerous: float
    oilManometerMinWarning: float
    oilManometerMaxWarning: float
    oilManometerMaxDangerous: float
    # Oil thermometer
    oilThermometerScale: float
    oilThermometerMinDangerous: float
    oilThermometerMinWarning: float
    oilThermometerMaxWarning: float
    oilThermometerMaxDangerous: float
    # Watter thermometer
    watterThermometerScale: float
    watterThermometerMinDangerous: float
    watterThermometerMinWarning: float
    watterThermometerMaxWarning: float
    watterThermometerMaxDangerous: float
    # Odometer
    odometerDistanceScale: float

    # Constructor

    def __init__(self, config: ConfigParser) -> None:
        # Init
        te = "TACHOMETER_ENGINE"
        self.tachometerEngineScale               = config.getfloat(te, "TachometerEngineScale")
        self.tachometerEngineRaceMinDangerous    = config.getint(te, "TachometerEngineRaceMinDangerous")
        self.tachometerEngineRaceMinWarning      = config.getint(te, "TachometerEngineRaceMinWarning")
        self.tachometerEngineRaceMaxWarning      = config.getint(te, "TachometerEngineRaceMaxWarning")
        self.tachometerEngineRaceMaxDangerous    = config.getint(te, "TachometerEngineRaceMaxDangerous")
        self.tachometerEngineStreetMinDangerous  = config.getint(te, "TachometerEngineStreetMinDangerous")
        self.tachometerEngineStreetMinWarning    = config.getint(te, "TachometerEngineStreetMinWarning")
        self.tachometerEngineStreetMaxWarning    = config.getint(te, "TachometerEngineStreetMaxWarning")
        self.tachometerEngineStreetMaxDangerous  = config.getint(te, "TachometerEngineStreetMaxDangerous")
        tgb = "TACHOMETER_GEARBOX"
        self.tachometerGearboxScale              = config.getfloat(tgb, "TachometerGearboxScale")
        self.tachometerGearboxDeviationWarning   = config.getint(tgb, "TachometerGearboxDeviationWarning")
        self.tachometerGearboxDeviationDangerous = config.getint(tgb, "TachometerGearboxDeviationDangerous")
        tg = "TACHOMETER_GEARS"
        self.tachometerGear1Ratio                = config.getfloat(tg, "TachometerGear1Ratio")
        self.tachometerGear2Ratio                = config.getfloat(tg, "TachometerGear2Ratio")
        self.tachometerGear3Ratio                = config.getfloat(tg, "TachometerGear3Ratio")
        self.tachometerGear4Ratio                = config.getfloat(tg, "TachometerGear4Ratio")
        self.tachometerGear5Ratio                = config.getfloat(tg, "TachometerGear5Ratio")
        a = "ACCELEROMETER"
        self.accelerometerScale                  = config.getfloat(a, "AccelerometerScale")
        self.accelerometerRaceMinDangerous       = config.getfloat(a, "AccelerometerRaceMinDangerous")
        self.accelerometerRaceMinWarning         = config.getfloat(a, "AccelerometerRaceMinWarning")
        self.accelerometerRaceMaxWarning         = config.getfloat(a, "AccelerometerRaceMaxWarning")
        self.accelerometerRaceMaxDangerous       = config.getfloat(a, "AccelerometerRaceMaxDangerous")
        self.accelerometerStreetMaxWarning       = config.getfloat(a, "AccelerometerStreetMaxWarning")
        self.accelerometerStreetMaxDangerous     = config.getfloat(a, "AccelerometerStreetMaxDangerous")
        swe = "STEERING_WHEEL_ENCODER"
        self.steeringWheelEncoderWarning         = config.getint(swe, "SteeringWheelEncoderWarning")
        self.steeringWheelEncoderDangerous       = config.getint(swe, "SteeringWheelEncoderDangerous")
        s = "SPEEDOMETER"
        self.speedometerRpmScale                 = config.getfloat(s, "SpeedometerRpmScale")
        self.speedometerSpeedScale               = config.getfloat(s, "SpeedometerSpeedScale")
        self.speedometerStreetMinDangerous       = json.loads(config.get(s, "SpeedometerStreetMinDangerous"))
        self.speedometerStreetMinWarning         = json.loads(config.get(s, "SpeedometerStreetMinWarning"))
        self.speedometerStreetMaxWarning         = json.loads(config.get(s, "SpeedometerStreetMaxWarning"))
        self.speedometerStreetMaxDangerous       = json.loads(config.get(s, "SpeedometerStreetMaxDangerous"))
        om = "OIL_MANOMETER"
        self.oilManometerScale                   = config.getfloat(om, "OilManometerScale")
        self.oilManometerMinDangerous            = config.getfloat(om, "OilManometerMinDangerous")
        self.oilManometerMinWarning              = config.getfloat(om, "OilManometerMinWarning")
        self.oilManometerMaxWarning              = config.getfloat(om, "OilManometerMaxWarning")
        self.oilManometerMaxDangerous            = config.getfloat(om, "OilManometerMaxDangerous")
        ot = "OIL_THERMOMETER"
        self.oilThermometerScale                 = config.getfloat(ot, "OilThermometerScale")
        self.oilThermometerMinDangerous          = config.getint(ot, "OilThermometerMinDangerous")
        self.oilThermometerMinWarning            = config.getint(ot, "OilThermometerMinWarning")
        self.oilThermometerMaxWarning            = config.getint(ot, "OilThermometerMaxWarning")
        self.oilThermometerMaxDangerous          = config.getint(ot, "OilThermometerMaxDangerous")
        wt = "WATTER_THERMOMETER"
        self.watterThermometerScale              = config.getfloat(wt, "WatterThermometerScale")
        self.watterThermometerMinDangerous       = config.getint(wt, "WatterThermometerMinDangerous")
        self.watterThermometerMinWarning         = config.getint(wt, "WatterThermometerMinWarning")
        self.watterThermometerMaxWarning         = config.getint(wt, "WatterThermometerMaxWarning")
        self.watterThermometerMaxDangerous       = config.getint(wt, "WatterThermometerMaxDangerous")
        wt = "ODOMETER"
        self.odometerDistanceScale = config.getfloat(wt, "OdometerDistanceScale")


