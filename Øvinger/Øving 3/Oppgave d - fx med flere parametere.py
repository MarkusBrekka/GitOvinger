# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:42:44 2023

@author: marku
"""

import math



def euler_x(x=2,m=40):
    summen = 0
    for i in range(0,m+1):
        resultat = (x**i)/ math.factorial(i)
        summen = summen + resultat
    return summen

fx = euler_x()

print(math.sqrt(fx))
print(math.e)

