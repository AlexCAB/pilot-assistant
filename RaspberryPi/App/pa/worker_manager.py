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
created: 2019-12-19
"""

import time
import traceback
from typing import List

from PyQt5.QtCore import QThreadPool

from worker import Worker
import logging


class WorkerManager(QThreadPool):

    # Constructor

    def __init__(self, workers: List[Worker]) -> None:
        # Init
        super(WorkerManager, self).__init__()
        self.workers = workers

    # Methods

    def startAll(self) -> None:
        logging.debug(f"[WorkerManager.start] Start all workers.")
        for w in self.workers:
            self.start(w)

    def stopAll(self) -> None:
        logging.debug(f"[WorkerManager.stop] Stop all workers.")
        for w in self.workers:
            try:
                w.stop()
            except:
                traceback.print_exc()
        while self.activeThreadCount() != 0:
            time.sleep(0.01)
