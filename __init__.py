"""
Double Decay Chi Squared Minimisation Algorithm

@author: Kit Risbey
"""

import sys
import dataLoader

def runner(args):
    '''
    The main runner to call all the other functions
    :params args: Array of the run time arguments
    '''
    
    # load the data
    data = dataLoader.dataLoader(args[1])
    print(data)    

if __name__ == '__main__':
    
    print('Starting double decay....\n')
    
    try:
        runner(sys.argv)   
        
    except Exception as err:
        print('Calculation failed with error:')
        print(err)
    
    print('\n....end')
  