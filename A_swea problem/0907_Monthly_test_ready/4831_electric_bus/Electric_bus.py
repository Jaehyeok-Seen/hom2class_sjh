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







# def electric_bus(start, can_move, charge_count): #number로 N받으면 정류장의 인덱스 리스트 만들기
#     global min_charge, charge_station, N, K
#     # can_move = K    #이동할 수 있는 수 => 이렇게 로컬변수로 선언하면 재귀호출될때마다 초기화, 위에 함수호출시 매개변수로..
#     # charge_count = 0   #현재 충전 횟수
#     if start >= N: #시작점에서 종착지에 도착한다면 종료(넘어갈 수도 있으니)
#         min_charge = min(min_charge,charge_count)
#         return
#
#     if can_move <= 0 : #갈 수 있는 칸수가 0이되면 끝 => 이부분은 생각 못함
#         return
#     # 위조건문 순서도 중요했다.
#     # 현재 연료로 목적지까지 갈 수 있다면
#     if start + can_move >= N:
#         min_charge = min(min_charge, charge_count)
#         return
#=============완전탐색=========================
    # # 충전소에 있을 때
    # if start in charge_station and start != 0:
    #     # 현재 연료로 다음 충전소에 갈 수 있는지 확인
    #     next_station = None
    #     for station in sorted(charge_station):
    #         if station > start and station <= start + can_move:
    #             next_station = station
    #             break
    #         # 다음 충전소가 없거나 너무 멀다면 반드시 충전
    #     if next_station is None or start + can_move < next_station:
    #         electric_bus(start + 1, K - 1, charge_count + 1)
    #     else:
    #         # 다음 충전소가 있다면 충전하거나 안하거나 선택
    #         electric_bus(start + 1, K - 1, charge_count + 1)  # 충전
    #         electric_bus(start + 1, can_move - 1, charge_count)  # 안충전
    #
    # else:
    #     electric_bus(start+1,can_move-1,charge_count)
#==================================
    # 충전소에서 무조건 충전 (탐욕적)
    if start in charge_station and start != 0:
        electric_bus(start + 1, K - 1, charge_count + 1)
    else:
        electric_bus(start + 1, can_move - 1, charge_count)


T= int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    charge_station = set(map(int,input().split())) #중복되지 않으니까 셋으로 검색속도 더 빠름
    """
    M = 정류장의 총 수
    N = 목표 종착지
    K = 이동할 수 있는 칸 수
    """
    min_charge = float('inf')

    electric_bus(0,K,0)

    if min_charge == float('inf'):
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {min_charge}')
#===============================================디버깅용
# import sys
#
# sys.stdin = open('sample_input.txt')
#
#
# def electric_bus(start, can_move, charge_count, path=""):
#     global min_charge, charge_station, N, K
#
#     # 디버깅용 출력
#     if charge_count <= 5:  # 너무 많은 출력 방지
#         print(f"위치: {start}, 연료: {can_move}, 충전횟수: {charge_count}, 경로: {path}")
#
#     if start >= N:
#         print(f"★ 도착! 충전횟수: {charge_count}, 경로: {path}")
#         min_charge = min(min_charge, charge_count)
#         return
#
#     if can_move <= 0:
#         print(f"✗ 연료부족, 경로: {path}")
#         return
#
#     if start in charge_station and start != 0:
#         # 충전하는 경우
#         electric_bus(start + 1, K - 1, charge_count + 1, path + f"→{start}(충전)")
#
#         # 충전하지 않는 경우 - 이 부분이 문제일 수 있음
#         if can_move > 1:
#             electric_bus(start + 1, can_move - 1, charge_count, path + f"→{start}(패스)")
#     else:
#         electric_bus(start + 1, can_move - 1, charge_count, path + f"→{start}")
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     charge_station = set(map(int, input().split()))
#
#     print(f"\n=== 테스트 케이스 {tc} ===")
#     print(f"K={K}, N={N}, 충전소={sorted(charge_station)}")
#
#     min_charge = float('inf')
#     electric_bus(0, K, 0, "시작")
#
#     if min_charge == float('inf'):
#         print(f'#{tc} 0')
#     else:
        print(f'#{tc} {min_charge}')