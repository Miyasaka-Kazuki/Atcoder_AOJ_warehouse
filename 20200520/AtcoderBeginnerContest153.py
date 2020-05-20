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


#C++に変えたら全部できたので上のコードもおそらく正しい

#pythonの上のコード
# #include <iostream>
# #include <bits/stdc++.h>
# using namespace std;
# const int INF = 1001001001;

# int main(void){
#     int H, N;
#     cin >> H >> N;
#     vector<int> dp(H + 1, INF);
#     dp[0] = 0;
#     for(int i = 0; i < N; i++){
#         int A, B;
#         cin >> A >> B;
#         for(int j = 0; j < H; j++){
#             int nj = min(j + A, H);
#             dp[nj] = min(dp[nj], dp[j] + B);
#         }
#     }
#     cout << dp[H] << endl;
# }


#pythonの下のコード
# #include <iostream>
# #include <bits/stdc++.h>
# using namespace std;
# const int INF = 1001001001;

# int main(void){
#     int H, N;
#     cin >> H >> N;
#     vector<int> dp(H + 1, INF);
#     dp[0] = 0;
#     for(int i = 0; i < N; i++){
#         int A, B;
#         cin >> A >> B;
#         for(int j = 1; j <= H; j++){
#             int nj = max(j - A, 0);
#             dp[j] = min(dp[j], dp[nj] + B);
#         }
#     }
#     cout << dp[H] << endl;
# }
