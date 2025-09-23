def binary_to_decimal(binary_n,N):
    result_list = []
    for i in range(N):
        split_data = binary_n[(i*7) : (i*7)+7]
        #7개씩 바꿀 수 있도록 재료 준비 완료

        decimal_number = 0
        pow = 0 # 시작은 2의 0승

        for digit in reversed(split_data):
            if digit == "1":
                decimal_number += 2**pow
            pow += 1

        result_list.append(decimal_number)

    return result_list

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    hex_number = input()
    target_length = len(hex_number) * 4
    binary = f'{int(hex_number, 16) : 0{target_length}b}'
    # 11101000001100000011110011000011000011101011110011111100110011111
    """
    2진법 숫자를 7bit씩 쪼깨서 10진법으로 변경하기
    16진수 1자리 = 2진수 4자리 이기 때문이에요!
    01D06079861D79F99F (18자리 16진수)
    18 × 4 = 72비트 필요    
    앞자리 0들이 중요한 정보!
    """

    result = binary_to_decimal(binary,len(binary)//7+1)
    print(f'#{tc} {" ".join(map(str,result))}')