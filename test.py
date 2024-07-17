from svd import svd

# Convert Python list to Slice_Slice_float64
stacked_list = svd.Slice_Slice_float64([
    svd.go.Slice_float64([1, 2, 3]),
    svd.go.Slice_float64([4, 5, 6])
])

output_dim = 2

# Call the Compress function with the converted data
result = svd.Compress(stacked_list, output_dim)

print(result)
