

"""
사과의 좌표값을 튜플로 묶어두고 거리 계산은 x끼리 abs y끼리 abs해서 더한 값이 이동거리이다.

"""
def moving(indx,my_list,current):
    global min_dist
    if indx == len(final_path):
        min_dist = min(min_dist,current)
        return

    for i in range(1,len(my_list)):

        x1, y1 = final_path[i]
        x2, y2 = final_path[i-1]
        distance = abs(x2 - x1) + abs(y2 - y1)
        current += distance

    return current


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    path = [(0,0)]
    min_dist = float('inf')
    for _ in range(N):
        x,y = map(int,input().split())
        path.append((x,y))
    final_path = path[:] +[(0,0)]

    result = moving(0,final_path,0)
    print(f'#{tc} {result}')


