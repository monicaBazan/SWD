from Bio import SeqIO

import sys
import os


    # Check if filename is provided as a command-line argument
if len(sys.argv) != 2:
    print("Error: Please provide a filename as a command-line argument.")
    print("Usage: python program.py <filename>")
    sys.exit(1)
    
    # Get the filename from the command-line argument
filename = sys.argv[1]
print("filename :", filename)
if os.path.exists(filename): 

    input_file = open(filename, 'r')


    for cur_record in SeqIO.parse(input_file, "fasta") :
         #count nucleotides in this record...
         gene_name = cur_record.name
       
         C_count = cur_record.seq.upper().count('C')
         G_count = cur_record.seq.upper().count('G')
         length = len(cur_record.seq)
         cg_percentage = float(C_count + G_count) / length 
         
         
    print(cg_percentage) 
    input_file.close()    