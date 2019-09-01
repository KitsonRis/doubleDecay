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
    
    # set out the different arguments
    A = float(args[2])
    B = float(args[3])
    lam1 = float(args[4])
    lam2 = float(args[5])
    threshold = float(args[6])
    
    # load the data
    data = dataLoader.dataLoader(args[1])  
    
    # initial chi-square
    initChi = calculations.calculateChiSquare(
            A,
            B,
            lam1,
            lam2,
            data)
    print('Initial chi-squared: %.2f' %(initChi))
    
    # continue until the breakout clause is met
    breakout = False
    counter = 1
    while breakout == False:
        
        # set up the +/-10% grids for parameters
        gridA = calculations.getGrid(A)
        gridB = calculations.getGrid(B)
        gridLam1 = calculations.getGrid(lam1)
        gridLam2 = calculations.getGrid(lam2)
        
        chiNew = initChi
        
        print('Iteration %i, Chi-Sq: %.2f' %(counter, chiNew))
        

        counter += 1
        # check if can exit the loop
        if counter > 10: # have a forced exit for development work 
            breakout = True
        
    
    # set up the grid of the parameters

if __name__ == '__main__':
    
    print('Starting double decay....\n')
    
    try:
        runner(sys.argv)   
        
    except Exception as err:
        print('Calculation failed with error:')
        print(err)
    
    print('\n....end')
  