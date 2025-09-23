#============전역변수들================
original_set = []   #원본 집합 (예: [1,2,3])
current_set = []    #현재 만들고 있는 부분집합
all_subset =[]      #모든 부분집합들을 저장할 리스트
index = 0           #현재 고려하고 있는 원소의 인덱스
#=====================================

def initialize(input_set):
    """
    초기화 함수 정의
    원본 집합을 설정하고 모든 변수들을 초기상태로 만듦
    """
    global original_set, current_subset, all_subsets, index
    original_set = input_set[:]     #복사해서 저장
    current_subset = []             #빈 리스트로 시작
    all_subsets = []                #결과 저장할 리스트
    index = 0                       #첫 번째 원소부터 시작

def promising(current_index):
    """
    유망성 검사 함수
    - 현재 인덱스가 유효한 범위인지 확인
    - Powerset에서는 항상 True (모든 경우를 다 고려해야

    """
    # 인덱스가 집합 크기를 넘지 않으면 유망함
    return current_index <= len(original_set)

def is_solution(current_index):
    """
    해답 확인 함수
    모든 원소를 다 고려했는지 확인
    인덱스가 집합 크기와 같으면 하나의 부분집합 완성
    """
    return current_index == len(original_set)

def write_solution():
    """
    해답 출력 함수
    현재 만들어진 부분집합을 결과에 추가
    current_subset을 복사해서 저장
    """
    global all_subsets, current_subset
    all_subsets.append(current_subset[:])
    print(f'부분집합 발견: {current_subset}')

def get_children(current_index):
    """
    자식 노드들 반환 함수
    현재 인덱스의 원소에 대해 두 가지 선택이 있음
    1) 포함하는 경우(include)
    2) 포함하지 않는 경우 (exclude)
    """
    if current_index < len(original_set):
        return ['include', 'exclude']  # 두 가지 선택지
    else:
        return []  # 더 이상 선택할 원소가 없음

def make_choice(current_index, choice):
    """
    선택 실행 함수
    - include: 현재 원소를 부분집합에 추가
    - exclude: 현재 원소를 부분집합에 추가하지 않음
    """
    global current_subset, original_set

    if choice == 'include':
        current_subset.append(original_set[current_index])
        print(f"  → {original_set[current_index]} 포함: {current_subset}")
    elif choice == 'exclude':
        print(f"  → {original_set[current_index]} 제외: {current_subset}")

def undo_choice(current_index, choice):
    """
    선택 취소 함수 (백트래킹의 핵심!)
    - include했던 원소를 다시 제거
    - exclude는 원래 아무것도 안 했으니 취소할 것도 없음
    """
    global current_subset, original_set

    if choice == 'include':
        removed = current_subset.pop()  # 마지막에 추가한 원소 제거
        print(f"  ← {removed} 제거 (백트래킹): {current_subset}")
    elif choice == 'exclude':
        print(f"  ← {original_set[current_index]} 제외 취소 (아무것도 안함): {current_subset}")

# ===== 메인 백트래킹 함수 =====
def checknode(current_index):
    """
    백트래킹 메인 함수
    - 의사코드의 구조를 그대로 따름
    """
    print(f"\n=== checknode({current_index}) 호출 ===")
    print(f"현재 부분집합: {current_subset}")

    if promising(current_index):
        print(f"인덱스 {current_index}는 유망함")

        if is_solution(current_index):
            print("해답 발견!")
            write_solution()
        else:
            print(f"인덱스 {current_index}에서 선택지 탐색")
            for choice in get_children(current_index):
                print(f"\n--- {choice} 선택 ---")
                make_choice(current_index, choice)  # 선택 실행
                checknode(current_index + 1)  # 재귀 호출
                undo_choice(current_index, choice)  # 백트래킹
    else:
        print(f"인덱스 {current_index}는 유망하지 않음 (종료)")

def generate_powerset(input_set):
    """
    파워셋 생성 메인 함수
    """
    print(f"=== 파워셋 생성 시작: {input_set} ===")
    initialize(input_set)
    checknode(0)  # 인덱스 0부터 시작
    print(f"\n=== 최종 결과 ===")
    print(f"모든 부분집합: {all_subsets}")
    return all_subsets

# ===== 사용 예시 =====
if __name__ == "__main__":
    # 간단한 예시로 [1, 2] 집합의 파워셋 구하기
    result = generate_powerset([1, 2])
    print(f"\n[1, 2]의 파워셋: {result}")