# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:16:13 2023

@author: marku
"""

def postoppsett():
    navn = input("Hvem skal posten adresseres til?\n")
    gateadresse = input("Hva er gatenavn/nummer til adressanten?\n")
    
    postnummer = input("Hva er postnummeret til adressanten?\n")
    while postnummer.isdecimal() == False or len(postnummer) != 4:
            postnummer = input("Vennligst skriv inn et 4-sifret postnummer:")
            
    poststed = input("Hva er navnet på poststedet til adressanten?\n")
    print(f"Til: {navn} \n{gateadresse} \n{postnummer} {poststed}")
    
postoppsett()