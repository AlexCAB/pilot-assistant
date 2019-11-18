#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

  TODO

author: CAB
website: github.com/alexcab
last edited: 2019-11-15
"""

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPolygon


class PolygonsMapping(object):

    # Constants

    TACHOMETER_ENGINE = {
        0: QPolygon([QPoint(6, 0), QPoint(30, 45), QPoint(123, 38), QPoint(115, 0)]),
        2: QPolygon([QPoint(38, 57), QPoint(40, 62), QPoint(127, 54), QPoint(126, 48)]),
        4: QPolygon([QPoint(47, 74), QPoint(50, 79), QPoint(133, 71), QPoint(132, 66)]),
        6: QPolygon([QPoint(57, 92), QPoint(60, 98), QPoint(138, 88), QPoint(137, 83)]),
        8: QPolygon([QPoint(68, 112), QPoint(71, 117), QPoint(144, 105), QPoint(143, 99)]),
        10: QPolygon([QPoint(79, 131), QPoint(84, 141), QPoint(153, 126), QPoint(150, 116)]),
        12: QPolygon([QPoint(91, 153), QPoint(94, 158), QPoint(159, 141), QPoint(157, 136)]),
        14: QPolygon([QPoint(103, 170), QPoint(105, 175), QPoint(165, 157), QPoint(163, 152)]),
        16: QPolygon([QPoint(115, 169), QPoint(118, 194), QPoint(174, 173), QPoint(171, 169)]),
        18: QPolygon([QPoint(127, 208), QPoint(130, 212), QPoint(181, 190), QPoint(179, 186)]),
        20: QPolygon([QPoint(141, 227), QPoint(146, 253), QPoint(194, 211), QPoint(189, 201)]),
        22: QPolygon([QPoint(156, 248), QPoint(159, 252), QPoint(203, 225), QPoint(200, 221)]),
        24: QPolygon([QPoint(170, 265), QPoint(173, 269), QPoint(214, 240), QPoint(211, 237)]),
        26: QPolygon([QPoint(183, 280), QPoint(187, 284), QPoint(225, 254), QPoint(222, 250)]),
        28: QPolygon([QPoint(198, 295), QPoint(201, 299), QPoint(238, 267), QPoint(233, 264)]),
        30: QPolygon([QPoint(213, 311), QPoint(220, 318), QPoint(253, 282), QPoint(247, 276)]),
        32: QPolygon([QPoint(231, 327), QPoint(235, 331), QPoint(266, 293), QPoint(262, 289)]),
        34: QPolygon([QPoint(247, 340), QPoint(251, 343), QPoint(280, 305), QPoint(276, 302)]),
        36: QPolygon([QPoint(266, 354), QPoint(269, 356), QPoint(296, 315), QPoint(292, 312)]),
        38: QPolygon([QPoint(283, 365), QPoint(287, 367), QPoint(312, 325), QPoint(308, 322)]),
        40: QPolygon([QPoint(299, 374), QPoint(307, 379), QPoint(332, 335), QPoint(323, 331)]),
        42: QPolygon([QPoint(320, 384), QPoint(324, 387), QPoint(346, 343), QPoint(341, 340)]),
        44: QPolygon([QPoint(338, 393), QPoint(342, 395), QPoint(362, 349), QPoint(357, 347)]),
        46: QPolygon([QPoint(357, 400), QPoint(362, 402), QPoint(379, 357), QPoint(374, 355)]),
        48: QPolygon([QPoint(376, 407), QPoint(380, 409), QPoint(369, 364), QPoint(391, 362)]),
        50: QPolygon([QPoint(395, 412), QPoint(404, 415), QPoint(418, 370), QPoint(409, 368)]),
        52: QPolygon([QPoint(416, 418), QPoint(421, 420), QPoint(434, 376), QPoint(429, 374)]),
        54: QPolygon([QPoint(436, 422), QPoint(441, 424), QPoint(451, 380), QPoint(446, 379)]),
        56: QPolygon([QPoint(455, 426), QPoint(460, 428), QPoint(469, 383), QPoint(464, 382)]),
        58: QPolygon([QPoint(473, 429), QPoint(478, 431), QPoint(486, 388), QPoint(461, 386)]),
        60: QPolygon([QPoint(493, 432), QPoint(502, 434), QPoint(509, 390), QPoint(499, 390)]),
        62: QPolygon([QPoint(516, 435), QPoint(520, 436), QPoint(526, 393), QPoint(521, 392)]),
        64: QPolygon([QPoint(533, 437), QPoint(543, 397), QPoint(543, 396), QPoint(538, 395)]),
        66: QPolygon([QPoint(552, 439), QPoint(556, 439), QPoint(561, 397), QPoint(556, 397)]),
        68: QPolygon([QPoint(570, 440), QPoint(575, 441), QPoint(579, 400), QPoint(574, 399)]),
        70: QPolygon([QPoint(589, 442), QPoint(599, 442), QPoint(602, 402), QPoint(592, 401)]),
        72: QPolygon([QPoint(611, 443), QPoint(616, 443), QPoint(618, 403), QPoint(613, 403)]),
        74: QPolygon([QPoint(630, 444), QPoint(635, 444), QPoint(637, 403), QPoint(632, 404)]),
        76: QPolygon([QPoint(649, 445), QPoint(654, 445), QPoint(655, 404), QPoint(650, 404)]),
        78: QPolygon([QPoint(668, 446), QPoint(674, 446), QPoint(674, 405), QPoint(669, 405)]),
        80: QPolygon([QPoint(685, 446), QPoint(694, 446), QPoint(695, 406), QPoint(685, 406)]),
        82: QPolygon([QPoint(706, 447), QPoint(711, 447), QPoint(711, 406), QPoint(707, 406)]),
        84: QPolygon([QPoint(726, 447), QPoint(731, 447), QPoint(731, 407), QPoint(726, 407)]),
        86: QPolygon([QPoint(746, 448), QPoint(800, 448), QPoint(800, 408), QPoint(746, 408)])}

    TACHOMETER_GEARBOX = {
        0: QPolygon([QPoint(121, 0), QPoint(128, 38), QPoint(215, 32), QPoint(227, 0)]),
        2: QPolygon([QPoint(132, 48), QPoint(134, 53), QPoint(216, 45), QPoint(216, 39)]),
        4: QPolygon([QPoint(138, 65), QPoint(139, 70), QPoint(217, 62), QPoint(216, 57)]),
        6: QPolygon([QPoint(142, 82), QPoint(144, 87), QPoint(218, 76), QPoint(217, 72)]),
        8: QPolygon([QPoint(149, 98), QPoint(151, 104), QPoint(219, 93), QPoint(219, 88)]),
        10: QPolygon([QPoint(155, 115), QPoint(159, 125), QPoint(222, 111), QPoint(220, 101)]),
        12: QPolygon([QPoint(162, 135), QPoint(164, 139), QPoint(224, 124), QPoint(223, 119)]),
        14: QPolygon([QPoint(168, 150), QPoint(171, 155), QPoint(227, 137), QPoint(226, 132)]),
        16: QPolygon([QPoint(176, 167), QPoint(178, 172), QPoint(231, 152), QPoint(230, 147)]),
        18: QPolygon([QPoint(184, 183), QPoint(187, 188), QPoint(236, 166), QPoint(234, 162)]),
        20: QPolygon([QPoint(194, 200), QPoint(199, 208), QPoint(245, 184), QPoint(241, 176)]),
        22: QPolygon([QPoint(205, 218), QPoint(208, 222), QPoint(251, 196), QPoint(248, 191)]),
        24: QPolygon([QPoint(216, 233), QPoint(219, 237), QPoint(260, 209), QPoint(257, 205)]),
        26: QPolygon([QPoint(227, 246), QPoint(230, 251), QPoint(269, 221), QPoint(265, 217)]),
        28: QPolygon([QPoint(239, 259), QPoint(242, 264), QPoint(278, 232), QPoint(275, 228)]),
        30: QPolygon([QPoint(250, 272), QPoint(258, 279), QPoint(290, 244), QPoint(283, 237)]),
        32: QPolygon([QPoint(266, 285), QPoint(270, 289), QPoint(300, 251), QPoint(296, 248)]),
        34: QPolygon([QPoint(280, 269), QPoint(283, 300), QPoint(312, 261), QPoint(309, 258)]),
        36: QPolygon([QPoint(295, 306), QPoint(299, 311), QPoint(325, 270), QPoint(320, 267)]),
        38: QPolygon([QPoint(311, 217), QPoint(315, 320), QPoint(338, 279), QPoint(334, 276)]),
        40: QPolygon([QPoint(325, 325), QPoint(334, 330), QPoint(356, 289), QPoint(347, 283)]),
        42: QPolygon([QPoint(343, 335), QPoint(348, 338), QPoint(368, 295), QPoint(364, 292)]),
        44: QPolygon([QPoint(359, 342), QPoint(364, 345), QPoint(383, 301), QPoint(378, 299)]),
        46: QPolygon([QPoint(376, 350), QPoint(381, 353), QPoint(397, 308), QPoint(393, 306)]),
        48: QPolygon([QPoint(393, 357), QPoint(398, 359), QPoint(413, 314), QPoint(408, 312)]),
        50: QPolygon([QPoint(410, 362), QPoint(420, 366), QPoint(433, 321), QPoint(424, 318)]),
        52: QPolygon([QPoint(430, 369), QPoint(435, 371), QPoint(448, 325), QPoint(443, 324)]),
        54: QPolygon([QPoint(447, 373), QPoint(452, 375), QPoint(462, 330), QPoint(475, 328)]),
        56: QPolygon([QPoint(465, 377), QPoint(470, 379), QPoint(478, 335), QPoint(474, 332)]),
        58: QPolygon([QPoint(482, 281), QPoint(487, 383), QPoint(495, 338), QPoint(490, 337)]),
        60: QPolygon([QPoint(500, 384), QPoint(510, 387), QPoint(516, 342), QPoint(507, 340)]),
        62: QPolygon([QPoint(522, 387), QPoint(527, 388), QPoint(533, 344), QPoint(528, 343)]),
        64: QPolygon([QPoint(539, 390), QPoint(544, 392), QPoint(550, 346), QPoint(545, 345)]),
        66: QPolygon([QPoint(557, 392), QPoint(562, 393), QPoint(567, 349), QPoint(562, 347)]),
        68: QPolygon([QPoint(575, 394), QPoint(580, 395), QPoint(584, 351), QPoint(579, 351)]),
        70: QPolygon([QPoint(593, 395), QPoint(603, 396), QPoint(606, 352), QPoint(595, 351)]),
        72: QPolygon([QPoint(614, 397), QPoint(619, 397), QPoint(621, 353), QPoint(617, 353)]),
        74: QPolygon([QPoint(633, 398), QPoint(638, 398), QPoint(640, 354), QPoint(635, 354)]),
        76: QPolygon([QPoint(651, 399), QPoint(656, 399), QPoint(657, 355), QPoint(652, 355)]),
        78: QPolygon([QPoint(670, 400), QPoint(674, 400), QPoint(675, 356), QPoint(670, 356)]),
        80: QPolygon([QPoint(686, 400), QPoint(695, 400), QPoint(697, 356), QPoint(687, 456)]),
        82: QPolygon([QPoint(707, 401), QPoint(712, 401), QPoint(712, 356), QPoint(707, 356)]),
        84: QPolygon([QPoint(726, 401), QPoint(731, 401), QPoint(731, 357), QPoint(726, 357)]),
        86: QPolygon([QPoint(746, 401), QPoint(800, 401), QPoint(357, 800), QPoint(746, 357)])
    }

    ACCELEROMETER = {
        "C": (QPoint(629, 158), QPoint(678, 206)),
        "P": (QPoint(527, 56), QPoint(778, 306))
    }

    STEERING_WHEEL_ENCODER = {
        -7: QPolygon([QPoint(523, 0), QPoint(529, 0), QPoint(529, 80), QPoint(523, 80)]),
        -6: QPolygon([QPoint(538, 0), QPoint(542, 0), QPoint(542, 61), QPoint(538, 65)]),
        -5: QPolygon([QPoint(551, 0), QPoint(555, 0), QPoint(555, 50), QPoint(551, 53)]),
        -4: QPolygon([QPoint(564, 0), QPoint(568, 0), QPoint(568, 43), QPoint(564, 45)]),
        -3: QPolygon([QPoint(577, 0), QPoint(581, 0), QPoint(581, 37), QPoint(577, 39)]),
        -2: QPolygon([QPoint(590, 0), QPoint(594, 0), QPoint(594, 33), QPoint(590, 35)]),
        -1: QPolygon([QPoint(603, 0), QPoint(607, 0), QPoint(607, 30), QPoint(603, 31)]),
        0: QPolygon([QPoint(618, 0), QPoint(688, 0), QPoint(688, 27), QPoint(653, 25), QPoint(618, 27)]),
        +1: QPolygon([QPoint(699, 0), QPoint(703, 0), QPoint(703, 31), QPoint(699, 30)]),
        +2: QPolygon([QPoint(712, 0), QPoint(716, 0), QPoint(716, 34), QPoint(712, 33)]),
        +3: QPolygon([QPoint(725, 0), QPoint(729, 0), QPoint(729, 39), QPoint(725, 37)]),
        +4: QPolygon([QPoint(738, 0), QPoint(742, 0), QPoint(742, 45), QPoint(738, 43)]),
        +5: QPolygon([QPoint(751, 0), QPoint(755, 0), QPoint(755, 53), QPoint(751, 50)]),
        +6: QPolygon([QPoint(764, 0), QPoint(768, 0), QPoint(768, 65), QPoint(764, 61)]),
        +7: QPolygon([QPoint(777, 0), QPoint(783, 0), QPoint(783, 80), QPoint(777, 80)])}

    TURN_INDICATOR = {
        "L": QPolygon([
            QPoint(389, 251), QPoint(412, 288), QPoint(412, 240), QPoint(437, 240),
            QPoint(437, 263), QPoint(412, 263), QPoint(412, 275)]),
        "R": QPolygon([
            QPoint(460, 240), QPoint(485, 239), QPoint(485, 228), QPoint(508, 251),
            QPoint(485, 275), QPoint(485, 263), QPoint(460, 263)])}

    INDICATORS = {
        "O": {
            "C": QPoint(239, 427),
            "P": [
                QPolygon([QPoint(2, 27), QPoint(18, 18), QPoint(18, 27), QPoint(5, 34)]),
                QPolygon([QPoint(19, 2), QPoint(48, 2), QPoint(69, 27), QPoint(47, 15), QPoint(41, 22), QPoint(18, 22)]),
                QPolygon([QPoint(23, 27), QPoint(37, 29), QPoint(22, 29)]),
                QPolygon([QPoint(69, 27), QPoint(71, 24), QPoint(73, 25)]),
                QPolygon([QPoint(76, 18), QPoint(74, 13), QPoint(75, 10), QPoint(78, 14)])]},
        "W": {
            "C": QPoint(182, 360),
            "P": [
                QPolygon([QPoint(13, 1), QPoint(41, 1)]),
                QPolygon([QPoint(0, 12), QPoint(18, 12)]),
                QPolygon([QPoint(36, 12), QPoint(53, 12)]),
                QPolygon([QPoint(24, 14), QPoint(23, 8), QPoint(31, 8), QPoint(31, 15)]),
                QPolygon([QPoint(26, 15), QPoint(29, 15), QPoint(29, 46), QPoint(26, 46)]),
                QPolygon([QPoint(28, 23), QPoint(35, 23)]),
                QPolygon([QPoint(28, 30), QPoint(35, 30)]),
                QPolygon([QPoint(28, 37), QPoint(35, 37)]),
                QPolygon([QPoint(28, 44), QPoint(35, 44)])]}}

    SPEED_NUMBERS = {
        "A": QPolygon([QPoint(11, 142), QPoint(22, 137), QPoint(59, 136), QPoint(63, 152), QPoint(18, 152),  QPoint(11, 146)]),
        "B": QPolygon([QPoint(7, 80), QPoint(17, 91), QPoint(20, 131), QPoint(10, 137)]),
        "C": QPolygon([QPoint(0, 15), QPoint(12, 21), QPoint(15, 62), QPoint(6, 71)]),
        "D": QPolygon([QPoint(0, 9), QPoint(0, 5), QPoint(5, 0), QPoint(53, 0), QPoint(50, 15), QPoint(13, 15)]),
        "E": QPolygon([QPoint(58, 0), QPoint(64, 5), QPoint(70, 72), QPoint(58, 62), QPoint(54, 15)]),
        "F": QPolygon([QPoint(60, 90), QPoint(70, 79), QPoint(74, 145), QPoint(69, 152), QPoint(63, 135)]),
        "G": QPolygon([QPoint(12, 76), QPoint(17, 68), QPoint(58, 68), QPoint(63, 77), QPoint(59, 84), QPoint(17, 84)])}

    STANDARD_NUMBERS = {
        "A": QPolygon([QPoint(4, 44), QPoint(6, 42), QPoint(22, 42), QPoint(24, 44), QPoint(22, 46), QPoint(5, 46)]),
        "B": QPolygon([QPoint(0, 26), QPoint(2, 24), QPoint(4, 26), QPoint(4, 41), QPoint(2, 43), QPoint(0, 41)]),
        "C": QPolygon([QPoint(0, 5), QPoint(2, 3), QPoint(4, 5), QPoint(4, 20), QPoint(2, 22), QPoint(0, 20)]),
        "D": QPolygon([QPoint(5, 0), QPoint(22, 0), QPoint(24, 2), QPoint(22, 4), QPoint(6, 4), QPoint(4, 1)]),
        "E": QPolygon([QPoint(23, 6), QPoint(26, 4), QPoint(27, 5), QPoint(27, 20), QPoint(25, 22), QPoint(23, 20)]),
        "F": QPolygon([QPoint(23, 26), QPoint(25, 24), QPoint(27, 26), QPoint(27, 41), QPoint(26, 42), QPoint(23, 40)]),
        "G": QPolygon([QPoint(4, 23), QPoint(6, 21), QPoint(21, 21), QPoint(23, 23), QPoint(21, 25), QPoint(6, 25)])}

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
        "C": QPoint(182, 360),
        "P": {
             "A": QPolygon([QPoint(4, 101), QPoint(14, 92), QPoint(74, 92), QPoint(84, 101)]),
             "B": QPolygon([QPoint(0, 55), QPoint(5, 51), QPoint(12, 57), QPoint(12, 91), QPoint(0, 99)]),
             "C": QPolygon([QPoint(0, 2), QPoint(12, 10), QPoint(12, 44), QPoint(5, 49), QPoint(0, 45)]),
             "D": QPolygon([QPoint(4, 0), QPoint(84, 0), QPoint(74, 8), QPoint(14, 8)]),
             "E": QPolygon([QPoint(76, 10), QPoint(88, 2), QPoint(88, 45), QPoint(82, 49), QPoint(76, 44)]),
             "F": QPolygon([QPoint(76, 56), QPoint(82, 51), QPoint(88, 56), QPoint(88, 99), QPoint(76, 90)]),
             "G": QPolygon([QPoint(10, 50), QPoint(15, 46), QPoint(73, 46), QPoint(78, 50), QPoint(74, 54), QPoint(13, 54)]),
             "M": QPolygon([QPoint(43, 43), QPoint(66, 11), QPoint(73, 11), QPoint(73, 20), QPoint(56, 43)]),
             "J": QPolygon([QPoint(15, 89), QPoint(15, 81), QPoint(33, 57), QPoint(47, 57), QPoint(23, 89)])},
        "M": {
            "N": ["B", "C", "E", "F", "M", "J"],
            "1": ["B", "C"],
            "2": ["A", "B", "G", "E", "D"],
            "3": ["A", "B", "G", "C", "D"],
            "4": ["F", "G", "B", "C"],
            "5": ["A", "F", "G", "C", "D"]}}

    SPEEDOMETER = {
        1: QPoint(273, 54),
        10: QPoint(349, 54),
        100: QPoint(425, 54)}

    STOPWATCH = {
        "MS1":  QPoint(478, 0),
        "MS10":  QPoint(445, 0),
        "S1":  QPoint(405, 0),
        "S10":  QPoint(372, 0),
        "M1":   QPoint(332, 0),
        "M10":   QPoint(299, 0),
        "H1":   QPoint(259, 0)}

    OIL_MANOMETER = {
        0.01: QPoint(72, 433),
        0.1: QPoint(40, 433),
        1:  QPoint(0, 433)}

    OIL_THERMOMETER = {
         1: QPoint(66, 386),
         10: QPoint(33, 386),
         100: QPoint(0, 386)}

    WATTER_THERMOMETER = {
         1: QPoint(66, 303),
         10: QPoint(33, 303),
         100: QPoint(0, 30)}


    # Methods

    #def () -> List[QPolygon]:




