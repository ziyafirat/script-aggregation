'''
Created on May 8, 2018

@author: osboxes
'''

import os
from argospyt.argosp import *
import numpy as np
from argospyt.plotDensities import *

print('***************** hello Density **********************')

os.system("echo 'hello world'")
os.system("echo 'argos Density start--------'")




def processDensity(proportions,rangeStart,rangeEnd,swarmSize,radiusSpot,resultDir):
    for prop in proportions:    
        t1 = []        
        t2 = [] 
        
        for x in range(rangeStart, rangeEnd):        
            print ("start Density :" , x)
            inform = swarmSize * prop
            print ("prop:" + str(prop))
            print ("inform:", str(inform))
            resultFolder = 'FirstRuns_A' + radiusSpot + '_N' + str(swarmSize) + '_P' + str(inform) 
            resultFile = resultFolder + '/output_run_' + str(x) + '.txt'
            print ("Starting density..  ", str(x)) 
            filename = resultDir + '/' + resultFile
            data = np.loadtxt(filename);

            x, y, z = data.T
            
            t1 = np.hstack((t1, x))
            t2 = np.hstack((t2, y))
            
        ab = np.zeros(t1.size, dtype=[('var1', int), ('var2', float)])
        ab['var1'] = t1
        ab['var2'] = t2        
        resultff = resultDir + '/' + resultFolder + '/density.txt'
        outfile = np.savetxt(resultff, ab, delimiter="\t", fmt="%s")
        print('recorded.',resultff)
        fld=resultDir + '/' + resultFolder + '/densities'
        plotSingleDensity(str(swarmSize), str(inform), radiusSpot, fld , resultff)
        
        
print('***************** Density Finish **********************')

