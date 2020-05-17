# ・A - Remaining Balls
S, T = input().split()
A, B = list(map(int, input().split()))
U = input()

if U == S:
    A -= 1
else:
    B -= 1
print(A, B)


# ・B - I miss you...
S = input()
print('x' * len(S))


# ・C - Distinct or Not
N = int(input())
A = list(map(int, input().split()))
print('YES' if len(set(A)) == N else 'NO')


# ・D - Dice in Line
N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

aves = [(i + 1) / 2 for i in P]
max_ave = sum(aves[0:K])
temp = max_ave
for i in range(N - K):
    temp -= aves[i]
    temp += aves[i + K]
    if temp > max_ave:
        max_ave = temp
print(max_ave)
