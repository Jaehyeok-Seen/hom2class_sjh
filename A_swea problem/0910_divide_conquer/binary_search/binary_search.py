def binary_search(arr, target):
    """
    정렬된 배열에서 target 값을 이진 탐색으로 찾기
    찾으면 인덱스 반환, 못 찾으면 -1 반환
    """
    left = 0  # 왼쪽 끝
    right = len(arr) - 1  # 오른쪽 끝
    prev_dir = 0
    #처음에는 0으로 두고 오른쪽 방향이면 1, 왼쪽방향이면 -1

    while left <= right:  # 교차하지 않을 때까지 반복
        mid = (left + right) // 2  # 중간 인덱스

        if arr[mid] == target:  # 찾았다!
            return True
        elif arr[mid] < target:  # 중간값이 작으면
            if prev_dir == 1:
                return False
            prev_dir = 1
            left = mid + 1  # 오른쪽 절반 탐색
        else:  # 중간값이 크면
            if prev_dir == -1:
                return False
            prev_dir = -1
            right = mid - 1  # 왼쪽 절반 탐색

    return False # 못 찾음


# 메인 코드
import sys

sys.stdin = open('5207_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))  # 정렬된 리스트 A
    B = list(map(int, input().split()))  # 찾을 값들 B
    A.sort()

    count = 0  # 찾은 개수

    # B의 각 원소를 A에서 찾기
    for target in B:
        if binary_search(A,target):
            count +=1

    print(f'#{tc} {count}')