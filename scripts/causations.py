# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:30:37 2021

@author: mpozi
"""

import pandas as pd
from utils import *
import numpy as np
import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import os

stop = datetime.date(2021, 4, 16)
start = datetime.date(2020, 1, 21)
ndays = (stop - start).days

T = pd.date_range(start, stop, periods = ndays).to_pydatetime()

with open('../data/BIG_CSV.csv') as f:
    p = pd.read_csv(f)
    
X = p.new_cases[p.loc.isin(['Denmark'])]

