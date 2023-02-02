## Studied BPR 

한 줄 : collaborative filtering 관련 논문으로 특히 optimization에 관한 논문이다. 

### Abstract 
BPR 논문은 implicit feedback 에서 추천 문제를 다룬다. 
여기서 추천은 user가 선호할만한 personalized ranking item list을 예측하는 것이다. 
Matrix Factorization과 knn은 추천에서 가장 많이 쓰이는 대표적인 방법이다. 
하지만 기존의 opimization 기법들은 랭킹을 고려하지 않은 방식으로, 본 논문은 베이지안 추론에 기반한 optimization 기법 (BPR-Opt)를 제시해 아이템들에 대한 유저의 선호 강도를 반영할 수 있도록 하였다. 
나아가 이를 MF와 KNN에 적용한 결과 기존의 것보다 우수함을 증명하였다.

### Introduction 
Implicit data는 explicit data보다 데이터 양이 많지만, 데이터로부터 user의 선호강도를 추론해야 하기 대문에 더 어렵다. 

논문은 이런 상황에서 contribution을 만들었다. 

- 베이지안 추론(Maximum a posteriori MAP)에 기반한 optimization 기법인 BPR-Opr를 제시했다. 이는 Area under curve인 AUC를 최대화하는 문제와 동치임을 보였다.
- BPR-Opt를 최대화하기 위한 알고리즘 LEARN BPR를 제안한다.
- LEARN BPR를 MF, KNN에 적용했다.
- 다른 optimization기법보다 우수했다.

### Related Work 

> Implicit Data

Implicit data의 행렬은 클릭 여부와 같은 바이너리 타입으로 이루어져 있다. 따라서 이런 경우 user가 특정 아이템을 클릭할 확률을 예측하는 문제로 풀게 된다. 이런 문제를 푸는 optimization 방법에는 regularized least square가 있다. 하지만 이는 ranking optimization이 아니다. 
여기서 ranking이란 두 아이템의 선호 강도를 반영하는 것을 의미한다. 어떤 유저가 한 아이템을 다른 아이템보다 선호한다면 이때 item i > item j라고 표시할 수 있는 것이 ranking이다.

Implicit data의 주요 특징은 부정적인 데이터가 관측되지 않는 점이다. 관측되지 않은 데이터가 유저가 관심이 없어서인지 그저 알지 못한 것인지 알 수 없다. (real negative feedback vs missing value) 
따라서 이를 모두 고려하여 모델링해야 한다.


### Formalization 
U, I가 각각 user, item 집단이라고 한다. 
이때 관측 가능한 (user, item) 쌍 s 는 S 의 일부로, S는 U x I에 포함된다. 

본 논문의 목표는 각 유저별 personalized total ranking 을 구하는 것이다.
예를 들어 5개의 item이 있는 집단 I가 있다고 하자 . I={I1,I2,I3,I4,I5}
여기서 Ir>u I2 >u I1 .. 이런 순서로 선호하게 되면 I4 >u I1은 >u은 한가지 예시가 된다. 
비교하는 >u는 다음과 같은 속성을 만족한다. 
item간의 order를 정의하는 것으로 집합론에서 사용한 개념이다. 

- totality : i, j가 같지 않다면 i가 j보다 선호되거나 j가 i보다 선호된다.
- antisymmetry : i 가 j보다 선호되고 j보다 i가 선호된다면 이는 i랑 j가 같다는 의미이다.
- transitivity : i가 j보다 선호되고 j가 k보다 선호된다면 i는 k보다 선호된다.


### Problem Setting 
implicit data는 real negative와 missing을 모두 고려해서 모델링해야 한다고 했다. 
하지만 기존의 방식은 missing을 모두 negative하다고 간주하고 문제를 해결했었다.

![image](https://user-images.githubusercontent.com/68208055/216260437-94134340-dd55-4d00-9d05-b75fc0c76e23.png)

위의 그림이 기존 방식을 보여주는 행렬이다. 관측된 데이터는 1로, 관측되지 않은 데이터는 0으로 무조건 통일하여 missing과 real negative를 구분하지 않고 있다. 


![image](https://user-images.githubusercontent.com/68208055/216260464-f2fa8f28-8097-4666-831e-6af25e85f91d.png)

따라서 논문은 새로운 design matrix를 제안한다. 
New Deisgn Matrix는 다음 3가지 전제가 있다. 

- user은 관측되지 않은 아이템을 관측하지 않은 모든 아이템보다 더 선호한다.
- 관측한 item들에 대해서는 선호강도를 추론할 수 없다. item을 더 선호하는지는 알 수 없다.
- 관측되지 않은 item들에 대해서는 선호강도를 추론할 수 없다. 즉 어떤 아이템을 더 비선호하는지 알 수 없다.


u1에 대해서만 보면 Iu+는 I2, I3이 있고 관측안된 아이템은 I1, I4이다. 
이때 design matrix를 만들면 I2 I3은 I1 I4에 대해서 선호되고 I1 I4는 i2 I3에 대해서 덜 선호된다. 
이렇게 하면 관측되지 않은 아이템에 대해서도 정보가 생기기 때문에 간접적으로 학습이 가능하다. 
그리고 관측되지 않은 아이템들에 대해서도 순서를 매길 수 있다. 기존 방식은 모두 0으로 예측되어 순서를 매길 수 없었던 것과 
달리 ranking을 학습함으로써 이를 추론할 수 이도록 한다. 







