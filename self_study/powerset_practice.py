def my_powerset(arr, index, current_subset):
    if index == len(num_li):
        if sum(current_subset) == target:
            subset.append(current_subset)
        return

    #부분 집합
    #포함 안하는경우
    my_powerset(arr, index+1, current_subset)
    #포함 하는 경우
    my_powerset(arr, index+1, current_subset + [arr[index]])

num_li = [1,2,3,4,5,6,7,8,9,10]
subset = []
target = 10

my_powerset(num_li,0,[])
print(subset)