#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:33:12 2021

@author: vishakha
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

col_list=["Degree of urbanization (Urban-centric locale)"]
col_list1=["Percent of total enrollment that are women"]
df=pd.read_csv("IPEDS_data.csv", usecols=col_list)
dg=pd.read_csv("IPEDS_data.csv", usecols=col_list1)
print(df["Degree of urbanization (Urban-centric locale)"])
print(dg["Percent of total enrollment that are women"])
dfedges, dgedges = np.linspace(-4, 4, 42), np.linspace(-25, 25, 42)
hist, dfedges, dgedges = np.histogram2d(df, dg, (dfedges, dgedges))
xidx = np.clip(np.digitize(df, dfedges), 0, hist.shape[0]-1)
yidx = np.clip(np.digitize(dg, dgedges), 0, hist.shape[1]-1)
c = hist[xidx, yidx]
plt.scatter(df, dg, c=c)

plt.show()
