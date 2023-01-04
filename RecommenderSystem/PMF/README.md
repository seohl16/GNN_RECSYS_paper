# Studied PMF 
PMF 논문은 무려 2007년에 나온 추천 시스템 관련 논문이다. 

latent based collaborative filtering 관련 고전이자 클래식한 논문이므로 그 아이디어를 이해하는 것이 중요하다. 

## Concepts 
### Latent based collaborative filtering 
Recommender system 모델들은 크게 content-based와 collaborative based로 나뉜다. 이 중 협업 필터링이 더 각광받게 되었다. 

협업 필터링은 또 model based와 memory based로 나뉘었는데 이 중 PMF은 model based 즉 latent factor를 찾는 추천 시스템 방법론을 기반으로 하고 있다. 

Latent based collaborative filtering은 matrix factorization 행렬 분해를 사용한다. 


### Sparse matrix of recommender system 

보통 다른 분야의 딥러닝 모델을 훈련 시킬 때는 데이터의 pre processing 전처리 단계에서 dropna 와 같은 방법으로 na 값을 없애고 학습을 진행한다. 

하지만 추천 시스템은 다른 분야와 다르게 NaN 즉 빈 값에 대응할 필요가 있다. 

왜냐하면 보통 유저-아이템 간의 매트릭스에서 유저가 평가하지 않은 아이템들은 당연 그 평점이 Nan 값을 갖기 때문이다. 

Matrix를 분해하는 방법으론 PCA와 SVD 같은 방법이 존재한다. \
하지만 두 방법 모두 NaN 즉 undefined value에 대해서 대응을 잘 못한다고 한다.  

따라서 본 논문은 Matrix를 분해하기 위해 Probablistic matrix factorization이라는 새로운 방법을 제안한다. 


## PMF (Probablistic Matrix Factorization) 

![image](https://user-images.githubusercontent.com/68208055/210516979-c909dc02-1268-4784-a650-70c6c40d7631.png)

만약 어떤 쇼핑몰에서 n명의 유저와 m개의 아이템이 있다고 하자. 이 matrix는 원본 매트릭스 n * m 크기를 갖고, 군데군데 Nan 또는 undefined 값으로 채워져 있다. PMF 논문에서는 이 Matrix를 preference matrix R이라고 불렀다.

이 matrix를 user 정보가 담긴 latent matrix인 (n, d)와 item 정보가 담긴 (d, m) latent matrix로 만든다고 하자. 두 매트릭스를 곱하면 원본 매트릭스인 n * m이 된다. 유저 관련 matrix는 논문에서 user coefficient matrix UT라고 말했고 d * m으로 행렬은 factor matrix V라고 불렀다.

여기서 d는 우리가 조정할 하이퍼파라미터로, 우리가 조절할 latent factor 차원 크기를 의미한다. d는 user가 선호하는 장르든, 아이템 분류든 feature를 의미하게 된다. 
보통 d는 10~250 값을 가지며, grid search 등을 통해 적절한 value를 찾을 수 있다.

Ut와 V를 가지고 우리는 stochastic gradient descent(sgd)로 value를 최적화할 것이다. 
따라서 sgd를 위해 learning rate와 epoch도 하이퍼 파라미터로 요구된다.

## Ut와 V를 학습하는 간단한 과정 

![슬라이드3](https://user-images.githubusercontent.com/68208055/210517888-5a471cdb-b8e7-4a39-ad52-97a5abb9c37e.PNG)

가장 먼저 user - item - rating으로 만들어진 표가 있을 것이다. 
이를 (user n * item m) 차원의 matrix로 바꿔준다. (이해를 위해) 
이제 빈 값을 채우기 위해 학습을 진행한다. 위의 예시에서는 d를 2로 가정하고 latent matrix를 구해본다. 

크기 (3 * 4 ) = (3 * 2 ) * (2 * 4)



![슬라이드4](https://user-images.githubusercontent.com/68208055/210518024-82f44c8d-e796-4b2e-9308-e5257fe614c6.PNG)

먼저 빨간색 latent matrix들을 random한 값으로 채운 다음 (n, d)와 (d, m)을 곱해서 (n, m) 행렬을 구한다. 
그리고 나서 실제로 채워있었던 칸들의 값과 새로운 행렬에서 같은 위치의 예측 값 간의 차이를 줄이기 위한 학습을 진행한다. 
위의 예시에서 첫번째 칸에 대한 예측값은 2.2지만 실제 값은 3점이므로 그 차이 극간을 줄이기 위해 노력한다. 


## Reference 
- [https://towardsdatascience.com/introduction-to-latent-matrix-factorization-recommender-systems-8dfc63b94875](https://towardsdatascience.com/introduction-to-latent-matrix-factorization-recommender-systems-8dfc63b94875)
- [http://katbailey.github.io/mf/#/title](http://katbailey.github.io/mf/#/title)
- [https://www.kaggle.com/code/robottums/probabalistic-matrix-factorization-with-suprise/notebook](https://www.kaggle.com/code/robottums/probabalistic-matrix-factorization-with-suprise/notebook)
- [https://wooono.tistory.com/149](https://wooono.tistory.com/149)

