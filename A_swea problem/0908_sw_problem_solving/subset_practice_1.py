arr = ['a', 'b', 'c']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1: #0x1 = 1 (16진법 표기) 0x1 = 001 (이진법)
            #즉, tar & 0x1 = tar & 1과 똑같음
            print(arr[i], end='')
        tar >>= 1
   #위에는 자리비교

for tar in range(1 << n):
    print('{',end= '')
    get_sub(tar)
    print('}')
#
#



problem_arr = ['A','B','C','D','E']
N = len(problem_arr)
result = []
def finding_subset(target):
    subset = [] #이부분 추가해야한다. 현재 부분집합
    for i in range(N):
        #0,1,2,3,4,
        if target & 0x1: #참이라면
            subset.append(problem_arr[i])
            print(problem_arr[i],end='')
        target >>= 1
    result.append(subset) #완성된 부분집합을 결과에 추가

for target in range(1<<N):
    print('{', end='')
    finding_subset(target)
    print('}')

count = 0
for my_subset in result:
    if len(my_subset) >= 2:
        count += 1
print(count)