

# from argospyt.argosDensity import *
import os
import xml.etree.cElementTree as ET
# import subprocess

import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# from matplotlib.colors import lnorm
from scipy.stats import kde
from asyncore import write
from sys import path
from numpy.core.fromnumeric import size
from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors
import matplotlib as m

if __name__ == '__main__':
    pass

print('***************** hello **********************')

os.system("echo 'hello world'")
os.system("echo 'argos start--------'")
spotnname = 'black_100'
spotnname2 = 'white_100'
user = 'osboxes'
argosdir = '/home/' + user + '/Ziya/argos3-aggregation'
path = argosdir + '/experiments'
resultDir = '/home/' + user + '/Ziya/DATAV15'  # argosdir + '/build'

proportions =[0]#, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  

clocklen = '10000'  # 2500 * 10 =25000
calcClockLen = int(clocklen) / 100  # for plot calc


changesize = 100


binhist=7;



# #campo converted foot-bot
# if changesize==20: 
#     radiusSpot = 0.767 
#     blackSpotSize = 1.3 
#     whiteSpotSize = 1.3     
#     areaSize = 3.067*2  
#     positionSize = 1.8  
#      
# if changesize==50: 
#     radiusSpot = 1.093012
#     blackSpotSize = 1.8
#     whiteSpotSize = 1.8  
#     areaSize = 4.377*2  
#     positionSize = 3.1 
#  
# if changesize==100: 
#     radiusSpot = 1.328 
#     blackSpotSize = 2.6 
#     whiteSpotSize = 2.6 
#     areaSize = 5.312*2  
#     positionSize = 3.7 

# if changesize==20: 
#     radiusSpot = 0.4 
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
#     radiusSpot = 0.875 
#     blackSpotSize = 3.5 
#     whiteSpotSize = 3.5 
#     areaSize = 9.16*2  
#     positionSize = 6.2 
 
if changesize==20: 
    radiusSpot = 0.9 # round((1.0 * changesize), 1) # spot size
    blackSpotSize = 1.5  #round((1.5 * changesize), 1) #spots distance
    whiteSpotSize = 1.5  #round((1.5 * changesize), 1) #spots distance    
    areaSize = 4.17*2  #round((8 * changesize), 1)  # area size
    positionSize = 2  #round((2 * changesize), 1)
        
if changesize==50: 
    radiusSpot = 1.4 # round((1.0 * changesize), 1) # spot size
    blackSpotSize = 2.3  #round((1.5 * changesize), 1) #spots distance
    whiteSpotSize = 2.3  #round((1.5 * changesize), 1) #spots distance
    areaSize = 6.47*2  #round((8 * changesize), 1)  # area size
    positionSize = 4.3   #round((2 * changesize), 1)
    
if changesize==100: 
    radiusSpot = 2.0 # round((1.0 * changesize), 1) # spot size
    blackSpotSize = 3.5  #round((1.5 * changesize), 1) #spots distance
    whiteSpotSize = 3.5  #round((1.5 * changesize), 1) #spots distance
    areaSize = 9.16*2  #round((8 * changesize), 1)  # area size
    positionSize = 6.2   #round((2 * changesize), 1)


rangeStart = 0
rangeEnd = 200
swarmSize = changesize  #round((20 * changesize), 1)
noiseLevel=0

print ("path:" , path)

nn=[];      
bbww1=[];
bbww2=[];
bbww3=[];
bbww4=[];
bbww5=[];
   
bbb1=[]
bbb2=[]   
bbb5=[]
www1=[]
www2=[]   
www5=[] 
t1 = []        
t2 = [] 
tt1 = []
tt2 = []

t1b = []        
t2b = [] 
tt1b = []
tt2b = []

t3 = []        
t4 = [] 
t5 = [] 
tt3 = []
tt4 = []

t5b = []
t5w = []

tlargeb = []
tlargew = []

t3w = []        
t4w = [] 
tt3w = []
tt4w = []

tt5 = []
tout = []
tsmall = []

qq = []
pp = []

countwhite=0
countblack=0
 

for prop in proportions:    
     
    print ("prop :" , prop)
     
    for x in range(rangeStart, rangeEnd):        
        print ("start Density :" , x)
        inform = swarmSize * prop
        print ("prop:" + str(prop))
        print ("inform:", str(inform))
        resultFolder = 'FirstRuns_A' + str(radiusSpot) + '_N' + str(swarmSize) + '_P' + str(inform) 
        resultFile = resultFolder + '/output_run_' + str(x) + '.txt'
        print ("Starting density..  ", str(x)) 
        filename = resultDir + '/' + resultFile
        data = np.loadtxt(filename);
 
        x, y, z,w1,w2,b1,b2 = data.T

#       all spots
        bb1 = b1[999:1000]
        bbww1= np.hstack((bbww1, bb1))        
 
        bb2 = b2[999:1000]
        bbww2 = np.hstack((bbww2, bb2))        
         
        ww1 = w1[999:1000]
        bbww3 = np.hstack((bbww3, ww1))        
         
        ww2 = w2[999:1000]
        bbww4 = np.hstack((bbww4, ww2))
                      
        #black
        yy3 = y[999:1000]
          
        t1 = np.hstack((t1, str(prop)))
        t2 = np.hstack((t2, yy3))
         
        #white  
        zz3 = z[999:1000]
           
        t3 = np.hstack((t3, str(prop)))
        t4 = np.hstack((t4, zz3))

        nn = np.hstack((nn, swarmSize))
        
        
        ttout1=1-abs(yy3+zz3)
        tout=np.hstack((tout, ttout1))
        
        tbigspot=0

        if yy3 > zz3:    
            if bb1 > bb2:
                t5=np.hstack((t5, bb1))
                tbigspot=bb1
                countblack=countblack+1
            else :
                t5=np.hstack((t5, bb2))
                tbigspot=bb2
                countblack=countblack+1
        else:
            if ww1 > ww2:
                t5=np.hstack((t5, ww1))
                tbigspot=ww1
                countwhite=countwhite+1
            else:
                t5=np.hstack((t5, ww2))
                tbigspot=ww2
                countwhite=countwhite+1
                
           
        if bb1 > bb2:
            tlargeb=np.hstack((tlargeb, bb1))
            tbigspot=bb1
        else :
            tlargeb=np.hstack((tlargeb, bb2))
            tbigspot=bb2
    
        if ww1 > ww2:
            tlargew=np.hstack((tlargew, ww1))
            tbigspot=ww1
        else:
            tlargew=np.hstack((tlargew, ww2))
            tbigspot=ww2
    
        
        ttout1small=abs(tbigspot-ttout1)
        tsmall=np.hstack((tsmall, ttout1small))
        
        
    mediann=np.percentile(t2,50) 
    mediann25=np.percentile(t2,25)
    mediann75=np.percentile(t2,75)
    
    
    q = np.percentile(t2, [25, 50, 75])

    ab = np.zeros(t1.size, dtype=[('var1', float), ('var2', float),('var3', float), ('var4', float)])
    ab['var1'] = t1
    ab['var2'] = t2 
    ab['var3'] = tlargeb
    ab['var4'] = tlargew        
    qq.append(t2)
    probfolder = 'prob'    
    resultff1 = resultDir + '/' + probfolder 
    if not os.path.exists(resultff1):
        os.makedirs(resultff1)
    resultff = resultff1 + '/densityprob' + spotnname + '.txt'
    outfile = np.savetxt(resultff, ab, delimiter="\t", fmt="%s")
    print('recorded.', resultff)
    fld = resultDir + '/' + probfolder + '/densitiesprob'
    if not os.path.exists(fld):
        os.makedirs(fld)
        
    ab2 = np.zeros(t1.size, dtype=[('var1', float), ('var2', float),('var3', float), ('var4', float)])
    ab2['var1'] = t3
    ab2['var2'] = t4 
    ab2['var3'] = tlargeb
    ab2['var4'] = tlargew    
    pp.append(t4)     
    probfolder = 'prob'    
    resultff1 = resultDir + '/' + probfolder 
    if not os.path.exists(resultff1):
        os.makedirs(resultff1)
    resultff22 = resultff1 + '/densityprob' + spotnname2 + '.txt'
    outfile = np.savetxt(resultff22, ab2, delimiter="\t", fmt="%s")
    print('recorded.', resultff22)
    fld = resultDir + '/' + probfolder + '/densitiesprob'
    if not os.path.exists(fld):
        os.makedirs(fld)
        
    ab6 = np.zeros(t1.size, dtype=[('var5', float), ('var6', float), ('var7', float), ('var8', float), ('var9', float), ('var10', float),('var11', float),('var12', float),('var13', float),('var14', float)])
    ab6['var5'] = t1
    ab6['var6'] = t4 
    ab6['var7'] = t2   
    ab6['var8'] = bbww1 
    ab6['var9'] = bbww2  
    ab6['var10'] = bbww3 
    ab6['var11'] = bbww4 
    ab6['var12'] = t5  
    ab6['var13'] = tout  
    ab6['var14'] = tsmall   
    pp.append(t5)       
    probfolder = 'prob'    
    resultff1 = resultDir + '/' + probfolder 
    if not os.path.exists(resultff1):
        os.makedirs(resultff1)
    resultffall = resultff1 + '/densityprobAllSpots.txt'
    outfile = np.savetxt(resultffall, ab6, delimiter="\t", fmt="%s")
    print('recorded.', resultffall)
    fld = resultDir + '/' + probfolder + '/densitiesprob'
    if not os.path.exists(fld):
        os.makedirs(fld)
    lennn=len(bbww1)
    print('len:'+str(len(bbww1)))
    
        
N = str(swarmSize).replace(".", "_")
Q = str(inform).replace(".", "_")
S = str(radiusSpot).replace(".", "_")
setting = fld 
fn = resultff

fn22 = resultff22
 
filename = fn

filename2 = fn22

fnall = resultffall
 
filenameall = fnall
 
print("file:", fn)
print("filefilenameall:", filenameall)

 
data = np.loadtxt(filename);

x, y, blacklarge, whitelarge = data.T

data22 = np.loadtxt(filename2);

x2, y2, blacklarge, whitelarge = data22.T


dataall = np.loadtxt(filenameall);

xall, yall, zall,w1all,w2all,b1all,b2all,histallb,histallout,histallsmalls = dataall.T


# Python program to count the  
# number of numbers in a given range 
# using traversal and mutliple line code 

def countRange(list1, l, r): 
    c = 0 
    # traverse in the list1 
    for x in list1:         
        # condition check 
        if x>= l and x< r: 
            c+= 1 
                   
    return c 
   
# 
lwb1=[0] 
ddsd=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

ww0v10=['0-10']
ww10v20=['10-20']
ww20v30=['20-30']
ww30v40=['30-40']
ww40v50=['40-50']
ww50v60=['50-60']
ww60v70=['60-70']
ww70v80=['70-80']
ww80v90=['80-90']
ww90v100=['90-100']

def count(listb,listw, l, r, vx): 
    c = 0 
    idx=0
    llw=[]
    global ddsd,lwb1,ww0v10,ww10v20,ww20v30,ww30v40,ww40v50,ww50v60,ww60v70,ww70v80,ww80v90,ww90v100
    # traverse in the list1 
    for x in listw: 
        
        # condition check 
        if x>= l and x< r: 
            c+= 1 
            rangew=listb[idx]
            llw = np.hstack((llw, rangew))
            
      
        
        
        
        idx+=1
    
    vv=countRange(llw, 0, 0.1)
    
    dd=[countRange(llw, 0, 0.1),countRange(llw, 0.1, 0.2),countRange(llw, 0.2, 0.3),countRange(llw, 0.3, 0.4),countRange(llw, 0.4, 0.5),
        countRange(llw, 0.5, 0.6),countRange(llw, 0.6, 0.7),countRange(llw, 0.7, 0.8),countRange(llw, 0.8, 0.9),countRange(llw, 0.9, 1.1)]
    
    lwb1 = np.hstack((lwb1, vx))
    ww0v10=np.hstack((ww0v10, countRange(llw, 0, 0.1)))
    ww10v20=np.hstack((ww10v20, countRange(llw, 0.1, 0.2)))
    ww20v30=np.hstack((ww20v30, countRange(llw, 0.2, 0.3)))
    ww30v40=np.hstack((ww30v40, countRange(llw, 0.3, 0.4)))
    ww40v50=np.hstack((ww40v50, countRange(llw, 0.4, 0.5)))
    ww50v60=np.hstack((ww50v60, countRange(llw, 0.5, 0.6)))
    ww60v70=np.hstack((ww60v70, countRange(llw, 0.6, 0.7)))
    ww70v80=np.hstack((ww70v80, countRange(llw, 0.7, 0.8)))
    ww80v90=np.hstack((ww80v90, countRange(llw, 0.8, 0.9)))
    ww90v100=np.hstack((ww90v100, countRange(llw, 0.9, 1.1)))
    
    ddsd=[ww90v100,ww80v90,ww70v80,ww60v70,ww50v60,ww40v50,ww30v40,ww20v30,ww10v20,ww0v10,lwb1]
    
#     ab7 = np.zeros(t1.size, dtype=[('var5', float), ('var6', float), ('var7', float), ('var8', float), ('var9', float), ('var10', float),('var11', float),('var12', float),('var13', float),('var14', float),('var15', float)])
#     ab7['var5'] = lwb1
#     ab7['var6'] = ww0v10 
#     ab7['var7'] = ww10v20   
#     ab7['var8'] = ww20v30 
#     ab7['var9'] = ww30v40  
#     ab7['var10'] = ww40v50 
#     ab7['var11'] = ww50v60 
#     ab7['var12'] = ww60v70  
#     ab7['var13'] = ww70v80 
#     ab7['var14'] = ww80v90 
#     ab7['var15'] = ww90v100   
#     pp.append(t1)       
    probfolder = 'prob'    
    resultff7 = resultDir + '/' + probfolder 
    if not os.path.exists(resultff7):
        os.makedirs(resultff7)
    resultffall7 = resultff7 + '/densityprobAllSpotsRange.txt'
    outfile7 = np.savetxt(resultffall7, ddsd, delimiter="\t", fmt="%s")
    print('recorded.', resultffall7)
#     fld = resultDir + '/' + probfolder + '/densitiesprob'
#     if not os.path.exists(fld):
#         os.makedirs(fld)
#     lennn=len(bbww1)
#     print('len:'+str(len(bbww1)))
#     if l>=0.9:
#         lwb1 = np.hstack((lwb1, l))
#         ww0v10=np.hstack((ww0v10, 0))
#         ww10v20=np.hstack((ww10v20, 0.1))
#         ww20v30=np.hstack((ww20v30, 0.2))
#         ww30v40=np.hstack((ww30v40, 0.3))
#         ww40v50=np.hstack((ww40v50, 0.4))
#         ww50v60=np.hstack((ww50v60, 0.5))
#         ww60v70=np.hstack((ww60v70, 0.6))
#         ww70v80=np.hstack((ww70v80, 0.7))
#         ww80v90=np.hstack((ww80v90, 0.8))
#         ww90v100=np.hstack((ww90v100, 0.9))
#     
#         ddsd=[lwb1,ww90v100,ww80v90,ww70v80,ww60v70,ww50v60,ww40v50,ww30v40,ww20v30,ww10v20,ww0v10]
#         
#         outfile7 = np.savetxt(resultffall7, ddsd, delimiter="\t", fmt="%s")
#         print('recorded.', resultffall7)
        
    return c 
      
# driver code 
list1 = yall 
l = 0.1
r = 0.2

blac1=count(yall,zall, 0, 0.1,'0-10')
blac1=count(yall,zall, 0.1, 0.2,'10-20')
blac1=count(yall,zall, 0.2, 0.3,'20-30')
blac1=count(yall,zall, 0.3, 0.4,'30-40')
blac1=count(yall,zall, 0.4, 0.5,'40-50')
blac1=count(yall,zall, 0.5, 0.6,'50-60')
blac1=count(yall,zall, 0.6, 0.7,'60-70')
blac1=count(yall,zall, 0.7, 0.8,'70-80')
blac1=count(yall,zall, 0.8, 0.9,'80-90')
blac1=count(yall,zall, 0.9, 1.1,'90-100')
 


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
    
if not os.path.exists(setting + '/boxplot'):
    os.makedirs(setting + '/boxplot')  

plt.figure(figsize=(14, 7))
plt.clf()
 
# plt.set_title('Hexbin')
 
plt.plot(x, y, 'ko')
plt.plot(x2, y2, 'ko') 

num_bins = 200

#--------------------------2DHist----------------

# fig, axes = plt.subplots(nrows=1, ncols=2)
# 
# data = np.vstack([
#     histallb,
#     histallout
# ])
# 
# gammas = [0.8, 0.5, 0.3]
# 
# #axes[0, 0].set_title('Linear normalization')
# axes[0, 0].hist2d(histallb, histallout, bins=10)
# axes[0, 0].hist2d(histallout, histallb, bins=10)
# 
# 
# 
# # for ax, gamma in zip(axes.flat[1:], gammas):
# #     ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
# # axes.hist2d(histallb, histallout, bins=10, cmap='Greys')
# # axes.hist2d(histallout, histallb, bins=10, cmap='Greys')
# 
# #axes.hist2d(histallb,histallout, bins=100, norm=mcolors.PowerNorm(0.3))
# 
# fig.tight_layout()

# def _dark_colormap(c):
#     r,g,b = m.colors.colorConverter.to_rgb(c)
#     cdict = {'red':   ((0.0, 1.0, 1.0),
#                        (1.0,     0.0,   0.0)),
#              'green': ((0.0, 1.0, 1.0),
#                        (1.0,    0.0,   0.0)),
#              'blue':  ((0.0, 1.0, 1.0),
#                        (1.0,      0.0,   0.0))
#             }
#     return m.colors.LinearSegmentedColormap('_', cdict) 
# 
# def grayify_cmap(cmap):
#     """Return a grayscale version of the colormap"""
#     cmap = plt.cm.get_cmap(cmap)
#     colors = cmap(np.arange(cmap.N))
#     
#     # convert RGBA to perceived greyscale luminance
#     # cf. http://alienryderflex.com/hsp.html
#     RGB_weight = [0.469, 0.187, 0.114]
#     luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
#     colors[:, :3] = luminance[:, np.newaxis]
#     
#     return cmap.from_list(cmap.name + "_grayscale", colors, cmap.N)
# 
# 
# cdict = {
#   'red'  :  ( (0.0, 0.25, .25), (0.02, .59, .59), (1., 1., 1.)),
#   'green':  ( (0.0, 0.0, 0.0), (0.02, .45, .45), (1., .97, .97)),
#   'blue' :  ( (0.0, 1.0, 1.0), (0.02, .75, .75), (1., 0.45, 0.45))
# }
# 
# cm = m.colors.LinearSegmentedColormap('my_colormap', cdict, 1024)


# colors = ["#ffffff", "#DCDCDC", "#D3D3D3", "#C0C0C0", "#A9A9A9","#808080","#696969","#2F4F4F","#000000"]
# cmap= m.colors.ListedColormap(colors)
# cmap.set_under("crimson")
# cmap.set_over("w")
# norm= m.colors.Normalize(vmin=0,vmax=40)
# 
# fig, ax = plt.subplots()
# im = ax.hist2d(histallb,histallout,cmap=cmap, norm=norm)
# 
# #fig.colorbar(0,200)

plt.figure(figsize=(12, 10))
plt.clf()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('N=' + str(swarmSize), fontsize=23 )

colors = ["#FFFFFF", "#D3D3D3", "#C0C0C0", "#A9A9A9","#989898","#808080","#696969","#484848","#202020","#121212","#080808","#000000"]
cmap = m.colors.ListedColormap(colors)
cmap.set_over('0.25')
cmap.set_under('0.75')

bounds = [0, 1, 3, 6, 10, 17, 25, 35, 50,100,150, 200]
norm = m.colors.BoundaryNorm(bounds, cmap.N)
# cb2 = m.colorbar.ColorbarBase(ax, cmap=cmap,
#                                 norm=norm,
#                                 boundaries=[0] + bounds + [13],
#                                 extend='both',
#                                 ticks=bounds,
#                                 spacing='proportional',
#                                 orientation='vertical')

plt.hist2d(zall,yall, bins=5, cmap=cmap, norm=norm)
plt.colorbar(norm=norm,spacing='proportional',ticks=[0, 25, 50,100,150, 200])
#cb2.colorbar(bounds);
 
plt.xlabel('max('r'$\phi$$_b$)', fontsize=16)
plt.ylabel('max('r'$\phi$$_w$)', fontsize=16)
plt.xlim(0,1)
#plt.ylim(0,0.35)

ax=plt.gca()
ax.tick_params(axis='both', which='major', labelsize=16)

# plt.axis([0, nTotalGenerations, 0, maxThreshold])

# plt.show()

plt.draw()

plt.savefig(setting + '/hist2D/' + spotnname + 'hist2D-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

# 
#     
#  
# plt.clf()
# 
# fig = plt.figure()
# ax = fig.add_subplot(111)
#  
# # plt.set_title('Hexbin')
# plt.title('N=' + str(swarmSize), fontsize=23 )
# 
# cdict = plt.cm.get_cmap('spectral_r')._segmentdata
# cdict['red'][0] = (0, 1, 1)
# cdict['green'][0] = (0, 1, 1)
# cdict['blue'][0] = (0, 1, 1)
# my_cmap = m.colors.LinearSegmentedColormap('my_cmap', cdict)
# 
# 
# plt.hist2d(histallb,histallout, bins=5, cmap=_dark_colormap('black'))
# #plt.hist2d(histallb,histallout, bins=5, cmap=plt.cm.get_cmap('Greys', 3))
# #plt.hist2d(histallb, histallout, bins=(10, 10), cmap=plt.cm.colors)
# plt.colorbar()
# plt.clim(0, 200);
# #plt.clim(30, 200);
#  
# plt.xlabel('max('r'$\phi$$_b$,'r'$\phi$$_w$)', fontsize=19)
# plt.ylabel(''r'$\phi$$_f$', fontsize=19)
# plt.xlim(0,1)
# plt.ylim(0,0.1)
# 
# ax=plt.gca()
# ax.tick_params(axis='both', which='major', labelsize=16)
# 
# # plt.axis([0, nTotalGenerations, 0, maxThreshold])
# 
# # plt.show()
# 
# plt.draw()
# 
# plt.savefig(setting + '/hist2D/' + spotnname + 'hist2D-N' + N + '_Q' + Q + '-S' + S + '.png')
# 
# plt.close()

#----------------------------------------------- 


#--------------------------Median ---------

# ax = sns.tsplot(time="timepoint", value="BOLD signal", unit="subject", condition="ROI", data=qq)

#-------------------------------------------------

# tips =t1 # sns.load_dataset(data)
# 
# sns.stripplot(x="day", y="total_bill", hue="smoker",
# data=tips, jitter=True,
# palette="Set2", split=True,linewidth=1,edgecolor='gray')
# 
# sns.boxplot(x="day", y="total_bill", hue="smoker",
# data=tips,palette="Set2",fliersize=0)
# 
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.);

# dd=pd.melt(df,id_vars=['Group'],value_vars=['Apple','Orange'],var_name='fruits')
# sns.boxplot(x='Group',y='value',data=dd,hue='fruits')
 
 
# ------ boxplot-------------  
def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

#     
# collectn_1 = y[0:100]  # np.random.normal(100, 10, 200)
# collectn_2 = y[100:200]  # np.random.normal(80, 30, 200)
# collectn_3 = y[200:300]  # np.random.normal(90, 20, 200)
# collectn_4 = y[300:400]  # np.random.normal(70, 25, 200)
# collectn_5 = y[400:500]
# collectn_6 = y[500:600]
# collectn_7 = y[600:700]
# collectn_8 = y[700:800]
# collectn_9 = y[800:900]
# collectn_10 = y[900:1000]
# collectn_11 = y[1000:1100]
# 
# data_a = qq  # [[1,2,5], [5,7,2,2,5], [7,2,5],[1,2,5], [5,7,2,2,5], [7,2,5],[1,2,5], [5,7,2,2,5], [7,2,5],[1,2,5], [5,7,2,2,5], [7,2,5]]
# data_b = pp  # [[6, 4, 2], [1, 2, 5, 3, 2], [2, 3, 5, 1], [6, 4, 2], [1, 2, 5, 3, 2], [2, 3, 5, 1]]
# 
# ticks = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
# 
# plt.figure()
# 
# bpl = plt.boxplot(data_a, positions=np.array(range(len(data_a))) * 3 - 0.4, sym='',vert=True,notch=True, patch_artist=True,widths=0.6)
# bpr = plt.boxplot(data_b, positions=np.array(range(len(data_b))) * 3 + 0.4, sym='',vert=True,notch=True, patch_artist=True, widths=0.6)
# set_box_color(bpl, '#000000')  # colors are from http://colorbrewer2.org/
# set_box_color(bpr, '#808080')
# 
# # draw temporary red and blue lines and use them to create a legend
# plt.plot([], c='#000000', label='Black')
# plt.plot([], c='#808080', label='White')
# plt.xlabel('Proportion of informed', fontsize=30)
# plt.ylabel('Black / White Spots', fontsize=30)
# plt.legend()
# 
# ax = plt.gca()
# ax.set_title('N='+ str(swarmSize)+'')
# ax.tick_params(axis='both', which='major', labelsize=14)
# 
# plt.xticks(range(0, len(ticks) * 3, 3), ticks)
# plt.xlim(-3, len(ticks) * 3)
# plt.ylim(0, 1)
# plt.tight_layout()
# 
# plt.savefig(setting + '/boxplot/' + spotnname + 'boxplot-N' + N + 'Q' + Q + '-S' + S + 'new.png')
# plt.close()
# #-----------------------------------------------------

 
plt.figure(figsize=(14, 7))
plt.clf()
# plt.hexbin(x, y, gridsize=nbins, cmap=plt.get_cmap('gray'))

ticks = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
# Create data
# np.random.seed(10)
# collectn_1 =np.percentile(y[0:100],50)  # np.random.normal(100, 10, 200)
# collectn_2 =np.percentile(y[100:200],50)  # np.random.normal(80, 30, 200)
# collectn_3 =np.percentile(y[200:300],50)  # np.random.normal(90, 20, 200)
# collectn_4 =np.percentile(y[300:400],50)  # np.random.normal(70, 25, 200)
# collectn_5 =np.percentile(y[400:500],50)
# collectn_6 =np.percentile(y[500:600],50)
# collectn_7 =np.percentile(y[600:700],50)
# collectn_8 =np.percentile(y[700:800],50)
# collectn_9 =np.percentile(y[800:900],50)
# collectn_10 =np.percentile(y[900:1000],50)
# collectn_11 =np.percentile(y[1000:1100],50)
# 
# collectn_125 =np.percentile(y[0:100],25)  # np.random.normal(100, 10, 200)
# collectn_225 =np.percentile(y[100:200],25)  # np.random.normal(80, 30, 200)
# collectn_325 =np.percentile(y[200:300],25)  # np.random.normal(90, 20, 200)
# collectn_425 =np.percentile(y[300:400],25)  # np.random.normal(70, 25, 200)
# collectn_525 =np.percentile(y[400:500],25)
# collectn_625 =np.percentile(y[500:600],25)
# collectn_725 =np.percentile(y[600:700],25)
# collectn_825 =np.percentile(y[700:800],25)
# collectn_925 =np.percentile(y[800:900],25)
# collectn_1025 =np.percentile(y[900:1000],25)
# collectn_1125 =np.percentile(y[1000:1100],25)
# 
# collectn_175 =np.percentile(y[0:100],75)  # np.random.normal(100, 10, 200)
# collectn_275 =np.percentile(y[100:200],75)  # np.random.normal(80, 30, 200)
# collectn_375 =np.percentile(y[200:300],75)  # np.random.normal(90, 20, 200)
# collectn_475 =np.percentile(y[300:400],75)  # np.random.normal(70, 25, 200)
# collectn_575 =np.percentile(y[400:500],75)
# collectn_675 =np.percentile(y[500:600],75)
# collectn_775 =np.percentile(y[600:700],75)
# collectn_875 =np.percentile(y[700:800],75)
# collectn_975 =np.percentile(y[800:900],75)
# collectn_1075 =np.percentile(y[900:1000],75)
# collectn_1175 =np.percentile(y[1000:1100],75)
# 
# collectn_1yy =np.percentile(y2[0:100],50)  # np.random.normal(100, 10, 200)
# collectn_2yy=np.percentile(y2[100:200],50)  # np.random.normal(80, 30, 200)
# collectn_3yy =np.percentile(y2[200:300],50)  # np.random.normal(90, 20, 200)
# collectn_4yy =np.percentile(y2[300:400],50)  # np.random.normal(70, 25, 200)
# collectn_5yy =np.percentile(y2[400:500],50)
# collectn_6yy =np.percentile(y2[500:600],50)
# collectn_7yy=np.percentile(y2[600:700],50)
# collectn_8yy =np.percentile(y2[700:800],50)
# collectn_9yy =np.percentile(y2[800:900],50)
# collectn_10yy =np.percentile(y2[900:1000],50)
# collectn_11yy =np.percentile(y2[1000:1100],50)
# 
# collectn_1yy25 =np.percentile(y2[0:100],25)  # np.random.normal(100, 10, 200)
# collectn_2yy25=np.percentile(y2[100:200],25)  # np.random.normal(80, 30, 200)
# collectn_3yy25 =np.percentile(y2[200:300],25)  # np.random.normal(90, 20, 200)
# collectn_4yy25 =np.percentile(y2[300:400],25)  # np.random.normal(70, 25, 200)
# collectn_5yy25 =np.percentile(y2[400:500],25)
# collectn_6yy25 =np.percentile(y2[500:600],25)
# collectn_7yy25=np.percentile(y2[600:700],25)
# collectn_8yy25 =np.percentile(y2[700:800],25)
# collectn_9yy25 =np.percentile(y2[800:900],25)
# collectn_10yy25 =np.percentile(y2[900:1000],25)
# collectn_11yy25 =np.percentile(y2[1000:1100],25)
# 
# collectn_1yy75 =np.percentile(y2[0:100],75)  # np.random.normal(100, 10, 200)
# collectn_2yy75=np.percentile(y2[100:200],75)  # np.random.normal(80, 30, 200)
# collectn_3yy75 =np.percentile(y2[200:300],75)  # np.random.normal(90, 20, 200)
# collectn_4yy75 =np.percentile(y2[300:400],75)  # np.random.normal(70, 25, 200)
# collectn_5yy75 =np.percentile(y2[400:500],75)
# collectn_6yy75 =np.percentile(y2[500:600],75)
# collectn_7yy75=np.percentile(y2[600:700],75)
# collectn_8yy75 =np.percentile(y2[700:800],75)
# collectn_9yy75 =np.percentile(y2[800:900],75)
# collectn_10yy75 =np.percentile(y2[900:1000],75)
# collectn_11yy75 =np.percentile(y2[1000:1100],75)

# data22 = np.concatenate((collectn_1, collectn_1, collectn_175, collectn_125), 0)
# 
# fig, axs = plt.subplots(2, 3)
# 
# # basic plot
# axs[0, 0].boxplot(data22)
# axs[0, 0].set_title('basic plot')

#---------------------

# collectn_1 = y[0:100]  # np.random.normal(100, 10, 200)
# collectn_2 = y[100:200]  # np.random.normal(80, 30, 200)
# collectn_3 = y[200:300]  # np.random.normal(90, 20, 200)
# collectn_4 = y[300:400]  # np.random.normal(70, 25, 200)
# collectn_5 = y[400:500]
# collectn_6 = y[500:600]
# collectn_7 = y[600:700]
# collectn_8 = y[700:800]
# collectn_9 = y[800:900]
# collectn_10= y[900:1000]
# collectn_11 = y[1000:1100]

# collectn_1 = y[0:200]  # np.random.normal(100, 10, 200)
# collectn_2 = y[200:400]  # np.random.normal(80, 30, 200)
# collectn_3 = y[400:600]  # np.random.normal(90, 20, 200)
# collectn_4 = y[600:800]  # np.random.normal(70, 25, 200)
# collectn_5 = y[800:1000]
# collectn_6 = y[1000:1200]
# collectn_7 = y[1200:1400]
# collectn_8 = y[1400:1600]
# collectn_9 = y[1800:2000]
# collectn_10 = y[2000:2200]
# collectn_11 = y[2200:2400]

collectn_1 = blacklarge[0:200]  # np.random.normal(100, 10, 200)
collectn_2 = blacklarge[200:400]  # np.random.normal(80, 30, 200)
collectn_3 = blacklarge[400:600]  # np.random.normal(90, 20, 200)
collectn_4 = blacklarge[600:800]  # np.random.normal(70, 25, 200)
collectn_5 = blacklarge[800:1000]
collectn_6 = blacklarge[1000:1200]
collectn_7 = blacklarge[1200:1400]
collectn_8 = blacklarge[1400:1600]
collectn_9 = blacklarge[1800:2000]
collectn_10 = blacklarge[2000:2200]
collectn_11 = blacklarge[2200:2400]

# collectn_1 = y[0:50]  # np.random.normal(100, 10, 200)
# collectn_2 = y[50:100]  # np.random.normal(80, 30, 200)
# collectn_3 = y[100:150]  # np.random.normal(90, 20, 200)
# collectn_4 = y[150:200]  # np.random.normal(70, 25, 200)
# collectn_5 = y[200:250]
# collectn_6 = y[250:300]
# collectn_7 = y[300:350]
# collectn_8 = y[250:400]
# collectn_9 = y[400:450]
# collectn_10= y[450:500]
# collectn_11 = y[500:550]
 
# # combine these different collections into a list    
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4, collectn_5, collectn_6, collectn_7, collectn_8, collectn_9, collectn_10, collectn_11]
  
# collectn_1y = y2[0:100]  # np.random.normal(100, 10, 200)
# collectn_2y = y2[100:200]  # np.random.normal(80, 30, 200)
# collectn_3y = y2[200:300]  # np.random.normal(90, 20, 200)
# collectn_4y = y2[300:400]  # np.random.normal(70, 25, 200)
# collectn_5y = y2[400:500]
# collectn_6y = y2[500:600]
# collectn_7y = y2[600:700]
# collectn_8y = y2[700:800]
# collectn_9y = y2[800:900]
# collectn_10y = y2[900:1000]
# collectn_11y = y2[1000:1100]
 
# collectn_1y = y2[0:200]  # np.random.normal(100, 10, 200)
# collectn_2y = y2[200:400]  # np.random.normal(80, 30, 200)
# collectn_3y = y2[400:600]  # np.random.normal(90, 20, 200)
# collectn_4y = y2[600:800]  # np.random.normal(70, 25, 200)
# collectn_5y = y2[800:1000]
# collectn_6y = y2[1000:1200]
# collectn_7y = y2[1200:1400]
# collectn_8y = y2[1400:1600]
# collectn_9y = y2[1800:2000]
# collectn_10y = y2[2000:2200]
# collectn_11y = y2[2200:2400]

collectn_1y = whitelarge[0:200]  # np.random.normal(100, 10, 200)
collectn_2y = whitelarge[200:400]  # np.random.normal(80, 30, 200)
collectn_3y = whitelarge[400:600]  # np.random.normal(90, 20, 200)
collectn_4y = whitelarge[600:800]  # np.random.normal(70, 25, 200)
collectn_5y = whitelarge[800:1000]
collectn_6y = whitelarge[1000:1200]
collectn_7y = whitelarge[1200:1400]
collectn_8y = whitelarge[1400:1600]
collectn_9y = whitelarge[1800:2000]
collectn_10y = whitelarge[2000:2200]
collectn_11y = whitelarge[2200:2400]

# collectn_1y = y2[0:50]  # np.random.normal(100, 10, 200)
# collectn_2y = y2[50:100]  # np.random.normal(80, 30, 200)
# collectn_3y = y2[100:150]  # np.random.normal(90, 20, 200)
# collectn_4y = y2[150:200]  # np.random.normal(70, 25, 200)
# collectn_5y = y2[200:250]
# collectn_6y = y2[250:300]
# collectn_7y = y2[300:350]
# collectn_8y = y2[250:400]
# collectn_9y = y2[400:450]
# collectn_10y= y2[450:500]
# collectn_11y = y2[500:550]
 
# # combine these different collections into a list    
data_to_ploty = [collectn_1y, collectn_2y, collectn_3y, collectn_4y, collectn_5y, collectn_6y, collectn_7y, collectn_8y, collectn_9y, collectn_10y, collectn_11y]

# plt.boxplot(data_to_plot)
# plt.boxplot(data_to_ploty)
bpl = plt.boxplot(data_to_plot, positions=np.array(range(len(data_to_plot))) * 3 - 0.4, sym='', vert=True, notch=True, patch_artist=True, widths=0.7)
bpr = plt.boxplot(data_to_ploty, positions=np.array(range(len(data_to_ploty))) * 3 + 0.4, sym='', vert=True, notch=True, patch_artist=True, widths=0.7)
set_box_color(bpl, '#000000')  # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#808080')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#000000', label=r'$\phi$$_b$', linewidth=10)
plt.plot([], c='#808080', label=r'$\phi$$_w$', linewidth=10)
plt.xlabel('proportion of informed robots', fontsize=30)
plt.ylabel('proportion aggregation', fontsize=30)
plt.legend()
plt.legend(loc='upper left')

ax = plt.gca()
ax.set_title('N=' + str(swarmSize) + ' ', fontsize=25)
ax.tick_params(axis='both', which='major', labelsize=18)

plt.xticks(range(0, len(ticks) * 3, 3), ticks)
plt.xlim(-3, len(ticks) * 3)
plt.ylim(0, 1)
plt.tight_layout()
# plt.plot(y, x, 'ko')
# plt.xlabel('Prop', fontsize=30)
# plt.ylabel('Spot', fontsize=30)
ax = plt.gca()
 
ax.tick_params(axis='both', which='major', labelsize=18)
ax.set_xticklabels(['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'])
# plt.show()
 
plt.legend(loc='lower right', fontsize=25)

plt.draw()
 
plt.savefig(setting + '/boxplot/boxplot-N' + N + 'Q' + Q + '-S' + S + '.png')
# plt.savefig(setting + '/boxplot/' + spotnname + 'boxplot-N' + N + 'Q' + Q + '-S' + S + '.png')
 
plt.close()
    
# -----------------------------------  histogram----------------- 

plt.figure(figsize=(14, 7))
plt.clf()

fig = plt.figure()
ax = fig.add_subplot(111)

column4 = histallb

#plt.hist(histallb, num_bins,facecolor='grey',normed=1)
plt.hist(histallb,binhist,facecolor='grey')
#plt.hist(histallw,num_bins,facecolor='white')

#plt.hist(column4,20,density=True, facecolor='g', alpha=0.75)
plt.title('N=' + str(swarmSize), fontsize=23 )
#plt.title('N=50', fontsize=23 )
plt.xlabel('max('r'$\phi$$_b$,'r'$\phi$$_w$)', fontsize=19)
plt.ylabel("frequency", fontsize=19)
plt.xlim(0,1)
plt.ylim(0,200)
ax = plt.gca()
ax.tick_params(axis='both', which='major', labelsize=16)


#ax.set_xticklabels(0, 1)
#ax.set_xticklabels(['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'])
# ax.xaxis.set_ticks_position('none') 
#plt.show()

plt.draw()
 
plt.savefig(setting + '/boxplot/histogram-N' + N + 'Q' + Q + '-S' + S + '.png')



# # ----------------------------------- 2 black histogram----------------- 
# 
# plt.figure(figsize=(14, 7))
# plt.clf()
# 
# fig = plt.figure()
# ax = fig.add_subplot(111)
# 
# column4 = z4
# num_bins = 10
# plt.hist(column4,num_bins,facecolor='grey')
# 
# plt.title('N=' + str(swarmSize), fontsize=23 )
# #plt.title('N=50', fontsize=23 )
# plt.xlabel('max('r'$\phi$$_b$,'r'$\phi$$_w$)', fontsize=19)
# plt.ylabel("frequency", fontsize=19)
# plt.xlim(0,1)
# ax = plt.gca()
# ax.tick_params(axis='both', which='major', labelsize=16)
# 
# 
# plt.draw()
#  
# plt.savefig(setting + '/boxplot/2BlackHistogram-N' + N + 'Q' + Q + '-S' + S + '.png')
# 
# 
# #------------------------------------------
# 
# # ----------------------------------- 2 white histogram----------------- 
# 
# plt.figure(figsize=(14, 7))
# plt.clf()
# 
# fig = plt.figure()
# ax = fig.add_subplot(111)
# 
# column4 = z5
# num_bins = 10
# plt.hist(column4,num_bins,facecolor='grey')
# 
# plt.title('N=' + str(swarmSize), fontsize=23 )
# #plt.title('N=50', fontsize=23 )
# plt.xlabel('max('r'$\phi$$_b$,'r'$\phi$$_w$)', fontsize=19)
# plt.ylabel("frequency", fontsize=19)
# plt.xlim(0,1)
# ax = plt.gca()
# ax.tick_params(axis='both', which='major', labelsize=16)
# 
# 
# plt.draw()
#  
# plt.savefig(setting + '/boxplot/2WhiteHistogram-N' + N + 'Q' + Q + '-S' + S + '.png')
# 
# 
# #------------------------------------------





# fig = plt.gcf()
# 
# plot_url = py.plot_mpl(fig, filename='mpl-basic-histogram')


# # Fixing random state for reproducibility
# np.random.seed(19680801)
# 
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
# 
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
# 
# 
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

#----------------



# # function for setting the colors of the box plots pairs
# def setBoxColors(bp):
#     setp(bp['boxes'][0], color='blue')
#     setp(bp['caps'][0], color='blue')
#     setp(bp['caps'][1], color='blue')
#     setp(bp['whiskers'][0], color='blue')
#     setp(bp['whiskers'][1], color='blue')
#     setp(bp['fliers'][0], color='blue')
#     setp(bp['fliers'][1], color='blue')
#     setp(bp['medians'][0], color='blue')
#  
#     setp(bp['boxes'][1], color='red')
#     setp(bp['caps'][2], color='red')
#     setp(bp['caps'][3], color='red')
#     setp(bp['whiskers'][2], color='red')
#     setp(bp['whiskers'][3], color='red')
#     setp(bp['fliers'][2], color='red')
#     setp(bp['fliers'][3], color='red')
#     setp(bp['medians'][1], color='red')
#  
# # Some fake data to plot
# A= [[1, 2, 5,],  [7, 2]]
# B = [[5, 7, 2, 2, 5], [7, 2, 5]]
# C = [[3,2,5,7], [6, 7, 3]]
#  
# fig = figure()
# ax = axes()
# hold(True)
#  
# # first boxplot pair
# bp = boxplot(A, positions = [1, 2], widths = 0.6)
# setBoxColors(bp)
#  
# # second boxplot pair
# bp = boxplot(B, positions = [4, 5], widths = 0.6)
# setBoxColors(bp)
#  
# # thrid boxplot pair
# bp = boxplot(C, positions = [7, 8], widths = 0.6)
# setBoxColors(bp)
#  
# # set axes limits and labels
# xlim(0,9)
# ylim(0,9)
# ax.set_xticklabels(['A', 'B', 'C'])
# ax.set_xticks([1.5, 4.5, 7.5])
#  
# # draw temporary red and blue lines and use them to create a legend
# hB, = plot([1,1],'b-')
# hR, = plot([1,1],'r-')
# legend((hB, hR),('Apples', 'Oranges'))
# hB.set_visible(False)
# hR.set_visible(False)
#  
# savefig(setting + '/boxplot/' + spotnname + 'boxplot-N' + N + 'Q' + Q + '-S' + S + '234.png')
# show()
 
plt.xlabel('Prop', fontsize=30)
 
plt.ylabel('Spot', fontsize=30)
 
ax = plt.gca()
 
ax.tick_params(axis='both', which='major', labelsize=24)
 
# plt.show()
 
plt.draw()
 
plt.savefig(setting + '/scatter/' + spotnname + 'scatter-N' + N + '_Q' + Q + '-S' + S + '.png')
 
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

plt.savefig(setting + '/hexbin/' + spotnname + 'hexbin-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

# plt.figure(figsize=(14, 7))
# 
# plt.clf()
# 
# # plt.set_title('Hexbin')
# 
# plt.hist2d(x, y, bins=nbins, cmap=plt.get_cmap('gray'))
# # plt.hist2d(x, y, bins=nbins, cmap=plt.cm.colors)
# # plt.colorbar()
# 
# plt.xlabel('Prop')
# 
# plt.ylabel('Spot')
# 
# # plt.axis([0, nTotalGenerations, 0, maxThreshold])
# 
# # plt.show()
# 
# plt.draw()
# 
# plt.savefig(setting + '/hist2D/' + spotnname + 'hist2D-N' + N + '_Q' + Q + '-S' + S + '.png')
# 
# plt.close()

# Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents

# k = kde.gaussian_kde(data.T)
# 
# xi, yi = np.mgrid[x.min():x.max():nbins * 1j, y.min():y.max():nbins * 1j]
# 
# zi = k(np.vstack([xi.flatten(), yi.flatten()]))
# 
# plt.figure(figsize=(14, 7))
# 
# plt.clf()
# 
# # plt.set_title('Hexbin')
# 
# plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.get_cmap('gray'))
# 
# # plt.colorbar()
# 
# plt.xlabel('Prop')
# 
# plt.ylabel('Spot')
# 
# # plt.axis([0, nTotalGenerations, 0, maxThreshold])
# 
# # plt.show()
# 
# plt.draw()
# 
# plt.savefig(setting + '/gaussianKDE/' + spotnname + 'gaussianKDE-N' + N + '_Q' + Q + '-S' + S + '.png')
# 
# plt.close()
# 
# plt.figure(figsize=(14, 7))
# 
# plt.clf()
# 
# # plt.set_title('Hexbin')
# 
# plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))
# 
# # plt.colorbar()
# 
# plt.xlabel('Prop')
# 
# plt.ylabel('Spot')
# 
# # plt.axis([0, nTotalGenerations, 0, maxThreshold])
# 
# # plt.show()
# 
# plt.draw()
# 
# plt.savefig(setting + '/density/' + spotnname + 'density-N' + N + '_Q' + Q + '-S' + S + '.png')
# 
# plt.close()
# 
# plt.figure(figsize=(14, 7))
# 
# plt.clf()
# 
# # plt.set_title('Hexbin')
# 
# plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))
# 
# plt.contour(xi, yi, zi.reshape(xi.shape))
# 
# # plt.colorbar()
# 
# plt.xlabel('Prop')
# 
# plt.ylabel('Spot')
# 
# # plt.axis([0, nTotalGenerations, 0, maxThreshold])
# 
# # plt.show()
# 
# plt.draw()
# 
# plt.savefig(setting + '/contour/' + spotnname + 'contour-N' + N + '_Q' + Q + '-S' + S + '.png')
#
#plt.close()

print('******************* Finish ************************')

