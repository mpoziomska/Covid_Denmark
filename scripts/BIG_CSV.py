# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import datetime
import os
folder = '../data/'
l = os.listdir(folder)

stop = datetime.date(2021, 4, 16)
start = datetime.date(2020, 1, 21)
ndays = (stop - start).days

with open(folder + 'owid-covid-data.csv') as f:
    p = pd.read_csv(f)

countries = ['Denmark', 'United Kingdom', 'South Korea', 'China', 'Switzerland']

#p = p[p.continent.isin(['Europe']) | p.location.isin(countries)]
p = p[p.location.isin(countries)]

D = p.copy()
d = {}
for i in p.columns:
    d[i] = 'owid-covid-data_' + i
D.rename(columns = d, inplace = True)

T = pd.date_range(start, stop, periods = ndays).to_pydatetime()

a=0

for i in l:
    if '.csv' in i and 'BIG' not in i and 'owid' not in i:
        with open(folder + i) as f:
            p = pd.read_csv(f)
        print(i)
        col = list(p.columns)[3:]
        i = i.split('.')[0]
        for c in col:
            D[i + "_" + c] = np.nan
        for coun in countries:
            x = p[p.Entity.isin([coun])].copy()
            #print(len(x), coun)
            for day in T:
                day = str(day).split(' ')[0]
                a = x[x.Day.isin([day])]
                #print(a.testing_policy)
                if len(a) == 1:
                    #print("DUPA", i, len(col))
                    for c in col:
                        #print(D[D['owid-covid-data_location'].isin([coun]) & D['owid-covid-data_date'].isin([day])])
                        D[i + "_" + c][D['owid-covid-data_location'].isin([coun]) & D['owid-covid-data_date'].isin([day])] = float(a[c])
                        #print(i, D[i + "_" + c][D['owid-covid-data_location'].isin([coun]) & D['owid-covid-data_date'].isin([day])])
d = {'owid-covid-data_location' : 'location', 'owid-covid-data_date' : 'date', 'owid-covid-data_total_cases' : 'total_cases', 'owid-covid-data_new_cases' : 'new_cases', 
     'owid-covid-data_new_cases_smoothed' : 'new_cases_smoothed', 'owid-covid-data_total_deaths' : 'total_deaths',
       'owid-covid-data_new_deaths' : 'new_deaths', 'owid-covid-data_new_deaths_smoothed' : 'new_deaths_smoothed',
       'owid-covid-data_total_cases_per_million' : 'total_cases_per_million',
       'owid-covid-data_new_cases_per_million' : 'new_cases_per_million',
       'owid-covid-data_new_cases_smoothed_per_million' : 'new_cases_smoothed_per_million',
       'owid-covid-data_total_deaths_per_million' : 'total_deaths_per_million',
       'owid-covid-data_new_deaths_per_million' : 'new_deaths_per_million',
       'owid-covid-data_new_deaths_smoothed_per_million' : 'new_deaths_smoothed_per_million'}
D = D[D.columns[2:]]
D.rename(columns = d, inplace = True)
#print(D.columns)
#print(D[D.columns[2:5]][D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])])
'''D.new_cases[D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])] = 2001.0
D.total_cases[D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])] += 2 * 2001.0
D.new_cases_smoothed[D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])] += 2 * 2001.0 / 7
#print(D[D.columns[2:5]][D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])])

#print(D[D.columns[10:11]][D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])])

D.total_cases_per_million[D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])] += 2 * 38969.974
D.new_cases_per_million[D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])] = 345.464
D.new_cases_smoothed_per_million[D.date.isin(['2021-03-24']) & D.location.isin(['Denmark'])] += 2 * 345.464 / 7'''

D.loc[870 : 894, 'total_cases'] += 4002.0

for i in D.columns:
    pass
    #print(i, len(D[D[i].notna()]))

D.to_csv('../data/BIG_CSV.csv')