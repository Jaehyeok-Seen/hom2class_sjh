'''
수식문자열을 읽어서 후위 표기법으로 나타내시오 연산시키는거 아님 그냥 표현만
2+3*4/5 예를 들면 아래와 같이 출력된다.
2 3 4 * 5 / +
입력 예시
2
2+3*4/5
(6+5*(2-8)/2)

'''
def my_push(top, stack, item):
    if top == -1:  # 비어있다면 push가능
        top += 1
        stack[top] = item
    elif top == len(stack) - 1:
        raise AttributeError('overflow')
    else:
        top += 1
        stack[top] = item
    return top, stack


def my_pop(top, stack):
    if top == -1: # 비어있다면 pop불가
        raise AttributeError('Empty')
    item = stack[top]
    top -= 1
    return item

# 우선순위 부터 구현
# ICP = in coming priority
# ISP  = in stack priority
ICP = { '(' : 0 , '+': 1, '-': 1, '*': 2, '/': 2, ')': '-'} #'-'는 내가 알아보는 특이 케이스에 대한 정의
ISP = { '(' : 3 , '+': 1, '-': 1, '*': 2, '/': 2, ')': '-'}
#')'는 특이 케이스 만나게 된다면 그 즉시 pop해서 연산하는 작업 실시


def postfix(expression):
    global top,stack # 읽어올때는 괜찮으나 수정을 원할 때는 전역변수로 받아야한다.
    result = ""
    for char in expression: # 리스트에서 하나씩 꺼내서 비교
        if char.isdigit(): #만약 값이 정수라면
            result += char +' ' # 후위표현식에는 숫자와 숫자 사이 공백 필요
        elif char== ')':  # ')'기호라면 '('를 만날때까지 pop한다.
            while len(stack[top]) >= 0:

                result += my_pop(top, stack)+' ' #pop해서 나온 token을 바로바로 공백과 함께 result에 더해준다.
                if char == '(':
                    break
        elif char == '(':
            #처음 정수 my_pop(top,stack) 다음 정수
            top, stack = my_push(top,stack,char)

        else:
            # print(stack[top],top,char)  디버깅 할 때 사용했음
            # stack에 대해 정의가 이루어져야 밑에서 호출이가능하다.
            # 최초상태가 스택이 0인경우를 정의해주지 않아서
            # 스택이 비어있을 때 비교할 대상이 없다.
            if top == -1:
                my_push(top,stack,char)

            elif ISP[char] == ISP[stack[top]]:
                token_item = my_pop(top,stack)
                my_push(top,stack,char)
                result += token_item
    return result

import sys
sys.stdin = open('sample_input.txt')

    #열린괄호를 만난다면 push한다.

T = int(input())  #테스트 케이스 2개

for tc in range(1,T+1):
    test_list = [*input()]
    top = -1
    stack = [0]*len(test_list)

    # print(test_list) ['2', '+', '3', '*', '4', '/', '5']

    print(postfix(test_list))