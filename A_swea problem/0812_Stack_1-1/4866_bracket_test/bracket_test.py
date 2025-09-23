import sys
sys.stdin = open('sample_input.txt')


def my_push(top,stack,item):
    if top >= len(stack)-1:
        return top,None
    top +=1
    stack[top] = item
    return top, True     # 아래 함수정의와 통일된 반환값을 정해주는 것도 중요

def my_pop(top,stack):
    if top == -1:
        return top, None
    item = stack[top]
    top -= 1
    return top, item


T = int(input())          #주어지는 테스트 문장 T개를 받아서
for tc in range(1,T+1):
    # 괄호가 제대로 짝을 이뤘는지 검사하는 프로그램
    # 열린괄호를 만나면 스택에 쌓아두고, 닫힌괄호를 
    #정상적으로 짝을 이룬경우 1, 아닌 경우 0을 출력
    str_list =  input()
    test_list = [text for text in str_list]
    # print(test_list) ['p', 'r', 'i', 'n', 't', '(', "'", '{', '}', ' ', '{', '}', "'", '.', 'f', 'o', 'r', 'm', 'a', 't', '(', '1', ',', ' ', '2', ')', ')']
    # 출력 확인
    top = -1
    result = 1
    stack = [0]*len(test_list)
    for check in test_list: #test_list에서 하나씩 꺼내서 확인

        #열린 괄호를 만나게 된다면
        if check in '[({': 
            top,success = my_push(top,stack,check) # push함수 사용해서 스택에 push, 함수로 리턴값을 어디다가 저장하지 않는 실수 함
        

        #닫힌 괄호의 경우
        elif check in '])}':
            top,item = my_pop(top,stack)

            if item is None:  # 닫힌 괄호를 만나서 pop했는데 item이 없게 나온다면 짝이 안맞는거니까
                result = 0
                break

            elif (item == '(' and check ==')') or (item == '[' and check == ']') or (item == '{' and check == '}'):
                #괄호의 짝을 맞춰본다. 맞을 경우만 계속하게끔
                continue
            else:
                result = 0  # 매칭 실패
                break


    if result == 0 or top != -1:  # 문제 몇개가 오답이라 수정하게 됐다. 오답의 경우를 조금더 세분화해서 명시하자
        result = 0
    else:
        result = 1

    print(f'#{tc} {result}')





















# T = int(input())
# for tc in range(1,T+1):
#     #주어지는 테스트 문장 T개를 받아서
#     #괄호가 제대로 짝을 이뤘는지 검사하는 프로그램
#     #정상적으로 짝을 이룬경우 1, 아닌 경우 0을 출력
#     str_list =  input()
#     test_list = [tt for tt in str_list]

#     top = -1
#     stack = [0]*(len(test_list))
#     result = 1   #성공이라고 가정하자

#     for char in str_list:
#         if char in '({[':  # 열린 괄호
#             top = push(stack, top, char)
#         elif char in ')}]':  # 닫힌 괄호
#             top, popped_item = pop(stack, top)
#             if popped_item is None:  # 스택이 비어있음
#                 result = 0
#                 break
#             if (popped_item, char) in [('(', ')'), ('{', '}'), ('[', ']')]:
#                 pass  # 짝이 맞음!
#             else:
#                 result = 0  # 짝이 안 맞음!
#                 break

#     if top != -1:
#         result = 0

#     print(f'#{tc} {result}')









