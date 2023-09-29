# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:55:42 2023

@author: marku
"""

def km_nm(kilometer):
    resultat = kilometer/1.852
    return resultat
readname = input("Hva er navnet på filen du ønsker å åpne?")
readable = open(readname+".txt", "r")
writeable = open(readname+"_nautiske_mil.txt", "w")

for linje in readable:
    print(km_nm(float(linje)))
    writeable.write(str(km_nm(float(linje))))
    writeable.write("\n")

readable.close()
writeable.close()