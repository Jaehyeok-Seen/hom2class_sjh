# 1.

def synergy(lst):
    total = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            ing1 = lst[i]
            ing2 = lst[j]
            total += ingredient[ing1][ing2] + ingredient[ing2][ing1]
    return total


def combination(idx, chosen):
    global min_diff

    if len(chosen) == (N // 2):
        other = [i for i in range(N) if i not in chosen]
        s1 = synergy(chosen)
        s2 = synergy(other)
        result = abs(s1 - s2)
        min_diff = min(min_diff, result)
        return

    if idx >= N:
        return

    combination(idx + 1, chosen + [idx])
    combination(idx + 1, chosen)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    ingredient = [list(map(int, input().split())) for _ in range(N)]

    min_diff = 10000000000000000

    combination(0, [])

    print(f"#{t} {min_diff}")