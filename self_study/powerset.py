"""
{1,2,3,4,5,6,7,8,9,10}
의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
"""

def powerset(arr,index,current_set,):
    global target
    if index == len(arr):
        if sum(current_set) == target:
            result.append(current_set)
        return
    #순서가 상관 있나? ??
    # 총 만들어지느 개수는 2^10 =1024가 맞나?

    # 포함 하지 않는 경우
    powerset(arr, index+1, current_set)
    # 포함하는 경우
    powerset(arr, index +1 ,current_set+[arr[index]])

my_arr=[1,2,3,4,5,6,7,8,9,10]
target = 10
result = []
powerset(my_arr,0,[])
print(result)