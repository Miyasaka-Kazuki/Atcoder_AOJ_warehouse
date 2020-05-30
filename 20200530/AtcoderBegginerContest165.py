# ・A - We Love Golf
K = int(input())
A, B = list(map(int, input().split()))

print('OK') if (A + K - 1) // K * K <= B else print('NG')


# ・B - 1%
X = int(input())

m = 100
count = 0
while m < X:
    m = int(m * 1.01)
    count += 1
print(count)


# ・C - Many Requirements
import copy
N, M, Q = list(map(int, input().split()))
Qs = [[0] * 4 for i in range(Q)]
for i in range(Q):
    Qs[i][0], Qs[i][1], Qs[i][2], Qs[i][3] = list(map(int, input().split()))
ans = -1

# 再帰で全探索
# 後ろから<=Mまで順番に1増加させることで、それぞれ<=Mの広義単調増加の全探索ができる
def dfs(A):
    global ans
    if len(A) == N + 1:
        sum_ = 0
        for i in range(Q):
            if A[Qs[i][1]] - A[Qs[i][0]] == Qs[i][2]:
                sum_ += Qs[i][3]
        ans = max(ans, sum_)
        return
        
    A.append(A[-1])
    while (A[-1] <= M):
        dfs(copy.copy(A))
        A[-1] += 1
    return

dfs([1])
print(ans)

