# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:18:09 2021

@author: mpozi
"""

import pandas as pd

with open('../data/income-support-covid.csv') as f:
    p = pd.read_csv(f)

with open('../data/income-support-covid.txt', 'w') as f:
    
    f.writelines("Source: " + "Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8")
        
    f.writelines("\n\nIncome support captures if the government is covering the salaries or providing direct cash payments, universal basic income, or similar, of people who lose their jobs or cannot work.")
    
    f.writelines("\n\nNo income support, Covers <50% of lost salary, Covers >50% of lost salary")
    
    f.writelines("\n\nUnique countries: " + str(len(p.Entity.unique())))
    
    
    p = p[p.Entity.isin(['Denmark'])]
        
    f.writelines("\n\nRows for Denmark: " + str(len(p)))
    
    f.writelines("\n\nFrom " + p.Day[p.index[0]] + " to " + p.Day[p.index[-1]])
    
    f.writelines("\n\nNot nan rows for each column:")
    
    for i in p.columns:
        f.writelines("\n" + i + " " + str(len(p[p[i].notna()])))

