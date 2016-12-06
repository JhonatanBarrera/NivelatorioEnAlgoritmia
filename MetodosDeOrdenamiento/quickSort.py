#! /usr/bin/python2.7.8
# -*- coding: utf-8 -*-

# Python program for implementation of QuickSort
import argparse
from math import floor
from sys import setrecursionlimit
from time import clock

setrecursionlimit(10000)
	
def PARTITION(A,p,r):
	x = A[r]
	i = p
	for j in range(p,r):
		if A[j] <= x:
			A[i],A[j] = A[j],A[i]
			i = i + 1
	A[i],A[r] = A[r],A[i]
	return i
#END PARTITION

def QUICKSORT(A,p,r):
	if p<r:
		q = PARTITION(A,p,r)
		QUICKSORT(A,p,q-1)
		QUICKSORT(A,q+1,r)
#END QUICKSORT

def ORDERDATAFILE(nums):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
    args = parser.parse_args()

    with open(args.file) as file:
        data = file.read()
        for word in data.split():
            nums.append(int(word))

	t_ini = clock()
	QUICKSORT(nums,0,len(nums)-1)
	t_fin = clock()
	#print nums

    if args.file:
        print (args.file, (t_fin - t_ini))
# end READDATAFILE

if __name__ == "__main__":
    nums = []
    ORDERDATAFILE(nums)
