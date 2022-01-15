#GiG

import numpy as np
import pandas as pd
from pathlib import Path

from deep_blocker import DeepBlocker
from tuple_embedding_models import  AutoEncoderTupleEmbedding, CTTTupleEmbedding, HybridTupleEmbedding, SIFEmbedding, CTTCosineTupleEmbedding,TripletTupleEmbedding
from vector_pairing_models import ExactTopKVectorPairing
import blocking_utils

def do_blocking(folder_root, left_table_fname, right_table_fname, cols_to_block, tuple_embedding_model, vector_pairing_model):
    folder_root = Path(folder_root)
    left_df = pd.read_csv(folder_root / left_table_fname)
    right_df = pd.read_csv(folder_root / right_table_fname)

    db = DeepBlocker(tuple_embedding_model, vector_pairing_model)
    candidate_set_df = db.block_datasets(left_df, right_df, cols_to_block)
    
    ## matches.csv can be generated by calling preprocess_files in the blocking_utils.py file. Check the function for more details
    golden_df = pd.read_csv(Path(folder_root) /  "matches1.csv")
    statistics_dict = blocking_utils.compute_blocking_statistics(candidate_set_df, golden_df, left_df, right_df)
    return statistics_dict

if __name__ == "__main__":

    folder_root = "data/Structured/DBLP-ACM" # Path of folder containing data
    left_table_fname, right_table_fname = "tableA.csv", "tableB.csv" #Table names
    cols_to_block = ["id","title","authors","venue","year"] # Columns to be blocked in the above tables

    embedding_functions = {"SIF" : SIFEmbedding,
                            "Autoencoder" : AutoEncoderTupleEmbedding,
                            "CTT" : CTTTupleEmbedding,
                            "CTTCosine" : CTTCosineTupleEmbedding,
                            "Hybrid" : HybridTupleEmbedding,
                            "SBERT" : TripletTupleEmbedding}

    
    embedding_func = "Autoencoder"
    tuple_embedding_model = embedding_functions[embedding_func]()
    topK_vector_pairing_model = ExactTopKVectorPairing(K=5)
    print(f'using {embedding_func} embedding')
    statistics_dict = do_blocking(folder_root, left_table_fname, right_table_fname, cols_to_block, tuple_embedding_model, topK_vector_pairing_model)
    print(statistics_dict)
