
input_file_path = 'data/original_all.txt'

processed_data = []

with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        columns = line.split('\t')
        if len(columns) >= 34:
            title = columns[9]  
            abstract = columns[33]  
            combined_text = title + ". " + abstract
        elif len(columns) >= 10:
            combined_text = columns[9] 
        else:
            continue  
        processed_data.append(combined_text)

output_file_path = 'data/extracted_text.txt'


with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for item in processed_data:
        output_file.write(item + '\n')
