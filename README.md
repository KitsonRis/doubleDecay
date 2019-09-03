# doubleDecay
This is a repeat of a previous university assignment but written in Python. 

A sample file of 'experimental' radioactive decay data was provided where the decay parameters are uknown. The only known is that the decay follows the double exponential which satisfies the formula:

```math
y(t) = A\exp(-\lambda_1 t) + B\exp(-\lambda_2 t)
```

This script runs a Chi-square minimising algorithm in order to determine the parameters A, B, lambda_1 and lambda_2 provided a set of initial conditions. The way this works is by creating a 'grid' of paramters that have been slightly modified and taking the lowest values of A, B, lambda_1 and lambda2_ and resetting this grid. This is repated until the different in Chi-squared is less than the user defined threshold. Once this has been found the results are displayed and a graph plotted. 

To run this script it can be run through Python or via the shell script decayRunner.sh while passing the input file location, the initial guesses of values A, B, lambda_1 and lambda_2 in that order and the defined threshold, for example

```bash
sh runDecay.sh data.csv 900 500 0.008 0.0002 0.001
```
