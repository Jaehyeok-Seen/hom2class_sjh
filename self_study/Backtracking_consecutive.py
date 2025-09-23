# # swea 강의 교안에 나온느 순열을 구하는 백트래킹 알고리즘
# def construct_candidates(a, k, input, c):
#     in_perm =[False]*NMAX
#
#     for i in range(1,k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(1, input+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#         return ncandidates

"""
부분집합의 개수 = 2**n

"""


# 순열 생성 알고리즘 (Backtracking)

# def generate_permutations(arr):
#     """
#     주어진 배열의 모든 순열을 생성하는 함수
#     """
#     result = []  # 모든 순열을 저장할 리스트
#     P = arr[:]  # 원본 배열 복사 (원본 보호)
#     N = len(P)  # 배열 길이
#
#     def f(i, N):
#         """
#         i: 현재 결정할 위치
#         N: 전체 길이
#         """
#         print(f"f({i}, {N}) 호출 - 현재 P: {P}")
#
#         if i == N:  # 순열 완성
#             print(f"  → 순열 완성: {P}")
#             result.append(P[:])  # 복사해서 저장
#         else:
#             print(f"  → 위치 {i}에 올 수 있는 후보들 탐색")
#             for j in range(i, N):  # i부터 N-1까지
#                 print(f"    j={j}: P[{i}]와 P[{j}] 교환 시도")
#
#                 # 교환 전 상태 출력
#                 print(f"      교환 전: {P}")
#
#                 # P[i]와 P[j] 교환
#                 P[i], P[j] = P[j], P[i]
#                 print(f"      교환 후: {P}")
#
#                 # 다음 위치로 재귀 호출
#                 f(i + 1, N)
#
#                 # 백트래킹: 교환 되돌리기
#                 P[i], P[j] = P[j], P[i]
#                 print(f"      복원 후: {P} (백트래킹)")
#
#     print(f"=== 순열 생성 시작: {arr} ===")
#     f(0, N)  # 0번 위치부터 시작
#     print(f"=== 최종 결과 ===")
#     print(f"모든 순열: {result}")
#     return result
#
#
# # 간단한 예시로 [1, 2] 테스트
# if __name__ == "__main__":
#     print("=== [1, 2] 순열 생성 ===")
#     result1 = generate_permutations([1, 2])
#
#     print("\n" + "=" * 50)
#     print("=== [1, 2, 3] 순열 생성 ===")
#     result2 = generate_permutations([1, 2, 3])


def generate_permutations(arr):
    """
    주어진 배열의 모든 순열을 생성하는 함수
    """
    result = []  # 모든 순열을 저장할 리스트
    P = arr[:]  # 원본 배열 복사 (원본 보호)
    N = len(P)  # 배열 길이

    def f(i, N):
        """
        i: 현재 결정할 위치
        N: 전체 길이
        """
        if i == N:  # 순열 완성
            result.append(P[:])  # 복사해서 저장
        else:
            for j in range(i, N):  # i부터 N-1까지
                # P[i]와 P[j] 교환
                P[i], P[j] = P[j], P[i]

                # 다음 위치로 재귀 호출
                f(i + 1, N)

                # 백트래킹: 교환 되돌리기
                P[i], P[j] = P[j], P[i]

    f(0, N)  # 0번 위치부터 시작
    return result


# 사용 예시
if __name__ == "__main__":
    result1 = generate_permutations([1, 2])
    print(f"[1, 2] 순열: {result1}")

    result2 = generate_permutations([1, 2, 3])
    print(f"[1, 2, 3] 순열: {result2}")