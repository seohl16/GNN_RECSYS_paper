# Studied TransE 

> 한줄요약 : TransE 논문은 지식 그래프에서 가장 기반이 되는 Translation based model이며, 저차원의 벡터 공간에서 가볍고 성능이 좋은 모델을 제시했다는 의의가 존재한다. 

## 0. Abstract 


[TransE]() is an approach to modeling multi-relational data in which entities and relationships are represented as low-dimensional vectors, or embeddings. 
This approach allows for the efficient calculation of the similarity between entities, as well as the probability of a relationship holding between two given entities. 
TransE has proven to be an effective model for knowledge graph completion tasks, (link prediction) 
and has been applied to large scale dataset with 1M entities, 25K relationships, and more than 17M training samples. 
Its success is due to its ability to capture relational information in a distributed and scalable way.

TransE는 multi-relational 데이터를 저차원의 벡터으로 표현하는 새로운 임베딩 방법을 제안한 논문이다. 
본 논문은 entities 간의 유사도를 계산 가능하게 해주며, entities 두 개 사이의 연결 가능성에 대한 확률을 제시할 수 있게 해준다. 
TransE는 knowledge graph completion(link prediction) 태스크에서 좋은 성능을 보였으며, 1M 엔티티가 포함된 대규모 데이터셋에서도 적용가능함을 보였다. 
이 성공은 relational information을 분산적이고 적용 가능한 방법으로 정보를 추출할 수 있는 능력 덕분으로 볼 수 있다.

## 1. Introduction 

[Multi-relational data]()는 directed graph로, 노드들과 (head, label, tail)로 표현되는 엣지로 구성된 그래프를 의미한다. 
여기서 (head, label, tail)(이후 (h, l, t)로 표현)은 label이라는 관계 타입을 가진 head - tail relationship을 의미한다. 

Multi relational data는 다양한 분야에서 사용되고 있다. 

- SNS : entites는 member, edges는 friendship/social relationship
- Recommender System : entites 는 user, edges는 buying, rating, reviewing, searching
- Knowledge Bases(KBs) such as Freebase : entities는 abstract concept, relationship : facts that involve both concept

본 논문은 이 중에서 Knowledge Bases (Wordnet and Freebase in this paper)에 집중할 예정이다. 
이 KB에 대한 표현이 가능하면 새로운 fact를 보충 지식을 크게 요하지 않고 자동적으로 집어넣는 것이 가능해질 수 있다. automatically add new fact without requiring extra knowledge. 

(참고 : Wordnet은 단어 상하관계를 나타내는 네트워크고, freebase는 다양한 데이터를 모아둔 wikipedia의 조상격 사이트로 현재 WikiData가 이어받은 네트워크다)


**Modeling multi-relational data** 

Relational data 관계를 갖는 데이터에서 어려운 점은 국소적(locality)인 관계에서 엔티티와 엣지는 서로 다른 관계 타입을 동시에 가질 수 있다는 점이다. 
따라서 multi-relational data는 이런 동시다발적인 관계를 잘 보여줄 수 있는 방법을 생각해봐야 한다. 

single relational data로 관계성을 보여주는데 성공한 user-item clustering이나 matrix factorization technique 과거 사례들을 보며 
우리도 이런 multi relational data를 latent attribute를 배우는 방식으로 학습해보기로 했다.

**Relationships as translations in the embedding space**

TransE is an energy-based model that represent low dimensional vector for each entity and each relationship. 
The relationship can be represented as (h, l t) where the embedding of tail entity t 
is the sum of embedding of the head entity h and vector that depends on relationship l. 

TransE는 에너지 기반 모델로, 각 엔티티와 관계를 저차원의 벡터로 표현하는 것을 목표로 하는 모델이다. 
이 관게는 (h, l, t) 조합으로 표현할 수 있는데, 이때 `tail entity t`는 `head entity h와 relationship을 나타내는 l 벡터의 합의 결과`라고 볼 수 있다.
아래 그림을 참고 

![image](https://user-images.githubusercontent.com/68208055/211745833-458a5a28-ab33-4f24-9c00-0448a479897d.png)


The main motivation behind translation based parameterization is that hierarchical relationships are commin in knowledge base and translations are natural transformations for representing them. 
The siblings are organized at x axis and parent-child relationship corresponds to translation on the y axis.  
Another motivation comes from the recent work where authors learn word embeddings from free text and some 1 to 1 relationships are represented by the model as translations in the embedding space. 

우리가 translation을 사용한 이유는 두 가지가 있다.  
우선 지식 그래프 (knowledge base)에서 계층적인 관계가 비교적 common한데, 이를 잘 나타낼 수 있는 것이 translation이다. 형제 관계는 x axis로 parent child 관계는 y axis로 대입할 수 있다. 
또 다른 이유는 최근 연구들이 word embedding의 일대일 관계를 나타낼 때 translation을 사용했기 때문이다. 
여기서 더 나아가 우리는 여러 일대일 관계를 translation으로 표현할 수 있다고 보았다.

## 2. Translation-based model 

### Background knowledge for loss function

2장에서는 TransE의 loss function에 대해 알아볼 것이다. 이때 함수를 이해하기 위해 파라미터 설명부터 하면.. 

- the set of entities `E`는 엔티티 집합, the set of relationship `L` 관계 집합을 의미한다. 
- `training set S`는 (h, l, t)라는 triplets로 구성되어 있다. 
- `(h, l, t)`안에는 h, t entities와 둘의 관계인 l의 조합으로 구성되어 있다. `h, t` ≤ `E` and `l` ≤ `L`
- 우리의 목표는 h + l ~= t로 h + ㅣ합 결과가 t에 가깝게 만드는 것이다. 
- `d`는 dissimilarity measure이다. 
- `k`는 embedding dimension 크기다.
- `γ`는 margin hyperparameter를 의미한다. 
- [x]+는 []안의 결과인 x에서 0보다 큰 값만 남긴다는 뜻 
- h’, l, t’는 h 또는 t를 랜덤하게 다른 엔티티로 바꾼다는 뜻이다. 대신 둘다 동시에 바꾸지는 않는다. 

> 참고로 dissimilarity measure는 두 대상이 얼마나 다른지 보여주는 measurement다. 
similarity measure이 보통 0~1 사이 유사도를 표현하는 것과 다르게,  dissimilarity measure는 비슷하면 최소 0, 다르면 값이 무한정 커질 수 있다. 
본 논문에서 이 dissimilarity measure로 L1, L2 norm을 사용했다. 

> [x]+ 설명 ![image](https://user-images.githubusercontent.com/68208055/211747033-043b00ec-8c46-49e7-9f2b-37f284d9e152.png)

### Loss function

![image](https://user-images.githubusercontent.com/68208055/211746631-85d54bdb-3a76-48f1-8678-e0fb8b663afa.png)

위 이미지는 TransE의 loss function이다. 모델은 d(h + l, t)을 최소한으로 나오도록 학습하려고 한다. d(h+l, t)는 다름 함수에 training set의 triplet 하나를 넣은 것을 의미한다. 더 나아가 noise가 있는 corrupted triplet인 d(h’ + l + t’)과의 차이는 크게 하고 싶다. 

만약 d(h + l, t)의 값이 작으면 [] 안 결과 값은 작을 것이고 []+ 에 의해서 loss가 0이 될 것이다. 
만약 d(h+1, t)의 값이 크고 d(h’ + l, t’)은 엉뚱하게 작으면 [] 안 값은 클 것이고  loss는 크게 나올 것이다.  
모델은 training set안에 triplet (h, l, t)의 dissimilarity 즉 energy가 낮은 상황, (h’, l, t’)의 dissimilarity 즉 energy가 큰 상황을 원하게 된다.

Optimization을 위해서는 미니배치 sgd를 사용할 것이고, L2-norm의 constraint는 1이다. 


![image](https://user-images.githubusercontent.com/68208055/211747747-12e2fa7a-6aa0-4d14-a2b0-687ba16c1904.png)

자세한 optimization procedure은 Algorithm 1에 있다. All embedding for entities and relationship은 random하게 초기화된다. 그리고 각 iteration마다, embedding vector of the entities는 normalized된다. 그리고 triplet 배치를 만들고 각 triplet마다 또 corrupted noise triplet을 만든다. 파라미터는 graident step에 따라 업데이트한다. 

## 3. Related Works 

본 논문에서 Related works로 두 개의 논문과 비교분석한다 : Structure Embeddings (SE) and Neural Tensor Model 

[Structure Embeddings 이하 SE]() 모델은 entities를 Rk(k 크기의 벡터를 갖는 행렬), relationship을 두 개의 matrices L1과 L2로 임베딩한다. 
SE는 d(L1h, L2t)의 dissimilarity function 결과가 corrupted triplet에 있어서 크도록 학습한다. 

SE의 basic idea는 두 개의 엔티티가 같은 triplet에 속해 있다면, 특정 relationship을 나타내는 임베딩 스페이스에서 임베딩 위치가 가깝도록 만들게 한다. 
head와 tail에 두 가지 다른 projection matrice를 사용하는 것은 달라지는 관계를 설명하기 위한 것이다. 

엄밀히 말하면 k+1개의 dimension을 가진 SE는 k dimension 을 갖는 모델보다 affine transformation을 더 많이 표현할 수 있다. 
하지만 TransE는 SE보다 단순하면서도 더 좋은 성능을 보였다. 

다음 related work로는 [Neural Tensor Model]()이 있다. 이 모델은 s(h, l, t) score를 학습하는데 식은 다음과 같다. 
![image](https://user-images.githubusercontent.com/68208055/211750822-5b2cfa18-dbfd-4a90-a26d-5352e2749367.png)

여기서 L는 R(k^2) 크기 matrix이다. 

만약 TransE의 dissimilarity function으로 제곱유클리드 거리를 사용했다면 식은 다음과 같다. 
![image](https://user-images.githubusercontent.com/68208055/211750850-5e3dddbb-b1f9-462e-8eb1-5f3c13c03587.png)

우리의 norm constraint를 1로 유지하자는 전제와 loss function 식을 생각해보면 corrupted triplet과 비교할 때 변수들의 절대값제곱은 크게 의미가 없어 진다. 

따라서 dissimilarity 계산에서 유효한 것은 마지막 ht + l(t-h) 부분이 된다. 이는 Neural Tensor Model의 score 식과 굉장히 유사하다. 

우리는 이 모델로 실험을 진행하지 않았지만 (거의 비슷한 시기에 공개되었기 때문에), TransE는 적은 파라미터를 사용해 기존 모델에 비해 학습과정을 단순하게 바꾸었고, underfitting을 막아주었다는 장점이 있다. 

**TransE depending on interaction**

TransE는 2way interaction을 표현하는데 강점이 있다. 반면 3 way interaction을 설며하는데에는 어려움이 있었다. 
예를 들어 Kinships dataset이라고 작은 크기의 데이터셋이 있었는데, TransE는 여기서 최신 SOTA 모델에 비해 성능이 좋지 않았다. 
그 이유는 이 데이터셋에서 ternary 3자 관계 (ex. 의사-환자-처방)이 중요했는데, TransE는 이런 관계를 잘 표현하지 못했기 때문이다. 
하지만, TransE는 2way interaction이 주인 대규모 데이터셋에서는 효과를 보였다. 이는 TransE가 데이터셋에 따라 성능 차이가 존재함을 보여준다. 


## 4. Experiments   

생략 


## 5. Conclusion 

The model’s contribution은 다음과 같다. 

- Knowledge base의 hierarhical relationship을 보여주는 embedding을 학습했다.
- Freebase data의 large scale에서도 잘 작동했다.

Future work로는 다양한 태스크에 적용하는 것이다. 
예를 들어 word representation에 적용하면 더욱 쓸모가 있을 것으로 기대된다.




