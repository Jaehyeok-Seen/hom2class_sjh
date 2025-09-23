# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_number = ""

    if n == 0:
        return "0"

    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        binary_number = str(remain) + binary_number
        n = n // 2

    return binary_number


print(decimal_to_binary(0))


# 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""

    if n == 0:
        return 0

    # 0보다 클 때까지 16로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 16
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        n = n // 16

    return hexadecimal_number


print(decimal_to_hexadecimal(17))
print(decimal_to_hexadecimal(31))

# 내장 함수가 "있기는 하다"! (직접 구현하는 방법을 연습하자)
print(bin(5))
print(hex(31))


# 2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == "1":
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number


print(binary_to_decimal("11101"))
