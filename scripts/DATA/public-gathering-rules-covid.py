# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:18:09 2021

@author: mpozi
"""

import pandas as pd

with open('../data/public-gathering-rules-covid.csv') as f:
    p = pd.read_csv(f)

with open('../data/public-gathering-rules-covid.txt', 'w') as f:
    
    f.writelines("Source: " + "Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8")
    
    f.writelines("Restrictions are given based on the size of public gatherings as follows:\n1 - Restrictions on very large gatherings (the limit is above 1000 people)\n2 - gatherings between 100-1000 people\n3 - gatherings between 10-100 people\n4 - gatherings of less than 10 people")
    
    f.writelines("Unique countries: " + str(len(p.Entity.unique())))
    
    p = p[p.Entity.isin(['Denmark'])]
        
    f.writelines("\n\nRows for Denmark: " + str(len(p)))
    
    f.writelines("\n\nFrom " + p.Day[p.index[0]] + " to " + p.Day[p.index[-1]])
    
    f.writelines("\n\nNot nan rows for each column:")
    
    for i in p.columns:
        f.writelines("\n" + i + " " + str(len(p[p[i].notna()])))

