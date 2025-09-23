import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    """
    16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어
    10진수로 변환해서 출력해보자
    """
    hex_list = input().strip()
    binary_list = f'{int(hex_list,16):0{len(hex_list)*4}b}'
    #콜론과 0사이에 공백이 있으니까 오류가 생김 0이 6개만 들어옴
    #7bit씩 묶는다고 했으니까
    binary_result = []

    for i in range(0,len(binary_list),7):

        set1 = binary_list[i:i+7]
        pow = 0
        decimal_value = 0

        for j in reversed(set1):
            if j == '1':
                decimal_value += 2**pow
                pow+=1
            else:
                pow+=1
        binary_result.append(decimal_value)
    print(f"#{tc}", *binary_result)

