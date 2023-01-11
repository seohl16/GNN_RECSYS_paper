# Studied GCN 
GCN은 graph structured data를 사용해서 semi-supervised learning을 적용한 모델 

It works on simple nodes that are connected with edges like papers citing each others. 


## Contribution 
GCN 논문의 두 가지 contribution이 있다. 

1. 그래프에 직접적으로 적용할 수 있는 간단한 layer wise propagation rule을 도입했다. 
2. semi supervised node classification task에서 잘 작동하는 것을 보인다.

## Concepts 
### Transductive 
GCN은 다수의 노드가 레이블이 없을 때 노드 레이블을 추측하는 태스크에서 성능을 확인한 모델이다. 

하나의 그래프에서 다수 노드가 레이블이 없을 때 transductive 관점으로 볼 수 있다. 

여기서 *Transductive*이란 *unlabeled data*에 대해서 특성을 활용해 새로운 예측을 진행하는 것을 의미한다. 

반대로 *inductive*은 *labeled 노드*를 참고해서 읽는 방식으로, supervised 방식으로 볼 수 있다. 

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/456414b0-3d3d-4c79-b98f-78cacdf3e9bf/transduction-image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230103T083813Z&X-Amz-Expires=86400&X-Amz-Signature=8341de05367232cb20d7838189f210bcb3eb0990e85cddface2cfdafe4692db7&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22transduction-image.PNG.png%22&x-id=GetObject)

출처 :  [Transduction Wikipedia](https://en.wikipedia.org/wiki/Transduction_(machine_learning))

위 그림을 바탕으로 Inductive와 Transductive의 차이를 살펴보겠다. 

Inductive approach는 labeled point들을 일단 학습하고 이를 이용해서 주변 unlabeled point에 대한 label을 예측하게 한다. 

여기서 문제점은 이 approach의 모델은 소수의 노드로만 학습을 진행할 수 밖에 없고, 클러스터를 학습하지 않아 성능이 좋지는 않을 것이라는 점이다. 

만약 그림에서 빨간색으로 묶인 가운데의 점들을 예측할 때 Inductive 모델을 활용하면 A나 C일 확률이 높아진다. \
왜냐하면 inductive model은 모여있는 클러스터를 보지 않고 단순히 A, C의 point 들과의 거리를 확인할 것이기 때문이다.

Transductive approach는 모든 데이터의 이점을 취하게 된다. 이때는 그들이 실제로 묶여진 cluster를 참고해서 묶이게 된다. 

다시 그림에서 예시를 들면, 같은 빨간색 점들을 transductive algorithm으로 예측하게 되면 이제 B로 예측할 확률이 높아진다. 그 이유는 다른 점들도 고려하게 되어 B에 모여있는 점이 하나의 클러스터로 학습될 가능성이 높아지기 때문이다.

### Smoothing and Laplacian regularization

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/92e8e416-c039-4801-a932-93f785d5caad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230103T084216Z&X-Amz-Expires=86400&X-Amz-Signature=e21641947208b2374a9a174befeba48c5b147f395caf07b3a0a96e29ad2e6aff&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

GCN에 학습할 대상은 레이블이 매우 적은 데이터이다.    

라플라시안 정규화를 loss function에 추가해서 과적합을 막았다. 

### Layer wise propagation rule

gcn is similar to densenet, conv2dnet’s layers. It has activation function and input and output. 

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fab80614-accf-466f-bd0e-d64e54f2f20c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230103T084155Z&X-Amz-Expires=86400&X-Amz-Signature=90949c7176f031a59089a130eff1a6f75ce6fcbc07e633a518a32a4f3b823b81&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

GCN에서 정의한 layer wise propagation rule은 다음 그림과 같다. 

H는 레이어의 아웃풋을 의미하며 H0은 입력 X, H1은 첫번째 레이어의 아웃풋이라고 볼 수 있다. H(l+1)은 H(l)번째 layer의 propagation 결과를 수식에 넣은 output이라고 볼 수 있다.

## Reference

[https://hyelimkungkung.tistory.com/57](https://hyelimkungkung.tistory.com/57)

[https://github.com/dmlc/dgl/tree/master/examples/tensorflow/gcn](https://github.com/dmlc/dgl/tree/master/examples/tensorflow/gcn)

[https://thejb.ai/gcn/](https://thejb.ai/gcn/)

[https://github.com/dmlc/dgl/issues/2322](https://github.com/dmlc/dgl/issues/2322)

[https://d2l.ai/chapter_multilayer-perceptrons/backprop.html](https://d2l.ai/chapter_multilayer-perceptrons/backprop.html)
