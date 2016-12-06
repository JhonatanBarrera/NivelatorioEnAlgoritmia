#! /usr/bin/python2.7.8
# -*- coding: utf-8 -*-

# Python program for implementation of Random Quick Sort
import argparse
from math import floor
from random import randint
from time import clock

def PARTITION(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    print(A)
    return i + 1
#END PARTITION

def RANDOM_PARTITION(A,p,r):
    i = randint(p,r)
    A[r],A[i] = A[i],A[r]
    return PARTITION(A,p,r)
#END RANDOM_PARTITION

def RANDOM_QUICKSORT(A,p,r):
    if p<r:
        q = RANDOM_PARTITION(A,p,r)
        RANDOM_QUICKSORT(A,p,q-1)
        RANDOM_QUICKSORT(A,q+1,r)
#END RANDOM_QUICKSORT

def ORDERDATAFILE(nums):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
    args = parser.parse_args()

    with open(args.file) as file:
        data = file.read()
        for word in data.split():
            nums.append(int(word))

    t_ini = clock()
    RANDOM_QUICKSORT(nums,0,len(nums)-1)
    t_fin = clock()
    
    if args.file:
        print(args.file, (t_fin - t_ini))
# end READDATAFILE

if __name__ == "__main__":
    nums = []
    ORDERDATAFILE(nums)
