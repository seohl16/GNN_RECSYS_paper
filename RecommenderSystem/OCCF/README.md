## Studied OCCF 

본 논문에서 우리는 implicit feedback을 바탕으로 하는 데이터셋에서 협업 필터링 모델에 대해 알아보았다. (이렇게 암시적 피드백만들 활용하는 협업 필터링 방법을 단일-클래스 협업 필터링 즉 One class collaborative filtering이라고 부른다) OCCF 기반 방법들은 암식적 피드백만으로 구체적인 선호도를 정확히 추론하고, 이를 기반으로 추천을 제공하는 것이다. 

이러한 OCCF 기반 방법들은 point-wise와 pair-wise 방식으로 나뉜다. point wise학습방식에는 Weighted Regularized Matrix Factorization(WRMF)와 Neural Matrix Factorization(NeuMF)가 있다. 

pair-wise 학습방식에는 Bayesian Personalized Ranking(BPR)와 Group Bayesian Personalized ranking(GBPR)과 Collaborative Filtering via learning pairwise preferences over item-sets (CoFISet), BPR with multi-type pair wise preferences(M-BPR)이 있다. 

Pair-wise 학습 방식은 사용자가 피드백을 준 상품을 주지 않은 상품보다 더 선호한다는 가정을 바탕으로 상대적인 선호도 차이를 최대화하는 방향으로 학습을 진행한다. 

우리의 대표적인 findings는 implicit user observation은 두 개의 paired magnitudes로 바꿀 수 있다는 점인데 두가지는 preferences & confidence level이다. 

다시 말해, 각 user-item pair에 대해 우리는 input data에서 user가 좋아할지 안좋아할지에 대한 예측과(preference) 이 estimate에 대한 강조 레벨(confidence level)을 찾을 수 있었다. 

이 preference-confidence 분할은 implicit feedback 분석에 key role이 될 것으로 여겨진다.
