# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:24:39 2023

@author: marku
"""

valuta_fra = input("Hvilken valuta ønsker du å veksle fra?")
valuta_til = input("Hvilken valuta ønsker du å veksle til?")
try:
    kurs = float(input(f"Hva er kursen fra {valuta_fra} til {valuta_til}?"))
except ValueError:
    kurs = float(input("Vennligst skriv et reelt tall for kursen:"))
avbryter = True

while avbryter == True:
    try:
        veksling_verdi = float(input(f"Hvor mye {valuta_fra} ønsker du å veksle til {valuta_til}?"))
    except ValueError:
        veksling_verdi = float(input("Vennligst skriv et reelt tall for mengden du ønsker å veksle."))
    if veksling_verdi <= 0:
        
        avbryter = False
    else:
        veksling_resultat = veksling_verdi * kurs
        print(f"{veksling_verdi} {valuta_fra} kan veksles til {veksling_resultat} {valuta_til}.")
    
print("Takk for at du benyttet dette programmet.")