#! /usr/bin/python2.7.8
# -*- coding: utf-8 -*-

# Python program for implementation of Counting Sort
import argparse
from math import floor
from time import clock

def COUNTINGSORT(alist):
    length = len(alist)
    if not length: return
    if min(alist) < 0: raise ValueError('integer values must be >= 0')
    counts = [0] * (max(alist)+1)
    for val in alist: counts[val] += 1
    for i in range(1, len(counts)): counts[i] += counts[i-1]
    results = [0] * length
    for i in range(length-1, -1, -1):
        val = alist[i]
        counts[val] -= 1
        results[ counts[val] ] = val
    alist[:] = results
    #print(results)

def ORDERDATAFILE(nums):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
    args = parser.parse_args()

    with open(args.file) as file:
        data = file.read()
        for word in data.split():
            nums.append(int(word))

    t_ini = clock()
    COUNTINGSORT(nums)
    t_fin = clock()
    
    if args.file:
        print(args.file, (t_fin - t_ini))
# end READDATAFILE

if __name__ == "__main__":
    nums = []
    ORDERDATAFILE(nums)
