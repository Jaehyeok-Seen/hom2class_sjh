def enq(n):
    global last
    last += 1 #마지막 정점 추가
    heap[last] = n

    c = last
    p = c // 2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2