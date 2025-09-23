def maxone_count(N,arr):
    max_count = 0
    i =0
    
    while i < N:
        if arr[i]==1:
            curr_count = 0
            while i < N and arr[i] ==1:
                curr_count +=1
                i += 1
                max_count = max(max_count,curr_count)
        else:
            i+=1  
            
    return max_count

    def maxone_count(N, arr):
        max_count = 0
        current_count = 0
    
        for i in range(N):
            if arr[i] == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
    
        return max_count