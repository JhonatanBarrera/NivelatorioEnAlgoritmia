import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Nombre del archivo a procesar.")
parser.add_argument("-l", "--length", help="Cantidad de elementos.")
parser.add_argument("-u", "--units", help="Longitud por elemento.")
args = parser.parse_args()

with open(args.file, 'a') as file:
    for i in range(0,int(args.length)):
        n = random.randint(1, 9)
        file.write(str(n))
        for i in range(1,int(args.units)):
            n = random.randint(0, 9)
            file.write(str(n))
        file.write(' ')
