# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:53:24 2023

@author: Diego
"""

import matplotlib.pyplot as plt

def renteverdi(startverdi, rente, aar):
    okningstall = 1.0 + rente/100
    verdi = startverdi*okningstall**aar
    return verdi

liste = [i for i in range(0,21)]

resultatliste = [renteverdi(300000,3,aar) for aar in liste]

plt.plot(resultatliste)
plt.xticks(liste)
plt.show()