"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
def pre_order(T):
    if T > 0:
        print(T, end=' ')    # 현재 노드 출력
        pre_order(left[T])   # 왼쪽 서브트리 순회
        pre_order(right[T])  # 오른쪽 서브트리 순회




V = int(input()) # 정점의 수
E = V-1
arr = list(map(int,input().split()))

parent = [0]*(V+1) #정점의 수에 맞춰 인덱스로 저장하기 위해 처음 0을 비워두고
left = [0]*(V+1)   #정점의 수 +1 만큼 빈 리스트들을 부모 왼쪽 오른쪽 만들어둔다.
right = [0]*(V+1)

for i in range(E): #간선의 수만큼 반복돌려서 꺼내고
    p = arr[i*2]   #두개씩 담겨있는 리스트에서 부모인자 자식 인자 받아와야하니 x2 x2+1 이렇게 받아온다.
    c = arr[i*2+1]
    parent[c] = p

    if left[p] == 0: # 이조건은 필수
        left[p] = c
    else:
        right[p] = c

root = 1 #시작이 뿌리인 1로 가정해두고
for j in range(1, V+1):
    if parent[j] == 0: #j의 부모가 없는 경우 그 j는 루트다.
        root = j
        break

pre_order(root)

# 5번 노드의 조상 찾기
current = 5
ancestors = []

while parent[current] != 0:  # 루트까지 올라가기
    parent_node = parent[current]
    ancestors.append(parent_node)  # 조상 리스트에 추가
    current = parent_node          # 부모로 이동

