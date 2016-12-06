#! /usr/bin/python2.7.8
# -*- coding: utf-8 -*-

# Python program for implementation of Selection Sort
import argparse
from math import floor
from time import clock

def SELECTIONSORT(V):
	j = 0
	while j != len(V):
		for i in range(j, len(V)):
			if V[i] < V[j]:
				V[j],V[i] = V[i],V[j]
		j = j+1                        
	#print V
#END SELECTIONSORT

def ORDERDATAFILE(nums):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
    args = parser.parse_args()

    with open(args.file) as file:
        data = file.read()
        for word in data.split():
            nums.append(int(word))

    t_ini = clock()
    SELECTIONSORT(nums)
    t_fin = clock()

    if args.file:
        print(args.file, (t_fin - t_ini))
# end READDATAFILE

if __name__ == "__main__":
    nums = []
    ORDERDATAFILE(nums)
