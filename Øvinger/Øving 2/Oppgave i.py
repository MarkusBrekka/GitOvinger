# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:49:52 2023

@author: marku
"""

import turtle

kanter = int(input("Hvor mange kanter ønsker du å ha i mangekanten din?"))
vinkel = 360/kanter

if kanter < 3:
    print("Dette er ikke nok kanter til å lage en mangekant. Husk huskeregelen: En, to, mange!")

else:
    turtle.setup(500,800,900,0)
    for i in range(0,kanter):
            turtle.forward(10)
            turtle.left(vinkel)
    
turtle.done()
