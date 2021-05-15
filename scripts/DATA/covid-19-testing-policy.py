# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:18:09 2021

@author: mpozi
"""

import pandas as pd

with open('../data/covid-19-testing-policy.csv') as f:
    p = pd.read_csv(f)

with open('../data/covid-19-testing-policy.txt', 'w') as f:
    
    f.writelines("Source: " + "Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8")
        
    f.writelines("\n\n– No testing policy.\n– Only those who both (a) have symptoms and also (b) meet specific criteria (e.g. key workers, admitted to hospital, came into contact with a known case, returned from overseas).\n– Testing of anyone showing COVID-19 symptoms.\n– Open public testing (e.g. “drive through” testing available to asymptomatic people).")
    
    f.writelines("\n\nUnique countries: " + str(len(p.Entity.unique())))
    
    p = p[p.Entity.isin(['Denmark'])]
        
    f.writelines("\n\nRows for Denmark: " + str(len(p)))
    
    f.writelines("\n\nFrom " + p.Day[p.index[0]] + " to " + p.Day[p.index[-1]])
    
    f.writelines("\n\nNot nan rows for each column:")
    
    for i in p.columns:
        f.writelines("\n" + i + " " + str(len(p[p[i].notna()])))

