# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:20:09 2023

@author: marku
"""

valuta_fra = input("Hvilken valuta ønsker du å veksle fra?")
valuta_til = input("Hvilken valuta ønsker du å veksle til?")
kurs = float(input(f"Hva er kursen fra {valuta_fra} til {valuta_til}?"))

avbryter = True
veksling_verdi = 1

while veksling_verdi:
    veksling_verdi = float(input(f"Hvor mye {valuta_fra} ønsker du å veksle til {valuta_til}?"))
    if veksling_verdi <= 0:
        
        break
    else:
        veksling_resultat = veksling_verdi * kurs
        print(f"{veksling_verdi} {valuta_fra} kan veksles til {veksling_resultat} {valuta_til}.")
        continue
    
print("Takk for at du benyttet dette programmet.")
