"""
Double Decay Chi Squared Minimisation Algorithm

@author: Kit Risbey
"""

import sys

import calculations
import dataLoader

def runner(args):
    '''
    The main runner to call all the other functions
    :params args: Array of the run time arguments
    '''
    
    # load the data
    data = dataLoader.dataLoader(args[1])  
    
    # initial chi-square
    initChi = calculations.calculateChiSquare(
            float(args[2]),
            float(args[3]),
            float(args[4]),
            float(args[5]),
            data)
    print('Initial chi-squared: %.2f' %(initChi))

if __name__ == '__main__':
    
    print('Starting double decay....\n')
    
    try:
        runner(sys.argv)   
        
    except Exception as err:
        print('Calculation failed with error:')
        print(err)
    
    print('\n....end')
  