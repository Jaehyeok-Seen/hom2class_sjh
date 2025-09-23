import sys
sys.stdin = open('input.txt')

"""
학생이 방으로 돌아가야함

복도를 이용해서 돌아가야 하는데 경로가 중복되면 기다렸다가 갈 수 있음

방 앞의 복도의 사용횟수를 카운팅하고
중복되는 횟수의 복도는 기다린 횟수로 판단할 수 있음

복도의 사용횟수를 조사하면 최소 단위 시간을 판단할 수 있음

방 앞의 복도를 구별해야 함
1,2번방= > ??
3,4번방= > ??

단순히 방이 2개라 2를 나눠서 어떻게 하면 되는데
현재 방 번호로는 상당히 패턴 잡기가 까다로움
현재 방번호에서 -1을 하고 나누기 2를 한 몫을 복도의 인덱스로 가져가면 됨

1,2번방  => 0번 복도
3,4번방 = > 1번 복도
...
399,400번방 = > 199번 복도
총 200개의 복도가 필요.

1번에서 4번으로 이동하면, 0,1 번 복도가 사용됨
3번에서 6번으로 이동하면, 1,2번 복도가 사용됨
여기에서 1번 복도가 2번사용되기 때문에 2번의 단위 시간이 필요함
"""
T= int(input())
for tc in range(1,T+1):
    N = int(input()) #돌아가야할 학생 수
    bokdo_list = [0] * 200 #복도 리스트
    for _ in range(N):
        start_room, end_room = map(int, input().split())

        # 맹점: 큰번호 방에서 작은 방 번호로 돌아가는 경우가 range특성상 빠지게 된다.
        # 항상 문제에는 없어도 역으로 돌아가는 경우를 고려해야 함!
        if start_room > end_room:
            start_room, end_room = end_room, start_room
            # 해당 방의 복도를 계산
        start_bokdo = (start_room - 1) // 2
        end_bokdo = (end_room - 1) // 2

        for i in range(start_bokdo, end_bokdo +1): #끝나는 방 앞 복도까지 사용
            bokdo_list[i] +=1

    #모든 학생들이 돌아갔다면 사용된 복도의 횟수가 bokdo_list에 카운팅됨
    print(f"#{tc} {max(bokdo_list)}")
