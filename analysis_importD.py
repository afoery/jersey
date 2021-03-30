#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:26:12 2020

@author: alisha
"""

import pandas as pd
import functions

def import_df(path):
    '''this function imports the csv file and drops selected subjects and
    control if desired
    '''
    
    #import csv file 
    df = pd.read_csv(path, index_col = None, header = 0)

        
    #delete first two columns as we don't need them
    df = functions.deleteFirstTwoColumns(df)
    
    #numbers that were presented
    numbers = [84,12,86,83,89,83,85,85,14,16,89,17,16,83,12,12,85,17,86,
         14,86,88,86,18,17,15,85,83,89,86,17,84,84,17,82,85,88,
         83,87,12,89,14,16,14,84,14,12,85,83,85,87,14,13,87,88,
         16,84,86,16,87,
         
         15,82,14,18,15,17,19,17,84,83,16,88,83,
         15,83,83,16, 83,16,84,15,19,19,86,82,85,17,16,15,16,87,
         18,17,87,18,12,16,18,19,88,17,86,87,88,12,87,85,14,15,
         13,19,89,86,17,13,85,15,12,86,17]
    
    #delete subjects that not completed experiment entirely
    df = df[df.Progress == ('100' or '99' or '98')]
    
    #delete subjects that did not answer properly
    df = df[df.RandomID != '98156']#subject did not complete experiment
#    df = df[df.RandomID != '71530'] #potential outlier
    
    #drop subjects that admitted to not follow instructions
    df = df[df.Q625 != 'No'] #did they follow instructions?
    df = df[df.Q626 != 'No'] #did they do their best?
    df = df[df.Q627 != 'No'] #quiet room, no distractions?

        
    df.index = range(len(df)) #re-indexing rows
    
    return df, numbers


def extract_data(df, cols):
    
    columns = [cols+ str(i) + '_1' for i in range(120)]
    
    df1 = df[columns]
    
    df1.columns = [x for x in range(120)] #name columns with numbers 0-120
    
    #convert str to float
    df1 = df1.astype(float)
    
    return df1