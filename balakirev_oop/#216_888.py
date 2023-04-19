n = map(int, input().split())
# 8 11 -5 10 -1 0 7
n = sorted(n)
print(*n[:3])

# print(*sorted(input().split(), key=int)[:3])
