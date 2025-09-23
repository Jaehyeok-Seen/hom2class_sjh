import sys
sys.stdin = open('input.txt')

T, N = map(int,input().split())
nums = list(map(int, input().split()))
sizes = [[False] for _ in range(100)]

for i in range(0, 2*N, 2):
    sizes[nums[i]].append(nums[i+1])