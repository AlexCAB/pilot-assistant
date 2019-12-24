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

from PyQt5.QtCore import  QObject, pyqtSignal
from gpiozero.pins.pigpio import PiGPIOFactory

from worker import Worker

from gpiozero import Button


class CabinComSignals(QObject):
    outRaceModeIsOn          = pyqtSignal(bool)
    outStopwatchButtonIsOn   = pyqtSignal(bool)
    outOdometerButtonIsOn    = pyqtSignal(bool)
    outTurnLeftSignalIsOn    = pyqtSignal(bool)
    outTurnRightSignalIsOn   = pyqtSignal(bool)
    outSteeringWhilePosition = pyqtSignal(int)
    outAccelerometer         = pyqtSignal(float, float, float)


class CabinCom(QObject):

    # Parameters

    PIN_DRIVE_MODE = 17
    PIN_STOPWATCH = 27
    PIN_ODOMETER = 22
    PIN_TERN_LEFT = 23
    PIN_TURN_RIGHT = 24
    PIN_STEERING_ENCODER_CLK = 5
    PIN_STEERING_ENCODER_DT = 6
    PIN_STEERING_ENCODER_SW = 26
    PIN_STEERING_ENCODER_MAX_COUNT = 7

    # Constructor

    def __init__(self) -> None:
        # Init
        super(CabinCom, self).__init__()
        self.signals = CabinComSignals()
        self.worker = Worker(timeout=0.1, job=self.job)
        self.doInit = True
        self.timer = 0
        self.raceModeIsOn = False
        self.turnLeftSignalIsOn = False
        self.turnRightSignalIsOn = False
        self.steeringWhilePosition = 0
        self.accelerometerX = 0.0
        self.accelerometerY = 0.0
        self.accelerometerZ = 0.0
        # Init driving mode switch
        self.drivingModeSwitch = Button(self.PIN_DRIVE_MODE, bounce_time=.01)
        # Init stopwatch button
        self.stopwatchButton = Button(self.PIN_STOPWATCH, pull_up=False, bounce_time=.01)
        self.stopwatchButton.when_activated = self.stopwatchIsPressed
        self.stopwatchButton.when_deactivated = self.stopwatchIsReleased
        # Init odometer button
        self.odometerButton = Button(self.PIN_ODOMETER, pull_up=False, bounce_time=.01)
        self.odometerButton.when_activated = self.odometerIsPressed
        self.odometerButton.when_deactivated = self.odometerIsReleased
        # Init turn left button
        self.turnLeftSignalButton = Button(self.PIN_TERN_LEFT, pull_up=False, bounce_time=.01)
        # Init turn right button
        self.turnRightSignalButton = Button(self.PIN_TURN_RIGHT, pull_up=False, bounce_time=.01)
        # Init steering while encoder
        self.steeringWheelEncoderClkButton = Button(self.PIN_STEERING_ENCODER_CLK, bounce_time=.002)
        self.steeringWheelEncoderClkButton.when_activated = self.steeringWheelEncoderClkIsPressed
        self.steeringWheelEncoderDtButton = Button(self.PIN_STEERING_ENCODER_DT,  bounce_time=.002)
        self.steeringWheelEncoderDtButton.when_activated = self.steeringWheelEncoderDtIsPressed
        self.steeringWheelEncoderSwButton = Button(self.PIN_STEERING_ENCODER_SW, bounce_time=.01)
        self.steeringWheelEncoderSwButton.when_activated = self.steeringWheelEncoderSwIsPressed

    # Worker job

    def job(self) -> None:
        logging.debug(f"[CabinCom.job]  Tick # {self.timer}")
        # Set driving mode
        if self.drivingModeSwitch.value != self.raceModeIsOn or self.doInit:
            self.signals.outRaceModeIsOn.emit(self.drivingModeSwitch.value)
            self.raceModeIsOn = self.drivingModeSwitch.value
        # Set stopwatch
        if self.doInit:
            self.signals.outStopwatchButtonIsOn.emit(self.stopwatchButton.value)
        # Set odometer
        if self.doInit:
            self.signals.outOdometerButtonIsOn.emit(self.odometerButton.value)
        # Set turn left
        if self.turnLeftSignalButton.value != self.turnLeftSignalIsOn or self.doInit:
            self.signals.outTurnLeftSignalIsOn.emit(self.turnLeftSignalButton.value)
            self.turnLeftSignalIsOn = self.turnLeftSignalButton.value
        # Set turn right
        if self.turnRightSignalButton.value != self.turnRightSignalIsOn or self.doInit:
            self.signals.outTurnRightSignalIsOn.emit(self.turnRightSignalButton.value)
            self.turnRightSignalIsOn = self.turnRightSignalButton.value
        # Set steering while encoder
        if self.doInit and self.steeringWheelEncoderSwButton.value:
            self.signals.outSteeringWhilePosition.emit(0)
        # Reset do init flag
        self.doInit = False




        # if self.timer % 1 == 0:
        #     self.accelerometerX += 0.5
        #     if self.accelerometerX > 10.0:
        #         self.accelerometerX = -10.0
        #     self.accelerometerY += 0.2
        #     if self.accelerometerY > 10.0:
        #         self.accelerometerY = -10.0
        #     self.accelerometerZ += 0.5
        #     if self.accelerometerZ > 10.0:
        #         self.accelerometerZ = -10.0
        #     self.signals.outAccelerometer.emit(self.accelerometerX, self.accelerometerY, self.accelerometerZ)

        self.timer += 1

    # Functions

    def stopwatchIsPressed(self) -> None:
        logging.debug(f"[Logic.stopwatchIsPressed] Emmit outStopwatchButtonIsOn = True")
        self.signals.outStopwatchButtonIsOn.emit(True)

    def stopwatchIsReleased(self) -> None:
        logging.debug(f"[Logic.stopwatchIsReleased] Emmit outStopwatchButtonIsOn = False")
        self.signals.outStopwatchButtonIsOn.emit(False)

    def odometerIsPressed(self) -> None:
        logging.debug(f"[Logic.odometerIsPressed] Emmit outOdometerButtonIsOn = True")
        self.signals.outOdometerButtonIsOn.emit(True)

    def odometerIsReleased(self) -> None:
        logging.debug(f"[Logic.odometerIsReleased] Emmit outOdometerButtonIsOn = False")
        self.signals.outOdometerButtonIsOn.emit(False)

    def steeringWheelEncoderClkIsPressed(self) -> None:
        logging.debug(f"[Logic.steeringWheelEncoderClkIsPressed] Decrease position.")
        if self.steeringWheelEncoderDtButton.value and \
                self.steeringWhilePosition > -self.PIN_STEERING_ENCODER_MAX_COUNT:
            self.steeringWhilePosition -= 1
            self.signals.outSteeringWhilePosition.emit(self.steeringWhilePosition)

    def steeringWheelEncoderDtIsPressed(self) -> None:
        logging.debug(f"[Logic.steeringWheelEncoderDtIsPressed] Increase position.")
        if self.steeringWheelEncoderClkButton.value and \
                self.steeringWhilePosition < self.PIN_STEERING_ENCODER_MAX_COUNT:
            self.steeringWhilePosition += 1
            self.signals.outSteeringWhilePosition.emit(self.steeringWhilePosition)

    def steeringWheelEncoderSwIsPressed(self) -> None:
        logging.debug(f"[Logic.steeringWheelEncoderSwIsPressed] Reset position.")
        self.steeringWhilePosition = 0
        self.signals.outSteeringWhilePosition.emit(0)
