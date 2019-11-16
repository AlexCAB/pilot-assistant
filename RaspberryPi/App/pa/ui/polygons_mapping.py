#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

  TODO

author: CAB
website: github.com/alexcab
last edited: 2019-11-15
"""

from PyQt5.QtCore import QPoint


class PolygonsMapping(object):

    tachometerEngine = {
        0.0: [QPoint(6, 0), QPoint(30, 45), QPoint(123, 38), QPoint(115, 0)],
        0.2: [QPoint(38, 57), QPoint(40, 62), QPoint(127, 54), QPoint(126, 48)],
        0.4: [QPoint(47, 74), QPoint(50, 79), QPoint(133, 71), QPoint(132, 66)],
        0.6: [QPoint(57, 92), QPoint(60, 98), QPoint(138, 88), QPoint(137, 83)],
        0.8: [QPoint(68, 112), QPoint(71, 117), QPoint(144, 105), QPoint(143, 99)],
        1.0: [QPoint(79, 131), QPoint(84, 141), QPoint(153, 126), QPoint(150, 116)],
        1.2: [QPoint(91, 153), QPoint(94, 158), QPoint(159, 141), QPoint(157, 136)],
        1.4: [QPoint(103, 170), QPoint(105, 175), QPoint(165, 157), QPoint(163, 152)],
        1.6: [QPoint(115, 169), QPoint(118, 194), QPoint(174, 173), QPoint(171, 169)],
        1.8: [QPoint(127, 208), QPoint(130, 212), QPoint(181, 190), QPoint(179, 186)],
        2.0: [QPoint(141, 227), QPoint(146, 253), QPoint(194, 211), QPoint(189, 201)],
        2.2: [QPoint(156, 248), QPoint(159, 252), QPoint(203, 225), QPoint(200, 221)],
        2.4: [QPoint(170, 265), QPoint(173, 269), QPoint(214, 240), QPoint(211, 237)],
        2.6: [QPoint(183, 280), QPoint(187, 284), QPoint(225, 254), QPoint(222, 250)],
        2.8: [QPoint(198, 295), QPoint(201, 299), QPoint(238, 267), QPoint(233, 264)],
        3.0: [QPoint(213, 311), QPoint(220, 318), QPoint(253, 282), QPoint(247, 276)],
        3.2: [QPoint(231, 327), QPoint(235, 331), QPoint(266, 293), QPoint(262, 289)],
        3.4: [QPoint(247, 340), QPoint(251, 343), QPoint(280, 305), QPoint(276, 302)],
        3.6: [QPoint(266, 354), QPoint(269, 356), QPoint(296, 315), QPoint(292, 312)],
        3.8: [QPoint(283, 365), QPoint(287, 367), QPoint(312, 325), QPoint(308, 322)],
        4.0: [QPoint(299, 374), QPoint(307, 379), QPoint(332, 335), QPoint(323, 331)],
        4.2: [QPoint(320, 384), QPoint(324, 387), QPoint(346, 343), QPoint(341, 340)],
        4.4: [QPoint(338, 393), QPoint(342, 395), QPoint(362, 349), QPoint(357, 347)],
        4.6: [QPoint(357, 400), QPoint(362, 402), QPoint(379, 357), QPoint(374, 355)],
        4.8: [QPoint(376, 407), QPoint(380, 409), QPoint(369, 364), QPoint(391, 362)],
        5.0: [QPoint(395, 412), QPoint(404, 415), QPoint(418, 370), QPoint(409, 368)],
        5.2: [QPoint(416, 418), QPoint(421, 420), QPoint(434, 376), QPoint(429, 374)],
        5.4: [QPoint(436, 422), QPoint(441, 424), QPoint(451, 380), QPoint(446, 379)],
        5.6: [QPoint(455, 426), QPoint(460, 428), QPoint(469, 383), QPoint(464, 382)],
        5.8: [QPoint(473, 429), QPoint(478, 431), QPoint(486, 388), QPoint(461, 386)],
        6.0: [QPoint(493, 432), QPoint(502, 434), QPoint(509, 390), QPoint(499, 390)],
        6.2: [QPoint(516, 435), QPoint(520, 436), QPoint(526, 393), QPoint(521, 392)],
        6.4: [QPoint(533, 437), QPoint(543, 397), QPoint(543, 396), QPoint(538, 395)],
        6.6: [QPoint(552, 439), QPoint(556, 439), QPoint(561, 397), QPoint(556, 397)],
        6.8: [QPoint(570, 440), QPoint(575, 441), QPoint(579, 400), QPoint(574, 399)],
        7.0: [QPoint(589, 442), QPoint(599, 442), QPoint(602, 402), QPoint(592, 401)],
        7.2: [QPoint(611, 443), QPoint(616, 443), QPoint(618, 403), QPoint(613, 403)],
        7.4: [QPoint(630, 444), QPoint(635, 444), QPoint(637, 403), QPoint(632, 404)],
        7.6: [QPoint(649, 445), QPoint(654, 445), QPoint(655, 404), QPoint(650, 404)],
        7.8: [QPoint(668, 446), QPoint(674, 446), QPoint(674, 405), QPoint(669, 405)],
        8.0: [QPoint(685, 446), QPoint(694, 446), QPoint(695, 406), QPoint(685, 406)],
        8.2: [QPoint(706, 447), QPoint(711, 447), QPoint(711, 406), QPoint(707, 406)],
        8.4: [QPoint(726, 447), QPoint(731, 447), QPoint(731, 407), QPoint(726, 407)],
        8.6: [QPoint(746, 448), QPoint(800, 448), QPoint(800, 408), QPoint(746, 408)]
    }

    tachometerGearbox = {
        0.0: [QPoint(121, 0), QPoint(128, 38), QPoint(215, 32), QPoint(227, 0)],
        0.2: [QPoint(132, 48), QPoint(134, 53), QPoint(216, 45), QPoint(216, 39)],
        0.4: [QPoint(138, 65), QPoint(139, 70), QPoint(217, 62), QPoint(216, 57)],
        0.6: [QPoint(142, 82), QPoint(144, 87), QPoint(218, 76), QPoint(217, 72)],
        0.8: [QPoint(149, 98), QPoint(151, 104), QPoint(219, 93), QPoint(219, 88)],
        1.0: [QPoint(155, 115), QPoint(159, 125), QPoint(222, 111), QPoint(220, 101)],
        1.2: [QPoint(162, 135), QPoint(164, 139), QPoint(224, 124), QPoint(223, 119)],
        1.4: [QPoint(168, 150), QPoint(171, 155), QPoint(227, 137), QPoint(226, 132)],
        1.6: [QPoint(176, 167), QPoint(178, 172), QPoint(231, 152), QPoint(230, 147)],
        1.8: [QPoint(184, 183), QPoint(187, 188), QPoint(236, 166), QPoint(234, 162)],
        2.0: [QPoint(194, 200), QPoint(199, 208), QPoint(245, 184), QPoint(241, 176)],
        2.2: [QPoint(205, 218), QPoint(208, 222), QPoint(251, 196), QPoint(248, 191)],
        2.4: [QPoint(216, 233), QPoint(219, 237), QPoint(260, 209), QPoint(257, 205)],
        2.6: [QPoint(227, 246), QPoint(230, 251), QPoint(269, 221), QPoint(265, 217)],
        2.8: [QPoint(239, 259), QPoint(242, 264), QPoint(278, 232), QPoint(275, 228)],
        3.0: [QPoint(250, 272), QPoint(258, 279), QPoint(290, 244), QPoint(283, 237)],
        3.2: [QPoint(266, 285), QPoint(270, 289), QPoint(300, 251), QPoint(296, 248)],
        3.4: [QPoint(280, 269), QPoint(283, 300), QPoint(312, 261), QPoint(309, 258)],
        3.6: [QPoint(295, 306), QPoint(299, 311), QPoint(325, 270), QPoint(320, 267)],
        3.8: [QPoint(311, 217), QPoint(315, 320), QPoint(338, 279), QPoint(334, 276)],
        4.0: [QPoint(325, 325), QPoint(334, 330), QPoint(356, 289), QPoint(347, 283)],
        4.2: [QPoint(343, 335), QPoint(348, 338), QPoint(368, 295), QPoint(364, 292)],
        4.4: [QPoint(359, 342), QPoint(364, 345), QPoint(383, 301), QPoint(378, 299)],
        4.6: [QPoint(376, 350), QPoint(381, 353), QPoint(397, 308), QPoint(393, 306)],
        4.8: [QPoint(393, 357), QPoint(398, 359), QPoint(413, 314), QPoint(408, 312)],
        5.0: [QPoint(410, 362), QPoint(420, 366), QPoint(433, 321), QPoint(424, 318)],
        5.2: [QPoint(430, 369), QPoint(435, 371), QPoint(448, 325), QPoint(443, 324)],
        5.4: [QPoint(447, 373), QPoint(452, 375), QPoint(462, 330), QPoint(475, 328)],
        5.6: [QPoint(465, 377), QPoint(470, 379), QPoint(478, 335), QPoint(474, 332)],
        5.8: [QPoint(482, 281), QPoint(487, 383), QPoint(495, 338), QPoint(490, 337)],
        6.0: [QPoint(500, 384), QPoint(510, 387), QPoint(516, 342), QPoint(507, 340)],
        6.2: [QPoint(522, 387), QPoint(527, 388), QPoint(533, 344), QPoint(528, 343)],
        6.4: [QPoint(539, 390), QPoint(544, 392), QPoint(550, 346), QPoint(545, 345)],
        6.6: [QPoint(557, 392), QPoint(562, 393), QPoint(567, 349), QPoint(562, 347)],
        6.8: [QPoint(575, 394), QPoint(580, 395), QPoint(584, 351), QPoint(579, 351)],
        7.0: [QPoint(593, 395), QPoint(603, 396), QPoint(606, 352), QPoint(595, 351)],
        7.2: [QPoint(614, 397), QPoint(619, 397), QPoint(621, 353), QPoint(617, 353)],
        7.4: [QPoint(633, 398), QPoint(638, 398), QPoint(640, 354), QPoint(635, 354)],
        7.6: [QPoint(651, 399), QPoint(656, 399), QPoint(657, 355), QPoint(652, 355)],
        7.8: [QPoint(670, 400), QPoint(674, 400), QPoint(675, 356), QPoint(670, 356)],
        8.0: [QPoint(686, 400), QPoint(695, 400), QPoint(697, 356), QPoint(687, 456)],
        8.2: [QPoint(707, 401), QPoint(712, 401), QPoint(712, 356), QPoint(707, 356)],
        8.4: [QPoint(726, 401), QPoint(731, 401), QPoint(731, 357), QPoint(726, 357)],
        8.6: [QPoint(746, 401), QPoint(800, 401), QPoint(357, 800), QPoint(746, 357)]
    }

    accelerometer = {
        "C": (QPoint(629, 158), QPoint(678, 206)),
        "P": (QPoint(527, 56), QPoint(778, 306))
    }

    wheelEncoder = {
        -7: [QPoint(523, 0), QPoint(529, 0), QPoint(529, 80), QPoint(523, 80)],
        -6: [QPoint(538, 0), QPoint(542, 0), QPoint(542, 61), QPoint(538, 65)],
        -5: [QPoint(551, 0), QPoint(555, 0), QPoint(555, 50), QPoint(551, 53)],
        -4: [QPoint(564, 0), QPoint(568, 0), QPoint(568, 43), QPoint(564, 45)],
        -3: [QPoint(577, 0), QPoint(581, 0), QPoint(581, 37), QPoint(577, 39)],
        -2: [QPoint(590, 0), QPoint(594, 0), QPoint(594, 33), QPoint(590, 35)],
        -1: [QPoint(603, 0), QPoint(607, 0), QPoint(607, 30), QPoint(603, 31)],
        0:  [QPoint(618, 0), QPoint(688, 0), QPoint(688, 27), QPoint(653, 25), QPoint(618, 27)],
        +1: [QPoint(699, 0), QPoint(703, 0), QPoint(703, 31), QPoint(699, 30)],
        +2: [QPoint(712, 0), QPoint(716, 0), QPoint(716, 34), QPoint(712, 33)],
        +3: [QPoint(725, 0), QPoint(729, 0), QPoint(729, 39), QPoint(725, 37)],
        +4: [QPoint(738, 0), QPoint(742, 0), QPoint(742, 45), QPoint(738, 43)],
        +5: [QPoint(751, 0), QPoint(755, 0), QPoint(755, 53), QPoint(751, 50)],
        +6: [QPoint(764, 0), QPoint(768, 0), QPoint(768, 65), QPoint(764, 61)],
        +7: [QPoint(777, 0), QPoint(783, 0), QPoint(783, 80), QPoint(777, 80)]
    }
