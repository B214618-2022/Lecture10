#!/bin/python3

# Getting sequence, setting variables
my_dna = open("DNA_file.txt").read()
my_dna = my_dna.replace('\n', '')
coding_dna = ''
intron = my_dna[63:90]
exon_1 = my_dna[0:63]
exon_2 = my_dna[90:]

# Splicing
coding_dna = exon_1 + exon_2

# Finding rounded percentage coding
perc_coding = round((len(coding_dna)/len(my_dna)*100))

# Outputs
print("\n\nThe spliced coding sequence is: \n" + coding_dna + '\n\n')
print("The percentage of the sequence that is coding is: \n" + str(perc_coding) + "% \n\n")
print("Full sequence with coding regions highlighted: \n" + exon_1 + intron.lower() + exon_2 + '\n\n')
