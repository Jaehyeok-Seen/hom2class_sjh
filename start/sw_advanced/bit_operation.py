

secret_code = 1004

print( 7070 ^ secret_code)
print(6258 ^ secret_code) # 원래 숫자로 돌아온다.

#=============================================
print(1 << 1, bin(1 << 1)) #2 0b10
print(1 << 4, bin(1 << 4)) #16 0b10000
print(7 >> 1) #3
#항상 2진수로 바꾸고 해야한다
# 7 = 4+2+1
# 7 = 111

num = 1
for _ in range(5):
    print(num, end=' ')
    num = num << 1
print()
num = 2
for _ in range(5):
    print(num, end=' ')
    num= num << 1
"""
제곱을 이런식으로 구할 수도 있다.
"""