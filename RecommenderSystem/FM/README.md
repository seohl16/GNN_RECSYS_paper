## Studied FM (Factorization Machine) 

### 0. Abstract

기존 머신러닝 알고리즘 SVM은 sparse한 추천시스템 데이터에서 좋은 성능을 보이지 못했다. 하지만 Factorization machine FM은 factorized parameter를 이용해 variable 사이의 interaction을 모델링한다. 이로써 sparse한 데이터에 대해서도 잘 대응할 수 있었다. 

FM 전의 matrix factorization 모델인 SVD++, PITF, FPMC와 같은 MF 모델들은 special input data에 대해서만 적용가능했다. 또한 각 태스크마다 equation과 optimization algorithm이 따로 만들어져야 했다. 하지만 FM은 도메인에서 자유롭고, factorization model에 대한 전문가적 지식이 없어도 유저들이 쉽게 적용 가능할 것으로 보인다. 

### I. Introduction

SVM은 많은 사람들이 즐겨 사용하는 머신러닝 모델이다. 하지만 이들은 sparse한 데이터에서 비선형적인 kernel space의 적절한 hyperplane(구분선)을 찾기 어려워한다.  그리고 MF 모델들은 real valued feature vector과 같은 standard prediction data에 적용하기 어렵고, 태스크마다 알고리즘이 조금씩 달라 한 태스크를 위해 개발되면, 다른 태스크에 동시 적용하기 어렵다는 문제가 있었다. 

본 논문에서는 Factorization Machine이라는 새로운 예측기를 소개한다. 모델은 linear time 내로 연산하는 빠른 속도를 보였고, 파라미터 수 역시 적은 것을 보였다. 

정리하면 FM의 장점들은 다음과 같다. 
1) FM은 SVM과 달리 sparse data에서 연산이 가능하다. 
2) FM은 linear complexity로 Netflix와 같은 거대한 데이터셋에서도 적용가능했다. 
3) FM은 input data가 SOTA 모델에 비해 any real valued feature vector가 가능하다. 

### II. Prediction under Sparsity

- 머신러닝 태스크를 가장 간단하게 말하면 function : R → T로 바꾸는 과정이며, 여기에 넣는 인풋 x는 real valued feature vector이고 Rn 매트릭스로 표현된다.
- T는 target domain이고 방법이 regression이면 R, binary면 +- 등으로 표현
- 만약 supervised model이라면, Dataset이 (x, y) 세트 즉 라벨도 함께 구성될 것으로 기대된다.
- ranking task에서 라벨 y는 feature vector의 score가 되고, 이를 rating따라 sorting이 가능하다.
- 이런 랭킹 태스크는 pairwise training data가 필요하다. 비교할 수 있는 쌍으로 데이터가 구성된다. 만약 한 데이터 (xA, xB) 가 있다면 이는 xA는 xB보다 랭킹이 높다-는 뜻이다.
- 이런 relation은 불균형하기 때문에 보통 positive training instance만 존재한다.

- 본 논문에서 인풋 x는 굉장히 sparse하고(산개되어 있고) 대부분의 x안의 값이 0이다.
- m(x)는 feature vector x 안에 non zero value의 개수를 뜻한다.
- mD는 m(x)의 평균을 의미한다.
- Huge sparsity m << n 은 purchase recommender system이나 bag of word approach같은 텍스트 분야에서도 많이 등장한다.
- huge sparsity는 이러한 category로 나눠야 하는 도메인에서 꾸준히 대응해야 하는 문제다.

Example 1 뮤비 리뷰 시스템을 정의해보자 
U는 유저를 뜻하고 I는 영화를 뜻한다. 
S는 (A, T, 2020Yr, 5점), ….로 구성될 것이다. 

![image](https://user-images.githubusercontent.com/68208055/216263736-27f117de-376c-4d82-84ca-5ef1ea85ac3e.png)

(A, T, 2020Yr, 5점)를 표현하기 되면 
- blue section User에서 A에 해당하는 사람만 1로 표시하고 나머지 0 
- orange section Movie에서 T에 해당하는 영화만 1로 표시하고 나머지 0 
- yellow section Movie에서 A라는 유저가 본 모둔 영화의 movie rating을 sum이 1이 되도록 normalize한 값 
- green section Time은 본 시간을 의미한다. 
- (2009년 January)로 시작해서 month을 표시 
- 마지막 purple section Last Movie rated은 유저가 마지막으로 본 영화를 1로 표시하고 나머지 0 
- 본 논문은 이 예시를 계속 쓰겠지만 명심할 점은 FM은 이런 추천 시스템 데이터뿐만 아니라 거의 모든 데이터에 applicable하다는 것이다. 

## III. Factorization Machine (FM)

1) Model Equation 

![image](https://user-images.githubusercontent.com/68208055/216263778-6d20ec72-7f11-4f60-a407-0a3de57e1f8f.png)

degree 2 인 FM 의 model equation을 하나씩 분해해보자 
- w0는 global bias
- w1 ~ wn은 각 인풋에 대응하는 weight(논문에서 strength라고 표현)
- k는 dimension  hyperparameter
- <vi, vj>는 V안의 k factor가 있는 ith variable vector 두개를 내적한 값
- wij라고 xi xj 곱 앞에 붙는 strength가 있었는데 이걸 따로 parameter로 정의하기 보다 factorization을 활용했다. 이부분이 key point다.

2) Expressiveness 

- positive definite matrix W 에서는 V * Vt = W라는 행렬이 존재한다.
- 이는 FM이 k가 충분히 크면 어떤 W든 표현할 수 있다는 것을 보여준다.
- 하지만 K가 너무 커도 지나치게 복잡한 관계를 표현하기 위한 데이터가 충분치 않기 때문에 적절한 k값을 골라야 한다.
- 궁극적으로 K를 적절하게 작게 만드는 것이 일반화에 도움을 준다.

3) Parameter Estimation Under Sparsity 

- 산개된 환경에서 모든 variable간의 관계를 보여주기에 데이터가 충분하지 않을 수 있다.
- FM은 이런 환경에서도 잘 찾는 모습을 보이는데, 그 이유는 factorizing을 통해 독립성을 쪼개기 때문이다. 이는 한 관계를 위해 정의한 데이터가 다른 관계를 정의하는데도 도움을 주는 것이다.

예시를 이용해서 알아보자
- 우리는 Alice user과 Start Trek간의 관계 즉 rating target y를 알고 싶다고 하자.
- alice와 start trek가 동시에 non-zero인 경우 즉 Alice가 rating을 한 경우는 존재하지 않는다. 따라서 wA, st interaction은 존재하지 않는다. (direct estimate would lead to no interaction)
- 하지만 factorized interaction parameter인 <VA, VST>로 우리는 예측을 할 수 있다.
- Bob, Charlie가 vb vc를 모두 Star war를 봤고 비슷한 rating을 해서 비슷한 vector를 가질 것이다.
- Star Trek은 Start war에 Bob이 비슷한 rating을 보였기 비슷할 것으로 추정된다.
- Alice가 Startwar에 매긴거랑 starttrek에 매긴거가 유사할 것으로 보인다.
