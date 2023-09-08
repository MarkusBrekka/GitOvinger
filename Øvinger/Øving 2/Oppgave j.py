# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:16:02 2023

@author: marku
"""

import turtle
turtle.setup(500,800,900,0)

radius = 10

for i in range(0,6):

    radius = radius + 10

    for i in range(0,4):
        turtle.left(90)
        turtle.circle(radius)
        
    turtle.left(10)

turtle.bye()