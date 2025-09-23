"""
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
3+4+5*6+7
=>
34+56*+7+
=>44
문자열안에는 + * 두개만 존재
"""
import sys
sys.stdin = open('input.txt')


def calculate_postfix(postfix):
    stack = []

    for char in postfix:
        if char.isdigit():  # 숫자면
            stack.append(int(char))
        else:  # 연산자면
            # 오른쪽 피연산자 먼저 pop
            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '*':
                stack.append(a * b)

    return stack[0]

T = 10
for tc in range(1,T+1):
    N = int(input())
    cal_list = list(input())

    stack = [] #연산자만 들어오고 나갈예정
    post = [] #후위 표기식으로 변경된 수식이 담길예정
    for str1 in cal_list:
        if not str1.isdigit(): #반복해서 나온 문자가 연사자일 경우
            if str1 == '+':
                if stack : # 비어있지 않은 스택일 경우 같은거나 낮은경우 둘다이기때문에 무조건 pop
                    temp = stack.pop(-1)
                    post.append(temp)
                    stack.append(str1)

                else:
                    stack.append(str1) #빈 스택일 경우 append

            else: #'*'일 경우
                if stack :
                    if stack[-1]=='*':
                        temp = stack.pop(-1)
                        post.append(temp)
                        stack.append(str1)
                    else:
                        stack.append(str1)
                else:
                    stack.append(str1) #빈 스택일 경우 append


        else: #정수일 경우
            post.append(str1)

    print(calculate_postfix(post))




#"연산자를 스택에 쌓아둔다"
#같은 연산자가 나오면 스택에서 꺼내고 비교대상을 append
#높은 연산자가 나오면 스택에 넣는다
#낮은 연산자가 나오면 스택에서 꺼내고 넣는다
