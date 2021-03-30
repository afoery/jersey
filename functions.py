#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:47:43 2020


just some functions

@author: alisha
"""
import pandas as pd
import os

    

def deleteFirstTwoColumns (df):
    df = df.drop(0)
    df = df.drop(1)
    df.index = range(len(df))
    return df



def relevant_data(df, columns , length, create_cols = True):
    '''
    this function extract the important columns of the qualtrics csv file
    '''
    if create_cols:
        columns = [columns+ str(i) for i in range(length)]
        
    extracted = df[columns]
    
    #rename columns
    if isinstance(extracted, pd.DataFrame):
        extracted.columns = [x for x in range(extracted.shape[1])]

    return extracted


def get_data_in_parentDic(data):
    
    #get path to data file
    path = os.getcwd()
    path_parent = os.path.abspath(os.path.join(path, os.pardir))
    path_data = path_parent + F'/{data}.csv'
    
    return path_data






