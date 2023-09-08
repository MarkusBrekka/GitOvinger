# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:55:52 2023

@author: marku
"""

# E = m*g*h
# m = masse
# g = gravitasjonsakselerasjonen = 9.81 m/s**2
# h = høyden over overflaten


g = 9.81
m = float(input("Skriv inn massen til objektet i kg:"))
h = float(input("Skriv inn høyden til objektet over overlaten i meter:"))

e = m*g*h

print(f"Den potensielle energien til objektet er {e} Joules!")