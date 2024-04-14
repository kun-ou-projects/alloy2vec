import sys
import os
from concurrent.futures import ProcessPoolExecutor
from alloy2vec.processing import process

mtp = process.MaterialsTextProcessor()

def process_file(file_path):
    processed_sentences = []
    with open(file_path, 'r', encoding="utf-8") as reader:
        for line in reader:
            try:
                columns = line.strip().split('\t')
                combined_line = ' '.join(columns)

                processed = mtp.process(combined_line, normalize_materials=True, convert_num=True, exclude_punct=True, make_phrases=True)
                processed_sentences.append(processed[0])
            except Exception as e:
                print(f"Error processing line: {line} - {e}")
    return processed_sentences


def get_sentences(path):
    sentences = []
    temp_folder = "training/tmp_data"
    os.makedirs(temp_folder, exist_ok=True)

    total_lines = sum(1 for _ in open(path, 'r', encoding="utf-8"))
    lines_per_file = (total_lines + 79) // 80

    split_command = f"split -l {lines_per_file} {path} {temp_folder}temp_"
    os.system(split_command)

    files_to_process = [os.path.join(temp_folder, f) for f in os.listdir(temp_folder) if f.startswith("temp_")]

    with ProcessPoolExecutor() as executor:
        results = executor.map(process_file, files_to_process)

    for result in results:
        sentences.extend(result)

    # Clean up temporary files
    for temp_file_path in files_to_process:
        os.remove(temp_file_path)

    return sentences
    
def save_sentences(sentences, output_path):
    with open(output_path, 'w', encoding="utf-8") as file:
        for sentence in sentences:
            file.write(' '.join(sentence) + '\n')

if __name__ == "__main__":
    path = "..."
    sentences = get_sentences(path)
    output_path = "..."
    save_sentences(sentences, output_path)
