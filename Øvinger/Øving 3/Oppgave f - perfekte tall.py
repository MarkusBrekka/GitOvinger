# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:25:42 2023

@author: marku
"""

import delelig as vedlegg

def perfekt_tall(tall):
    upper_range = int((tall/2)+1)
    perfekt = 1
    for i in range(2,upper_range):
        if vedlegg.delelig(tall, i) == True:
            perfekt += i
            print(f"{i} er en faktor av {tall}")
        else:
            continue
    if tall == perfekt:
        return True
    else:
        return False
    
tall = int(input("Hvilket tall ønsker du å sjekke om er perfekt?"))

if perfekt_tall(tall) == True:
    print(f"Gratulerer, {tall} er et perfekt tall!")
else:
    print(f"{tall} er desverre ikke et perfekt tall.")