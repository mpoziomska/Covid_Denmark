# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:18:09 2021

@author: mpozi
"""

import pandas as pd

with open('../data/covid-vaccination-policy.csv') as f:
    p = pd.read_csv(f)

with open('../data/covid-vaccination-policy.txt', 'w') as f:
    
    f.writelines("Source: " + "Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8")
        
    f.writelines("\n\nThis metric records policies for vaccine delivery for different groups.\n- Availability for ONE of following: key workers/ clinically vulnerable groups / elderly groups\n- Availability for TWO of following: key workers/ clinically vulnerable groups / elderly groups\n- Availability for ALL of following: key workers/ clinically vulnerable groups / elderly groups\n- Availability for all three plus partial additional availability (select broad groups/ages)\n- Universal availability")
    
    f.writelines("\n\nUnique countries: " + str(len(p.Entity.unique())))
    
    p = p[p.Entity.isin(['Denmark'])]
        
    f.writelines("\n\nRows for Denmark: " + str(len(p)))
    
    f.writelines("\n\nFrom " + p.Day[p.index[0]] + " to " + p.Day[p.index[-1]])
    
    f.writelines("\n\nNot nan rows for each column:")
    
    for i in p.columns:
        f.writelines("\n" + i + " " + str(len(p[p[i].notna()])))

