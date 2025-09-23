import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    data = list(map(int,input().split()))

    # 조사를 한다. 어디서부터 어디까지 어떻게?


    result = 0 #최종 결과값, 각 윈도우마다 단순 증가 패턴인 경우 1씩 증가할 것.
    for i in range(0,N,M):
        #print(i)
        #내가 조사를 해야하는 
    # window= [data[i:i+M] for i in range(0,N,M) if i+M <= N]


        search_data = data[i:i+M]
        print(search_data)
        now = search_data[0]

    # 값이  단 한개여서 아래의 for문으로도 검사를 진행할 일이 없어도 성공으로 간주
    is_valid = True

    for next in search_data[1:]:
        if now < next:
            now = next # 다음 조하러 가기 위해 now업데이트
        #아니다? 조사 종료
        else:
            is_valid = False
            break
    #이번 조사 대상 search_data를 가지고 조사를 끝냈을 때
    #정상적으로 끝까지 조사를 마쳤는지 알고 싶ㅇ
    if is_valid:
        result += 1
    print(result)