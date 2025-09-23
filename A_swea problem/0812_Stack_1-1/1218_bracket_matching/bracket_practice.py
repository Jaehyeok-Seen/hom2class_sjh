def push(top, stack, item):
    if top >= len(stack)-1:
        raise AttributeError('overflow')
    top += 1
    stack[top] = item
    return top
    
def pop(top, stack):
    if top == -1:
        raise AttributeError('empty')
    item = stack[top]
    top -= 1
    return top, item

def Corrector_function(test_list):
    top = -1
    result = 1 # 일단 검사 통과한 1이라고 가정하고 예외상황시 0으로 변경
    stack = [0] * len(test_list)

    for test in test_list: #리스틀 풀어서 한개 한개 확인 하겠다.
        if test in '({[<': #한개에 해당하는 test가 열린부호가 맞다면
            top = push(top,stack,test) #정의해둔 push함수에 의해 스택에 쌓아둔다.
        
        elif test in ']}>)': #한개에 해당하는 test가 닫힌부호라면?
            if top != -1:
                top, test_item = pop(top,stack)

                if (test_item=='(' and test == ')') or \
                    (test_item=='[' and test == ']') or \
                    (test_item=='{' and test == '}') or \
                    (test_item=='<' and test == '>'):
                    pass   #열린부호와 닫힌부호가 쌍이면 참이니까 그대로 pass

                else:
                    result = 0  #열린부호와 닫힌부호가 쌍인 경우 이외에는 모두 
                    
            else:
                result = 0 # top이 비어있는 경우도 result=0
    
    if result == 1 and top != -1: # {{{ 이렇게만 스택에 남아있다고 하자 그럼 예외코드도 없기 때문에 result =1이지만 오답
        result = 0

    return result           
           
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    N = int(input())
    list = input()
    test_list = [check for check in list]
    print(Corrector_function(test_list))


