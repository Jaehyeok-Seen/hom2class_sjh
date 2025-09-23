import sys
sys.stdin = open('input.txt')

bit_pattern = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

T = int(input())
for tc in range(1,T+1):
    password_code = input().strip() #16진수 str
    #일단 16진수를 2진수로 바꿔야한다.
    binary_password_code = f'{int(password_code,16) : 0{len(password_code)*4}b}' #2진수로 변경시 길이는 x4해줘야한다.
    #f-string문법 이용시 int(문자열,몇진수인지)
    #이진법으로 받기 완료(그러나 제일 앞이 0이거나,연속할 경우 생략되기때문에) => 0{길이}를 붙여줘야함
    #6개씩 받아서 암호가 있는지 확인
    result = []
    i = 0
    while i <= len(binary_password_code) - 6: #6자리씩 보면되는거니까 마지막 지점을 이렇게 지정
        check = binary_password_code[i:(i+6)]
        my_value = bit_pattern.get(check)
        if my_value is not None:
            result += str(my_value)
            i += 6
        else:
            i += 1
    print(f'#{tc}', *result)

