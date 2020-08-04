#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2020/7/21 10:48
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ts = pd.Series(np.random.randn(1000),
              index=pd.date_range('1/1/2000', periods=1000))


ts = ts.cumsum()

ts.plot()

