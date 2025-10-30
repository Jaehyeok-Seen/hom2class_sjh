from collections import deque


def moving():
    bridge = deque([0] * w)  # 다리를 w 길이의 큐로 초기화 (0은 빈 공간)
    bridge_w = 0  # 현재 다리 위의 총 무게
    cnt = 0  # 경과 시간
    indx = 0  # 다음에 올라갈 트럭의 인덱스

    while indx < n or bridge_w > 0:  # 모든 트럭이 올라가고 다리가 비워질 때까지
        cnt += 1

        # 다리에서 트럭 하나 내보내기
        exited = bridge.popleft()
        bridge_w -= exited

        # 새 트럭을 다리에 올릴 수 있는지 확인
        if indx < n:
            if bridge_w + truck_w[indx] <= L:  # 무게 제한 확인
                bridge.append(truck_w[indx])
                bridge_w += truck_w[indx]
                indx += 1
            else:
                bridge.append(0)  # 트럭을 올릴 수 없으면 빈 공간 추가

    return cnt


n, w, L = map(int, input().split())
truck_w = list(map(int, input().split()))

final_result = moving()
print(final_result)