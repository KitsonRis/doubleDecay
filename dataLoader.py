#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Loading the data from file

@author: kitrisbey
"""

import pandas as pd

def dataLoader(fileName):
    '''
    Loading the decay data
    :parmas fileName string: the file name of the data
    :returns: dataframe of the file
    '''

    return pd.read_csv(fileName)
