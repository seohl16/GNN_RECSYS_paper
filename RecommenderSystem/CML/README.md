# Studied CML 

## Abstract

Metric Learning은 데이터 간 관계를 잘 나타내도록 임베딩한 결과 사이 관계(거리)를 학습하는 알고리즘을 의미한다. 
본 논문에서 우리는 metric learning과 collaborative filtering 간의 연관성에 대해서 연구하였고, 그 결과 **Collaborative Metric Learning(CML)** 이 탄생했다. 
CML은 user의 선호도 (user-item) 뿐만 아니라 user-user, item-item 간의 유사도 역시 표현할 수 있는 metric space를 학습했다. 
CML은 기존 collaborative filtering 관련 sota 모델에서 성능을 뛰어넘었을 뿐만 아니라 
Top-K recommendation task에서 nearest-neighbor search with negligibale accuracy reduction을 사용해서 엄청난 시간 단축을 보였다. 

## 1. Introduction

**Metric Learning**

![image](https://user-images.githubusercontent.com/68208055/212266302-ee09d62b-9c26-4c9f-b02b-4a7e697d863f.png)

Distance는 KNN, Kmeans, SVM과 같은 많은 머신러닝 알고리즘에서 기초가 되는 개념이다. 
Metric learning algorithm은 데이터 간의 유사도를 잘 잡아 내는 distance metric을 생성한다. 
이는 이미지 분류, 문서 복원, 단백질 함수 예측 등 태스크에서 필수적인 알고리즘이 되었다. 

본 CML 논문에서는 metric learning이 collaborative filtering 문제에서 어떻게 적용되고, 여타 sota 모델들과 비교할 예정이다. 
Metric learning의 목표는 어떤 object pair가 similar한지 dissimilar한지를 잘 표현할 수 있는 distance metric을 만드는 것이다. 
특히 우리는 similar pair간에는 가까운 위치에, dissimilar pair 간에는 멀게 위치하도록 하고 싶다. 
예를 들어 face recognition에서 metric learning이 사용된다면 같은 사람의 사진은 가깝게, 
다른 사람들의 사진은 멀게 embedding되는 알고리즘을 학습하게 된다. 

**Triangle Inequality**

![image](https://user-images.githubusercontent.com/68208055/212269195-1c14205a-2324-40f7-baa7-7134f7c00e58.png)

수학적으로 metric은 여러 조건을 충족해야 하는데, 이 중 triangle inequality가 일반화할 때 가장 중요한 문제가 된다. 
Triangle inequality란 세 개의 object가 있을 때, 두 pairwise 거리의 합은 남은 하나의 거리보다 길어야 한다는 것이다. 
(삼각형 결정 조건 : 길이가 가장 긴 변의 길이는 다른 두 변 길이의 합보다 작아야 삼각형을 그릴 수 있다) 

> (x, z): d(y, z) ≤ d(x, y) + d(x, z).

이를 recommmender system에 적용해보면, x가 y랑 z와 가까워질 때 learned metric은 (x, y) (x, z)를 가깝게 만들 뿐만 아니라, (y,z)도 상대적으로 가까워질 가능성이 높아진다. 
이렇듯, 아직 우리가 정의하지 못한 (y,z)에도 x와의 각각의 관계를 보고 '유사하다'고 보며 영향을 주는 과정을 논문에서는 “similarity propagation” process라고 불렀다. learned metric가 주어진 다른 정보들로 모르는 정보까지 영향을 주게 되는 것이다. 

이 유사도 전파(similarity propagation)은 CF와 긴밀하게 연관되어 있다. 유사도 전파가 보지 못한 pair (y,z)에 영향을 주듯, 
Collaborative Filtering에서도 user과 item의 latent vector를 가지고 아직 보지 못한 user-item pair에도 일반화하려고 하기 때문이다. 
matrix factorization의 경우 user-item vector간의 내적 값으로 known rating을 학습하고, 그 결과로 얻은 vector간 내적으로 새로운 rating을 예측하기 때문이다. 

Matrix factorization과 metric learning은 개념적으로 유사하지만 완전 같지는 않다. 
왜냐하면 dot product는 매우 중요한 triangle inequality 정의를 성립하고 있지 않기 때문이다. 
Matrix factorization은 user의 general한 관심사(interest)를 학습할 수는 있어도, triangle inequality가 성립되지 않으면 선호 정보를 정확히 표현하지 못할 수도 있다. 
또한 기존 matrix factorization알고리즘들은 user-user과 item-item 간의 관계를 표현하는데 한계가 있었다. 

본 논문에서는 user 선호뿐만 아니라 user-user, item-item간의 유사도 역시 학습한 CML을 소개한다. 
우리는 implicit feedback dataset에 집중했고, CML은 다양한 추천 도메인에서 기존 SOTA 모델을 압도하는 성능을 보임을 보여줄 것이다. 
CML의 contribution은 user의 내재된 선호도 파악했다는 것이다. Flickr photographic dataset에서 user의 내재된 선호를 파악해 추천해주는 모습을 보였다. 
또한 CML은 image, text, tag 등 다양한 item feature를 복합적으로 파악했다. 
마지막으로 CML은 Top-K recommendation 태스크에서 매우 빠르면서도 정확한 성능을 보여주었다.

2장 생략 

## 3. Collaborative metric learning
최근 CF는 특정 유저가 이 아이템에 대해서 어떤 rating을 줄지 예측하는 것이 아니라 item들간의 상대적인 선호 차이를 알아내는 것을 목표로 삼고있다.
본 장에서는 CML이 이런 상대적인 관계를 어떻게 자연스럽게 알아낼 수 있는지 설명하려고 한다.

user-item pair S는 impliit feedback이 보였던 user-item 조합으로, positive feedback만 존재한다. 이를 활용해 비슷한 pair들은 가깝게 만들고, 상대적으로 다른 pair들은 멀리 떨어뜨리려고 한다. 이 과정에서 triangle inequality rule에 의해, 

같은 아이템을 좋아한 유저들
비슷한 유저가 좋아했던 아이템들
을 클러스터링하려고 한다.
이렇게 되면 어떤 유저가 등장하든간에,
그 유저가 직전에 좋아했던 아이템들과
비슷한 취향을 가진 유저가 좋아했던 아이템
들로 nearest neighbor item들이 나올 것이다.

우리는 user-item pair뿐만 아니라 user-user item-item 관계도 반영해서 성능을 더 올릴 수 있었다.

![image](https://user-images.githubusercontent.com/68208055/212313884-f0ab7cf9-f7d7-4c1e-b42f-4136076631c3.png)

CML은 위의 loss function을 가지고 있다. Lm, Lf, Lc 각각에 대해 차례대로 알아보겠다. 

### 3.1. Model formulation

첫번째 loss는 metric loss(Lm)다.

![image](https://user-images.githubusercontent.com/68208055/212313965-cd8d5b65-9f4a-4297-9523-c536b248f4cb.png)


우리 모델은 user과 item vector을 각각 u, v로 표현할 것이다. (같은 dimension에 존재)
그리고 이 vector을 distance 함수로 계산한다. 만약 j를 선호하고 k를 선호하지 않는다면 위의 식에서 d(i, j)는 d(i, k)보다 작아야 한다. 만약 차이가 크면 0이 되어서 loss가 0이 되고 반대면 값이 커져, 줄여야 하는 대상이 된다. 
m은 safety margin size다.
[x]+ 는 max(x, 0)이다.
w는 ranking loss weight다. 이는 3.2 에서 설명된다.

이 loss function은 LMNN과 유사하지만, 중요한 차이가 있다.

- L pull term이 없다. 왜냐하면 item은 많은 유저에게 좋아해질 수 있고 모든 유저에게 다 당겨지는 것이 현실적으로 가능하지 않기 때문이다. 하지만 push loss는 존재한다. push loss는 positive item을 유저에게 가깝게 만들기 때문이다.
- Top-K recommendation을 개선하기 위해 weighted ranking loss를 도입했다.


### 3.2. Approximated Ranking Weight
위 metric loss에는 weightij가 있었다. 우리는 아이디어로 Weighted Approximate-Rank Pairwise(WARP) loss를 참고했다. wij는 다음 식처럼 표현된다. 


![image](https://user-images.githubusercontent.com/68208055/212314347-bf77b173-01e5-4591-b6c4-437982d2d0ab.png)


rankd(i, j)는 user i의 item j의 순위를 의미한다. 값은 0~J(J는 전체 아이템 개수를 의미) 가지며, 가장 높은 순위는 0의 값을 가진다.
우리는 positive item j를 rank에 따라 weight를 줄 수 있다. 이는 낮은 rank에 있는 positive item을 위에 있는 아이템보다 무겁게 처벌한다. 하지만 rank(i, j)를 각 graident descent step에서 계산하는 것은 연산 비용이 비싸다.

그래서 Weston은 “Distance metric learning with application to clustering with side-information”논문에서 negative item을 랜덤으로 샘플해서 비교하는 방법을 취했다.
N은 imposter k를 찾기 위한 negative items 집합이라고 하면, rank(i, j)는 [J / N ] 내림을 한 것 과 같은 값이 된다. 이는 object detection에서 사용했던 negative sample mining이랑 비슷한 과정이다. (논문 : Efficient sample mining for object detection
sample 횟수 U는 보통 10이나 20으로 설정해서 샘플하는 과정이 너무 길지 않도록 한다.


최신 GPU를 사용하면 병행하는 것이 가능해진다.
각 user-item pair(i, j) 마다 U개의 negative item을 병행하여 뽑는다. 그리고 처음 공식을 계산한다.
M은 U 샘플에서 imposter개수를 의미한다. rank(i, j)는 이제 [J x M / U] 내림값이 된다.
매번 U개의 negative item을 샘플하는 것이 불필요해보일 수 있다.
하지만 CML이 epoch 몇 개만으로도 positive item을 훨씬 빠르게 high rank로 push하는 모습을 볼 수 있었다

### 3.3. Integrating Item Features

이번 장에서는 function loss를 알아볼 것이다. Transformation f는 raw feature를 우리가 원하는 latent space로 변환해주는 함수를 뜻한다. 

![image](https://user-images.githubusercontent.com/68208055/212314543-d84dfd24-731c-4445-bee1-6c4c80f3e9e7.png)

theta Θ 는 f 함수의 파라미터를 의미한다. 그래서 f()는 f(xj , theta) 즉 인풋과 파라미터를 받는 함수로 정의할 수 있다. 이 f로 우리는 dropout이 있는 MLP(multi layer perceptron)을 사용할 것이다. 위의 L2 norm loss function은 f()를 Gaussian prior로 취급하게 된다. 
f(x)는 item j의 raw feature를 넣은 MLP 함수의 결과를 의미하고, vj는 item의 vector를 의미한다. 
모델은 vj에 대한 정보를 더 많이 알기 때문에 vj의 위치를 미세 조절하게 된다.



논문은 Lf와 Lm은 서로에게 영향을 준다고 했다.   (mutually inform each other) 
Lf는 user preference와 가까운 feature를 배울 수 있게 도와주고, 
Lm은 비슷한 성격의 아이템들이 묶이도록 만들어 평가가 적은 아이템에 대해서도 잘 평가하도록 도와준다. 

### 3.4. Regularization

마지막 loss function은 covariance loss다. 

![image](https://user-images.githubusercontent.com/68208055/212314698-458eb5aa-0674-42ab-8ffe-5ffc46247966.png)

Weight가 너무 큰 값을 가지게 되면 모델이 많이 복잡해지는데, 이러한 구불구불한 함수를 가지지 않도록 적절한 regularization이 필요하다. 우리가 제안하는 kNN 형태의 모델은 dimension이 너무 많으면 data point가 지나치게 멀어져서 효과적이지 않다. (curse of dimensionality)

다른 matrix factorization model과 달리 L2 norm을 사용하지 않는다. l2 norm은 origin을 향해 모든 object를 당기는 성향이 있다. 이는 우리 모델과 같이 원점이 큰 의미가 없는 모델에서는 적용할 이유가 없게 된다.

![image](https://user-images.githubusercontent.com/68208055/212314779-3f24cdf3-7328-42a8-ae14-52d2fe7ed27b.png)


우리가 사용한 regularization technique은 covariance regularization이다. 이는 “Reducing overfitting in deep networks by decorrelating representations”이라는 논문에서 제안되었다. Covariance regularization은 DNN에서 activation 간의 correlation을 줄이는데 사용되었다.

우리는 metric learning에서 dimension 간의 correlation을 줄이는데도 효과가 있다는 것을 발견했다.
yn을 object의 latent vector라고 할 때 (object는 user / item 둘다 가능)
n은 batch size N에서 object의 index를 의미한다.

모든 dimension 간의 pair을 i, j라고 표현할 때 dimension간의 covariance는 Cij로 표현한다. 그리고 이 C를 convariance loss에 적용한 것이 아래 loss function이다. 여기서 covariance에 사용된 norm은 Frobenius norm이다.

Covariance는 dimension 간 중복을 알아낼 수 있는 수단인만큼, 이 loss는 dimension이 중복되는 것을 막아주고, whole system을 주어진 메모리 내에서 효과적으로 표현하도록 유도해준다.



### 3.5. Training procedure

결론적으로 우리가 제안하는 모델은 세 가지 loss가 존재한다.

![image](https://user-images.githubusercontent.com/68208055/212314874-244147f5-3de6-424e-920b-03d4880133e3.png)


λ 람다는 모델을 학습할 때 우리가 줄 수 있는 하이퍼 파라미터로 각 loss term의 weight를 나타낸다. 
우리는 이를 mini batch SGD로 줄이게 되고, learning rate control은 AdaGrad를 사용했다. 
학습과정은 다음과 같다. 

- sample N positive pairs from S
- Each pair, sample U negative items and rank
- for each pair keep item k that maximize hinge loss and form a mini batch of size N
- compute gradient and update parameter
- Censor norm u and v by y = y / max(||y||, 1)
- repeat until convergence

4장 실험 생략

## 5. Conclusion 

본 논문에서 우리는 새로운 CML이라는 논문을 소개했다. 이 모델은 user-item 관계뿐만 아니라 user-user/item-item similarity를 embedding space에 반영하였고, 그에 따른 regularization, feature fusion그리고 training technique을 소개했다. 

CML은 다양한 추천 도메인에서 압도적인 accuracy를 달성할 수 있었다. Top-K recommendation task에서 off-the shelf, nearest neighbor, search algorithm, 을 통해 시간을 줄일 수 있었고, CML이 user의 디테일하고 밝혀지지 않은 선호까지 알아내는 것을 보여주었다. 

Explicit feedback에서 implicit feedback으로 넘어오면서 Collaborative feedback은 rating을 예측하기 보다 user의 상대적인 선호도를 찾아내는 것으로 넘어갔다. Matrix factorization의 대안으로 우리는 CML 알고리즘으 이런 관계성을 직관적으로 찾아낼 수 있다고 본다. 

이는 metric-based algorithm (예를 들어 kNN, K-means, svm)이 CF에 적용될 가능성을 시사하고 있다. 우리는 item feature만 대응했었지만, future work으로 user feature역시 사용할 수 있을 것이다. 


그외 참고 : 

https://velog.io/@2chalsu/CMLCollaborative-Metric-Learning


