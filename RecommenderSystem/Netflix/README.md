## Studied Netflix 
## A basic matrix factorization model

본 논문에서 item vector은 qi 로 표현되고 user vector는 pu로 표현된다. qi의 구성 값은 item의 해당 factor에 대해서 positive or negtaive 값을 갖는지 표현하고 u의 factor에 대한 관심도를 역시 positive or negative로 표현한다. 내적한 결과 qiT*pu는 user u와 item i 간의 interaction을 잡아내고 있다. 이 둘의 관계는 rui로 표현한다. 

<img src="https://user-images.githubusercontent.com/68208055/216271308-e61e458a-0400-457e-af32-15289a3cf42d.png" height=70>

가장 challenging 한 것은 qi, pu를 computing하는 것이다. 만약 mapping만 잘 된다면 어떤 아이템이든지 user의 선호를 쉽게 계산할 수 있을 것이다. 이 예시로 들 수 있는 모델인 SVD(singular value decomposition)는 latent semantic factors 를 잘 잡아내는 technique이다. 하지만 추천 도메인에는 missing value가 많아 SVD를 사용하는데 있어 어려움을 초래한다. 

전통적인 SVD는 이런 undefined incomplete value에 대해 잘 대응하지 못할 뿐더러, 몇 개의 entries 만으로 모델을 학습하는 것은 overfitting될 확률을 높일 뿐이다. 

기존 시스템은 missing rating을 fill하거나 rating matrix를 두껍게 만드는 것(무조건 채우기로 추정)을 목표로 했다. 하지만 데이터를 대치하는 방법(imputation)은 데이터 양이 많아지면 계산 비용이 매우 비싸지게 된다. 그리고 잘못 채워진 정보는 전체 데이터를 크게 왜곡할수도 있다. 따라서 최근 연구들은 observed ratings로만 모델링을 한다. 

앞서 언급했던 user과 item latent vector들인 pu qi를 배우기 위해서 loss function은 regularized squared error를 최소화하는 것을 목표로 한다. 

<img src="https://user-images.githubusercontent.com/68208055/216271347-96db4694-fa28-4c31-897f-c944835a3d30.png" height=70>

여기서 K 집합은 실제 평점이 있는 (u, i) 숫자 조합을 의미한다. 시스템은 이렇게 실제로 유저가 평점을 매긴 데이터 ratings만 가지고 학습한다. 

하지만 모델의 목표는 전혀 모르는 데이터도 잘 예측하는 것이므로 기존 데이터에 대해 overfitting되지 않도록 해야 한다. 여기서 뒤에 있는 q, p의 제곱식이 weight가 지나치케 커지는 것을 방지해준다. PMF(Probailistic Matrix Factorization) 논문에서 이에 대한 증명을 잘 설명하고 있다. 

## Learning Algorithms

위에서 보았던 Equation 2 Loss Function의 local minimum을 찾기 위해 사용할 수 있는 방법은 Stochastic gradient descent(SGD)와 Alternating least squares (ALS)가 있다. 

> Stochastic gradient descent(SGD)

Stochastic gradient descent는 Simon Funk가 제안한 메소드로 알고리즘이 모든 ratings를 하나씩 살펴보면서 각 케이스마다 rui와의 차이를 계산한다. Gradient Descent를 수행하는 것과 같지만, 효율적이다. 실제 rating과의 차이인 prediction error은 eui라고 표현한다. 이 eui를 활용해서 qi, pu latent factor를 업데이트한다. 그리스어 기호는 γ gamma감마, λ lambda 람다라고 읽는다.  

<img src="https://user-images.githubusercontent.com/68208055/216271397-1335477d-fc24-4fb7-8587-ddc135ff1a27.png" height=110>


> Alternating least squares (ALS) 

qi pu는 모두 학습해야 할 미지의 대상이다. 따라서 loss function equation 2자체는 현재 convex하지 않다. (convex는 둥글둥글한 도형을 의미하고 만약 각이 안쪽으로 굽으면 concave하다고 함. local minimum을 찾으려면, convex해야 한다)

만약 둘 중 하나를 고정시키면 고정되지 않은 하나는 학습 가능해진다. 따라서 ALS technique은 둘을 번갈아 가며 학습을 해 수렴할 때까지 진행하는 방법을 의미한다. 

> 비교

SGD 방식이 보통 ALS보다 빠르고 쉽지만, ALS는 아래의 두 경우에 더 선호된다고 한다. 

첫번째는 시스템이 병렬화가 가능할 떄다. ALS에서는 q 다음 p를 독립적으로 학습하게 되는데 이는 병렬화가 가능한 요소를 제공한다. 

다른 경우는 시스템이 implicit data에 더 비중이 많이 둘 경우이다. Implicit data의 경우 training set이 sparse하지 않기 때문에 각각의 training case를 하나씩 확인하는 sgd 방법보다 als방법이 효율 측면에서 더 나을 수도 있다. 

## Adding Biases

협업 필터링에서 행렬 분해(MF)의 장점은 데이터의 다양한 특성을 반영할 수 있다는 점과, 다른 도메인에서도 적용할 수 있다는 것이다. 

원래 식 Equation 1 (rui = qTp) 은 user과 item 사이의 interaction을 잡아내려고 한다. 하지만 대부분의 observed variation은 biases, or intercepts와 같은 효과에 영향을 받는다. 예를 들어 어떤 유저는 점수를 후하게 줄 수 있고, 또 어떤 아이템은 다른 비슷한 아이템에 비해 좋은 점수를 받을 수 있다. 당연하지만, 몇몇 아이템은 다른 아이템보다 더 선호가 높고 유명한 경우를 쉽게 떠올릴 수 있다. 

따라서 단순한 qi * pu를 통해 선호를 설명하는 것은 불합리하다. 시스템은 그런 biases를 조정하기 위해 노력했고 그 결과 얻은 bias 식은 bui = u + bi + bu

rui에 있는 bias는 bui로 표현한다. 여기서 u는 전체 아이템에 대한 평균 평점을 의미하고, bu와 bi는 각각 유저와 아이템에 대한 average로부터 떨어진 차이를 의미한다. 

예를 들어 Joe라는 이름을 가진 유저가 있을 때 이 유저의 titanic 영화에 대한 선호를 측정하려고 한다고 가정하자. 모든 영화의 점수를 평균냈을 떄 3.7점이었다. titanic은 영화 전체 평점에 비해 0.5점 높다고 하고, Joe는 비판적인 사람이라 평균보다 0.3점 낮게 점수를 매긴다고 하자. 

그렇다면 이때 Joe가 titanic 영화에 대한 예상 점수는 3.7 + 0.5 - 0.3 = 3.9점이라고 볼 수 있다. 

따라서 이런 계산 방식을 rui에 포함하면 다음식이 된다. 

<img src="https://user-images.githubusercontent.com/68208055/216271695-9f8932ca-806f-41eb-85b2-810cf2fc9f3c.png" height=70>


정리하면 observed rating rui hat은 global average + item bias + user bias + user-item interaction을 나눌 수 있다. 

<img src="https://user-images.githubusercontent.com/68208055/216271657-e0a1829b-9e69-41f2-a85f-01471f80a907.png" height=110>


각 값의 절대값이 작게 하도록 norm까지 추가하면 우리가 최소화해야 하는 loss function 수식을 얻을 수 있다.

## Inputs with varying confidence levels

모든 observed ratings가 같은 weight를 갖는 것은 아니다. 대규모의 광고로 인해 rating이 만들어진 경우 장기간 특징을 정확하게 반영하기 어렵기 때문이다. 반대로, 몇몇 아이템에 대해 적대적인 유저를 대응해야할 수도 있다. 

또한 implicit dataset 시스템에서는 유저의 preference level을 점수 매기기가 어렵다. 왜냐하면 implicit은 rough binary representation으로 점수를 매기기 때문이다. (아마 좋아하는 듯, 아마 관심 없는 듯).  

이런 경우 confidence score가 도움이 될 수 있다. Confidence score는 frequency of actions을 통해 numerical value로 표현할 수 있다. 예를 들어 유저가 ceratin show를 몇 번이나 자주 봤는지, 또는 어떤 유저가 특정 아이템을 몇 번이나 자주 구매했는지가 confidence score 값이 될 수 있다. 이런 경우 each observation마다 confidence score가 될 수 있다. 이벤트가 한 번 발생할때는 다양한 이유가 있을 수 있지만 여러 번 일어나는 이벤트는 유저의 선호를 더 정확하게 반영할 것으로 해석할 수 있다. 

식에서는 confidence score은 cui로 표현했고, 이는 u, i 좌표의 특정 observation에 대한 개별적인 confidence score라고 볼 수 있다. 

<img src="https://user-images.githubusercontent.com/68208055/216272620-6c4fa0db-76ad-499f-9b79-bc6dc31a2005.png" height=130>




