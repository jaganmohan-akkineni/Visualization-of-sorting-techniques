import pylab
from random import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ms(alist):
    x = range(len(alist))
    imgidx = 0
    n = len(alist) 

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        ms(lefthalf)
        ms(righthalf)

        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

           
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

        plt.bar(x,alist,align='center', alpha = 0.1)
        pylab.title('Binomial merge')
        pylab.savefig("bubblesort_img" + '%04d' % imgidx + ".png")
        pylab.clf()
        imgidx = imgidx + 1

data = pd.read_csv('binomial.csv')
dataVal = data['18']
dataVal = dataVal[:100]

ms(dataVal)

