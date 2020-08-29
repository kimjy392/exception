# 이분탐색

> 정렬된 배열에서 시작점과 끝점으로 중간지점을 찾고 해당 지점이 이상일때 시작점을 중간지점으로 바꿔주고 이하일때 끝점을 중간지점으로 바꿔준다.

```python
def binarySearch(arr, lo, hi, key):
    if lo > hi: return -1

    mid = (lo + hi) >> 1
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, lo, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, hi, key)

def binary_search(arr, lo, hi, key):
    while lo <= hi:
        mid = (lo + hi) >> 1
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 45, 49, 62, 88]

hi = len(arr) - 1
print(sequence_search(arr, 39))
print(sequence_search(arr, 50))

print(binary_search(arr, 0, hi, 39))
print(binary_search(arr, 0, hi, 50))

print(binarySearch(arr, 0, hi, 39))
print(binarySearch(arr, 0, hi, 50))

```

* [1654. 백준 랜선 자르기](https://www.acmicpc.net/problem/1654)

  ```python
  K, N = map(int, input().split())
  lengths = []
  for _ in range(K):
      lengths.append(int(input()))
  start = 1
  end = max(lengths)
  while start <= end:
      mid = (start + end) // 2
      cnt = 0
      for length in lengths:
          cnt += (length // mid)
      if cnt < N:
          end = mid - 1
      elif cnt >= N:
          start = mid + 1
  
  print(end)
  ```

  이 문제에서는 최댓 값을 찾는 것이기 때문에 시작점을 올려서 찾아야한다. 그렇기 때문에 `=`를 시작점에 쓴 것을 볼 수 있다.

  반대로 최솟값을 찾기 위해서는 끝점을 내려야하기 때문에 `=` 끝점에 써야 한다.