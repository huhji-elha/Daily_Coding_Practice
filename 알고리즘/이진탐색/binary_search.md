[🏠 main으로](../../README.md)

# 이진 탐색 알고리즘

순차 탐색 : 리스트안에 있는 특정한 데이터를 찾기 위해 앞에서부터 탐색하는 방법.
이진 탐색 : **정렬되어 있는 리스트**에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법.
- 이진 탐색은 시작점, 끝점, 중간점을 이용해 탐색 범위를 설정한다.
- 각 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 밑이 2인 log N에 비례한다.

### 재귀함수로 이진 탐색 구현하기

* array는 반드시 정렬되어 있어야 함을 기억하기

```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
```

