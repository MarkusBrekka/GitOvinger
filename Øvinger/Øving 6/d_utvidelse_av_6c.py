# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:38:07 2023

@author: marku
"""

def km_nm(kilometer):
    resultat = kilometer/1.852
    return resultat

readname = input("Hva er navnet på filen du ønsker å åpne?")
try:
    readable = open(readname+".txt", "r")
except FileNotFoundError:
    readname = input("Sjekk at du har skrevet riktig filnavn og prøv igjen:")
    readable = open(readname+".txt", "r")
    
writeable = open(readname+"_nautiske_mil.txt", "w")

linjenummer = 0

for linje in readable:
    linjenummer += 1
    try:
        writeable.write(str(km_nm(float(linje))))
        writeable.write("\n")
    except ValueError:
        print(f"\n{linje} på linje #{linjenummer} kan ikke konverteres til et flyttall.")

readable.close()
writeable.close()