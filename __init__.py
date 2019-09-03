"""
Double Decay Chi Squared Minimisation Algorithm

@author: Kit Risbey
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd

import calculations
import dataLoader
import paramClass

def runner(args):
    '''
    The main runner to call all the other functions
    :params args: Array of the run time arguments
    '''
    
    initParams = paramClass.params(
            args[2],
            args[3],
            args[4],
            args[5]
            )
    print('Calculation starting.')
    initParams.printResults()
      
    # load the data
    data = dataLoader.dataLoader(args[1])  
    
    # initial chi-square
    initChi = calculations.calculateChiSquare(
            initParams,
            data)
    
    # continue until the breakout clause is met
    chiNew = initChi
    paramsNew = initParams
    chiDiff = 0.0
    breakout = False
    counter = 0
    while breakout == False:
        
        counter += 1
        print('Iteration %i...' %(counter))
        
        # set up the +/-10% grids for parameters
        gridA = calculations.getGrid(paramsNew.A)
        gridB = calculations.getGrid(paramsNew.B)
        gridLam1 = calculations.getGrid(paramsNew.lam1)
        gridLam2 = calculations.getGrid(paramsNew.lam2)
        
        # loop through each grid combo and work out the chi-sq
        for i in gridA:
            for j in gridB:
                for k in gridLam1:
                    for l in gridLam2:
                        paramsTemp = paramClass.params(i, j, k, l)
                        chiSqTemp = calculations.calculateChiSquare(
                                paramsTemp,
                                data)
                        # is this a lower chi-sq? If so update the variables
                        if chiSqTemp < chiNew:
                            chiDiff = abs(chiNew - chiSqTemp)
                            chiNew = chiSqTemp
                            paramsNew = paramsTemp
        
        # check if can exit the loop
        if chiDiff < float(args[6]):
        #if counter >= 2: # add in a force exit for simple debugging - comment out when not in use
            breakout = True       
    
    #print the results of the parameters
    print('Calculation completed.')
    paramsNew.printResults()
    print('Iteration %i, Chi-Sq: %.2f' %(counter, chiNew))
    
    # get the model for plotting
    yFit = []
    xFit = []
    for index, row in data.iterrows():
        yFit.append(calculations.calculateDoubleDecay(paramsNew, row['t']))
        xFit.append(row['t'])
    # change the index 
    modelData = pd.DataFrame({'t': xFit, 'yFit': yFit})
    modelData.set_index('t', inplace = True)
    
    # add to the loaded data to form a plot
    data.set_index('t', inplace = True)
    plotData = data.join(modelData)
    # plot the data
    plt.scatter(plotData.index, plotData['c'], color = 'red')
    plt.plot(plotData.index, plotData['yFit'], color = 'blue')
    # make the plot pretty
    plt.xlabel('Time [s]')
    plt.ylabel('Count [s^-1]')
    plt.title('Doube Exponential Decay')
    plt.show()    

if __name__ == '__main__':
    
    print('Starting double decay....\n')
    
    try:
        runner(sys.argv)   
        
    except Exception as err:
        print('Calculation failed:')
        print(err)
        
    print('\n....end')
  