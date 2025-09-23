'''
 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

'''

import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())
for tc in range(1,T+1):
    iron_list = input()
    #하나씩 다풀어서 리스트에 담아두기

    stack = []
    iron_list = iron_list.replace('()','1')
    cut_iron = 0
    for iron in iron_list:
        if iron == '(':
            stack.append(iron)
        elif iron == ')':
            cut_iron += 1
            stack.pop()
        else:
            cut_iron += len(stack)

    print(f'#{tc} {cut_iron}')

    # ===========스택 구성,초기화

    stack = []      # 빈리스트 생성
    cut_iron = 0    # 잘려나온 철의 개수 (답)

    #=============반복돌려서 스택 사용
    for i in range(len(iron_list)):
        # '('는 일단 stack에 쌓기
        if iron_list[i] == '(':
            check =1
            stack.append('(')

        # ')'인 경우에는
        else:
            stack.pop()
            #철봉의 끝이냐 레이저냐 구분

            if check == 1: #곧바로 닫힌괄호가 올 경우 이는 레이저가 된다.
                cut_iron += len(stack)
                check = 0
            else :
                cut_iron += 1
            check = 0

    print(f'#{tc} {cut_iron}')
            #레이저가 확정난다면 레이저 기준으로 스택에 있는 개수만큼 조각이 늘어난다.
    #
    #
    #
    #
    #
    # # ')'를 만나게 되면 철봉의 길이 그러나 바로 '('')'나오게 되면 레이저
    #
    # # 레이저의 조건 잡기
    #
    # # 언제 나무의 개수를 더하게 되는지
    #
    #
