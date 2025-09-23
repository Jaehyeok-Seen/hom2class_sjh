"""
이진 검색을 하기 위한 전제 조건: 자료가 정렬된 상태여야함

binary search = 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고
검색을 계속 진행하는 방법이다.

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자하는 목표 값을 비교
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색 수행, 크다면 자료 오른쪽 반
   에 대해서 새로 검색을 수행
4. 찾고자 하는 값을 찾을 때까지 1~3과정을 반복
"""
# 알고리즘 구현
# 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가작업
# 필요, 시작점과 종료점을 이용하여 검색을 반복 수행


def binarySearch(arr, N, key) #key를 찾으면 인덱스, 실패하면 -1반환
        start = 0
        end = N=1 #인덱스를 의미하니까 -1해줘야함
        while start <= end:
                middle = (start + end)//2
                if arr[middle] == key # 검색 성공을 의미
                    return middle
                elif arr[middle] > key:
                    end = middle - 1
                else:
                      end = middle + 1
        return -1



###재귀 함수 이용
## 자기 자신을 호출하면서 문제를 작게 만들어가는 함수
#elif에서 계속 값을 줄여가기 때문에 탈출하게 되는 조건을 if로 먼저 선언하고 코딩
def binarySearch2(a, low, high, key) :
    if low > high : # 검색 실패
        return False
    else:
        middle = (low + high) //2
        if key == a[middle] :
            return True
        elif key < a[middle] :
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
             return binarySearch2(a, middle+1,high, key) 

