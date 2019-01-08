

# from argospyt.argosDensity import *
import os.path
import xml.etree.cElementTree as ET
# import subprocess
import random
# from debian.changelog import change
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import kde
# from asyncore import write
# from sys import path

if __name__ == '__main__':
    pass

print('***************** hello **********************')

os.system("echo 'hello world'")
os.system("echo 'argos start--------'")
 
user = 'zfirat'
argosdir = '/home/student/z/f/' + user + '/Ziya/argos3-aggregation'  
  
#user = 'osboxes'
#argosdir = '/home/' + user + '/Documents/argos3-aggregation'
  
path = argosdir + '/experiments'
resultDir = argosdir + '/build'
# resultDir = '/home/Ziya/DATA/' 

proportions =[0.8] #0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  

informWhite=40

clocklen = '50000'  # 2500 * 10 =25000
totalSpots = 2
#changesize = 1
changesize = 50


## waitInsideSpot="10" countMaxNeighbors="5.0"   SwarmCampo10_8
## waitInsideSpot="10" countMaxNeighbors="4.0"   SwarmCampo4_10
## waitInsideSpot="10" countMaxNeighbors="7.0"   SwarmCampo7_10
## waitInsideSpot="10" countMaxNeighbors="6.0"   SwarmCampo8_8

   

## waitInsideSpot="1" countMaxNeighbors="7.0"   === 37.txt          radiusSpot = 1.093
## waitInsideSpot="10" countMaxNeighbors="7.0"  === 38.txt
## waitInsideSpot="1" countMaxNeighbors="6.0"    === 39.txt
##waitInsideSpot="1" countMaxNeighbors="5.0"    === 40.txt



#2 spots  S < N/2 
#     
# if changesize==20: 
#     radiusSpot = 0.33 
#     blackSpotSize = 0.7
#     whiteSpotSize = 0.7     
#     areaSize = 1.85*2  
#     positionSize = 1.2  
#       
# if changesize==50: 
#     radiusSpot = 0.50
#     blackSpotSize = 1.3  
#     whiteSpotSize = 1.3  
#     areaSize = 2.92*2  
#     positionSize = 2.0  
#   
# if changesize==100: 
#     radiusSpot = 0.69
#     blackSpotSize = 2.1 
#     whiteSpotSize = 2.1 
#     areaSize = 4.13*2  
#     positionSize = 2.7

  
#2 spots  N/2 < S < N
    
# if changesize==20: 
#     radiusSpot = 0.44 
#     blackSpotSize = 0.7
#     whiteSpotSize = 0.7     
#     areaSize = 1.85*2  
#     positionSize = 1.2  
#      
# if changesize==50: 
#     radiusSpot = 0.69
#     blackSpotSize = 1.3  
#     whiteSpotSize = 1.3  
#     areaSize = 2.92*2  
#     positionSize = 2.0  
#  
# if changesize==100: 
#     radiusSpot = 0.952
#     blackSpotSize = 2.1 
#     whiteSpotSize = 2.1 
#     areaSize = 4.13*2  
#     positionSize = 2.7

# if changesize==20: 
#     radiusSpot = 0.9 
#     blackSpotSize = 1.5 
#     whiteSpotSize = 1.5     
#     areaSize = 4.17*2  
#     positionSize = 2  
#     
# if changesize==50: 
#     radiusSpot = 0.625
#     blackSpotSize = 2.3  
#     whiteSpotSize = 2.3  
#     areaSize = 6.32*2  
#     positionSize = 4.3  
# 
# if changesize==100: 
#     radiusSpot = 2.0 
#     blackSpotSize = 3.5 
#     whiteSpotSize = 3.5 
#     areaSize = 9.16*2  
#     positionSize = 6.2 
    
    
##waitInsideSpot="10" countMaxNeighbors="5.0"    --  17.txt
##waitInsideSpot="10" countMaxNeighbors="6.0"    --  18.txt
##waitInsideSpot="10" countMaxNeighbors="7.0"    --  19.txt
##waitInsideSpot="1" countMaxNeighbors="6.0"    --  20.txt
##waitInsideSpot="1" countMaxNeighbors="5.0"    --  21.txt
##waitInsideSpot="1" countMaxNeighbors="7.0"    --  22.txt
##waitInsideSpot="1" countMaxNeighbors="12.0"    --  22.txt
##waitInsideSpot="1" countMaxNeighbors="18.0"    --  23.txt

##waitInsideSpot="1" countMaxNeighbors="5.0"    --  25.txt
##waitInsideSpot="1" countMaxNeighbors="4.0"    --  26.txt
##waitInsideSpot="1" countMaxNeighbors="8.0"    --  27.txt
##waitInsideSpot="1" countMaxNeighbors="9.0"    --  28.txt
##waitInsideSpot="1" countMaxNeighbors="15.0"    --  29.txt
##waitInsideSpot="1" countMaxNeighbors="20.0"    --  30.txt
##waitInsideSpot="1" countMaxNeighbors="25.0"    --  31.txt
##waitInsideSpot="1" countMaxNeighbors="30.0"    --  32.txt

##waitInsideSpot="10" countMaxNeighbors="20.0"    --  41.txt
##waitInsideSpot="10" countMaxNeighbors="15.0"    --  42.txt
##waitInsideSpot="10" countMaxNeighbors="25.0"    --  43.txt working good
##waitInsideSpot="10" countMaxNeighbors="10.0"    --  44.txt
##waitInsideSpot="10" countMaxNeighbors="5.0"    --  45.txt
##waitInsideSpot="1" countMaxNeighbors="12.0"    --  46.txt
##waitInsideSpot="1" countMaxNeighbors="18.0"    --  47.txt
##waitInsideSpot="1" countMaxNeighbors="22.0"    --  48txt

##waitInsideSpot="10" countMaxNeighbors="25.0"    --  0.txt 20 swarm
##waitInsideSpot="10" countMaxNeighbors="25.0"    --  0.txt 100 swarm


    
# realone 
    
if changesize==20: 
    radiusSpot = 0.9 
    blackSpotSize = 1.5 
    whiteSpotSize = 1.5     
    areaSize = 4.17*2  
    positionSize = 2  
      
if changesize==50: 
    radiusSpot = 1.4 
    blackSpotSize = 2.3  
    whiteSpotSize = 2.3  
    areaSize = 6.47*2  
    positionSize = 4.3  
  
if changesize==100: 
    radiusSpot = 2.0 
    blackSpotSize = 3.5 
    whiteSpotSize = 3.5 
    areaSize = 9.16*2  
    positionSize = 6.2  

#campo epuck
# if changesize==20: 
#     radiusSpot = 0.334 
#     blackSpotSize = 0.5 
#     whiteSpotSize = 0.5     
#     areaSize = 1.335*2  
#     positionSize = 0.7  
#      
# if changesize==50: 
#     radiusSpot = 0.476 
#     blackSpotSize = 2.3  
#     whiteSpotSize = 2.3  
#     areaSize = 1.905*2  
#     positionSize = 4.3  
#  
# if changesize==100: 
#     radiusSpot = 2.0 
#     blackSpotSize = 3.5 
#     whiteSpotSize = 3.5 
#     areaSize = 9.16*2  
#     positionSize = 6.2  

#1.093011  //20 timestep
#1.093012  //50 timestep
#1.093013  //80 timestep
#1.093014  //100 timestep
#waitInsideSpot="10" countMaxNeighbors="6"   1 spot ame values SwarmAme7 and SwarmAme6 500.00 timesrun  --   countMaxNeighbors="7" SwarmAme8  --  
#waitInsideSpot="10" countMaxNeighbors="8"   1 spot campo waitInsideSpot="8"


## waitInsideSpot="5" countMaxNeighbors="5.0"    8.txt
## waitInsideSpot="25" countMaxNeighbors="5.0"    9.txt
## waitInsideSpot="25" countMaxNeighbors="7.0"    10.txt
## waitInsideSpot="5" countMaxNeighbors="4.0"    11.txt
## waitInsideSpot="15" countMaxNeighbors="4.0"    12.txt
## waitInsideSpot="5" countMaxNeighbors="3.0"    13.txt
    
#campo converted foot-bot
# if changesize==20: 
#     radiusSpot = 0.767 
#     blackSpotSize = 1.3 
#     whiteSpotSize = 1.3     
#     areaSize = 3.067*2  
#     positionSize = 1.8  
#     
# if changesize==50: 
#     radiusSpot = 1.4 
#     blackSpotSize = 2.3  
#     whiteSpotSize = 2.3  
#     areaSize = 6.47*2  
#     positionSize = 4.3 
#      
# # if changesize==50: 
# #     radiusSpot = 1.4
# #     blackSpotSize = 1.8
# #     whiteSpotSize = 1.8  
# #     areaSize = 4.377*2  
# #     positionSize = 3.1 
#  
# if changesize==100: 
#     radiusSpot = 1.328 
#     blackSpotSize = 2.6 
#     whiteSpotSize = 2.6 
#     areaSize = 5.312*2  
#     positionSize = 3.7  


rangeStart = 0
rangeEnd = 100
swarmSize = changesize  
noiseLevel=0

print ("path:" , path)

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
        #informWhite=inform * informedWhite
        informBlack=inform - informWhite
        print ("prop:" + str(prop))
        print ("subpropwhite:" + str(informWhite))
        print ("subpropblack:" + str(informBlack))
        print ("inform:", str(inform))
        resultFolder = 'FirstRuns_A' + str(radiusSpot) + '_N' + str(swarmSize) + '_P' + str(inform)+ '_SP' + str(informWhite) 
        fileName = 'output_run_' + str(x) + '.txt'
        resultFile = resultFolder + '/' + fileName
          
        if not os.path.exists(resultDir + '/' + resultFolder):
            os.makedirs(resultDir + '/' + resultFolder)
            
        if os.path.isfile(resultDir + '/' + resultFile):
            print('file does exist. file:' + resultFile)
        else:
            print('file does NOT exist. file:' + resultFile)
                      
            rootloop = et.find('loop_functions')
            rootloop.set('output', resultFile)
            rootloop.set('radiusSpot', str(radiusSpot))
            rootloop.set('blackSpotSize', str(blackSpotSize))
            rootloop.set('whiteSpotSize', str(whiteSpotSize))  
            rootloop.set('totalSpots', str(totalSpots))  
            rootarea = et.find('arena')
            rootarea.set('size', str(areaSize) + ',' + str(areaSize) + ',1')
            rootdist = rootarea.find('distribute')
            rootpos = rootdist.find('position')
            minpos = '-' + str(positionSize) + ',-' + str(positionSize) + ',-0'
            rootpos.set('min', minpos)
            maxpos = str(positionSize) + ',' + str(positionSize) + ',0'
            rootpos.set('max', maxpos)
            rootqty = rootdist.find('entity')
            rootqty.set('quantity', str(swarmSize)) 
            rootcontroller = et.find('controllers')
            rootfootbot = rootcontroller.find('footbot_aggregation_controller')
            rootparam = rootfootbot.find('params')
            rootparam.set('numInformedRobot', str(inform)) 
            rootparam.set('numInformedRobotBlack', str(informBlack)) 
            rootparam.set('numInformedRobotWhite', str(informWhite)) 
            rootgroundS = rootfootbot.find('sensors')
            rootground = rootgroundS.find('footbot_motor_ground')
            rootground.set('noise_level', str(noiseLevel)) 
             
    #         rootparam.set('goStraight', str(goStraight))  
    #         rootparam.set('walkInsideSpot', str(walkInsideSpot))  
    #         rootparam.set('waitInsideSpot', str(waitInsideSpot))  
    #         rootparam.set('leaveInsideSpot', str(leaveInsideSpot))  
                 
            xmlFolder = 'aggregation_informedRatio_A' + str(radiusSpot) + '_N' + str(swarmSize) + '_P' + str(inform) 
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
     
# for prop in proportions:    
#     t1 = []        
#     t2 = [] 
#       
#     print ("prop :" , prop)
#       
#     for x in range(rangeStart, rangeEnd):        
#         print ("start Density :" , x)
#         inform = swarmSize * prop
#         print ("prop:" + str(prop))
#         print ("inform:", str(inform))
#         resultFolder = 'FirstRuns_A' + radiusSpot + '_N' + str(swarmSize) + '_P' + str(inform) 
#         resultFile = resultFolder + '/output_run_' + str(x) + '.txt'
#         print ("Starting density..  ", str(x)) 
#         filename = resultDir + '/' + resultFile
#         data = np.loadtxt(filename);
#   
#         x, y, z = data.T
#           
#         t1 = np.hstack((t1, x))
#         t2 = np.hstack((t2, y))
#           
#     ab = np.zeros(t1.size, dtype=[('var1', int), ('var2', float)])
#     ab['var1'] = t1
#     ab['var2'] = t2        
#     resultff = resultDir + '/' + resultFolder + '/density.txt'
#     outfile = np.savetxt(resultff, ab, delimiter="\t", fmt="%s")
#     print('recorded.',resultff)
#     fld=resultDir + '/' + resultFolder + '/densities'
#      
#     N=str(swarmSize)
#     Q=str(inform)
#     S=radiusSpot
#     setting=fld 
#     fn=resultff
#       
#     filename = fn
#   
#       
#     print("file:",fn)
#       
#     data = np.loadtxt(filename);
#   
#     x, y = data.T
#   
#       
#   
#     nbins = 100
#   
#       
#     print("setting:",setting)
#       
#     if not os.path.exists(setting):
#         os.makedirs(setting)    
#   
#     if not os.path.exists(setting+'/scatter'):
#         os.makedirs(setting+'/scatter')        
#   
#     if not os.path.exists(setting+'/hexbin'):
#         os.makedirs(setting+'/hexbin')
#   
#     if not os.path.exists(setting+'/hist2D'):
#         os.makedirs(setting+'/hist2D')    
#   
#     if not os.path.exists(setting+'/gaussianKDE'):
#         os.makedirs(setting+'/gaussianKDE')    
#   
#     if not os.path.exists(setting+'/density'):
#         os.makedirs(setting+'/density')    
#   
#     if not os.path.exists(setting+'/contour'):
#         os.makedirs(setting+'/contour')  
#     
#     if not os.path.exists(setting+'/boxplot'):
#         os.makedirs(setting+'/boxplot')        
#   
#     plt.figure(figsize = (14,7))
#     plt.clf()
#   
#     #plt.set_title('Hexbin')
#   
#     plt.plot(x, y, 'ko')
#   
#     plt.xlabel('Time', fontsize=30)
#   
#     plt.ylabel('Proportion of agents chosing a', fontsize=30)
#   
#     ax = plt.gca()
#   
#     ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
#   
#     #plt.show()
#   
#     plt.draw()
#   
#     plt.savefig(setting+'/scatter/scatter-N' + N +'Q'+Q+'-S'+S+ '.png')
#   
#     plt.close()
#   
#     # ------ boxplot-------------  
#     
# #     plt.figure(figsize = (14,7))
# #     plt.clf()
# #     
# #     plt.boxplot(x, notch, sym, vert, whis, positions, widths, patch_artist, bootstrap, usermedians, conf_intervals, meanline, showmeans, showcaps, showbox, showfliers, boxprops, labels, flierprops, medianprops, meanprops, capprops, whiskerprops, manage_xticks, hold, data)
# #     
# #     plt.plot(x, y, 'ko')
# #   
# #     plt.xlabel('Time', fontsize=30)
# #   
# #     plt.ylabel('Proportion of agents chosing a', fontsize=30)
# #   
# #     ax = plt.gca()
# #   
# #     ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
# #   
# #     #plt.show()
# #   
# #     plt.draw()
# #   
# #     plt.savefig(setting+'/scatter/scatter-N' + N +'Q'+Q+'-S'+S+ '.png')
# #   
# #     plt.close()
#       
#     # -----------------------------------    
#   
#       
#   
#     plt.figure(figsize = (14,7))
#   
#     plt.clf()
#   
#     #plt.set_title('Hexbin')
#   
#     plt.hexbin(x, y, gridsize=nbins, cmap=plt.get_cmap('gray'))
#   
#     #plt.colorbar()
#   
#     plt.xlabel('Time')
#   
#     plt.ylabel('Proportion of agents chosing a')
#   
#     #plt.axis([0, nTotalGenerations, 0, maxThreshold])
#   
#     #plt.show()
#   
#     plt.draw()
#   
#     plt.savefig(setting+'/hexbin/hexbin-N' + N +'Q'+Q+'-S'+S+ '.png')
#   
#     plt.close()
#   
#       
#   
#     plt.figure(figsize = (14,7))
#   
#     plt.clf()
#   
#     #plt.set_title('Hexbin')
#   
#     plt.hist2d(x, y, bins=nbins, cmap=plt.get_cmap('gray'))
#   
#     #plt.colorbar()
#   
#     plt.xlabel('Time')
#   
#     plt.ylabel('Proportion of agents chosing a')
#   
#     #plt.axis([0, nTotalGenerations, 0, maxThreshold])
#   
#     #plt.show()
#   
#     plt.draw()
#   
#     plt.savefig(setting+'/hist2D/hist2D-N' + N +'Q'+Q+'-S'+S+ '.png')
#   
#     plt.close()
#   
#       
#   
#       
#   
#     # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
#   
#     k = kde.gaussian_kde(data.T)
#   
#     xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
#   
#     zi = k(np.vstack([xi.flatten(), yi.flatten()]))
#   
#   
#     plt.figure(figsize = (14,7))
#   
#     plt.clf()
#   
#     #plt.set_title('Hexbin')
#   
#     plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.get_cmap('gray'))
#   
#     #plt.colorbar()
#   
#     plt.xlabel('Time')
#   
#     plt.ylabel('Proportion of agents chosing a')
#   
#     #plt.axis([0, nTotalGenerations, 0, maxThreshold])
#   
#     #plt.show()
#   
#     plt.draw()
#   
#     plt.savefig(setting+'/gaussianKDE/gaussianKDE-N' + N +'Q'+Q+'-S'+S+ '.png')
#   
#     plt.close()
#   
#       
#   
#     plt.figure(figsize = (14,7))
#   
#     plt.clf()
#   
#     #plt.set_title('Hexbin')
#   
#     plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))
#   
#     #plt.colorbar()
#   
#     plt.xlabel('Time')
#   
#     plt.ylabel('Proportion of agents chosing a')
#   
#     #plt.axis([0, nTotalGenerations, 0, maxThreshold])
#   
#     #plt.show()
#   
#     plt.draw()
#   
#     plt.savefig(setting+'/density/density-N' + N +'Q'+Q+'-S'+S+ '.png')
#   
#     plt.close()
#   
#       
#   
#     plt.figure(figsize = (14,7))
#   
#     plt.clf()
#   
#     #plt.set_title('Hexbin')
#   
#     plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))
#   
#     plt.contour(xi, yi, zi.reshape(xi.shape) )
#   
#     #plt.colorbar()
#   
#     plt.xlabel('Time')
#   
#     plt.ylabel('Proportion of agents chosing a')
#   
#     #plt.axis([0, nTotalGenerations, 0, maxThreshold])
#   
#     #plt.show()
#   
#     plt.draw()
#   
#     plt.savefig(setting+'/contour/contour-N' + N +'Q'+Q+'-S'+S+ '.png')
#   
#     plt.close()
#   
 
print('******************* Finish ************************')

