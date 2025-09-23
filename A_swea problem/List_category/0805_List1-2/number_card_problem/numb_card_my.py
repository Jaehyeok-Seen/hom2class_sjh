# import sys
# sys.stdin = open ('sample.txt')

# T= 3 #test 갯수는 3개라고 지정
# N = int(input())
# number_list = list(map(int,int(input().split())))

# count = [0]*max(number_list)

# for num in number_list:


problem = [4, 9, 10]
k = 10

count = [0]*11
for num in problem:
    count[num] += 1
    count[num] = count[num-1] + count[num]

print(count)