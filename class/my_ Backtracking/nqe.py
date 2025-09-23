# answer += 1 위치가 중요한 이유

def recur_with_explanation(row):
    global answer
    print("  " * row + f"recur({row}) 시작")

    if row == N:
        print("  " * row + f"🎉 완성! row({row}) == N({N})")
        print("  " * row + f"현재 path: {path}")
        print("  " * row + f"이것은 {answer + 1}번째 해답!")
        answer += 1  # ← 여기서 카운트!
        print("  " * row + f"answer = {answer}")
        return

    print("  " * row + f"row {row}에서 가능한 열들 탐색...")

    for col in range(N):
        if is_safe(row, col):  # 안전한 위치인지 확인
            print("  " * row + f"✅ ({row}, {col}) 안전 → 선택")
            path.append(col)
            board[row][col] = 1

            recur_with_explanation(row + 1)  # 다음 행으로

            # 백트래킹
            board[row][col] = 0
            path.pop()
            print("  " * row + f"❌ ({row}, {col}) 선택 해제")
        else:
            print("  " * row + f"❌ ({row}, {col}) 위험 → 스킵")


def is_safe(row, col):
    # 간단한 안전성 체크 (실제 N-Queen 체크보다 단순화)
    # 같은 열에 퀸이 있는지만 확인
    for i in range(row):
        if board[i][col] == 1:
            return False
    return True


# 시뮬레이션
N = 3
answer = 0
path = []
board = [[0] * N for _ in range(N)]

print("=== N-Queen 해답 카운팅 과정 ===")
print(f"N = {N}")
print("간단한 예시로 같은 열 체크만 함")
print()

# 실제 실행하면 너무 복잡하므로 개념 설명
print("=== 핵심 개념 ===")
print()
print("1️⃣ row == N에 도달했다는 것은:")
print("   - 0행부터 N-1행까지 모든 행에 퀸을 배치 완료")
print("   - N개의 퀸이 모두 배치된 상태")
print("   - 하나의 완전한 해답이 만들어진 상태")
print()
print("2️⃣ 이 시점에서 answer += 1:")
print("   - '유효한 해답 하나 발견!'")
print("   - 전체 해답 개수에 1 추가")
print()
print("3️⃣ 만약 다른 위치에 넣는다면:")

print("\n❌ 잘못된 위치 1: for문 안에서")
print("```python")
print("for col in range(N):")
print("    answer += 1  # ← 잘못!")
print("    path.append(col)")
print("```")
print("→ 모든 시도마다 카운트 (해답이 아닌데도 증가)")

print("\n❌ 잘못된 위치 2: 재귀 호출 후")
print("```python")
print("recur(row + 1)")
print("answer += 1  # ← 잘못!")
print("```")
print("→ 백트래킹할 때마다 카운트 (중복 카운트)")

print("\n✅ 올바른 위치: row == N일 때")
print("```python")
print("if row == N:")
print("    answer += 1  # ← 정확!")
print("    return")
print("```")
print("→ 완전한 해답이 만들어졌을 때만 카운트")

print("\n=== 실제 N=4 결과 예시 ===")
print("N=4일 때 가능한 해답: 2개")
print()
print("해답 1: [1, 3, 0, 2]")
print("Q . . .")
print(". . . Q")
print(". Q . .")
print(". . Q .")
print()
print("해답 2: [2, 0, 3, 1]")
print(". . Q .")
print("Q . . .")
print(". . . Q")
print(". Q . .")
print()
print("row == N에 2번 도달 → answer = 2")