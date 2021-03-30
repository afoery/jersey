#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:09:14 2020

@author: alisha
"""
import pandas as pd

def order_and_diff(numbers, ans):
    
    diff, high_num, low_num = ([] for i in range(3))
    for i in range(60):
        
        s = numbers[i] < numbers[i+60] #determine which number is bigger
        
        if s:
            
            d = (ans.loc[:,i+60] - ans.loc[:,i]).to_list()
            
            high_num.append(ans.loc[:,i+60])
            low_num.append(ans.loc[:,i])
                    
        else:
            
            d = (ans.loc[:,i] - ans.loc[:,i+60]).to_list()
            
            high_num.append(ans.loc[:,i])
            low_num.append(ans.loc[:,i+60])
            
        diff.append(d)
    
    #transform to df
    diff = pd.DataFrame(diff).T
    high_num = pd.DataFrame(high_num).T
    low_num = pd.DataFrame(low_num).T
    
    return diff, high_num, low_num