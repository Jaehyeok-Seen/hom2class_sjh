import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_station = list(map(int, input().split()))

    current_position = 0 # 버스가 있는 곳 (처음엔 0)
    charge_cnt = 0  # 충전 횟수 0으로 초기화

    while current_position + K < N:
        next_position = 0 #다음 이동할 곳을 0으로 만들어두고 아래에서 할당
        for station in charge_station: #충전소 위치를 풀어와서 현재 이동가능한 범위 내에 있는 걸 찾아낸다
            if current_position < station <= current_position + K:
                next_position = station


        if not next_position:
            charge_cnt = 0
            break

        current_position = next_position
        charge_cnt += 1

    print(f'#{tc} {charge_cnt}')
















    # while current_position + K < N:  # 아직 종점까지 못 가면 반복
    #     next_station = 0  # 다음에 갈 충전소
    #
    #     for station in charge_station:  # 모든 충전소를 반복으로 풀어서
    #         if current_position < station <= current_position + K: #파이썬에서는 and생략하고 이렇게 가능함
    #             next_station = station  # 가장 멀리 있는 충전소로 계속 갱신
    #
    #     if not next_station  :  # 갈 수 있는 충전소가 없으면
    #         cnt = 0  # 도착 불가능 → 0
    #         break
    #
    #     current_position = next_station  # 그 충전소로 이동
    #     cnt += 1  # 충전 횟수 +1
    #
    # print(f"#{tc} {cnt}")