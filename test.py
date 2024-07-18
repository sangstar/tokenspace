import numpy as np
from svd import svd

# Convert Python list to Slice_Slice_float64
data = svd.go.Slice_float64([1, 2, 3, 4, 5, 6])

rows = 2
cols = 3

output_dim = 2

# Call the Compress function with the converted data
result = svd.Compress(data, rows, cols, output_dim)

# Extract the data from the result

# Convert the extracted data to a NumPy array
numpy_array = np.array(data).reshape(rows, cols)

print(numpy_array)
