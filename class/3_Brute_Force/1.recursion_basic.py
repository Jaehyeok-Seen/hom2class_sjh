# 단순하게 작성하면 약 1,000번 정도 깊이에서 제한이 걸린다
    # maximum recursion depth exceeded
# 대부분 종료 조건과 함께 활용됨
#  - 자연스럽게 다음 재귀호출을 하지 않도록 구성

# 파라미터 n : 누적값
def KFC(n):
    if n == 3:  # 종료조건(기저조건 - base case) : 3
        return
    
    print(n, end=' ')
    KFC(n + 1)
    KFC(n + 1)
    print(n, end=' ')


KFC(0)  # 시작점 : 0
