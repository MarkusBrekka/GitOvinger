# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:40:34 2023

@author: Diego
"""

readname = input("Hva er navnet på filen du ønsker å åpne?")
try:
    readable = open(readname, "r")
except FileNotFoundError:
    readname = input("Sjekk at du har skrevet riktig filnavn og prøv igjen:")
    readable = open(readname, "r")
    
dictionary = dict()

for line in readable:
    line=line.strip()
    line=line.lower()
    words=line.split(" ")
    for word in words:
        if word in dictionary:
            dictionary[word] = dictionary[word]+1
        else:
            dictionary[word] = 1

for key in list(dictionary.keys()):
    print(key,":",dictionary[key])