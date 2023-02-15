## Studied DGI 

### Reference : 

[https://medium.com/stellargraph/do-i-know-you-flexible-unsupervised-and-semi-supervised-graph-models-with-deep-graph-infomax-96fbfd63ec31](https://medium.com/stellargraph/do-i-know-you-flexible-unsupervised-and-semi-supervised-graph-models-with-deep-graph-infomax-96fbfd63ec31)

[https://stellargraph.readthedocs.io/en/stable/demos/embeddings/deep-graph-infomax-embeddings.html](https://stellargraph.readthedocs.io/en/stable/demos/embeddings/deep-graph-infomax-embeddings.html)

2018년 논문

### Introduction 
graph로 neural network를 만드는 것은 매우 도전적인 태스크 중 하나다. 
지금까지는 graph convolutional network가 가장 유명하고, 이는 supervised learning이다. 
하지만 현실의 많은 그래프는 unlabeled이고, 가끔 큰 그래프에서 새로운 구조를 발견하는 것도 중요하므로, unsupervised graph learning이 필요하다. 

최근에 가장 유명한 unsupervised representation learning in graph는 random walk 기반 접근들이었고, 

> Node2Vec, DeepWalk, Line: Largescale information network embedding., Inductive representation learning on large graphs.

가끔 adjacency information을 다시 재건설하여 간단하게 만들기도 했다. 

> GVAE, Learning graph representations with embedding propagation

이런 encoder network들의 전제는 가까운 node들은 representation space에서도 가깝게 위치해야 한다는 것이다.

Random Walk는 다음과 같은 한계가 있다. 

- over emphasize proximity information at the expense of structural info
    - struc2vec: Learning node representations from structural identity.
- performance is highly dependent on hyperparameter choice
    - Node2vec, deepwalk
- introduction of stronger encoder models based on graph convolutions
    - Neural message passing for quantum chemistry

본 논문에서는 mutual information을 사용하는 unsupervised graph learning을 소개한다. 

mutual information은 Mutual Information Neural Estimation(MINE,2018) 논문으로 하여금 사용할 수 있게 되었다.

Hjelm은 고차원의 데이터의 임베딩을 학습하는 DIM이라는 모델을 소개했다. 
DIM은 encoder model로 하여금 이미지 전체와 지엽적 부분을 동시에 학습하게 하였다. 
하지만 DIM은 image data의 CNN구조에 의존하고 있고, 아직 graph에 mutual information maximiazation을 적용한 논문은 없는 걸로 안다. 
따라서 우리는 DIM을 그래프 도메인에 적용해보았다. 

Deep graph infomax는 transductive와 inductive 분류 태스크에서 모두 성능이 준수했고 가끔 supervise baseline마저 넘는 등 좋은 성과를 보였다.


### Overall Procedure of DGI

![image](https://user-images.githubusercontent.com/68208055/219012621-2cd7a1f9-470d-4bff-a0fc-f3f943ba4cd0.png)


Assuming the single-graph setup (i.e., (X, A) provided as input), we will now summarize the steps of the Deep Graph Infomax procedure:

1. Sample a negative example by using corruption function C 
    1. a original set is (X, A) and corrupted set is (~X, ~A)
2. Obtain patch representation for the input graph by passing it through the encoder 
    1. path representation is hi 
    2. H is the set of  { h1,h2,… hi,.. hn }
    3. the encoder is marked as E(X, A)
3. Repeat 2 for the corrupted set 
    1. path representation is ~hi 
    2. ~H is the set of { ~h1, ~h2,…  ~hi,.. ~hn }
    3. use the same encoder E(~X, ~A)
4. Summarize the input graph through the ‘readout function’ 
    1. readout function is R(H)
    2. the summary is s 
5. update the parameter of E, R, D by applying gradient descent to maximize Equation 1

