# Studied DeepWalk 

## :dizzy: Summary 
### DeepWalk Definition
**Deep walk** is a graph embedding method that uses method called 
'Random Walk' to make node sequence and use it on 
logics of language model to express the node in vector type.

### DeepWalk’s contribution
- learns the graph structure with **short random walks.**
- it’s representation outperform its competitors even with **less labeled data.**
- is **parallelizable** and can represent large web-scale graphs

### Input and Output
**Input:** *Graph = (V, E, X, Y) and HyperParameters (window size, embedding size ..)* 

**Output:**  *Φ: 𝑣 ∈ 𝑉→𝑅^(|V|*d)*

### Hierarchical Softmax 
- a multi-layer binary tree where the probability of a word is calculated on whether it goes to left or right edge 
- used in skip-gram to reduce time and computational cost -> from O(n) to O(log n) 
- can use Huffman coding to consider frequently accessed elements 

## :telescope: Experiments 
### Dataset info
- Datasets are BlogCatalog, Flickr, YouTube 
- Even with less labeld nodes(1~20%), DeepWalk performed well 

### Experiment on parameters 
- More training data, better performance 
- dimension should be at least 8 and dimension with 64, 128 are most efficient 
- In Flickr and BlogCatalog dataset, when gamma was 30, it had the most efficient performance 
- There seemed to be not much difference in performance between dimension sizes 
- The bigger gamma value, the better but quickly slows down when gamma is over 10

## :trackball: Coding implementation Tips
- Can use umap library(pip install umap-learn) to reduce dimension for visualization (128 -> 2 or 3d)
- basic coding implementation with karate graph is ipynb ver 1
- visualization is mostly in ipynb ver 2 and 3 
- kaggle dataset experiment is in ipynb ver 4
