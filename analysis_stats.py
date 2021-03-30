#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:17:51 2020

@author: alisha
"""
from scipy.stats import ttest_rel


def indiv_ttest(high_num, low_num):
    
    ttest_list = []
    for i in range(len(high_num)):
        h = high_num.loc[i,:].to_list()
        l = low_num.loc[i,:].to_list()
        
        ttest = ttest_rel(h,l)
        ttest_list.append((ttest[0], ttest[1]))
        
    return ttest_list