# Basic Background knowledge about RecommendSystem
![image](https://user-images.githubusercontent.com/68208055/210484947-08af89d2-3a03-47bf-93c8-be1dd8e06ac6.png)

Recommend System strategies are largely divided into Content-based filtering and Collaborative filtering.

## 1. Content-based filtering
Content-based filtering is content-based filtering which recommend item \
that has content similar to certain item. 

콘텐츠 기반 필터링은 대상 아이템과 유사한 아이템을 찾아 추천해주는 내용 기반 필터링입니다

It is said that in early recommendation system research, content-based filtering was used well, \
but after Netflix, latent factor collaborative filtering was used more. 

초기 추천 시스템 연구에서는 콘텐츠 기반 필터링이 잘 사용되었지만 \
그러나 넷플릭스 이후에는 잠재 요소 협업 필터링이 더 많이 사용되었다. 

## 2. Collaborative filtering 
Collaborative filtering은 협업 기반 필터링이다. 

It is a system that recommends based on user behavior such as user ratings and purchase history.\
Collaborative filtering is again divided into memory-based filtering (Neighborhood) and model-based (Latent factor) collaborative filtering.

협업 필터링은 사용자 등급, 구매 내역 등 사용자 행동을 기준으로 추천하는 시스템이다.\
협업 필터링은 다시 메모리 기반 필터링(Neighborhood)과 모델 기반(Latent factor) 협업 필터링으로 나뉜다.

### 2-1. Memory-based filtering (Nearest Neighborhood Collaborative filtering)
Nearest neighbor Collaborative filtering aims to predict items that users have not yet evaluated in user-item matrices.

Nearest neighbor Collaborative filtering은 사용자-아이템 행렬에서 사용자가 아직 평가하지 않은 아이템을 예측하는 것을 목표로 한다. 

Here, we have a matrix with column as item and row as users. \
However, this method will result in many empty values (sparse) because users cannot evaluate all the items in the store, vice versa. \
Therefore, latent based collaborative filtering is used well. 

이를 위해 column은 item, row는 유저로 구성된 행렬을 사용한다. \
하지만 이런 방식은 유저랑 아이템이 많아지면 유저가 평가하지 않은 아이템이 많아지면서 빈 값이 더 많아지게 된다. \
그래서 잠재 기반 협업 필터링이 잘 사용되게 되었다. 

User-based method groups user, while item-based groups item that show a similar reaction from users. \
In general, it is said that item-based is more accurate than user-based. \
THis is because buying the same product doesn't always mean that user has a similar interest. 

User-based는 유저 단위로 묶게 되고 item-based는 비슷한 반응이 보인 아이템 단위로 묶어준다. \
일반적으로 item-based가 user based보다 더 정확도가 높다고 한다. \
왜냐하면 같은 상품을 산다고, 유저 간의 취향이 비슷하다고 볼 수 없기 때문이다. 



