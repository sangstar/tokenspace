import numpy as np
from svd import svd
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/pythia-70m")
model = AutoModel.from_pretrained("EleutherAI/pythia-70m")



embedding_matrix = model.get_input_embeddings().weight

embedding_array = np.ascontiguousarray(embedding_matrix.detach().numpy())

flat_list = embedding_array.flatten().tolist()
data = svd.go.Slice_float64(flat_list)

rows, cols = embedding_array.shape

output_dim = 2

result = svd.Compress(data, rows, cols, output_dim)


numpy_array = np.array(result).reshape(rows, output_dim)

print(numpy_array)
