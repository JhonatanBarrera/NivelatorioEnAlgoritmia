#! /usr/bin/python2.7.8
# -*- coding: utf-8 -*-

# Python program for implementation of InsertionSort
import argparse
from math import floor
from time import clock

def INSERTIONSORT(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while i>=0 and A[i]>key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
	#print(A) # Sorted list.
# end INSERTIONSORT

def ORDERDATAFILE(nums):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
    args = parser.parse_args()

    with open(args.file) as file:
        data = file.read()
        for word in data.split():
            nums.append(int(word))

    t_ini = clock()
    INSERTIONSORT(nums)
    t_fin = clock()
    
    if args.file:
        print (args.file, (t_fin - t_ini))
# end READDATAFILE

if __name__ == "__main__":
    nums = []
    ORDERDATAFILE(nums)
