arr = ['a', 'b', 'c']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1: #0x1 = 1 (16진법 표기) 0x1 = 001 (이진법)
            #즉, tar & 0x1 = tar & 1과 똑같음
            print(arr[i], end='')
        tar >>= 1
   #위에는 자리비교

for tar in range(1 << n):
    print('{',end= '')
    get_sub(tar)
    print('}')
#

problem_arr = ['A','B','C','D','E']
N = len(problem_arr)
result = []
def finding_subset(target):
    subset = [] #이부분 추가해야한다. 현재 부분집합
    for i in range(N):
        #0,1,2,3,4,
        if target & 0x1: #참이라면
            subset.append(problem_arr[i])
            print(problem_arr[i],end='')
        target >>= 1
    result.append(subset) #완성된 부분집합을 결과에 추가

for target in range(1<<N):
    print('{', end='')
    finding_subset(target)
    print('}')

count = 0
for my_subset in result:
    if len(my_subset) >= 2:
        count += 1
print(count)

#================================================================================================
# ============== 첫 번째 예제: 기본 비트마스킹 부분집합 ==============
arr = ['a', 'b', 'c']
n = len(arr)  # 3


def get_sub(tar):
    """
    비트마스킹으로 부분집합을 출력하는 함수
    tar: 부분집합을 나타내는 이진수 (예: 5 = 101(2) = {a, c})
    """
    for i in range(n):  # 각 배열 원소에 대해
        if tar & 0x1:  # 0x1 = 1 (16진법) = 001(2)
            # tar의 맨 오른쪽 비트가 1이면 현재 원소 포함
            print(arr[i], end='')
        tar >>= 1  # tar를 오른쪽으로 1비트 시프트 (다음 비트 확인)


# 모든 부분집합 생성: 2^n = 2^3 = 8가지
for tar in range(1 << n):  # 1 << n = 2^n = 8 (0부터 7까지)
    """
    tar 값에 따른 이진수와 부분집합:
    0 = 000(2) = {} (공집합)
    1 = 001(2) = {a}
    2 = 010(2) = {b}  
    3 = 011(2) = {a,b}
    4 = 100(2) = {c}
    5 = 101(2) = {a,c}
    6 = 110(2) = {b,c}
    7 = 111(2) = {a,b,c}
    """
    print('{', end='')
    get_sub(tar)
    print('}')

print("\n" + "=" * 50)

# ============== 두 번째 예제: 부분집합을 리스트로 저장 ==============
problem_arr = ['A', 'B', 'C', 'D', 'E']
N = len(problem_arr)  # 5
result = []  # 모든 부분집합을 저장할 리스트


def finding_subset(target):
    """
    부분집합을 생성해서 result 리스트에 저장하는 함수
    """
    subset = []  # 현재 부분집합을 담을 임시 리스트

    for i in range(N):  # 0,1,2,3,4 (각 배열 인덱스)
        if target & 0x1:  # 현재 비트가 1이면
            subset.append(problem_arr[i])  # 해당 원소를 부분집합에 추가
            print(problem_arr[i], end='')  # 화면에도 출력
        target >>= 1  # 다음 비트로 이동

    result.append(subset)  # 완성된 부분집합을 전체 결과에 추가


# 모든 부분집합 생성: 2^5 = 32가지
for target in range(1 << N):  # 0부터 31까지
    print('{', end='')
    finding_subset(target)
    print('}')

print("\n" + "=" * 50)

# ============== 원소가 2개 이상인 부분집합 개수 세기 ==============
count = 0
for my_subset in result:
    if len(my_subset) >= 2:  # 부분집합 크기가 2 이상이면
        count += 1

print(f"원소가 2개 이상인 부분집합 개수: {count}")

# ============== 비트마스킹 동작 원리 설명 ==============
print("\n비트마스킹 동작 원리:")
print("예시: target = 5 (101₂)일 때")
print("i=0: 101 & 001 = 001 (True) → A 포함")
print("i=1: 010 & 001 = 000 (False) → B 제외")
print("i=2: 001 & 001 = 001 (True) → C 포함")
print("결과: {A, C}")