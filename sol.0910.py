import sys
sys.stdin = open('sample_input.txt')
"""
재료는 총 N개
음식별 재료는 N//2 만큼 뽑아서 요리를 진행 (조합_ 순서는 상관x)
 - 재료를 뽑는 순서는 상관없음 => 순열 X
 
음식 재료 N//2 중에서 2개씩 요리
 - 재료를 뽑는 순서는 상관 없음 = > 순열 X( 조합 )
 - 해당 재료를 뽑아서 요리를 했을 때의 총합을 구해서
 - A와 B의 차이를 계산하고 
 - 최소 값을 찾으면 끝
"""
#target : 뽑으려는 원래 리소스
#r :  몇 개를 뽑아야 하는지 선택하는 값
#choice : 현재 뽑은 요소가 들어있는 리스트
#start : 뽑는 요소의 인덱스 정보를 갱신
# [(1,2),(1,3),(1,4),...., (3,4)]반환이 되도록
def combination(target, r ,choice,start):
    result = []
    if len(choice) == r: # 뽑은 갯수가 목표하는 개수와 동일하면 종료
        result.append(choice[:]) # choice가 주소이기 때문에 원본이 바뀌면 append된 choice
        print(*choice, result)
        return result

    for idx in range(len(target)):
        choice.append(target[idx]) # 선택
        combination(target, r, choice, idx+1) # idx를
        choice.pop() #다른 선택을 위해 현재 선택된 값을 제거


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    S = [list(map(int,input().split()))]
    # 재료는 0번 부터 시작으로 진행
    ingredient_list = list(range(N))  # 모든 재료
    ingredient_a_list = combination(list(range(N)), N//2, [], 0)

    min_value = float('inf')
    # 절반의 조합 리스트에서 하나씩 조합을 꺼내 계산을 진행
    for ingredient_a in ingredient_a_list:
        # b의 재료는 모든 재료에서 a의 재료를 제외한 재료
        # ingredient_b = [for ingred in list(range(N)) if ingred not in ingredient_a]
        ingredient_b = list(set(range(N)) - set(ingredient_a))

        # 뽑은 재료에서 2개씩 뽑아 요리를 진행
        synergy_a = 0
        for i,j in combination(ingredient_a, 2, [], 0):
            synergy_a += S[i][j] + S[j][i]

        synergy_b = 0
        for i, j in combination(ingredient_b, 2, [],0):
            synergy_b += S[i][j] + S[j][i]
        min_value = min(min_value, abs(synergy_a-synergy_b))



    print(f'#{tc}', min_value)
