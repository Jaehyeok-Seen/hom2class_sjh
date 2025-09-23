def merge_sort(m):
    # 기저 조건: 리스트 길이가 1이면 이미 정렬됨
    if len(m) <= 1:
        return m

    # 중간점 계산 (리스트를 반으로 나눌 지점)
    middle = len(m) // 2

    # 왼쪽, 오른쪽 부분 리스트로 분할
    left = m[:middle]  # 중간점 이전 원소들
    right = m[middle:]  # 중간점 이후 원소들

    # 각 부분을 재귀적으로 정렬
    left = merge_sort(left)
    right = merge_sort(right)

    # 정렬된 두 부분을 병합하여 반환
    return merge(left, right)


def merge(left, right):
    result = []  # 결과를 담을 리스트
    i, j = 0, 0  # left와 right의 인덱스

    # 둘 다 원소가 있는 동안 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 왼쪽 첫 원소 ≤ 오른쪽 첫 원소
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 왼쪽에 원소가 남았으면 모두 추가
    while i < len(left):
        result.append(left[i])
        i += 1

    # 오른쪽에 원소가 남았으면 모두 추가
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# 사용 예시
if __name__ == "__main__":
    # 테스트
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"정렬 전: {test_list}")

    sorted_list = merge_sort(test_list)
    print(f"정렬 후: {sorted_list}")

    # 단계별 과정 보기
    print("\n--- 병합 과정 예시 ---")
    left_example = [1, 4, 7]
    right_example = [2, 5, 8]
    merged = merge(left_example, right_example)
    print(f"left: {left_example}")
    print(f"right: {right_example}")
    print(f"병합 결과: {merged}")