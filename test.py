import gensim.models
import numpy as np
from svd import svd
import typing
from typing import List, Tuple, Any
from gensim.models import KeyedVectors
import gensim.downloader as api
from tui import go
from tui import tui


model = api.load("glove-twitter-25")  # load glove vectors
embedding_matrix = model.vectors

embedding_array = np.ascontiguousarray(embedding_matrix)

flat_list = embedding_array.flatten().tolist()
data = svd.go.Slice_float64(flat_list)

rows, cols = embedding_array.shape

output_dim = 2

result = tui.CompressAndVisualize(data, rows, cols, output_dim, model.index_to_key)


# TODO: Send the compressed and original vectors to the TUI. Create a score
#       that incentivizes a low (close to 1) compressed rank (ranking similarity
#       to chosen word) and incentivizes as little change in rank as possible
#       from original vectors and compressed. That's to say, if a vector was
#       the most similar word to the chosen, and was still the most similar before compression,
#       that's the best possible score.

# TODO: Pass `result` to `tui.Visualize` and do the parsing on the Go
#       side. That way if I want to center on a new word I don't have to
#       re-run the python script. `result` has all the data I need.
#       Will be necessary for the TUI.

