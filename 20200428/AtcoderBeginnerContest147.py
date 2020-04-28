# ・C - HonestOrUnkind2
N = int(input())

evidences = [[] for _ in range(N)]
for i in range(N): # i:人の番号
    A = int(input())
    for _ in range(A): #  x:人の番号, y:正直者か見破る番号
        x, y = map(int, input().split())
        evidences[i].append((x - 1, y))
        
# 全通り試す(最大は2**15だから問題ない)
result = 0
for i in range(1, 2 ** N): # iのビットは正直者と不親切な人の割合
    consistent = True# 全通り試して矛盾がなければtrue
    for j in range(N):# ビット演算で一人ずつ見ていく
        if (i >> j) & 1 == 0: # 選んだ一人が不親切なら
            continue
        for x, y in evidences[j]: # x:人の番号, y:正直者か見破る番号
            if (i >> x) & 1 != y: # xで一人を選んで,yの証言と一致してなかったら矛盾
                consistent = False
    if consistent:
        result = max(result, bin(i).count('1'))
print(result)
