'''
Created on Apr 28, 2018

@author: osboxes
'''

import argospyt.argosDensity
import os
import xml.etree.cElementTree as ET
# import subprocess
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde
from asyncore import write
from sys import path


if __name__ == '__main__':
    pass

print('***************** hello **********************')

os.system("echo 'hello world'")
os.system("echo 'argos start--------'")

user = 'osboxes'
argosdir = '/home/' + user + '/Documents/argos3-aggregation'
path = argosdir + '/experiments'
resultDir = argosdir + '/build'

proportions = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  

clocklen = '2500' #2500 * 10 =25000
radiusSpot = '0.8'
blackSpotSize = '1.2'
whiteSpotSize = '1.2'
swarmSize = 20

rangeStart=0
rangeEnd=5
#argospyt.argosDensity.processDensity(proportions,rangeStart,rangeEnd,swarmSize,radiusSpot,resultDir);


et = ET.parse(os.path.join(path, 'aggregation.argos'))

for prop in proportions:      
        
    for x in range(rangeStart, rangeEnd):        
        print ("start progress:" , x)
        randseed = random.randint(1, 99999)
        print ("random:" + str(randseed))
        
        rootframe = et.find('framework')
        rootex = rootframe.find('experiment')
        rootex.set('random_seed', str(randseed))
        rootex.set('length', clocklen)
        inform = swarmSize * prop
        print ("prop:" + str(prop))
        print ("inform:", str(inform))
        resultFolder = 'FirstRuns_A' + radiusSpot +'_N' + str(swarmSize) + '_P' + str(inform) 
        resultFile = resultFolder + '/output_run_' + str(x) + '.txt' 
        
        if not os.path.exists(resultDir + '/' + resultFolder):
            os.makedirs(resultDir + '/' + resultFolder)
        
        rootloop = et.find('loop_functions')
        rootloop.set('output', resultFile)
        rootloop.set('radiusSpot', radiusSpot)
        rootloop.set('blackSpotSize', blackSpotSize)
        rootloop.set('whiteSpotSize', whiteSpotSize)    
        rootarea = et.find('arena')
        rootdist = rootarea.find('distribute')
        rootqty = rootdist.find('entity')
        rootqty.set('quantity', str(swarmSize)) 
        rootcontroller = et.find('controllers')
        rootfootbot = rootcontroller.find('footbot_aggregation_controller')
        rootparam = rootfootbot.find('params')
        rootparam.set('numInformedRobot', str(inform))       
        xmlFolder = 'aggregation_informedRatio_A' + radiusSpot +  '_N' + str(swarmSize) + '_P'+str(inform) 
        xmlargos = 'run_' + str(x) + '.argos'
        xmlPath = path + '/' + xmlFolder
        if not os.path.exists(xmlPath):
            os.makedirs(xmlPath)
        et.write(xmlPath + '/' + xmlargos)
        print ("File created  " , str(x))
        print ("Starting xml..  " , str(x))       
        os.chdir(argosdir + "/build")
        os.system("dir")
        os.system("argos3 -c ../experiments/" + xmlFolder + '/' + xmlargos)
       
       
argospyt.argosDensity.processDensity(proportions,rangeStart,rangeEnd,swarmSize,radiusSpot,resultDir);


print('******************* Finish ************************')

