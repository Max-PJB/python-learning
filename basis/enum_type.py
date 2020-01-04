#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/1/3 19:53
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

from enum import Enum

Color = Enum('Color', {'red': 1, 'blue': 2})

print(list(Color))
print(Color.red, Color(1), Color(2), Color.red.value == 1, Color.red.name == 'red')


class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS = (4.869e+24, 6.0518e6)
    EARTH = (5.976e+24, 6.37814e6)
    MARS = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27, 7.1492e7)
    SATURN = (5.688e+26, 6.0268e7)
    URANUS = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)

    def __init__(self, mass, radius):
        self.mass = mass  # in kilograms
        self.radius = radius  # in meters

    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)


print(Planet.EARTH.value)
print(Planet.EARTH.surface_gravity)


class ErrorCode2(Enum):
    ARG_ERROR = (101, '参数错误')
    NOT_FOUND = (202, '找不到')

    def __init__(self, code, message):
        self.code = code
        self.message = message


print(ErrorCode2.ARG_ERROR.code)
print(ErrorCode2.ARG_ERROR.message)

ErrorCode = Enum('ErrorCode', {'ARG_ERROR': 101, 'NOT_FOUND': 202})
print(ErrorCode.ARG_ERROR.value)


class ErrorCode1(Enum):
    ARG_ERROR = 101
    NOT_FOUND = 202


# 可以通过 cls['name'] ,cls(value) 来获取枚举， 通过 cls'.'name == ['name.]
print(ErrorCode1.ARG_ERROR, ErrorCode1.ARG_ERROR.name, ErrorCode1.ARG_ERROR.value)
print(ErrorCode1['ARG_ERROR'], ErrorCode1['ARG_ERROR'].name, ErrorCode1['ARG_ERROR'].value)
print(ErrorCode1(101), ErrorCode1(101).name, ErrorCode1(101).value)
