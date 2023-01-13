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
