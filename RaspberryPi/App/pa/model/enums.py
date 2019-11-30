#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

  TODO

author: CAB
website: github.com/alexcab
last edited: 2019-11-11
"""

from enum import Enum


class DashboardMode(Enum):
    race = 1
    street = 2


class DashboardLevel(Enum):
    inactive = 0
    ok = 1
    warning = 2
    dangerous = 3


class TurnIndication(Enum):
    none = 0
    left = 1
    right = 2
    both = 3

