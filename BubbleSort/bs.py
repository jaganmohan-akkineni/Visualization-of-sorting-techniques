import pylab
from random import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bs(arr):
    x = range(len(arr))
    imgidx = 0
    n = len(arr) 

    for i in range(n):        
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

        plt.bar(x,arr,align='center', alpha = 0.1)
        pylab.title('NBA bubble sort')
        pylab.savefig("bubblesort2_img" + '%04d' % imgidx + ".png")
        pylab.clf() 
        imgidx = imgidx + 1

data = pd.read_csv('NBA.csv')
dataVal = data['Age']
dataVal = dataVal[:100]

bs(dataVal)