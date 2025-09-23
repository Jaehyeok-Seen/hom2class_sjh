 #2진수를 10진수로 변환
def binary_to_decimal(bin_str):
    decimal_number = 0
    pow = 0
    for digit in reversed(bin_str):
        if digit == 1:
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number

binary_to_decimal('101110')

def binary_to_decimal(bin_str):
    decimal_number = 0
    pow =0
    for digit in reversed(bin_str):
        if digit == 1:
            decimal_number += 2**pow
          pow += 1

    return decimal_number