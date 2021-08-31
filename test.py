# -*- coding: utf-8 -*-
""" 
Created on 8/17/2021 6:03 PM
@author  : Kuro Kien
@File name    : test.py 
"""

import csv
import pandas as pd

# pd.set_option("display.max_rows", None, "display.max_columns", None)


df = pd.read_csv('export_csv_full_years_symptoom.csv')
# df = df.drop(df.columns[[0]], axis=1, inplace=True)
# df1 = df.groupby('matched_merk')[['matched_handelsbenaming','symptoom','count_sleuteltijd_incident_merk',
#                                   'average_sleuteltijd_incident_merk','suggestie']].agg(list).reset_index()

df = df.sort_values("matched_merk")
print(df)
dicts = {}
branch_arr = []
count_branch = 0
for i in range(6451):
    pro_name_arr = []
    name_branch = df.iloc[i,1]
    if name_branch not in branch_arr:
        branch_arr.append(name_branch)
        dicts[name_branch] = [df.iloc[i,2]]
    # else:
['FIAT': ['PUNTO':['Start niet','6893','21.51','23.79'],'PANDA':['Accu','7170','20.6','22.7']],'']
    # print(df.iloc[i,1])
# print(branch_arr)
# print(dicts)


