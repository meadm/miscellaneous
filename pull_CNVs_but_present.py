#!/bin/python
#this script will print all orthogroups in a dupliPHY-ML file that have at least one gene presence in every species but the number of genes is not the same for every species/strain. ie copy number variants.
#usage: pull_CNVs_but_present.py -f [CSV file to parse]

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='print only those orthogroups whose gene contents varies across columns in the file but have at least one gene in every species')
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
    #set a checking variable to "present"
    presence_check = 'present'
    #for every entry in the list after the first one (aka for all the gene/presence absence numbers)...
    for j in range(1,19):
        #convert the numbers in the list to an integer
        i[j] = int(i[j])
        #if any of the numbers in the orthogroup are 0's (aka the gene is missing in that species)
        if i[j] == 0:
            #change the presence checking variable
            presence_check = 'NOTpresent'
            break
    #if the gene is present at least once in every species (ie the presence checking variable is still set to "present")
    if presence_check == 'present':
        #set a checking variable that says all the gene numbers are the same
        sameness_check = 'same'
        #for every gene number in the line/list
        for j in range(1,19):
            #skip the first entry (ie continue through the loop to the next number)
            if j == 1:
                continue
            #if the number isn't the first number and if the number you're on is different from the number before, set the sameness variable to "NOTsame"
            elif i[j] != i[j-1]:
                sameness_check="NOTsame"
        #if the sameness variable says there is some difference in the number of genes in the orthogroup in each species, print out that line
        if sameness_check == 'NOTsame':
            print(i)
