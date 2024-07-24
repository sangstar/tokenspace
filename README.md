# wordspace
Visualize word2vec embeddings in a terminal window.

```
Enter text (exit! to escape): football
                     
             (sports)        
     (game)                
                     
             (soccer) (nba)  (tennis)     
              (basketball)       
        (games)             
         (season)   (winning)   (baseball)  (championship)    
              (hockey)      (boxing) 
                     
          ┼  (player)  (race) (teams)      
               (rugby)      
                     
                     
          (league)           
                     
                     
              (players)       
                     
                     
             (olympics)    
```

This package reduces word2vec vectors (loaded from Gensim)
to two dimensions by getting the singular value decomposition
of the embeddings matrix and approximating the matrix using 
its first two left singular vectors along with its values. If
the first two singular values are not much larger than the other
singular values, then the 2D approximation will be less reliable. Due
to this, the words mapped in the TUI use a custom score that
rewards high cosine similarity with the chosen word _before_
dimensionality reduction, and words that don't have their
performances (defined by closeness to the central word) greatly
affected after reduction. 

Experimentally, the performance before reduction has been the most
important metric for generating quality close words after
reduction, and the affect of performance drift is made tuneable
and recommended to be kept small.

### Installation
To run, make sure Python and Go runtimes are installed on your machine. Then, install
the package from source.

```bash
git clone https://github.com/sangstar/wordspace.git
cd wordspace
pip install -r requirements.txt
python -m wordspace -n 20 -x 10 -y 10 -a 0.05
```

Once entering the first word to visualize embeddings for, they
can be regenerated for any new word by inputting it in the terminal.

The available CLI args are:

```bash
Compress and visualize word embeddings using SVD.

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL         The name of the Gensim model to load.
  --output_dim OUTPUT_DIM
                        The output dimension for SVD compression.
  -n N, --n N           The number of most similar words to display
  -x X_WINDOW_SIZE, --x-window-size X_WINDOW_SIZE
                        The x window size for the TUI
  -y Y_WINDOW_SIZE, --y-window-size Y_WINDOW_SIZE
                        The y window size for the TUI
  -w NUM_WORKERS, --num-workers NUM_WORKERS
                        The number of workers to use
  -a ALPHA, --alpha ALPHA
                        A scalar to influence the impact of words thatdon't change much in terms of cosine similarity with the central word before and after singular
                        value decomposition. Usually best to keep the value very low.

```

