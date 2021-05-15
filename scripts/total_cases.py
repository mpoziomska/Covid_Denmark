# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 12:36:54 2021

@author: mpozi
"""

import pandas as pd
from utils import *
import numpy as np
import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

with open('../data/owid-covid-data.csv') as f:
    p = pd.read_csv(f)
    
p = p[p.location.isin(['Denmark']) & p.date.notna() & p.total_cases_per_million.notna()]


x = []
for i in p.index:
    a = p.date[i]
    x.append(np.datetime64(a).astype(datetime.datetime))

x = np.array(x)
y = np.array(p.total_cases_per_million, dtype='float') / 1000
xt = np.empty(14).astype(datetime.datetime)
xt[0] = min(x)

for i in range(1, len(xt)):
    xt[i] = xt[i - 1] + relativedelta(months=+1)
    
xticks = [xt, [i.strftime('%d-%b-%y') for i in xt]]

yt = np.arange(min(y), max(y) + 10, 10)
yticks = [yt, [str(int(i)) + "k" for i in yt]]

gif_line_plot(x=x, y=y, title='Total cases', xlim=[min(x), max(x) + relativedelta(days=+5)], ylim=[min(y), max(y) + 5], slow=None, ylabel='Cases per million in thousands', xlabel='Date', xticks=xticks, yticks=yticks, write_path='../images/total_cases.gif', sc=3)