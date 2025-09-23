import sys
sys.stdin = open('sample_input.txt')

def compare(month,total_cost):
    global min_result

    if total_cost >= min_result:
        return
    #이용계획 리스트를 받아 12개월을 다 돌면 종료
    if month > 12:
        min_result = min(min_result,total_cost)
        return


    # 만약 이용계획이 없는 달 즉 0이라면 끝낸다
    if schedule[month] == 0:
        compare(month +1, total_cost)
    else:
        # 1일권으로 다 사는 경우
        compare(month + 1, total_cost + (schedule[month] * day_p))
        # 1달권으로 다 사는 경우
        compare(month + 1, total_cost + month_p)
        # 3달권으로 다 사는 경우
        compare(month + 3, total_cost + three_month_p)
        # 1년권으로 다 사는 경우
        compare(month + 12, total_cost + year_p)


T=int(input())
for tc in range(1,T+1):

    day_p, month_p, three_month_p, year_p = map(int,input().split())
    schedule = [0] + list(map(int,input().split())) #리스트와 리스트 더해서 인덱스 편하게
    min_result = 100000000

    compare(1,0)

    print(f'#{tc} {min_result}')

"""
가장 적은 비용으로 수영장을 이용할 방법탐색
1일 이용권 
1달 이용권
3달 이용권 : 11월 12월에도 3달 이용권 사용가능
1년 이용권
가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램 작성
모든 종류의 이용권 요금은 10 이상 3,000 이하의 정수이다.

"""

