#!/bin/python3

my_dna = open("DNA_file").read()
my_dna = my_dna.replace('\n', '')
coding_dna = ''
coding_dna = coding_dna + my_dna[0:64]
print(coding_dna)
print(len(coding_dna))

print(my_dna)
