
def my_push(stack,top,item):
    if top >= len(stack)-1:
        raise AttributeError("overflow")   # raise는 오류가날때 어떻게 처리할지 정해주는 함
    top +=1
    stack[top] = item
    return top
    

def my_pop(stack,top):
    if top == -1:
        raise AttributeError("Empty")
    item = stack[top]
    top -= 1
    return top, item

def correct_function(list):
    global top
    stack = [0]*len(list)
    result = 1
    # 짝이 맞다는 결과를 임의로 설정하고 예외경우 0으로 바꾸기로한다.
    for char in list:
        #전체 리스트에서 하나씩 꺼냈을 때, 열린부호를 만나면 스택으로 쌓기로 한다.
        if char in '({[<':
            top = my_push(stack,top,char) # push함수에 의해서 top값들이 변경되면서 요소가 들어간다.
        
        #닫힌 부호를 만나면 스택에서 pop해서 열린부호의 item값 = test_item(열린부호)을 받아온다.
        elif char in ')]}>':
            if top != -1: #pop하기전에 스택이 비어있는 상황일 경우를 else로 빼둔다.
                top,test_item= my_pop(stack,top) #비어있지 않은경우 pop을 실행하고

                if (test_item == '(' and char ==')') or \
                    (test_item == '[' and char == ']') or \
                    (test_item == '<' and char == '>') or \
                    (test_item == '{' and char == '}'):
                    pass

                else:
                    result = 0
                    break
            else:
                result = 0
                break

    if result == 1 and top != -1:
        result = 0

    return result

            
            

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    N = int(input())
    bracket_list = input()
    bracket = [check for check in bracket_list]
    # print(bracket)
    top = -1
    stack = [0]*len(bracket)
    

    print(f'#{tc} {correct_function(bracket)}')



    
    
    
    
    
    
    
    
    
    
    
    
    # dictionary 이용용해서 번해보기






    # 정답맞추고 나면 클래스로도 해보기
# class My_Stack:
#     def __init__(self,size):
#         self.size = size
#         self.top = -1
#         self.stack = [0]*size

#     def push(self, item):
#         if self.top == self.size:
#             False
#             return -1
#         self.stack[self.top] = item
#         self.top += 1
#         return True

#     def pop(self):
#         if self.top == -1:
#             False
#             return -1
#         self.top -= 1
#         return self.stack[self.top]