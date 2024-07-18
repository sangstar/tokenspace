import gensim.models
import numpy as np
from svd import svd
import typing
from typing import List, Tuple, Any
from gensim.models import KeyedVectors

import gensim.downloader as api


def cos_sim(a: np.array, b: np.array) -> float:
    return (a.dot(b)) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_top_n(token: str, n: int, compressed: np.array, model: gensim.models.KeyedVectors) -> list[Any]:
    row_id = model.key_to_index[token]
    central_vec = compressed[row_id]
    most_sim = model.most_similar(token, topn=n)
    cols_of_top_n = [model.key_to_index[tok[0]] for tok in most_sim]
    return list(zip(most_sim, compressed[cols_of_top_n]))


model = api.load("glove-twitter-25")  # load glove vectors
model.most_similar("cat")
model.vectors
embedding_matrix = model.vectors

embedding_array = np.ascontiguousarray(embedding_matrix)

flat_list = embedding_array.flatten().tolist()
data = svd.go.Slice_float64(flat_list)

rows, cols = embedding_array.shape

output_dim = 2

result = svd.Compress(data, rows, cols, output_dim)

numpy_array = np.array(result).reshape(rows, output_dim)

print(numpy_array)

top = get_top_n("hello", 20, numpy_array, model)

print(top)
## TODO: Now, just need to pick a token, and see which ones are most similar using cos_sim
##       dear god please make sense
##       eventually, the TUI will have a central word, the top 10 (or however many) words will appear
##       their exact positions will be their 2D (thanks to SVD) positions relative to the central word
##       which means gotta find the translation for the word to (0,0) and apply to all top N words
