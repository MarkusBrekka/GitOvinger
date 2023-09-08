# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:58:58 2023

@author: marku
"""

def les_positivt_heltall(beskjed):
    tall = int(input(beskjed))
    while tall < 0:
        print("Du må skrive inn et ikke-negativt heltall!")
        tall = int(input(beskjed))
    return tall


tallet = les_positivt_heltall("Skriv inn hvilket tall du ønsker fakultetet av:")

resultat = 1
for i in range(1, tallet+1):
    print(i)
    resultat *= i
print("Etter for-løkka er ferdig")
print(resultat)
