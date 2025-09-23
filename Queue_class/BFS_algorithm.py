from collections import deque


# deque는 양쪽에서 삽입/삭제가 O(1)인 자료구조
# list의 pop(0)은 O(n)이라 비효율적이므로 deque 사용

def BFS(graph, start, visited):
    # BFS 함수 정의: 그래프, 시작점, 방문리스트를 매개변수로 받음

    queue = deque([start])
    # 큐를 deque로 생성하고 시작점을 넣어서 초기화

    while queue:
        # 큐가 비어있지 않으면 계속 반복 (큐에 노드가 있으면 True)

        v = queue.popleft()
        # 큐의 왼쪽(앞)에서 노드를 하나 꺼내서 v에 저장 (FIFO)

        visited[v] = True
        # 현재 노드 v를 방문했다고 표시

        print(v, end=' ')
        # 방문한 노드를 공백과 함께 출력 (줄바꿈 없이)

        for i in graph[v]:
            # 현재 노드 v와 연결된 모든 인접 노드들에 대해 반복

            if not visited[i]:
                # 인접 노드 i가 아직 방문하지 않았다면

                queue.append(i)
                # 그 노드를 큐의 오른쪽(뒤)에 추가


if __name__ == "__main__":
    # 스크립트가 직접 실행될 때만 아래 코드 실행

    graph = [
        [],  # 0번 인덱스는 사용 안함
        [2, 4, 5],  # 1번 노드는 2,4,5와 연결
        [1, 6],  # ← 여기 쉼표 누락! [1,6], 로 수정 필요
        [4],  # 3번 노드는 4와 연결
        [1, 3, 7],  # 4번 노드는 1,3,7과 연결
        [1, 8],  # 5번 노드는 1,8과 연결
        [2],  # 6번 노드는 2와 연결
        [4],  # 7번 노드는 4와 연결
        [5],  # 8번 노드는 5와 연결
    ]
    # 인접 리스트로 그래프 표현 (양방향 그래프)

    visited = [False] * 9
    # 9개 노드(0~8)에 대한 방문 여부를 False로 초기화

    BFS(graph, 1, visited)
    # 1번 노드부터 BFS 탐색 시작



def BFS(G, v, n ): #그래프 G, 탐색 시작점 v
    visited = [0]*(n+1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:                #큐가 비어있지 않은 경우
        t = queue.pop(0)        # 큐의 첫번째 원소 반환
        visit(t)
        for i in G[t]:          #t와 연결된 모든 정점에 대해
            if not visited[i]:  #인큐되지 않은 곳이라면
                queue.append(i)     #큐에 넣기
                visited[i] = visited[t] + 1     #n으로 부터 1만큼