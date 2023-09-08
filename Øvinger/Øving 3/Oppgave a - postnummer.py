# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:26:26 2023

@author: marku
"""

def postoppsett():
    navn = input("Hvem skal posten adresseres til?\n")
    gateadresse = input("Hva er gatenavn/nummer til adressanten?\n")
    postnummer = input("Hva er postnummeret til adressanten?\n")
    poststed = input("Hva er navnet på poststedet til adressanten?\n")
    print(f"Til: {navn} \n{gateadresse} \n{postnummer} {poststed}")
    
postoppsett()