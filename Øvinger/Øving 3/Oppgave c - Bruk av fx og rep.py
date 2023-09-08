# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:43:15 2023

@author: marku
"""

import oppgave_b as kmnm

konverteringsverdi = 1

while konverteringsverdi > 0:
    konverteringsverdi = float(input("Hvor mange km ønsker du å konvertere til nm? "))
    if konverteringsverdi > 0:
        print(f"Dette blir {kmnm.km_nm(konverteringsverdi)} nautiske mil. \n")
        
    else:
        print("Takk for at du brukte programmet.")
       