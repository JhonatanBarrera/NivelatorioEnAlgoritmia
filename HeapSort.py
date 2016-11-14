# Python program for implementation of heap Sort
from math import floor

def HEAPSORT(A):
    heapSize = len(A)
    BUILDMAXHEAP(A,heapSize)
    for i in range (heapSize,1,-1):
        A[0],A[i-1] = A[i-1],A[0]
        heapSize = heapSize - 1
        MAXHEAPIFY(A,1,heapSize)
#end HEAPSORT

def BUILDMAXHEAP(A,hS):
    for i in range(floor(hS/2),0,-1):
        MAXHEAPIFY(A,i,hS)
#end BUILD-MAX-HEAP

def MAXHEAPIFY(A,i,hS):
    l = 2*i
    r = 2*i+1

    if l <= hS and A[l-1] > A[i-1]:
        largest = l
    else: largest = i
    
    if r <= hS and A[r-1] > A[largest-1]:
        largest = r
        
    if largest != i:
        A[i-1],A[largest-1] = A[largest-1],A[i-1]
        MAXHEAPIFY(A,largest,hS)
# end MAX-HEAPIFY

arr = [4,10,3,5,1,6,5,4,8,12,54,-743,1,54,32]
HEAPSORT(arr)
n = len(arr)
print ("Sorted array is", arr)
