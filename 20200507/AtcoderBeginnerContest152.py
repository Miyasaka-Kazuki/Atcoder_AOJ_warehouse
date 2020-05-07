# ・A - AC or WA
N, M = list(map(int, input().split()))
print('Yes') if M >= N else print('No')


# ・B - Comparing Strings
a, b = input().split()
a_S = a * int(b)
b_S = b * int(a)
print(a_S) if a_S < b_S else print(b_S)


# ・C - Low Elements
N = int(input())
P = list(map(int, input().split()))

count = 0
min_P = P[0]
for i in range(N):
    if P[i] <= min_P:
        count += 1
        min_P = P[i]
print(count)
