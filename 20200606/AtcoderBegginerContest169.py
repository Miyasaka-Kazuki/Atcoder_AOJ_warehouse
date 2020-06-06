# ・A - Multiplication 1
A, B = list(map(int, input().split()))
print(A * B)


# ・B - Multiplication 2
# オーバーフローの問題
# オーバーフローする前にlimitを超えれば-1を出力するが、 
# ０が来たら途中でオーバーフローしても出力は０になるので先に０があるか検索しておく必要がある。
N = int(input())
A = list(map(int, input().split()))
limit = 1000000000000000000
ans = 1
for i in range(N):
    if A[i] == 0:
        ans = 0

flag = False
for i in range(N):
    ans *= A[i]  
    if ans > limit:
        flag = True
        break
print(-1) if flag else print(ans)


# ・C - Multiplication 3
AB = list(input().split())
A = int(AB[0])
# 小数 * 整数は誤差が出るが+-0.5より大きい誤差が出なければ,
# floatからintへの変換は切り捨てなので+0.5することで+-0.5以内の誤差なら正しく変換できる。
# (この問題は+0.5でなく+0.1でもACできた)
B = int(float(AB[1]) * 100 + 0.5) 
print(A * B // 100)


AB = list(input().split())
A = int(AB[0])
# こちらは文字列から直接ドット以外を抽出して実質100倍にしてから文字列を整数に変換したもの
# 小数は関わってないので正しく変換できる。
B = int(AB[1][:1] + AB[1][2:])
print(A * B // 100)
