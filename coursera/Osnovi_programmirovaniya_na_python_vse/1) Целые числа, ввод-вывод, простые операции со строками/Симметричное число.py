n = int(input())
a1 = n % 10
a2 = n // 10 - n // 100 * 10
a3 = n // 100 - n // 1000 * 10
a4 = n // 1000 - n // 10000 * 10
print((a3 + 1) // (a2 + 1) - (a1 - a4) + (a2 - a3))
print(-7 % 3)