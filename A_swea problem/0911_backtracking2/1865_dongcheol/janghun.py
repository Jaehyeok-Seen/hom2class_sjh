# 1.
def shelf(idx, hap):
    global min_diff

    if idx >= N:
        if hap >= B:
            diff = hap - B
            if diff < min_diff:
                min_diff = diff
        return

    if hap >= B and hap - B > min_diff:
        return

    shelf(idx + 1, hap + height[idx])
    shelf(idx + 1, hap)


T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_diff = 100000000000000000

    shelf(0, 0)

    print(f"#{t} {min_diff}")

