# 10진수를 2진수로 변경하는 프로그램
def decimal_to_binary(N):
    if N == 0:
        return '0'
    binary_num = ""

    while N > 0:
        remain = N % 2  # 2의 나머지를 할당해두고
        binary_num = str(remain) + binary_num
        N // 2  # while문의 종료를 위해서라도 2씩 계속 나눠야함

    return binary_num

#10진수를 16진수로 변경하는 프로그램
def decimal_to_hexadecimal(N):
    hexa_digits = '0123456789ABCDEF' # 문자열도 인덱스로 불러올 수 있으니까
    hexa_number = ""

    if N == 0:
        return 0

    while N > 0:
        remain = N % 16
        hexa_number = hexa_digits[remain] + hexa_number
        N //= 16

    return hexa_number

#2진수를 10진수로 변환
def binary_to_decimal(binary_num):
    print(int(binary_num,2))

binary_to_decimal('110101')
