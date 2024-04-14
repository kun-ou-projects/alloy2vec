import numpy as np
import gensim
from gensim.models import Word2Vec
import os
from scipy.ndimage import gaussian_filter

def get_normalized_vectors(model):
    vectors = model.wv.vectors
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    normalized_vectors = vectors / norms
    return normalized_vectors

def get_common_vocab(model1, model2):
    vocab_model1 = set(model1.wv.vocab.keys())
    vocab_model2 = set(model2.wv.vocab.keys())
    return vocab_model1.intersection(vocab_model2)

def procrustes_align_base_to_others(base_model_path, other_models_dir, output_dir, words=None, sigma=1):
    base_model = Word2Vec.load(base_model_path)
    
    other_models_paths = [os.path.join(other_models_dir, f) for f in os.listdir(other_models_dir) if '.' not in f]
       
    for path in other_models_paths:
        other_model = Word2Vec.load(path)
        if words is None:
            common_vocab = get_common_vocab(base_model, other_model)
        else:
            common_vocab = set(words).intersection(set(base_model.wv.vocab.keys()), set(other_model.wv.vocab.keys()))
            
        if not common_vocab:
            print(f"No common vocabulary between base model and {path}. Skipping alignment.")
            continue
        else:
            print(f"Common vocab size: {len(common_vocab)}")
        
        base_vectors = np.array([base_model.wv[word] for word in common_vocab])
        other_vectors = np.array([other_model.wv[word] for word in common_vocab])
        
        m = other_vectors.T.dot(base_vectors)
        u, _, v = np.linalg.svd(m, full_matrices=False)
        ortho = u.dot(v)
        
        transformed_vectors = other_model.wv.vectors.dot(ortho)
        normalized_transformed_vectors = transformed_vectors / np.linalg.norm(transformed_vectors, axis=1, keepdims=True)
        other_model.wv.vectors[:] = normalized_transformed_vectors
        
        original_filename = os.path.basename(path)
        aligned_model_filename = f"aligned_{original_filename}"
        aligned_model_path = os.path.join(output_dir, aligned_model_filename)
        other_model.save(aligned_model_path) 
        print(f"Aligned model saved to {aligned_model_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Procrustes align a base Word2Vec model to other models.")
    parser.add_argument("base_model", help="Path to the base model file")
    parser.add_argument("other_models_dir", help="Path to the directory containing other Word2Vec model files")
    parser.add_argument("--words", help="Optional path to a file containing words to align. One word per line.")
    parser.add_argument("--output", default="aligned_base_model", help="Output path for the aligned base model")
    
    args = parser.parse_args()
    
    if args.words:
        with open(args.words, 'r') as f:
            words = f.read().splitlines()
        procrustes_align_base_to_others(args.base_model, args.other_models_dir, args.output, words=words)
    else:
        procrustes_align_base_to_others(args.base_model, args.other_models_dir, args.output)