from Bio import SeqIO
import streamlit as st

#title in Streamlit app
st.title("GC Content Calculator")

st.write('Upload a sequence in fasta format')

#Field for user to enter the sequence
user_input = st.text_area("Enter sequence:", max_chars=None)

# Calculate button
if st.button("Calculate"):
    # Check if the input is not empty
    if user_input:
        # Process the content of the text field
        #count the number of appearances of C & G
        C_count = user_input.count('C')
        G_count = user_input.count('G')
        length = len(user_input)
        cg_percentage = float(C_count + G_count) / length 
        #print percentage
        st.write(cg_percentage) 
       
    else:
        #if press calculate but field is empty
        st.write("Please enter the fasta sequence before calculating.")

uploaded_file = st.file_uploader("Choose a file", type=["fasta"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the content of the file
    input_file = open(uploaded_file.name, 'r')
    #get the name and details fron the first line
   # gene_details = input_file.readline()
    for cur_record in SeqIO.parse(input_file, "fasta") :
         gene_name = cur_record.name
       
         C_count = cur_record.seq.upper().count('C')
         G_count = cur_record.seq.upper().count('G')
         length = len(cur_record.seq)
         cg_percentage = float(C_count + G_count) / length 
         
 #   st.write(gene_details)     
    st.write(cg_percentage) 
    input_file.close()    




