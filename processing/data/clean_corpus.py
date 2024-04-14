import os, re, sys

bad_chars = [',', ';', ':', '!', '.', '(', ')', '"', "*"] 

input_file_path = "data/extracted_all.txt"
output_file_path = "data/cleaned_all.txt"

os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

with open(output_file_path, 'a+') as corpus_w:
    with open(input_file_path, "r") as corpus:
        data = corpus.readlines()
        for line in data:
            for ii in bad_chars: 
                line = line.replace(ii, '') 
            corpus_w.write(line + '\n')
