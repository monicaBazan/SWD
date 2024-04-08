from Bio import SeqIO
import sys
import os

#Check if filename is provided as a command-line argument
if len(sys.argv) != 2:
    print("Error: Please provide a filename as a command-line argument.")
else:   
    # Get the filename from the command-line argument
    filename = sys.argv[1]
    
    if os.path.exists(filename): 
        input_file = open(filename, 'r')
        #read the FASTA file
        for cur_record in SeqIO.parse(input_file, "fasta") :
            gene_name = cur_record.name
            #count the number of appearances of C & G
            C_count = cur_record.seq.upper().count('C')
            G_count = cur_record.seq.upper().count('G')
            length = len(cur_record.seq)
            cg_percentage = float(C_count + G_count) / length 
            
        #print gene name
        print(gene_name)
        #print the percentage
        print(cg_percentage) 
        #close the file after
        input_file.close()
    else:
         print("Error: The filename does not exist. Please provide a valid filename.")      
