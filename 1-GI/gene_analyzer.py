import pandas as pd
import sys
import os

#Check if filename is provided as a command-line argument
if len(sys.argv) != 2:
    print("Error: Please provide a filename as a command-line argument.")

else:    
    #Get the filename from the command-line argument
    filename = sys.argv[1]
    if os.path.exists(filename):   
        #this list will store the chunks in dataframes for later concatenation 
        df_list = [] 
        #read the gzip file, we only read the necessary cols 
        for df_chunk in pd.read_csv(filename, compression='gzip',header=0, sep='\t', low_memory=False, usecols= ['#tax_id', 'type_of_gene'], chunksize=10000):
            df_list.append(df_chunk) 
        #And finally combine filtered df_lst into the final lareger output say 'df_final' dataframe 
        df_final = pd.concat(df_list, ignore_index=True)

        #Calculate the number of genes
        num_genes = len (df_final)   
        print ("Answer question 1:", num_genes)
        
        #Calculate how many homo sapiens, '9606'
        count_HS = len(df_final[df_final['#tax_id'] == 9606])
        print("Answer question 2:", count_HS)

        # Obtain a list of unique gene IDs to get all the gene types
        unique_gene_ids = df_final['type_of_gene'].unique()
        print("Answer question 3:", unique_gene_ids.tolist())
        
        #Show which gene occurs the most
        id_counts = df_final['type_of_gene'].value_counts()
        # Find the IDs that appear the most times
        most_common_ids = id_counts.idxmax()
        print("Answer question 4:", most_common_ids)

    else:
         print("Error: The filename does not exist. Please provide a valid filename.")  