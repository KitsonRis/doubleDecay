#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class to hold the data for the different starting parameters

@author: kitrisbey
"""

class params:
    
    def __init__(self, A, B, lam1, lam2):
        
        # the four parameters
        self.A = float(A)
        self.B = float(B)
        self.lam1 = float(lam1)
        self.lam2 = float(lam2)
        
    def printResults(self):
        '''
        Print the results in a nice formatted fashion
        '''
        
        print('Parameters:\n\tA: %.4f\n\tB: %.4f\n\tLambda-1: %.4f\n\tLambda-2: %.4f' % (self.A, self.B, self.lam1, self.lam2))