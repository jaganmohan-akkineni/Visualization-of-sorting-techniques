import pylab
from random import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ss(arr):
    x = range(len(arr))
    imgidx = 0
    n = len(arr) 

    for i in range(n):
        
        min_idx = i
        
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j 
      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plt.bar(x,arr,align='center', alpha = 0.1)
        pylab.title('NBA Selection sort')
        pylab.savefig("selectionsort2" + '%04d' % imgidx + ".png")
        pylab.clf() 
        imgidx = imgidx + 1

data = pd.read_csv('NBA.csv')
dataVal = data['Age']
dataVal = dataVal[:100]

ss(dataVal)