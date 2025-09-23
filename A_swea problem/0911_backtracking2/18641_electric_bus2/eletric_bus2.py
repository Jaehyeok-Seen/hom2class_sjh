import sys
sys.stdin = open('5208_input.txt')

def bus(indx, cnt): #cnt : 충전횟수, indx:위치
    global min_cnt
    if cnt >= min_cnt:
        return

    if indx + battery[indx] >= (N-1):
        min_cnt = min(min_cnt,cnt)
        return

    #모든 경우를 탐색 (모든 충전소 시도)
    for next_station in range(indx+1,min(indx+battery[indx]+1,N-1)):
        bus(next_station, cnt +1)


T=int(input())

for tc in range(1,T+1):
    information = list(map(int,input().split()))
    N = information[0]
    battery = information[1:]+[0]
    min_cnt = float('inf')
    bus(0,0)

    print(f'#{tc} {min_cnt}')

    # greedy 전략
def greedy_bus():
    current = 0
    cnt = 0

    while current + battery[current] < N-1:
        #목적지 못 갈 때까지
        best_station = current
        max_reach = 0

        for station in range(current+1,min(current + battery[current],N-1)):
            if station + battery[station] > max_reach:
                max_reach = station + battery[station]
                best_station = station

        current = best_station
        cnt += 1
    return cnt
