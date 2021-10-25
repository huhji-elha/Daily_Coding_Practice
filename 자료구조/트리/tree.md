[🏠 main으로](../../README.md)

# 트리 자료구조

```
🌲 트리란 계층 구조를 시뮬레이션하는 추상 자료형으로, 
루트 값과 부모-자식 관계의 서브트리로 구성되며 서로 연결된 노드의 집합이다.
```

- [트리 자료구조](#트리-자료구조)
  - [트리의 특징](#트리의-특징)
  - [그래프 vs 트리](#그래프-vs-트리)
  - [이진 트리 (Binary Tree)](#이진-트리-binary-tree)
    - [이진 트리의 직렬화와 역직렬화(Serialize vs Deserialize)](#이진-트리의-직렬화와-역직렬화serialize-vs-deserialize)
  - [이진 탐색 트리(Binary Search Tree)](#이진-탐색-트리binary-search-tree)
    - [자가 균형 이진 탐색 트리](#자가-균형-이진-탐색-트리)
    - [Tree 기본 알고리즘 풀이](#tree-기본-알고리즘-풀이)

---

## 트리의 특징

* 트리는 일상에서 쉽게 볼 수 있는 위아래 개념을 컴퓨터에서 표현한 구조이다.
* 중요한 속성 중 하나는 재귀로 정의된(Recursively Defined) 자기 참조(Self-Referential) 자료구조라는 것이다.
    즉, 트리는 여러개의 서브 트리가 쌓아 올려진 구조라고 생각할 수 있다.
    따라서 자식도 트리인 서브 트리 구성을 띈다.
* 트리는 항상 단방향 구조이다.

---

## 그래프 vs 트리
* 그래프와 트리의 핵심 차이점은 트리는 순환 구조가 아니라는 것이다.
    즉, 트리는 순환 구조를 갖지 않는 그래프이다. 
* 단방향, 양방향을 모두 구성할 수 있는 그래프와 달리 트리는 부모에서 자식 노드를 가리키는 단방향 뿐이다.
* 트리는 하나의 부모 노드만을 갖는다.
* 트리는 루트 또한 하나여야 하며, 모든 노드가 연결되어 있어야한다.


---


## 이진 트리 (Binary Tree)

트리 중에서 가장 널리 사용되는 트리 자료구조는 **이진 트리**와 **이진 탐색 트리**이다.

각 노드가 m개 이상의 자식을 가진 다항 트리도 있지만, 이진트리의 경우 최대 2개의 자식을 
갖는 간결한 형태이며 알고리즘으로 구현하는 것도 간결하게 처리할 수 있다.

이진트리의 유형은 다음과 같다.
![](https://miro.medium.com/max/16000/1*CMGFtehu01ZEBgzHG71sMg.png)

[*_reference_link*](https://towardsdatascience.com/5-types-of-binary-tree-with-cool-illustrations-9b335c430254)

* Full Binary Tree(정 이진 트리) : 모든 노드가 0 또는 2개의 자식 노드를 가진다.
* Complete Binary Tree(완전 이진 트리) : 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있다. 마지막 레벨의 노드는 왼쪽부터 채워져있다.
* Perfect Binary Tree(포화 이진 트리) : 모든 노드가 2개의 자식 노드를 갖고 있으며 모든 leaf node가 동일한 깊이를 갖는다. 가장 완벽한 모양의 트리.

### 이진 트리의 직렬화와 역직렬화(Serialize vs Deserialize)

이진 트리의 데이터 구조는 논리적인 구조이다. 실제 디스크 상에서 이러한 계층 구조로 저장되지 않는다. 
파일이나 디스크에 트리를 저장할 때는 물리적인 형태로 바꾸어주어야 하는데 이를 직렬화(Serialize)라고 한다.

반대로 물리적인 형태를 트리의 논리적인 구조로 바꾸는 작업을 역직렬화(Deserialize)라고 한다.

파이썬에는 `pickle`이라는 직렬화 모듈을 기본으로 제공한다. 이 모듈의 이름으로 인해 파이썬 객체의 계층 구조를 Byte Stream으로 변경하는 작업을 Pickling이라고도 한다.

<center><img src="https://lh3.googleusercontent.com/proxy/9tScM2YPL8NqFlRLu7A8wt2rYvOSAbYzWq6T7-pPCLanK2YQGq2DZ7yjSMeG3sZnWbJI2Rr5zOtKTyROzrYlk6BBzBmxEkwDrL2LvoqfD_pv4w"/></center>

[*_reference_link*](http://mishadoff.com/blog/dfs-on-binary-tree-array/)

아래 그림의 트리는 Complete Binary Tree로서 배열로 표현했을 때 모든 노드를 Null 값 없이 배치할 수 있다. 

**Complete Binary Tree는 트리의 특성상 배열에 빈틈없이 배치가 가능하다.** 위 그림에서는 index를 0부터 사용했지만 대개 트리의 경우 계산을 편하기 위해 index를 1부터 시작한다.


노드의 index를 알면 깊이가 얼마인지, 부모와 자식 노드가 배열의 어디에 위치하는지 바로 알아낼 수 있다. 

또한 index를 1부터 시작했을 때 트리의 깊이는 아래의 그림처럼 1, 2, 4, 8, ... 순으로 2배씩 증가하며, 현재 노드 `i`의 위치에서 부모의 위치는 `i/2`, 왼쪽 자식은 `2i`, 오른쪽 자식은 `2i+1`이 된다.

<center><img src="https://lh4.ggpht.com/-u2Lb-zvWCFE/ULBxmsa1mbI/AAAAAAAACFk/ZOAvwzAsJaU/clip_image001%25255B4%25255D_thumb%25255B1%25255D.gif?imgmax=800"/></center>

[*_reference_link*](https://www.google.com/url?sa=i&url=http%3A%2F%2Fagikarasugi2021ds.blogspot.com%2F2018%2F03%2Fpertemuan-5-tree-and-binary-tree-binary.html&psig=AOvVaw19Dt2bSsJpbT0JVo8OrliD&ust=1635078843741000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKibqNTF4PMCFQAAAAAdAAAAABAf)

---

## 이진 탐색 트리(Binary Search Tree)

이진 탐색 트리는 탐색의 효율을 높이기 위해 정렬한 트리를 말한다.

이진 트리를 정렬하는 규칙은 다음과 같다.

```
항상 노드의 왼쪽 서브트리에는 해당 노드의 값보다 같거나 작은 값들의 노드로 채워져있어야하고, 
오른쪽 서브트리에는 같거나 큰 값들로 이루어져 있어야한다.
```

이렇게 정렬했을 때 이 **트리의 탐색 시 시간 복잡도는 O(log n)이 된다.**


![](https://www.ida.liu.se/opendsa/Books/TDDC76F20/html/_images/BSTShape2.png)

[*_reference_link*](https://www.ida.liu.se/opendsa/Books/TDDC76F20/html/BST.html)

BST는 랜덤하게 생성해도 대부분의 경우 균형이 잘 맞는 왼쪽 트리와 같이 표현할 수 있지만,
균형이 많이 깨지면 오른쪽의 그래프와 같이 구성되며 이러한 경우 탐색 시 O(log n)이 아니라 **O(n)에 근접한 시간이 소요**될 수 있다.

(b) 트리와 같은 경우는 연결리스트와 다르지 않기 때문에 전혀 효율적이지 않다.

이를 해결하기 위해 고안된 것이 자가 균형 이진 탐색 트리(Self-balancing Binary Tree)이다.

### 자가 균형 이진 탐색 트리

자가 균형 이진 탐색 트리는 트리의 높이를 최대한 낮게 유지하는 것이 가능하다. 
오른쪽의 트리에서 40을 찾으려면 7번의 연산이 필요하다. 하지만 왼쪽의 트리에서는 3번만에 40을 찾을 수 있다.

만약 노드가 100만개라면 (b) 트리의 경우 100만번의 연산이 필요하다. 하지만 (a)트리와 같이 균형이 잡혀 있는 트리라면 밑이 2인 log 100만인 최대 19번에 어떤 값이든 찾아낼 수 있다.

이러한 자가 균형 이진 탐색 트리에는 **AVL 트리**와 **Red-Black 트리**가 있다.
특히 Red-Black 트리는 효율성이 높아 실무에서도 자주 사용되며 JAVA의 해시맵 또한 효율적인 저장 구조를 위해 해시 테이블의 개별 체이닝시 연결 리스트와 함께 Red-Black 트리를 사용한다.

---

### Tree 기본 알고리즘 풀이
* [BFS로 Binary Tree 구현하기](./Tree_이진_트리의_최대_깊이.py)
* [상태 값을 계산하는 DFS 트리 구현](./Tree_이진_트리의_직경.py)
* [상태 값을 계산하는 DFS 트리 응용](./Tree_가장_긴_동일값_경로.py)
* [Binary Tree 반전하기](./Tree_이진_트리_반전하기.py)
* [두 Binary Tree 합치기](./Tree_두_이진_트리_병합.py)
* [Binary Tree Serialize & Deserialize](./Tree_이진_트리_직렬화_역직렬화.py)
