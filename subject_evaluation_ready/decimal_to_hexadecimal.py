# 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF" #변화없이 사용만한다고하면 문자열이 더 빠르다.
    hexadecimal_number = ""

    if n == 0:
        return 0

    while n >0:
        remain = n % 16
        # 10~15를 어떻게 A~F로 변환할 수 있을까?
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        n //= 16

    return hexadecimal_number

print(decimal_to_hexadecimal(125))
