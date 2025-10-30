import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print(data)
    # 조사를 한다. 어디서부터 어디까지 어떻게?
    '''
        N: 9, M: 3
        0 1 2 3 4 5 6 7 8 9
        1 2 4 4 6 7 ...
        
        0 1 2
        1 2 4
        3 4 5
        4 6 7
        . . .
        
    '''
    result = 0  # 최종 결괏값. 각 윈도우마다 단순 증가 패턴인 경우 1씩 증가할 것.
    for i in range(0, N, M):
        # print(i)
        # 내가 조사를 해야하는 범위에 대해서만
            # i:i + M-1
        # 이번 윈도우 범위에 대해서만 단순 증가 패턴인지 찾자!
        search_data = data[i:i+M]
        # print(search_data)
        now = search_data[0]
        # 값이 단 한개여서 아래의 for문으로 검사를 진행할 일이 없어도 성공으로 간주
        is_valid = True
        for next in search_data[1:]:
            # next가 now보다 크다?
            if now < next:
                now = next  # 다음 조사하러 가기 위해 now 업데이트
            # 아니다? 조사 종료
            else:
                is_valid = False
                break
        # 이번 조사 대상 search_data를 가지고 조사를 끝냈을때
        # 정상적으로 끝가지 조사를 마쳤는지 알고 싶어
        if is_valid:    # 이번 조사대상 search_data는 단순 증가 패턴을 만족했니?
            result += 1 # 네
    print(f'#{tc} {result}')











