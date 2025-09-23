# def print_subset(bit):
#     for i in range(4):
#         if bit[i] == 1:

# bit = [0,0,0,0]
# for i in range(2) :
#     bit[0] = i      #0번 원소
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2) :
#                 bit[3] = l
#                 print_subset(bit)

# def generate_all_subsets(elements):
#     n = len(elements)              #몇개의 요소를 가지는지 n으로 지정
#     for i in range(2**n):  # 0부터 15까지
#         subset = []
#         for j in range(n):
#             if i & (1 << j):  # j번째 비트가 1인지 확인
#                 subset.append(elements[j])
#         print(f"{bin(i)} → {subset}")

# print(generate_all_subsets([2,6,8,5,2,1,0]))

def generate_all_subsets(elements):
    n = len(elements)
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(elements[j])
        print(subset)

print(generate_all_subsets([1,2,5,6,8]))

퀴즈 1 (기본 개념)
집합 {X, Y, Z} 3개 원소가 있을 때:
Q1-1. 총 몇 개의 부분집합이 생성될까요?
Q1-2. range(2**n)에서 i가 0부터 몇까지 반복될까요?
Q1-3. i=3일 때, 이진수로 표현하면?

2**3개가 생긴다.
7까지 반복
01인가?

퀴즈 2 (비트 이해)
i = 6  # 이진수: 0110
elements = ['A', 'B', 'C', 'D']
Q2-1. 6을 4자리 이진수로 써보세요
Q2-2. 이 이진수 패턴으로 만들어지는 부분집합은?
Q2-3. 왜 A와 D는 포함되지 않을까요?


퀴즈 3 (비트연산)
1 << 3 = ?
Q3-1. 위 결과를 이진수로 써보세요
Q3-2. 이것이 "3번째 위치 마스크"인 이유는?
Q3-3. 7 & (1 << 3)의 결과는? (7 = 0111)

퀴즈 4 (코드 추적)
pythoni = 5, j = 1일 때
if i & (1 << j):
Q4-1. 1 << 1의 결과는?
Q4-2. 5 & (1 << 1)을 단계별로 계산해보세요
Q4-3. 조건문 결과는 True/False?
하나씩 답해보세요! 틀려도 괜찮으니 생각나는 대로 써보세요 😊