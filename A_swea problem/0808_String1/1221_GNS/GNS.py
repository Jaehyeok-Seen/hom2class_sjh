def get_key_by_value(dictionary, value): #이부분은 도움 받아버림
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def alien_sort(list):
    test_list = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" :3, "FOR" : 4,
                 "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
    #예시
    #SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE
    our_sort = []
    result = ''
    for num in number_list:
        our_sort.append(test_list[num])
    our_sort.sort()

    for num2 in our_sort: #정렬된 우리방식의 숫자들(밸류값)을 통해 key를 받아와야함
        result += (get_key_by_value(test_list, num2)+' ')

    return result



import sys
sys.stdin = open('GNS_test_input.txt')

sorted_list = "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
T = int(input())
for tc in range(1,T+1):
    information = input().split()
    TC = information[0]
    word_count = int(information[1]) #단어의 개수
    number_list = input().split() #str 숫자 리스트





    print(f'{TC} \n{alien_sort(number_list)}')