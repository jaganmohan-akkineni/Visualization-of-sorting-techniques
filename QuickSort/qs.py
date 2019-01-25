import pylab
from random import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def quickSort(alist):
   imgidx = 0

   quickSortHelper(alist,0,len(alist)-1,imgidx)

def quickSortHelper(alist,first,last,imgidx):
   if first<last:

       splitpoint, imgidx = partition(alist,first,last,imgidx)

       quickSortHelper(alist,first,splitpoint-1,imgidx)
       quickSortHelper(alist,splitpoint+1,last,imgidx)


def partition(alist,first,last,imgidx):

   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
       plt.bar(x,alist,align='center', alpha = 0.1)
       pylab.title('NBA quick sort')
       pylab.savefig("quick2_img" + '%04d' % imgidx + ".png")
       pylab.clf() 
       imgidx = imgidx + 1

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark, imgidx
        

# running the algorithm
data = pd.read_csv('NBA.csv')
dataVal = data['Age']
dataVal = dataVal[:100]
x = range(len(dataVal))


quickSort(dataVal)