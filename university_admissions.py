#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:33:12 2021

@author: vishakha
"""
import pandas as pd
import matplotlib.pyplot as plt
col_list=["Degree of urbanization (Urban-centric locale)"]
col_list1=["Percent of total enrollment that are women"]
df=pd.read_csv("IPEDS_data.csv", usecols=col_list)
dg=pd.read_csv("IPEDS_data.csv", usecols=col_list1)
print(df["Degree of urbanization (Urban-centric locale)"])
print(dg["Percent of total enrollment that are women"])

plt.hist(df, bins=dg)
plt.show()