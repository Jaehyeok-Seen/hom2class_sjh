import sys
sys.stdin = open('./input.txt')

def preorder(node):
    if not node:
        return

    print(node, end = ' ')
    preorder(left[node])
    preorder(right[node])


"""
첫 줄에는 트리의 정점의 총 수 V
다음 줄에는  V-1개 간선이 나열
1 2 1 3 2 4 3 5 3 6...
1은 부모 정점, 2는 자식을 의미
간선은 부모 정점 번호가 작은 것 부터 나열,
부모 정점이 동일하다면, 자식 정점 번호가 작은 것 부터 나열

다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호 출력
"""
#방법1: 리스트 먼저 해보기================================================================

V = int(input()) #정점의 개수
information = list(map(int,input().split()))

parent = []
child = []
for i in range(0,len(information),2):
    x = information[i]
    y = information[i+1]
    parent.append(x)
    child.append(y)

#간선의 개수에 맞게 빈 리스트를 만든다.
# parent =[1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]                                            ✔  base   at 06:27:23 PM 
# child = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#트리형으로 풀어야하니까.. left, right로 나눠야함
left = [0] * (V+1) #0을 하나 만들어서 인덱스 맞춘다.
right = [0] * (V+1)

for k in range(V-1): #0~V-1까지 간선의 개수만큼
    p = parent[k]
    c = child[k]

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

preorder(1)



#
#
# V = int(input())
# edges = list(map(int,input().split()))
# parent = []
# child = []
# for i in range(0,len(edges),2):
#     parent.append(edges[i])
#     child.append(edges[i+1])
# # print(parent)
# # print(child)
#
# left = [0] * (V+1)
# right = [0] * (V+1)
# for k in range(len(parent)):
#     p = parent[k]
#     c = child[k]
#
#     if left[p] == 0:
#         left[p] = c
#     else:
#         right[p] = c
#
# print(left)
# print(right)
#
# def preorder(node):
#     if node == 0: # 만약 자식이 없다면
#         return
#
#     print(node,end = ' ')
#     preorder(left[node])
#     preorder(right[node])
#
# preorder(1)
#
# #방법2: 2차원 리스트(인접 리스트처럼)=================================================
#
#
#
#
# #방법3: 클래스 사용해서 ================================================================
# class Node:
#     def __init__(self,data = None):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def preorder(self,data):
#         if data is None:
#             return
#
#         print()