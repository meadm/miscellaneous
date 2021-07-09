#!/bin/python
#this script will print only the A. fumigatus virulence-associated genes of interest from a PHI-base database that is in csv format

#usage: python parse_phi-base.py -f [PHI-base file in csv format with NO headers]

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='Print only the A. fumigatus virulence-associated genes of interest from a PHI-base database that is in csv format')
#add an argument that is the DupliPHY summary file. can use either "-f" or "--file"
parser.add_argument("-f","--file",help="PHI-base file in csv format")

#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists
with open(args.file) as mainfilehandle:
    #this will leave commas in quotes alone
        #ex. the commas in "Both myoB and myoE are necessary for proper septation, conidiation, and conidial germination, but only myoB is required for conidial viability." are ignored when separating the values
    reader = csv.reader(mainfilehandle, quotechar='"', delimiter=',')
    l = list(reader)

#if the "Pathogen species" is "A. fumigatus" and "Mutant phenotype" is not "unaffected pathogenicity" OR "chemistry target: resistance to chemical ", print the list as a tab-separated line
for i in l:
    if i[19] == 'Aspergillus fumigatus' and i[34] != 'unaffected pathogenicity' and i[34] != 'chemistry target: resistance to chemical ':
        print(*i, sep='\t')
