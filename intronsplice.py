#!/bin/python3

# Getting sequence, setting variables
my_dna = open("DNA_file").read()
coding_dna = ''

# Tidying input
my_dna = my_dna.replace('\n', '')

# Splicing
coding_dna = coding_dna + my_dna[0:63] + my_dna[90:]

# Finding rounded percentage coding
perc_coding = round((len(coding_dna)/len(my_dna)*100))

# Outputs
print("The spliced coding sequence is: " + coding_dna)
print("The percentage of the sequence that is coding is: " + str(perc_coding) + "%")
