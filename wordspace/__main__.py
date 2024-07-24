import argparse
import gensim.models
import numpy as np
from tui import tui
import gensim.downloader as api


def main(model_name: str,
         output_dim: int,
         n: int,
         windowsize_x: int,
         windowsize_y: int,
         numworkers: int,
         alpha: float
         ):
    model = api.load(model_name)
    embedding_matrix = model.vectors

    embedding_array = np.ascontiguousarray(embedding_matrix)
    flat_list = embedding_array.flatten().tolist()
    data = tui.go.Slice_float64(flat_list)

    rows, cols = embedding_array.shape

    tui.CompressAndVisualize(n, windowsize_x, windowsize_y, numworkers, alpha, data, rows, cols, output_dim,
                             tui.go.Slice_string(model.index_to_key))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress and visualize word embeddings using SVD.")
    parser.add_argument("--model", type=str, default="glove-twitter-25", help="The name of the Gensim model to load.")
    parser.add_argument("--output_dim", type=int, default=2, help="The output dimension for SVD compression.")
    parser.add_argument("-n", "--n", type=int, default=20, help="The number of most similar words to display")
    parser.add_argument("-x", "--x-window-size", type=int, default=10, help="The x window size for the TUI")
    parser.add_argument("-y", "--y-window-size", type=int, default=10, help="The y window size for the TUI")
    parser.add_argument("-w", "--num-workers", type=int, default=10, help="The number of workers to use")
    parser.add_argument("-a", "--alpha", type=float, default=0.05, help="A scalar to influence the "
                                                                        "impact of words that don't change "
                                                                        "much in terms of cosine similarity "
                                                                        "with the central word before and "
                                                                        "after singular value decomposition. "
                                                                        "Usually best to keep the value very low.")

    args = parser.parse_args()
    main(args.model, args.output_dim, args.n, args.x_window_size, args.y_window_size, args.num_workers, args.alpha)
