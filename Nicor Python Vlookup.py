# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:30:12 2022

@author: Ryan
"""

#Import Statement
import pandas as pd

#First Dataframe
df1 = pd.read_excel(r"C:\Users\16307\Documents\Bills\Nicor Bills.xlsx", sheet_name="Therms", header=0, usecols="A:E")

#Second Dataframe
df2 = pd.read_excel(r"C:\Users\16307\Documents\Bills\Nicor Bills.xlsx", sheet_name="Daily Temp", header=0, usecols="A:D")

#Third Dataframe, Generic Left Join
df3 = pd.merge(df1, df2, how='left', on="Reading Date")

#Fourth Datframe, Vlookup mimic
df4 = pd.merge(df1, df2[['Reading Date', 'Daily Average Temperature']], how='left', on="Reading Date")
