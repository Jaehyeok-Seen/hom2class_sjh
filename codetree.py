
'''
7 4
5 5
2 4
4 6
3 5
'''

n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

result = [0]*(7+1)
for my_range in commands:
    a , b = my_range

    for i in range(a,b+1):
        result[i] += 1


print(max(result))
# Please write your code here.