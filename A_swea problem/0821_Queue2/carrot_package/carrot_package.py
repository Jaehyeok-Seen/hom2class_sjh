"""
여러 크기가 있을 때 3등분하는 방법들

예시: 당근 크기 = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6]
크기별 개수: 크기1=2개, 크기2=2개, 크기3=2개, 크기4=1개, 크기5=2개, 크기6=1개
"""

# 예시 데이터
carrots_count = [0, 2, 2, 2, 1, 2, 1, 0, 0, 0, 0]  # 인덱스=크기, 값=개수
# 크기 1: 2개, 크기 2: 2개, 크기 3: 2개, 크기 4: 1개, 크기 5: 2개, 크기 6: 1개

print("크기별 당근 개수:")
for i in range(1, 11):
    if carrots_count[i] > 0:
        print(f"크기 {i}: {carrots_count[i]}개")

print()
print("=== 누적합 만들기 ===")
total_sum = [0] * 11
total_sum[1] = carrots_count[1]
for i in range(2, 11):
    total_sum[i] = carrots_count[i] + total_sum[i - 1]

for i in range(1, 11):
    print(f"total_sum[{i}] = {total_sum[i]} (크기 1~{i}까지 총 개수)")

print()
print("=== 다양한 3등분 방법들 ===")

# 경계점들을 바꿔가며 여러 방법 시도
partition_methods = [
    (2, 4),  # 소(1~2), 중(3~4), 대(5~6)
    (1, 3),  # 소(1), 중(2~3), 대(4~6)
    (3, 5),  # 소(1~3), 중(4~5), 대(6)
    (2, 5),  # 소(1~2), 중(3~5), 대(6)
]

for method_num, (i, j) in enumerate(partition_methods, 1):
    print(f"\n방법 {method_num}: i={i}, j={j}")

    small_box = total_sum[i]  # 크기 1~i
    medium_box = total_sum[j] - total_sum[i]  # 크기 i+1~j
    large_box = total_sum[10] - total_sum[j]  # 크기 j+1~10

    print(f"  소상자(크기 1~{i}): {small_box}개")
    print(f"  중상자(크기 {i + 1}~{j}): {medium_box}개")
    print(f"  대상자(크기 {j + 1}~10): {large_box}개")

    # 조건 체크
    if small_box == 0 or medium_box == 0 or large_box == 0:
        print("  → 빈 상자 있음, 불가능!")
        continue

    max_val = max(small_box, medium_box, large_box)
    min_val = min(small_box, medium_box, large_box)
    diff = max_val - min_val

    print(f"  → 최대-최소 차이: {diff}")

print()
print("=== 핵심 이해 포인트 ===")
print("1. 경계점 i, j를 바꿔가면서 모든 3등분 방법을 시도")
print("2. 크기 순으로 나누니까 같은 크기는 자동으로 같은 상자에!")
print("3. 누적합으로 각 구간의 당근 개수를 빠르게 계산")
print("4. 조건 만족하는 것 중에서 차이가 최소인 방법 선택")

print()
print("=== 왜 이 방법이 모든 경우를 다 확인하나? ===")
print("i는 1~28, j는 i+1~29까지 → 총 약 28×29/2 = 406가지 방법")
print("각 방법마다 3등분해서 조건 체크하고 최적해 갱신!")
print("→ 가능한 모든 3등분 방법을 다 시도하는 완전탐색!")