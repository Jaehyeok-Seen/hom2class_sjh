import sys
sys.stdin = open('input.txt')

def find_leader(x):
    if x != leader[x]:
        leader[x] = find_leader(leader[x])
    return leader[x]

def union(x, y):
    root_x = find_leader(x)
    root_y = find_leader(y)

    if root_x < root_y:
        leader[root_y] = root_x
    else:
        leader[root_x] = root_y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # 총 만들어진 조의 개수
    result = 0
    '''
        아이디어
        1. 처음에 조의 관계를 어떻게 만들어야 할까?
            -> 문제에서 혼자 1인 조를 구성 할 수도 있다고 했음.
            -> 우리는 최초 상태를 모두가 전부아무도 아무를 지정안했을 때도 가정
        2. A가 B를 지목하면, A와 B는 한 조가 된다.
        2-1. B가 C를 지목하면, A, B, C는 모두 한 조가 되어야 한다.
            -> A, B, C가 한 조라는걸 알려면? 팀 이름을 정하거나... 아니면 대표 한명을 정해서
            -> A야 너네조 이름이 뭐야? B야 너네조... C야 너네조...
            -> 셋다 같은 이름이 나와야지 그걸 우리는 한 조라고 부를 수 있다.
        3. 신청서가 M장 있다. M장에 대한 정보는?
            M = 3
            A -> B를
            B -> C를
            D -> E를
            [A, B, B, C, D, E] -> 6명의 정보가 들어있네?
    '''
    # 학생은 1번부터 시작해서, N번까지 있다. 그래서 자기 자신을 조장으로 만들어야 한다.
    # 인덱스 0번은 안쓸꺼임!
    leader = list(range(N+1))
    # print(leader)
    '''
        M = 3
         0  1  2  3  4  5
        [A, B, B, C, D, E]
        0번째 신청서 -> A -> B (0, 1)
        1번째 신청서 -> B -> C (2, 3)
        2번째 신청서 -> D -> E (4, 5)
        ...
        M번째 신청서 -> (M*2, M*2+1)
    '''
    for i in range(M):
        # print(i*2, i*2+1)
        x, y = data[i*2], data[i*2+1]
        # x랑 y가 누군지 알아냈으니까?
        # 둘중 한명의 조장을 x로 바꿀까?
        # leader[y] = x
        union(x, y)
    # print(data)
    # print(leader)
    # 자, 이제 조 구성 다 끝났으니, 너네 조장 누군지 한번씩 확인해
    for i in range(N+1):
        find_leader(i)
    # print(leader)
    # 각 인원의 조장은 실존 인물로 생각하면? 1명이다.
        # 중복을 제거하자
    leader = set(leader)
    print(leader)
    result = len(leader) - 1    # 0번은 없음
    print(f'#{tc} {result}')