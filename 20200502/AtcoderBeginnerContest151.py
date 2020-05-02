# ・A - Next Alphabet
C = input()
print(chr(ord(C) + 1))


# ・B - Achieve the Goal
N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# M <= (Ai + ... + Ai-1 + x) / N の式変換
x = N * M - sum(A)
if 0 <= x <= K:
    print(x)
elif x < 0:
    print(0)
else:
    print(-1)


# ・C - Welcome to AtCoder
N, M = list(map(int, input().split()))
submits = [[] for i in range(M)]
for i in range(M):
    submits[i] = input().split()
    submits[i][0] = int(submits[i][0])

AC_number = [0 for i in range(N)] #バケット
WA_number = [0 for i in range(N)] #バケット
for i in range(M):
    #WAが出て、まだ終わってない問題なら
    if submits[i][1] != 'AC' and AC_number[submits[i][0] - 1] != 1:
        WA_number[submits[i][0] - 1] += 1

    #ACが出たら
    if submits[i][1] == 'AC':
        AC_number[submits[i][0] - 1] = 1

AC_count = 0
WA_count = 0
for i in range(N):
    if AC_number[i] == 1:
        AC_count += 1
        WA_count += WA_number[i]
print(AC_count, WA_count)
