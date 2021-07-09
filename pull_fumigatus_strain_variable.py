#!/bin/python
#this script will print all orthogroups in a dupliPHY-ML file that have at least one gene present in every species but fumigatus and have a variable number of genes in the A. fumigatus strains.
#usage: pull_fumigatus_strain_variable.py -f [CSV file to parse]

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='print only those orthogroups whose gene contents varies across A. fumigatus but are present in all other species')
#add an argument that is the file to be parsed. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    l = list(reader)

#for every list in the list of lists...
for i in l:
    #for every entry in the line except for the first entry (the orthogroup number)...
    for j in range(1,19):
        #convert the numbers in the list to an integer
        i[j] = int(i[j])
    #if the gene is present in the first species...
    if i[1] > 0:
        #define a variable that will make sure the gene is present in the first set of non-fumigatus species
        first_check = True
        #loop through the first set of non-fumigatus species
        for j in range(3,6):
            #if any of the species in the first set do not have the gene, break the loop and change the checking variable
            if i[j] == 0:
                first_check = False
                break
        #define a variable that will check the second set of non-fumigatus species
        second_check = True
        #loop through the second set of non-fumigatus species
        for j in range(10,19):
            #if any of the species in the second set do not have the gene, break the loop and change the checking variable
            if i[j] == 0:
                second_check = False
                break
        #if the first and second checking variables are still true (the genes are in all non-fumigatus species) and the gene is present in at least one fumigatus strain...
        if second_check and first_check and not i[2] + i[6] + i[7] + i[8] + i[9] == 0:
            #if one or more of the fumigatus strains are missing the gene
            if i[2] == 0 or i[6] == 0 or i[7] == 0 or i[8] == 0 or i[9] == 0:
                print(i)
