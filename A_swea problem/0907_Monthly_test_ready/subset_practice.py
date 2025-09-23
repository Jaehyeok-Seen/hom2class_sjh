bit = [0,0,0,0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # print(bit)



def making_bits(list_my,depth, max_depth):
    if depth == max_depth:
        print(list_my)
        return

    for i in range(2):
        bit[depth] = i
        making_bits(list_my, depth + 1, max_depth)

making_bits(bit,0,4)