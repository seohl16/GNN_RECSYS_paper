# Studied TransE 

한줄요약 : TransE 논문은 지식 그래프에서 가장 기반이 되는 Translation based model이며, 저차원의 벡터 공간에서 가볍고 성능이 좋은 모델을 제시했다는 의의가 존재한다. 

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
이 관게는 (h, l, t) 조합으로 표현할 수 있는데, 이때 tail entity t는 head entity h와 relationship을 나타내는 l 벡터의 합의 결과라고 볼 수 있다.
아래 그림을 참고 

![image](https://user-images.githubusercontent.com/68208055/211745833-458a5a28-ab33-4f24-9c00-0448a479897d.png)


The main motivation behind translation based parameterization is that hierarchical relationships are commin in knowledge base and translations are natural transformations for representing them. 
The siblings are organized at x axis and parent-child relationship corresponds to translation on the y axis.  
Another motivation comes from the recent work where authors learn word embeddings from free text and some 1 to 1 relationships are represented by the model as translations in the embedding space. 

우리가 translation을 사용한 이유는 두 가지가 있다.  
우선 지식 그래프 (knowledge base)에서 계층적인 관계가 비교적 common한데, 이를 잘 나타낼 수 있는 것이 translation이다. 형제 관계는 x axis로 parent child 관계는 y axis로 대입할 수 있다. 
또 다른 이유는 최근 연구들이 word embedding의 일대일 관계를 나타낼 때 translation을 사용했기 때문이다. 
여기서 더 나아가 우리는 여러 일대일 관계를 translation으로 표현할 수 있다고 보았다.

