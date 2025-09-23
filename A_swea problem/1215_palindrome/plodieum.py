import sys
sys.stdin = open('input.txt')

'''
가로와 세로의 단어들 중에서
길이가 x 인 단어를 찾고
그 단어가 회문인지 판단한 다음에
회문이라면 +1
모든 단어에 대한 판별이 끝나면
목적인 회문의 개수를 출력하면 끝!
'''
def is_palindrome(word):
    for i in range(len(word) // 2):
        word[i] == word[len(word)-1-i]


T = 10
N= 8 # 주어진 판의 크기

for tc in range(1, T+1):
    L = int(input())        #회문의 길이
    arr = [input() for _ in range(N)]

    print(L, arr)
    # 가로의(열 우선 탐색) 문자열을 찾는다. (길이가 L인 문자열)
    word = []
    for row in range(N):
    # 문자열 + 문자열 => 속도 저하 append로 더하는게 속도측면에서 이점이 존재
        for col in range(N-L+1):
            print(arr[row][col])
    #       horizontal.append()
    #