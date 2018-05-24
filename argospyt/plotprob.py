

# from argospyt.argosDensity import *
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
argosdir = '/home/' + user + '/Ziya/argos3-aggregation'
path = argosdir + '/experiments'
resultDir = '/home/' + user + '/Ziya/DATA'  # argosdir + '/build'

proportions = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  
# proportions = [0.2,0.3];
# proportions = [0.4,0.5];
# proportions = [0.6,0.7];
# proportions = [0.8,0.9];
# proportions = [1];

clocklen = '2500'  # 2500 * 10 =25000
calcClockLen = int(clocklen) / 100  # for plot calc

radiusSpot = '0.8'
blackSpotSize = '1.2'
whiteSpotSize = '1.2'
swarmSize = 20

rangeStart = 0
rangeEnd = 100

# rangeStart=50
# rangeEnd=100

# argospyt.argosDensity.processDensity(proportions,rangeStart,rangeEnd,swarmSize,radiusSpot,resultDir);

print ("path:" , path)

# et = ET.parse(os.path.join(path, 'aggregation.argos'))
# 
# for prop in proportions:      
#         
#     for x in range(rangeStart, rangeEnd):        
#         print ("start progress:" , x)
#         randseed = random.randint(1, 99999)
#         print ("random:" + str(randseed))
#         
#         rootframe = et.find('framework')
#         rootex = rootframe.find('experiment')
#         rootex.set('random_seed', str(randseed))
#         rootex.set('length', clocklen)
#         inform = swarmSize * prop
#         print ("prop:" + str(prop))
#         print ("inform:", str(inform))
#         resultFolder = 'FirstRuns_A' + radiusSpot +'_N' + str(swarmSize) + '_P' + str(inform) 
#         resultFile = resultFolder + '/output_run_' + str(x) + '.txt' 
#         
#         if not os.path.exists(resultDir + '/' + resultFolder):
#             os.makedirs(resultDir + '/' + resultFolder)
#         
#         rootloop = et.find('loop_functions')
#         rootloop.set('output', resultFile)
#         rootloop.set('radiusSpot', radiusSpot)
#         rootloop.set('blackSpotSize', blackSpotSize)
#         rootloop.set('whiteSpotSize', whiteSpotSize)    
#         rootarea = et.find('arena')
#         rootdist = rootarea.find('distribute')
#         rootqty = rootdist.find('entity')
#         rootqty.set('quantity', str(swarmSize)) 
#         rootcontroller = et.find('controllers')
#         rootfootbot = rootcontroller.find('footbot_aggregation_controller')
#         rootparam = rootfootbot.find('params')
#         rootparam.set('numInformedRobot', str(inform))       
#         xmlFolder = 'aggregation_informedRatio_A' + radiusSpot +  '_N' + str(swarmSize) + '_P'+str(inform) 
#         xmlargos = 'run_' + str(x) + '.argos'
#         xmlPath = path + '/' + xmlFolder
#         if not os.path.exists(xmlPath):
#             os.makedirs(xmlPath)
#         et.write(xmlPath + '/' + xmlargos)
#         print ("File created  " , str(x))
#         print ("Starting xml..  " , str(x))       
#         os.chdir(argosdir + "/build")
#         os.system("dir")
#         os.system("argos3 -c ../experiments/" + xmlFolder + '/' + xmlargos)
       
t1 = []        
t2 = [] 
tt1 = []
tt2 = []

for prop in proportions:    
     
    print ("prop :" , prop)
     
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
#         steps = 20
#         for j in range(0, int(calcClockLen)):    
#             starty = j * steps
#             endy = (j + 1) * steps
#                         
#             yy1 = y[starty:endy]
#             # yy1=y[10:20]
#             yy = yy1.sum() / steps
#             # yy1=yy1.sum()
#             t1 = np.hstack((t1, str(prop)))
#             t2 = np.hstack((t2, yy))
        zz=z[230:250]
        zz3=zz.sum()/20
#         
#         yy = y[230:250]
#         yy3=yy.sum()/20
        t1 = np.hstack((t1, str(prop)))
        t2 = np.hstack((t2, zz3))
    
#     steps = 20
#     yy2=0
#     for k in range(0, int(calcClockLen)):
#         for l in range(0,100):
#                 
#             starty = k * steps
#             endy = (k + 1) * steps
#                         
#             yy1 = y[starty:endy]
#             # yy1=y[10:20]
#             yy = yy1.sum() / steps
#             # yy1=yy1.sum()
#             t1 = np.hstack((t1, str(prop)))
#             t2 = np.hstack((t2, yy)) 
#     
#     t22=t2.sum()/2000
#     tt1 = np.hstack((tt1, str(prop)))
#     tt2 = np.hstack((tt2, t22))
    ab = np.zeros(t1.size, dtype=[('var1', float), ('var2', float)])
    ab['var1'] = t1
    ab['var2'] = t2        
    probfolder = 'prob'    
    resultff1 = resultDir + '/' + probfolder 
    if not os.path.exists(resultff1):
        os.makedirs(resultff1)
    resultff = resultff1 + '/densityprob.txt'
    outfile = np.savetxt(resultff, ab, delimiter="\t", fmt="%s")
    print('recorded.', resultff)
    fld = resultDir + '/' + probfolder + '/densitiesprob'
    if not os.path.exists(fld):
        os.makedirs(fld)
    
N = str(swarmSize)
Q = str(inform)
S = radiusSpot
setting = fld 
fn = resultff
 
filename = fn
 
print("file:", fn)
 
data = np.loadtxt(filename);

x, y = data.T

nbins = 100
 
print("setting:", setting)
 
if not os.path.exists(setting):
    os.makedirs(setting)    

if not os.path.exists(setting + '/scatter'):
    os.makedirs(setting + '/scatter')        

if not os.path.exists(setting + '/hexbin'):
    os.makedirs(setting + '/hexbin')

if not os.path.exists(setting + '/hist2D'):
    os.makedirs(setting + '/hist2D')    

if not os.path.exists(setting + '/gaussianKDE'):
    os.makedirs(setting + '/gaussianKDE')    

if not os.path.exists(setting + '/density'):
    os.makedirs(setting + '/density')    

if not os.path.exists(setting + '/contour'):
    os.makedirs(setting + '/contour')        

plt.figure(figsize=(14, 7))
plt.clf()

# plt.set_title('Hexbin')

plt.plot(x, y, 'ko')

plt.xlabel('Prop', fontsize=30)

plt.ylabel('Spot', fontsize=30)

ax = plt.gca()

ax.tick_params(axis='both', which='major', labelsize=24)

# plt.show()

plt.draw()

plt.savefig(setting + '/scatter/scatter-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

plt.figure(figsize=(14, 7))

plt.clf()

# plt.set_title('Hexbin')

plt.hexbin(x, y, gridsize=nbins, cmap=plt.get_cmap('gray'))

# plt.colorbar()

plt.xlabel('Prop')

plt.ylabel('Spot')

# plt.axis([0, nTotalGenerations, 0, maxThreshold])

# plt.show()

plt.draw()

plt.savefig(setting + '/hexbin/hexbin-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

plt.figure(figsize=(14, 7))

plt.clf()

# plt.set_title('Hexbin')

plt.hist2d(x, y, bins=nbins, cmap=plt.get_cmap('gray'))

# plt.colorbar()

plt.xlabel('Prop')

plt.ylabel('Spot')

# plt.axis([0, nTotalGenerations, 0, maxThreshold])

# plt.show()

plt.draw()

plt.savefig(setting + '/hist2D/hist2D-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

# Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents

k = kde.gaussian_kde(data.T)

xi, yi = np.mgrid[x.min():x.max():nbins * 1j, y.min():y.max():nbins * 1j]

zi = k(np.vstack([xi.flatten(), yi.flatten()]))

plt.figure(figsize=(14, 7))

plt.clf()

# plt.set_title('Hexbin')

plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.get_cmap('gray'))

# plt.colorbar()

plt.xlabel('Prop')

plt.ylabel('Spot')

# plt.axis([0, nTotalGenerations, 0, maxThreshold])

# plt.show()

plt.draw()

plt.savefig(setting + '/gaussianKDE/gaussianKDE-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

plt.figure(figsize=(14, 7))

plt.clf()

# plt.set_title('Hexbin')

plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))

# plt.colorbar()

plt.xlabel('Prop')

plt.ylabel('Spot')

# plt.axis([0, nTotalGenerations, 0, maxThreshold])

# plt.show()

plt.draw()

plt.savefig(setting + '/density/density-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

plt.figure(figsize=(14, 7))

plt.clf()

# plt.set_title('Hexbin')

plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))

plt.contour(xi, yi, zi.reshape(xi.shape))

# plt.colorbar()

plt.xlabel('Prop')

plt.ylabel('Spot')

# plt.axis([0, nTotalGenerations, 0, maxThreshold])

# plt.show()

plt.draw()

plt.savefig(setting + '/contour/contour-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

print('******************* Finish ************************')

