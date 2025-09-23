"""

재귀호출로 한번 해보기

"""
# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_number = ""
    if n == 0:
        return "0"

    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        binary_number =  str(remain) + binary_number
        n = n // 2
        pass

    return binary_number

print(decimal_to_binary(149))

#10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    while n > 0 :
        remain = n % 16
        #문제는 여기서 한자리수가 아닌 두자리수가 나올경우!
        # 0~ 15 숫자: 인덱스
        # 0~9 + A~F 로 바꿔야한다.

        hexadecimal_number = hex_digits[remain]+ hexadecimal_number
        n = n // 16
    return hexadecimal_number

print(decimal_to_hexadecimal(31))
print(decimal_to_hexadecimal(149))

# 내장함수가 있기는 하다
print(bin(31))
print(hex(149))
#0b11111     => 0b는 파이썬에서 이진법 표시
#0x95        => 0x는 파이썬에서 16진법 표시
"""
문제를 풀다가,
변화 X, 조회만 필요로 하는 경우는
무조건 문자열이 빠르고 편하다.

변화O 일 경우 => list, dictionary

"""

#2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == "1":
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number



print(binary_to_decimal("10010101"))

































def Binary_to_decimal(binar_str):
    
