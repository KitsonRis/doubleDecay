#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File to handle all of the different calculations

@author: kitrisbey
"""

from math import exp

def calculateChiSquare(params, data):
    '''
    Calculate the chi-square value
    :params params: object of the different parameters
    :params data: the loaded data file
    :returns: the chi-square value
    '''
    
    chi = 0.0
    
    for index, row in data.iterrows():
        yFit = calculateDoubleDecay(params, row['t'])
        chi += (pow((row['c'] - yFit), 2)) / pow(row['sig'], 2)
    
    return chi

def calculateDoubleDecay(params, t):
    '''
    Formula to calculate the double exponential decay
    C(t) = Aexp(-lam1 * t) + Bexp(-lam2 * t)
    :params params: object holding the different parameters
    :params t:
    :returns: the calcualted count value
    '''
    
    lhs = params.A * exp(-1 * params.lam1 * t)
    rhs = params.B * exp(-1 * params.lam2 * t)
    
    return lhs + rhs

def getGrid(param):
    '''
    Return the grid of +/-10% of the parameter
    :params param: the value to centre
    :returns: list of the values wiht the given range
    '''
    
    div = param * 0.01 
    
    upGrid = []
    loGrid = []
    for i in range(1,5):
        upIn = param + (i * div)
        upGrid.append(upIn)
        dnIn = param - (i * div)
        loGrid.append(dnIn)
    
    
    return loGrid + [param] + upGrid