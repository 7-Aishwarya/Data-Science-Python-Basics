# -*- coding: utf-8 -*-
"""Commonmathndstatsnumpy.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H2q_rwBrpFFwYalWfWmwC3XgUDSt7VNr
"""

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr

np.min(arr)

np.max(arr)

np.amin(arr,axis=1)

np.mean(arr)

np.median(arr)

np.std(arr)

np.var(arr)

np.percentile(arr,100)

deg = np.array([0,1,2,3,4])
np.sin(deg*np.pi/180)

np.cos(deg*np.pi/180)

np.tan(deg*np.pi/180)

np.arctan(deg*np.pi/180)

'''arcsin
arccos
arctan'''

x = np.array([1.0,0.2,2.2,9.8,5.2])
np.floor(x)

np.ceil(x)