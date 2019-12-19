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
import traceback
from typing import Callable

from PyQt5.QtCore import QRunnable, pyqtSlot


class Worker(QRunnable):

    # Constructor

    def __init__(self, timeout: float, job:  Callable[[], None]) -> None:
        # Init
        super(Worker, self).__init__()
        self.timeout = timeout
        self.job = job
        self.doWork = True

    # Run job

    @pyqtSlot()
    def run(self) -> None:
        logging.debug(f"[Worker.run] Start processing")
        while self.doWork:
            logging.debug(f"[Worker.run] Run job, timeout = {self.timeout}")
            try:
                self.job()
            except:
                traceback.print_exc()
            time.sleep(self.timeout)

    # Methods

    def stop(self) -> None:
        logging.debug(f"[Worker.stop] Stop processing")
        self.doWork = False



