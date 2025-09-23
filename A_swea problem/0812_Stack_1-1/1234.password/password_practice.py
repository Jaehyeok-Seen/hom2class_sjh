import sys
sys.stdin = open('input (1).txt')

T = 10
for tc in range(1, T+1):
    info = input().split()
    N = int(info[0])
    arr = info[1]

    stack = [0]*N

    top = -1

    for num in arr:
        if top != -1 and num == stack[top]:
            top -= 1
        else:
            top+=1
            stack[top] = num

    passwords = ""
    for pw in range(top+1):
        passwords += stack[pw]

    print(f'#{tc} {passwords}')