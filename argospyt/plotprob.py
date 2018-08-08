

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
resultDir = '/home/' + user + '/Ziya/DATAV10'  # argosdir + '/build'

proportions = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  
# proportions = [0.2,0.3];
# proportions = [0.4,0.5];
# proportions = [0.6,0.7];
# proportions = [0.8,0.9];
# proportions = [1];

clocklen = '10000'  # 2500 * 10 =25000
calcClockLen = int(clocklen) / 100  # for plot calc
# 
# radiusSpot = '0.8'
# blackSpotSize = '1.2'
# whiteSpotSize = '1.2'
# swarmSize = 20
# 
# rangeStart = 0
# rangeEnd = 100

changesize = 1

radiusSpot = round((0.9 * changesize), 1)
blackSpotSize = round((1.3 * changesize), 1)
whiteSpotSize = round((1.3 * changesize), 1)
swarmSize = round((20 * changesize), 1)
areaSize = round((6 * changesize), 1)
positionSize = round((2 * changesize), 1)
rangeStart = 0
rangeEnd = 200




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

t3 = []        
t4 = [] 
t5 = [] 
tt3 = []
tt4 = []

tt5 = []

qq = []
pp = []

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

#         

#       black 
        yy = y[980:1000]
        yy3 = yy.sum() / 20
        
        t1 = np.hstack((t1, str(prop)))
        t2 = np.hstack((t2, yy3))
        
#       White
        zz = z[980:1000]
        zz3 = zz.sum() / 20
         
        t3 = np.hstack((t3, str(prop)))
        t4 = np.hstack((t4, zz3))
        
        if yy3 > zz3:
            t5=np.hstack((t5, yy3))
        else:
            t5=np.hstack((t5, zz3)) 
            
#         print ("t5:" + str(t5))
    
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
        
    ab2 = np.zeros(t3.size, dtype=[('var3', float), ('var4', float)])
    ab2['var3'] = t3
    ab2['var4'] = t4   
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
            
    ab3 = np.zeros(t1.size, dtype=[('var5', float), ('var6', float), ('var7', float), ('var8', float)])
    ab3['var5'] = t1
    ab3['var6'] = t2   
    ab3['var7'] = t4 
    ab3['var8'] = t5   
    pp.append(t4)       
    probfolder = 'prob'    
    resultff1 = resultDir + '/' + probfolder 
    if not os.path.exists(resultff1):
        os.makedirs(resultff1)
    resultff33 = resultff1 + '/densityprobBlackWhite.txt'
    outfile = np.savetxt(resultff33, ab3, delimiter="\t", fmt="%s")
    print('recorded.', resultff33)
    fld = resultDir + '/' + probfolder + '/densitiesprob'
    if not os.path.exists(fld):
        os.makedirs(fld)
        
N = str(swarmSize).replace(".", "_")
Q = str(inform).replace(".", "_")
S = str(radiusSpot).replace(".", "_")
setting = fld 
fn = resultff

fn22 = resultff22
 
filename = fn

filename2 = fn22

fn33 = resultff33
 
filename3 = fn33
 
print("file:", fn)
print("file:", fn22)
print("file:", fn33)
 
data = np.loadtxt(filename);

x, y = data.T

data22 = np.loadtxt(filename2);

x2, y2 = data22.T

data33 = np.loadtxt(filename3);

x3, y3, w3, z3 = data33.T

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

collectn_1 = y[0:200]  # np.random.normal(100, 10, 200)
collectn_2 = y[200:400]  # np.random.normal(80, 30, 200)
collectn_3 = y[400:600]  # np.random.normal(90, 20, 200)
collectn_4 = y[600:800]  # np.random.normal(70, 25, 200)
collectn_5 = y[800:1000]
collectn_6 = y[1000:1200]
collectn_7 = y[1200:1400]
collectn_8 = y[1400:1600]
collectn_9 = y[1800:2000]
collectn_10 = y[2000:2200]
collectn_11 = y[2200:2400]

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
 
collectn_1y = y2[0:200]  # np.random.normal(100, 10, 200)
collectn_2y = y2[200:400]  # np.random.normal(80, 30, 200)
collectn_3y = y2[400:600]  # np.random.normal(90, 20, 200)
collectn_4y = y2[600:800]  # np.random.normal(70, 25, 200)
collectn_5y = y2[800:1000]
collectn_6y = y2[1000:1200]
collectn_7y = y2[1200:1400]
collectn_8y = y2[1400:1600]
collectn_9y = y2[1800:2000]
collectn_10y = y2[2000:2200]
collectn_11y = y2[2200:2400]

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
ax.set_title('N=' + str(swarmSize) + '', fontsize=25)
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

column4 = z3
num_bins = 10
#plt.hist(column4, num_bins,facecolor='grey',normed=1)
plt.hist(column4,num_bins,facecolor='grey')

#plt.hist(column4,20,density=True, facecolor='g', alpha=0.75)
plt.title('N=' + str(swarmSize), fontsize=23 )
#plt.title('N=50', fontsize=23 )
plt.xlabel('max('r'$\phi$$_b$,'r'$\phi$$_w$)', fontsize=19)
plt.ylabel("frequency", fontsize=19)
plt.xlim(0,1)
ax = plt.gca()
ax.tick_params(axis='both', which='major', labelsize=16)


#ax.set_xticklabels(0, 1)
#ax.set_xticklabels(['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'])
# ax.xaxis.set_ticks_position('none') 
#plt.show()

plt.draw()
 
plt.savefig(setting + '/boxplot/histogram-N' + N + 'Q' + Q + '-S' + S + '.png')


#------------------------------------------





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

plt.figure(figsize=(14, 7))

plt.clf()

# plt.set_title('Hexbin')

plt.hist2d(x, y, bins=nbins, cmap=plt.get_cmap('gray'))
# plt.hist2d(x, y, bins=nbins, cmap=plt.cm.colors)
# plt.colorbar()

plt.xlabel('Prop')

plt.ylabel('Spot')

# plt.axis([0, nTotalGenerations, 0, maxThreshold])

# plt.show()

plt.draw()

plt.savefig(setting + '/hist2D/' + spotnname + 'hist2D-N' + N + '_Q' + Q + '-S' + S + '.png')

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

plt.savefig(setting + '/gaussianKDE/' + spotnname + 'gaussianKDE-N' + N + '_Q' + Q + '-S' + S + '.png')

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

plt.savefig(setting + '/density/' + spotnname + 'density-N' + N + '_Q' + Q + '-S' + S + '.png')

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

plt.savefig(setting + '/contour/' + spotnname + 'contour-N' + N + '_Q' + Q + '-S' + S + '.png')

plt.close()

print('******************* Finish ************************')

