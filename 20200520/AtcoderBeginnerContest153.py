# ・E - Crested Ibis vs Monster
# おそらく合っているが、pythonが遅すぎてTLEがいくつか出た
H, N = list(map(int, input().split()))
dp = [float('inf') for i in range(H + 1)]

dp[0] = 0 # 初期化
for i in range(N): #ナップザック問題の動的計画法
    A, B = list(map(int, input().split()))
    for j in range(H):
        nj = min(j + A, H) # 配列外参照防止
        dp[nj] = min(dp[nj], dp[j] + B)
print(dp[H])


#  dpの作成方法を変えたもの(TLEの数は同じ)
H, N = list(map(int, input().split()))
dp = [float('inf') for i in range(H + 1)]

dp[0] = 0 # 初期化
for i in range(N): #ナップザック問題の動的計画法
    A, B = list(map(int, input().split()))
    for j in range(1, H + 1):
        nj = max(j - A, 0) # 配列外参照防止
        dp[j] = min(dp[j], dp[nj] + B)
print(dp[H])
