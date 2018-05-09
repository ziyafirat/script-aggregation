# -*- coding: utf-8 -*-

# Libraries

import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import kde

import os





def plotSingleDensity(N,Q,S,setting,fn):

    



    #stepsSkipped = ''

    stepsSkipped = '.step10.txt'

    #stepsSkipped = '.step100.txt'

    filename = fn

    
    print("file:",fn)
    
    data = np.loadtxt(filename);

    x, y = data.T

    

    nbins = 100

    
    print("setting:",setting)
    
    if not os.path.exists(setting):
        os.makedirs(setting)    

    if not os.path.exists(setting+'/scatter'):
        os.makedirs(setting+'/scatter')        

    if not os.path.exists(setting+'/hexbin'):
        os.makedirs(setting+'/hexbin')

    if not os.path.exists(setting+'/hist2D'):
        os.makedirs(setting+'/hist2D')    

    if not os.path.exists(setting+'/gaussianKDE'):
        os.makedirs(setting+'/gaussianKDE')    

    if not os.path.exists(setting+'/density'):
        os.makedirs(setting+'/density')    

    if not os.path.exists(setting+'/contour'):
        os.makedirs(setting+'/contour')        

    plt.figure(figsize = (14,7))
    plt.clf()

    #plt.set_title('Hexbin')

    plt.plot(x, y, 'ko')

    plt.xlabel('Time', fontsize=30)

    plt.ylabel('Proportion of agents chosing a', fontsize=30)

    ax = plt.gca()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 24)

    #plt.show()

    plt.draw()

    plt.savefig(setting+'/scatter/scatter-N' + N +'Q'+Q+'-S'+S+ '.png')

    plt.close()

    

    

    plt.figure(figsize = (14,7))

    plt.clf()

    #plt.set_title('Hexbin')

    plt.hexbin(x, y, gridsize=nbins, cmap=plt.get_cmap('gray'))

    #plt.colorbar()

    plt.xlabel('Time')

    plt.ylabel('Proportion of agents chosing a')

    #plt.axis([0, nTotalGenerations, 0, maxThreshold])

    #plt.show()

    plt.draw()

    plt.savefig(setting+'/hexbin/hexbin-N' + N +'Q'+Q+'-S'+S+ '.png')

    plt.close()

    

    plt.figure(figsize = (14,7))

    plt.clf()

    #plt.set_title('Hexbin')

    plt.hist2d(x, y, bins=nbins, cmap=plt.get_cmap('gray'))

    #plt.colorbar()

    plt.xlabel('Time')

    plt.ylabel('Proportion of agents chosing a')

    #plt.axis([0, nTotalGenerations, 0, maxThreshold])

    #plt.show()

    plt.draw()

    plt.savefig(setting+'/hist2D/hist2D-N' + N +'Q'+Q+'-S'+S+ '.png')

    plt.close()

    

    

    # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents

    k = kde.gaussian_kde(data.T)

    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]

    zi = k(np.vstack([xi.flatten(), yi.flatten()]))

    

    plt.figure(figsize = (14,7))

    plt.clf()

    #plt.set_title('Hexbin')

    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.get_cmap('gray'))

    #plt.colorbar()

    plt.xlabel('Time')

    plt.ylabel('Proportion of agents chosing a')

    #plt.axis([0, nTotalGenerations, 0, maxThreshold])

    #plt.show()

    plt.draw()

    plt.savefig(setting+'/gaussianKDE/gaussianKDE-N' + N +'Q'+Q+'-S'+S+ '.png')

    plt.close()

    

    plt.figure(figsize = (14,7))

    plt.clf()

    #plt.set_title('Hexbin')

    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))

    #plt.colorbar()

    plt.xlabel('Time')

    plt.ylabel('Proportion of agents chosing a')

    #plt.axis([0, nTotalGenerations, 0, maxThreshold])

    #plt.show()

    plt.draw()

    plt.savefig(setting+'/density/density-N' + N +'Q'+Q+'-S'+S+ '.png')

    plt.close()

    

    plt.figure(figsize = (14,7))

    plt.clf()

    #plt.set_title('Hexbin')

    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.get_cmap('gray'))

    plt.contour(xi, yi, zi.reshape(xi.shape) )

    #plt.colorbar()

    plt.xlabel('Time')

    plt.ylabel('Proportion of agents chosing a')

    #plt.axis([0, nTotalGenerations, 0, maxThreshold])

    #plt.show()

    plt.draw()

    plt.savefig(setting+'/contour/contour-N' + N +'Q'+Q+'-S'+S+ '.png')

    plt.close()




