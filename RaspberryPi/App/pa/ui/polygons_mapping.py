#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

  TODO

author: CAB
website: github.com/alexcab
last edited: 2019-11-15
"""

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPolygonF


class PolygonsMapping(object):

    # Constants

    TACHOMETER_ENGINE = {
        0: QPolygonF([QPointF(6, 0), QPointF(30, 45), QPointF(123, 38), QPointF(115, 0)]),
        2: QPolygonF([QPointF(38, 57), QPointF(40, 62), QPointF(127, 54), QPointF(126, 48)]),
        4: QPolygonF([QPointF(47, 74), QPointF(50, 79), QPointF(133, 71), QPointF(132, 66)]),
        6: QPolygonF([QPointF(57, 92), QPointF(60, 98), QPointF(138, 88), QPointF(137, 83)]),
        8: QPolygonF([QPointF(68, 112), QPointF(71, 117), QPointF(144, 105), QPointF(143, 99)]),
        10: QPolygonF([QPointF(79, 131), QPointF(84, 141), QPointF(153, 126), QPointF(150, 116)]),
        12: QPolygonF([QPointF(91, 153), QPointF(94, 158), QPointF(159, 141), QPointF(157, 136)]),
        14: QPolygonF([QPointF(103, 170), QPointF(105, 175), QPointF(165, 157), QPointF(163, 152)]),
        16: QPolygonF([QPointF(115, 169), QPointF(118, 194), QPointF(174, 173), QPointF(171, 169)]),
        18: QPolygonF([QPointF(127, 208), QPointF(130, 212), QPointF(181, 190), QPointF(179, 186)]),
        20: QPolygonF([QPointF(141, 227), QPointF(146, 253), QPointF(194, 211), QPointF(189, 201)]),
        22: QPolygonF([QPointF(156, 248), QPointF(159, 252), QPointF(203, 225), QPointF(200, 221)]),
        24: QPolygonF([QPointF(170, 265), QPointF(173, 269), QPointF(214, 240), QPointF(211, 237)]),
        26: QPolygonF([QPointF(183, 280), QPointF(187, 284), QPointF(225, 254), QPointF(222, 250)]),
        28: QPolygonF([QPointF(198, 295), QPointF(201, 299), QPointF(238, 267), QPointF(233, 264)]),
        30: QPolygonF([QPointF(213, 311), QPointF(220, 318), QPointF(253, 282), QPointF(247, 276)]),
        32: QPolygonF([QPointF(231, 327), QPointF(235, 331), QPointF(266, 293), QPointF(262, 289)]),
        34: QPolygonF([QPointF(247, 340), QPointF(251, 343), QPointF(280, 305), QPointF(276, 302)]),
        36: QPolygonF([QPointF(266, 354), QPointF(269, 356), QPointF(296, 315), QPointF(292, 312)]),
        38: QPolygonF([QPointF(283, 365), QPointF(287, 367), QPointF(312, 325), QPointF(308, 322)]),
        40: QPolygonF([QPointF(299, 374), QPointF(307, 379), QPointF(332, 335), QPointF(323, 331)]),
        42: QPolygonF([QPointF(320, 384), QPointF(324, 387), QPointF(346, 343), QPointF(341, 340)]),
        44: QPolygonF([QPointF(338, 393), QPointF(342, 395), QPointF(362, 349), QPointF(357, 347)]),
        46: QPolygonF([QPointF(357, 400), QPointF(362, 402), QPointF(379, 357), QPointF(374, 355)]),
        48: QPolygonF([QPointF(376, 407), QPointF(380, 409), QPointF(369, 364), QPointF(391, 362)]),
        50: QPolygonF([QPointF(395, 412), QPointF(404, 415), QPointF(418, 370), QPointF(409, 368)]),
        52: QPolygonF([QPointF(416, 418), QPointF(421, 420), QPointF(434, 376), QPointF(429, 374)]),
        54: QPolygonF([QPointF(436, 422), QPointF(441, 424), QPointF(451, 380), QPointF(446, 379)]),
        56: QPolygonF([QPointF(455, 426), QPointF(460, 428), QPointF(469, 383), QPointF(464, 382)]),
        58: QPolygonF([QPointF(473, 429), QPointF(478, 431), QPointF(486, 388), QPointF(461, 386)]),
        60: QPolygonF([QPointF(493, 432), QPointF(502, 434), QPointF(509, 390), QPointF(499, 390)]),
        62: QPolygonF([QPointF(516, 435), QPointF(520, 436), QPointF(526, 393), QPointF(521, 392)]),
        64: QPolygonF([QPointF(533, 437), QPointF(543, 397), QPointF(543, 396), QPointF(538, 395)]),
        66: QPolygonF([QPointF(552, 439), QPointF(556, 439), QPointF(561, 397), QPointF(556, 397)]),
        68: QPolygonF([QPointF(570, 440), QPointF(575, 441), QPointF(579, 400), QPointF(574, 399)]),
        70: QPolygonF([QPointF(589, 442), QPointF(599, 442), QPointF(602, 402), QPointF(592, 401)]),
        72: QPolygonF([QPointF(611, 443), QPointF(616, 443), QPointF(618, 403), QPointF(613, 403)]),
        74: QPolygonF([QPointF(630, 444), QPointF(635, 444), QPointF(637, 403), QPointF(632, 404)]),
        76: QPolygonF([QPointF(649, 445), QPointF(654, 445), QPointF(655, 404), QPointF(650, 404)]),
        78: QPolygonF([QPointF(668, 446), QPointF(674, 446), QPointF(674, 405), QPointF(669, 405)]),
        80: QPolygonF([QPointF(685, 446), QPointF(694, 446), QPointF(695, 406), QPointF(685, 406)]),
        82: QPolygonF([QPointF(706, 447), QPointF(711, 447), QPointF(711, 406), QPointF(707, 406)]),
        84: QPolygonF([QPointF(726, 447), QPointF(731, 447), QPointF(731, 407), QPointF(726, 407)]),
        86: QPolygonF([QPointF(746, 448), QPointF(800, 448), QPointF(800, 408), QPointF(746, 408)])}

    TACHOMETER_GEARBOX = {
        0: QPolygonF([QPointF(121, 0), QPointF(128, 38), QPointF(215, 32), QPointF(227, 0)]),
        2: QPolygonF([QPointF(132, 48), QPointF(134, 53), QPointF(216, 45), QPointF(216, 39)]),
        4: QPolygonF([QPointF(138, 65), QPointF(139, 70), QPointF(217, 62), QPointF(216, 57)]),
        6: QPolygonF([QPointF(142, 82), QPointF(144, 87), QPointF(218, 76), QPointF(217, 72)]),
        8: QPolygonF([QPointF(149, 98), QPointF(151, 104), QPointF(219, 93), QPointF(219, 88)]),
        10: QPolygonF([QPointF(155, 115), QPointF(159, 125), QPointF(222, 111), QPointF(220, 101)]),
        12: QPolygonF([QPointF(162, 135), QPointF(164, 139), QPointF(224, 124), QPointF(223, 119)]),
        14: QPolygonF([QPointF(168, 150), QPointF(171, 155), QPointF(227, 137), QPointF(226, 132)]),
        16: QPolygonF([QPointF(176, 167), QPointF(178, 172), QPointF(231, 152), QPointF(230, 147)]),
        18: QPolygonF([QPointF(184, 183), QPointF(187, 188), QPointF(236, 166), QPointF(234, 162)]),
        20: QPolygonF([QPointF(194, 200), QPointF(199, 208), QPointF(245, 184), QPointF(241, 176)]),
        22: QPolygonF([QPointF(205, 218), QPointF(208, 222), QPointF(251, 196), QPointF(248, 191)]),
        24: QPolygonF([QPointF(216, 233), QPointF(219, 237), QPointF(260, 209), QPointF(257, 205)]),
        26: QPolygonF([QPointF(227, 246), QPointF(230, 251), QPointF(269, 221), QPointF(265, 217)]),
        28: QPolygonF([QPointF(239, 259), QPointF(242, 264), QPointF(278, 232), QPointF(275, 228)]),
        30: QPolygonF([QPointF(250, 272), QPointF(258, 279), QPointF(290, 244), QPointF(283, 237)]),
        32: QPolygonF([QPointF(266, 285), QPointF(270, 289), QPointF(300, 251), QPointF(296, 248)]),
        34: QPolygonF([QPointF(280, 269), QPointF(283, 300), QPointF(312, 261), QPointF(309, 258)]),
        36: QPolygonF([QPointF(295, 306), QPointF(299, 311), QPointF(325, 270), QPointF(320, 267)]),
        38: QPolygonF([QPointF(311, 217), QPointF(315, 320), QPointF(338, 279), QPointF(334, 276)]),
        40: QPolygonF([QPointF(325, 325), QPointF(334, 330), QPointF(356, 289), QPointF(347, 283)]),
        42: QPolygonF([QPointF(343, 335), QPointF(348, 338), QPointF(368, 295), QPointF(364, 292)]),
        44: QPolygonF([QPointF(359, 342), QPointF(364, 345), QPointF(383, 301), QPointF(378, 299)]),
        46: QPolygonF([QPointF(376, 350), QPointF(381, 353), QPointF(397, 308), QPointF(393, 306)]),
        48: QPolygonF([QPointF(393, 357), QPointF(398, 359), QPointF(413, 314), QPointF(408, 312)]),
        50: QPolygonF([QPointF(410, 362), QPointF(420, 366), QPointF(433, 321), QPointF(424, 318)]),
        52: QPolygonF([QPointF(430, 369), QPointF(435, 371), QPointF(448, 325), QPointF(443, 324)]),
        54: QPolygonF([QPointF(447, 373), QPointF(452, 375), QPointF(462, 330), QPointF(475, 328)]),
        56: QPolygonF([QPointF(465, 377), QPointF(470, 379), QPointF(478, 335), QPointF(474, 332)]),
        58: QPolygonF([QPointF(482, 281), QPointF(487, 383), QPointF(495, 338), QPointF(490, 337)]),
        60: QPolygonF([QPointF(500, 384), QPointF(510, 387), QPointF(516, 342), QPointF(507, 340)]),
        62: QPolygonF([QPointF(522, 387), QPointF(527, 388), QPointF(533, 344), QPointF(528, 343)]),
        64: QPolygonF([QPointF(539, 390), QPointF(544, 392), QPointF(550, 346), QPointF(545, 345)]),
        66: QPolygonF([QPointF(557, 392), QPointF(562, 393), QPointF(567, 349), QPointF(562, 347)]),
        68: QPolygonF([QPointF(575, 394), QPointF(580, 395), QPointF(584, 351), QPointF(579, 351)]),
        70: QPolygonF([QPointF(593, 395), QPointF(603, 396), QPointF(606, 352), QPointF(595, 351)]),
        72: QPolygonF([QPointF(614, 397), QPointF(619, 397), QPointF(621, 353), QPointF(617, 353)]),
        74: QPolygonF([QPointF(633, 398), QPointF(638, 398), QPointF(640, 354), QPointF(635, 354)]),
        76: QPolygonF([QPointF(651, 399), QPointF(656, 399), QPointF(657, 355), QPointF(652, 355)]),
        78: QPolygonF([QPointF(670, 400), QPointF(674, 400), QPointF(675, 356), QPointF(670, 356)]),
        80: QPolygonF([QPointF(686, 400), QPointF(695, 400), QPointF(697, 356), QPointF(687, 456)]),
        82: QPolygonF([QPointF(707, 401), QPointF(712, 401), QPointF(712, 356), QPointF(707, 356)]),
        84: QPolygonF([QPointF(726, 401), QPointF(731, 401), QPointF(731, 357), QPointF(726, 357)]),
        86: QPolygonF([QPointF(746, 401), QPointF(800, 401), QPointF(357, 800), QPointF(746, 357)])
    }

    ACCELEROMETER = {
        "C": (QPointF(629, 158), QPointF(678, 206)),
        "S": (QPointF(527, 56), QPointF(778, 306))
    }

    STEERING_WHEEL_ENCODER = {
        -7: QPolygonF([QPointF(523, 0), QPointF(529, 0), QPointF(529, 80), QPointF(523, 80)]),
        -6: QPolygonF([QPointF(538, 0), QPointF(542, 0), QPointF(542, 61), QPointF(538, 65)]),
        -5: QPolygonF([QPointF(551, 0), QPointF(555, 0), QPointF(555, 50), QPointF(551, 53)]),
        -4: QPolygonF([QPointF(564, 0), QPointF(568, 0), QPointF(568, 43), QPointF(564, 45)]),
        -3: QPolygonF([QPointF(577, 0), QPointF(581, 0), QPointF(581, 37), QPointF(577, 39)]),
        -2: QPolygonF([QPointF(590, 0), QPointF(594, 0), QPointF(594, 33), QPointF(590, 35)]),
        -1: QPolygonF([QPointF(603, 0), QPointF(607, 0), QPointF(607, 30), QPointF(603, 31)]),
        0: QPolygonF([QPointF(618, 0), QPointF(688, 0), QPointF(688, 27), QPointF(653, 25), QPointF(618, 27)]),
        +1: QPolygonF([QPointF(699, 0), QPointF(703, 0), QPointF(703, 31), QPointF(699, 30)]),
        +2: QPolygonF([QPointF(712, 0), QPointF(716, 0), QPointF(716, 34), QPointF(712, 33)]),
        +3: QPolygonF([QPointF(725, 0), QPointF(729, 0), QPointF(729, 39), QPointF(725, 37)]),
        +4: QPolygonF([QPointF(738, 0), QPointF(742, 0), QPointF(742, 45), QPointF(738, 43)]),
        +5: QPolygonF([QPointF(751, 0), QPointF(755, 0), QPointF(755, 53), QPointF(751, 50)]),
        +6: QPolygonF([QPointF(764, 0), QPointF(768, 0), QPointF(768, 65), QPointF(764, 61)]),
        +7: QPolygonF([QPointF(777, 0), QPointF(783, 0), QPointF(783, 80), QPointF(777, 80)])}

    TURN_INDICATOR = {
        "L": {
            "C": QPointF(21, 298),
            "P": [
                QPointF(0, 23), QPointF(23, 0), QPointF(23, 12), QPointF(48, 12),
                QPointF(48, 35), QPointF(23, 35), QPointF(23, 47)]},
        "R": {
            "C": QPointF(92, 298),
            "P": [
                QPointF(0, 12), QPointF(25, 12), QPointF(25, 0), QPointF(48, 23),
                QPointF(25, 47), QPointF(25, 35), QPointF(0, 35)]}}

    INDICATORS = {
        "O": {
            "C": QPointF(283, 438),
            "P": [
                QPolygonF([QPointF(2, 27), QPointF(18, 18), QPointF(18, 27), QPointF(5, 34)]),
                QPolygonF([QPointF(19, 2), QPointF(48, 2), QPointF(69, 27), QPointF(47, 15), QPointF(41, 22), QPointF(18, 22)]),
                QPolygonF([QPointF(23, 27), QPointF(37, 29), QPointF(22, 29)]),
                QPolygonF([QPointF(69, 27), QPointF(71, 24), QPointF(73, 25)]),
                QPolygonF([QPointF(76, 18), QPointF(74, 13), QPointF(75, 10), QPointF(78, 14)])]},
        "W": {
            "C": QPointF(139, 367),
            "P": [
                QPolygonF([QPointF(13, 1), QPointF(41, 1)]),
                QPolygonF([QPointF(0, 12), QPointF(18, 12)]),
                QPolygonF([QPointF(36, 12), QPointF(53, 12)]),
                QPolygonF([QPointF(24, 14), QPointF(23, 8), QPointF(31, 8), QPointF(31, 15)]),
                QPolygonF([QPointF(26, 15), QPointF(29, 15), QPointF(29, 46), QPointF(26, 46)]),
                QPolygonF([QPointF(28, 23), QPointF(35, 23)]),
                QPolygonF([QPointF(28, 30), QPointF(35, 30)]),
                QPolygonF([QPointF(28, 37), QPointF(35, 37)]),
                QPolygonF([QPointF(28, 44), QPointF(35, 44)])]}}

    SPEED_NUMBERS = {
        "A": QPolygonF([QPointF(11, 142), QPointF(22, 137), QPointF(59, 136), QPointF(63, 152), QPointF(18, 152),  QPointF(11, 146)]),
        "B": QPolygonF([QPointF(7, 80), QPointF(17, 91), QPointF(20, 131), QPointF(10, 137)]),
        "C": QPolygonF([QPointF(0, 15), QPointF(12, 21), QPointF(15, 62), QPointF(6, 71)]),
        "D": QPolygonF([QPointF(0, 9), QPointF(0, 5), QPointF(5, 0), QPointF(53, 0), QPointF(50, 15), QPointF(13, 15)]),
        "E": QPolygonF([QPointF(58, 0), QPointF(64, 5), QPointF(70, 72), QPointF(58, 62), QPointF(54, 15)]),
        "F": QPolygonF([QPointF(60, 90), QPointF(70, 79), QPointF(74, 145), QPointF(69, 152), QPointF(63, 135)]),
        "G": QPolygonF([QPointF(12, 76), QPointF(17, 68), QPointF(58, 68), QPointF(63, 77), QPointF(59, 84), QPointF(17, 84)])}

    STANDARD_NUMBERS = {
        "A": QPolygonF([QPointF(4, 44), QPointF(6, 42), QPointF(22, 42), QPointF(24, 44), QPointF(22, 46), QPointF(5, 46)]),
        "B": QPolygonF([QPointF(0, 26), QPointF(2, 24), QPointF(4, 26), QPointF(4, 41), QPointF(2, 43), QPointF(0, 41)]),
        "C": QPolygonF([QPointF(0, 5), QPointF(2, 3), QPointF(4, 5), QPointF(4, 20), QPointF(2, 22), QPointF(0, 20)]),
        "D": QPolygonF([QPointF(5, 0), QPointF(22, 0), QPointF(24, 2), QPointF(22, 4), QPointF(6, 4), QPointF(4, 1)]),
        "E": QPolygonF([QPointF(23, 6), QPointF(26, 4), QPointF(27, 5), QPointF(27, 20), QPointF(25, 22), QPointF(23, 20)]),
        "F": QPolygonF([QPointF(23, 26), QPointF(25, 24), QPointF(27, 26), QPointF(27, 41), QPointF(26, 42), QPointF(23, 40)]),
        "G": QPolygonF([QPointF(4, 23), QPointF(6, 21), QPointF(21, 21), QPointF(23, 23), QPointF(21, 25), QPointF(6, 25)])}

    NUMBER_TO_SEGMENTS = {
        0: ["A", "B", "C", "D", "E", "F"],
        1: ["B", "C"],
        2: ["A", "B", "G", "E", "D"],
        3: ["A", "B", "G", "C", "D"],
        4: ["F", "G", "B", "C"],
        5: ["A", "F", "G", "C", "D"],
        6: ["A", "C", "D", "E", "F", "G"],
        7: ["A", "B", "C"],
        8: ["A", "B", "C", "D", "E", "F", "G"],
        9: ["A", "B", "C", "D", "F", "G"]}

    GEAR_NUMBER = {
        "C": QPointF(182, 360),
        "P": {
             "A": QPolygonF([QPointF(4, 101), QPointF(14, 92), QPointF(74, 92), QPointF(84, 101)]),
             "B": QPolygonF([QPointF(0, 55), QPointF(5, 51), QPointF(12, 57), QPointF(12, 91), QPointF(0, 99)]),
             "C": QPolygonF([QPointF(0, 2), QPointF(12, 10), QPointF(12, 44), QPointF(5, 49), QPointF(0, 45)]),
             "D": QPolygonF([QPointF(4, 0), QPointF(84, 0), QPointF(74, 8), QPointF(14, 8)]),
             "E": QPolygonF([QPointF(76, 10), QPointF(88, 2), QPointF(88, 45), QPointF(82, 49), QPointF(76, 44)]),
             "F": QPolygonF([QPointF(76, 56), QPointF(82, 51), QPointF(88, 56), QPointF(88, 99), QPointF(76, 90)]),
             "G": QPolygonF([QPointF(10, 50), QPointF(15, 46), QPointF(73, 46), QPointF(78, 50), QPointF(74, 54), QPointF(13, 54)]),
             "M": QPolygonF([QPointF(43, 43), QPointF(66, 11), QPointF(73, 11), QPointF(73, 20), QPointF(56, 43)]),
             "J": QPolygonF([QPointF(15, 89), QPointF(15, 81), QPointF(33, 57), QPointF(47, 57), QPointF(23, 89)])},
        "M": {
            "N": ["B", "C", "E", "F", "M", "J"],
            "1": ["B", "C"],
            "2": ["A", "B", "G", "E", "D"],
            "3": ["A", "B", "G", "C", "D"],
            "4": ["F", "G", "B", "C"],
            "5": ["A", "F", "G", "C", "D"]}}

    SPEEDOMETER = {
        1: QPointF(273, 54),
        10: QPointF(349, 54),
        100: QPointF(425, 54)}

    STOPWATCH = {
        "MS1":  QPointF(478, 0),
        "MS10":  QPointF(445, 0),
        "S1":  QPointF(405, 0),
        "S10":  QPointF(372, 0),
        "M1":   QPointF(332, 0),
        "M10":   QPointF(299, 0),
        "H1":   QPointF(259, 0)}

    OIL_MANOMETER = {
        0.01: QPointF(100, 433),
        0.1: QPointF(68, 433),
        1:  QPointF(28, 433)}

    OIL_THERMOMETER = {
         1: QPointF(240, 433),
         10: QPointF(207, 433),
         100: QPointF(174, 433)}

    WATTER_THERMOMETER = {
         1: QPointF(94, 368),
         10: QPointF(61, 368),
         100: QPointF(28, 368)}

    ODOMETER = {
        1: QPointF(479, 216),
        10: QPointF(446, 216),
        100: QPointF(413, 216),
        1000: QPointF(380, 216)}
