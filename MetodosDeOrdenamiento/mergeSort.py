#! /usr/bin/python2.7.8
# -*- coding: utf-8 -*-

# Python program for implementation of MergeSort
import argparse
from math import floor
from time import clock

def MERGE(A,p,q,r):
	n1 = q-p
	n2 = r-q-1
	L = []
	R = []

	for i in range(1,n1+2):
		L.insert(i-1,A[p+i-1])
	for j in range(1,n2+2):
		R.insert(j-1,A[q+j])

	L.insert(n1+1,1e400)
	R.insert(n2+1,1e400)

	i = 0
	j = 0

	for k in range (p,r+1):
		if L[i]<= R[j]:
			A[k] = L[i]
			i = i+1
		else:
			A[k] = R[j]
			j = j+1
	#print A
#END MERGE

def MERGESORT(A,p,r):
	if p<r:
		q = int(floor((p+r)/2))
		MERGESORT(A,p,q)
		MERGESORT(A,q+1,r)
		MERGE(A,p,q,r)
#END MERGESORT

def ORDERDATAFILE(nums):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
    args = parser.parse_args()

    with open(args.file) as file:
        data = file.read()
        for word in data.split():
            nums.append(int(word))

    t_ini = clock()
    MERGESORT(nums,0,len(nums)-1)
    t_fin = clock()
    #print nums
    
    if args.file:
        print (args.file, (t_fin - t_ini))
# end READDATAFILE

if __name__ == "__main__":
    nums = []
    ORDERDATAFILE(nums)
