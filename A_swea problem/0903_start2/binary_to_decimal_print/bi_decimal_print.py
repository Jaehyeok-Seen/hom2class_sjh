
def binary_decimal(binary_str,N):
    print_result = []

    for i in range(N):
        binary_result = binary_str[i*7 : (i+1)*7]

        decimal_number = 0
        pow = 0
        for digit in reversed(binary_result):
            if digit == "1":
                decimal_number += 2 ** pow
            pow += 1

        print_result.append(decimal_number)

    return print_result

import sys
sys.stdin = open('input.txt')

T = int(input())
N = int(input())
num_list = ""

for _ in range(N):
    info = input().strip().split()
    num_list += "".join(info)

result = binary_decimal(num_list,len(num_list)//7)
print(f'#1{ " ".join(map(str,result)) }')
