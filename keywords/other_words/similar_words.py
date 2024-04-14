import sys
import os
from gensim.models import Word2Vec

# Add the project directory to the system path
sys.path.append('/home/etica/Project/alloy2vec')

model_path = "/home/etica/Project/alloy2vec/alloy2vec/training/models/1model_with_wx_process_parallel_all"

file_paths = [
    
    "/home/etica/Project/alloy2vec/keywords/new_keyword/alloy.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/mechanical_properties.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_general.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_melt_ded.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_melt_general.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_melt_pbf.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_solid_binder.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_solid_cold_spray.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_solid_extrusion.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_solid_field_assisted.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_solid_friction_based.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/process_solid_general.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/thermal_properties.txt",
    "/home/etica/Project/alloy2vec/keywords/new_keyword/AA_family_all.txt",
]
    
def find_similar_words(model, word):
    """Find and return similar words for a given word using the provided model."""
    try:
        return model.wv.most_similar(word, topn=5)
    except KeyError:
        return []

def process_files(model_path, file_paths):
    """Process each file to find similar words for each keyword and write to a new file."""
    model = Word2Vec.load(model_path)
    
    for file_path in file_paths:
        similar_words = []
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                if words:
                    first_word = words[0]
                    similar = find_similar_words(model, first_word) + find_similar_words(model, first_word.lower())
                    similar_words.extend([word for word, _ in similar])

        # Determine the new file path
        file_name = "similar_" + os.path.basename(file_path)
        new_file_path = os.path.join('/home/etica/Project/alloy2vec/keywords/new_keyword/other_words', file_name)
        
        # Write the similar words to the new file
        with open(new_file_path, 'w') as new_file:
            for word in set(similar_words):  # Use `set` to remove duplicates
                new_file.write(f'{word}\n')

# Execute the processing
process_files(model_path, file_paths)