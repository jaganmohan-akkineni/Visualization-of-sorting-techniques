import pylab
from random import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def IS(arr):
    x = range(len(arr))
    imgidx = 0
    n = len(arr) 

    for i in range(1, len(arr)): 
        
        key = arr[i] 
        j = i-1
        
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        plt.bar(x,arr,align='center', alpha = 0.1)
        pylab.title('NBA insertion')
        pylab.savefig("insertionsort2_img" + '%04d' % imgidx + ".png")
        pylab.clf() 
        imgidx = imgidx + 1

data = pd.read_csv('NBA.csv')
dataVal = data['Age']
dataVal = dataVal[:100]


IS(dataVal)


 