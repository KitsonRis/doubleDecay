#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File to handle all of the different calculations

@author: kitrisbey
"""

from math import exp

def calculateChiSquare(A, B, lam1, lam2, data):
    '''
    Calculate the chi-square value
    :params A:
    :params B:
    :params lam1:
    :params lam2:
    :params data: the loaded data file
    :returns: the chi-square value
    '''
    
    chi = 0.0
    
    for index, row in data.iterrows():
        yFit = calculateDoubleDecay(A, B, lam1, lam2, row['t'])
        chi += (pow((row['c'] - yFit), 2)) / pow(row['sig'], 2)
    
    return chi

def calculateDoubleDecay(A, B, lam1, lam2, t):
    '''
    Formula to calculate the double exponential decay
    C(t) = Aexp(-lam1 * t) + Bexp(-lam2 * t)
    :params A:
    :params B:
    :params lam1:
    :params lam2:
    :params t:
    :returns: the calcualted count value
    '''
    
    lhs = A * exp(-1 * lam1 * t)
    rhs = B * exp(-1 * lam2 * t)
    
    return lhs + rhs