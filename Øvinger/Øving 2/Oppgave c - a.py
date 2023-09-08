# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:05:53 2023

@author: marku
"""


rekkevidde_km_str = input("Rekkevidden til din elbil i kilometer: ")
tur_lengde_km_str = input("Lengden til kjøreturen din i kilometer: ")
rekkevidde_km = int(rekkevidde_km_str)
tur_lengde_km = int(tur_lengde_km_str)
antall_ladinger = int(tur_lengde_km // (rekkevidde_km*0.8))

if tur_lengde_km < rekkevidde_km*0.8:
    print("Du trenger ikke lade bilen på denne strekningen.")

elif antall_ladinger == 1:
    print("Du trenger å lade bilen 1 gang på denne strekningen.")

else:
    print(f"Du trenger å lade bilen {antall_ladinger} ganger på denne strekningen.")
    
    