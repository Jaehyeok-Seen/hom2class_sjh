#10진수를 2진수로 변환
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_number = ""
    while n >0:
        remain = n % 2
        binary_number = str(remain) + binary_number
        n = n//2
    return binary_number

#===================list를 활용하는 방법=========================
target = int(input())

result = []
while target !=0:

    result.append(target%2)
    target //= 2

result.reverse()
print(''.join(map(str,result)))








