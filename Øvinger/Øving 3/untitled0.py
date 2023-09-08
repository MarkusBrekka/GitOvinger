# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:38:41 2023

@author: marku
"""

import math

def euler_x(x=2,m=40):
    summen = 0
    for i in range(0,m+1):
        resultat = (x**i)/ math.factorial(i)
        summen = summen + resultat
    return summen