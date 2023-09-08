# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:04:43 2023

@author: marku
"""

import math
diameter = float(input("Skriv diameter på skjermen i tommer; "))
vinkel = math.atan(9/16)
høyde = diameter * math.sin(vinkel)
bredde = diameter * math.cos(vinkel)
print(f"Skjermen er {bredde} tommer bred og {høyde} tommer høy.")

