import gensim.models
import numpy as np
from svd import svd
import typing
from typing import List, Tuple, Any
from gensim.models import KeyedVectors
import gensim.downloader as api
from tui import go
from tui import tui

def cos_sim(a: np.ndarray, b: np.ndarray) -> float:
    return (a.dot(b)) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_top_n(token: str, n: int, compressed: np.ndarray, gensim_model: gensim.models.KeyedVectors) \
        -> Tuple[str, List[float], List[str], List[float], List[List[float]]]:

    row_id = gensim_model.key_to_index[token]
    central_vec = compressed[row_id].tolist()
    most_sim = gensim_model.most_similar(token, topn=n)
    cols_of_top_n = [gensim_model.key_to_index[tok[0]] for tok in most_sim]
    vecs_of_top_n = np.array([compressed[row_id].tolist() for row_id in cols_of_top_n]).flatten().tolist()
    return (
        token,
        central_vec,
        [tok[0] for tok in most_sim],
        [tok[1] for tok in most_sim],
        vecs_of_top_n
    )


model = api.load("glove-twitter-25")  # load glove vectors
embedding_matrix = model.vectors

embedding_array = np.ascontiguousarray(embedding_matrix)

flat_list = embedding_array.flatten().tolist()
data = svd.go.Slice_float64(flat_list)

rows, cols = embedding_array.shape

output_dim = 2

result = svd.Compress(data, rows, cols, output_dim)

numpy_array = np.array(result).reshape(rows, output_dim)


top = get_top_n("tennis", 100, numpy_array, model)


# TODO: Pass `result` to `tui.Visualize` and do the parsing on the Go
#       side. That way if I want to center on a new word I don't have to
#       re-run the python script. `result` has all the data I need.
#       Will be necessary for the TUI.

new_top = [
    top[0],
    go.Slice_float32(top[1]),
    go.Slice_string(top[2]),
    go.Slice_float32(top[3]),
    go.Slice_float32(top[4]),
]

tui.Visualize(*new_top)
