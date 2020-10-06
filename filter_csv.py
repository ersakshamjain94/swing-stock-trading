#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:48:56 2020

@author: saksjain
"""

import pandas as pd
from io import *
def filter_bymarket():
    read_file = pd.read_csv('master.csv')
    
    filtered_with_market_purchase = read_file[read_file["MODE OF ACQUISITION \n"] == 'Market Purchase']
    filtered_with_market_purchase = filtered_with_market_purchase[(filtered_with_market_purchase['CATEGORY OF PERSON \n'] == 'Promoters' )| (filtered_with_market_purchase['CATEGORY OF PERSON \n'] == 'Promoter Group')]
    #Drop all columnns except SYMBOL and VALUE OF SECURITY
    filtered_with_market_purchase.drop(filtered_with_market_purchase.columns.difference(['SYMBOL \n','VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n']), 1, inplace=True)
    filtered_with_market_purchase['VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n'] = filtered_with_market_purchase['VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n'].apply(pd.to_numeric)
    consolidated = filtered_with_market_purchase.groupby('SYMBOL \n')['VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n'].sum()
    #consolidated.to_excel('consolidated.xlsx')
    consolidated = consolidated.div(10000000)
    consolidated = consolidated.rename('ValueInCrores')
    consolidated = consolidated.sort_values(ascending=False)
    
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    consolidated.to_excel(writer,sheet_name='Sheet1')
    writer.save()
    output.seek(0)
    return output
