# ・D - Handstand 2
# 数字を先頭と末尾のペアに変換
def toHeadTail(n):
    n = str(n)
    head = n[0]
    tail = n[-1]
    return (head, tail)

# 集計処理
def aggregate(N):
    pair_agg = {}
    for i in range(1, N + 1):
        pair = toHeadTail(i)
        if pair in pair_agg.keys():
            pair_agg[pair] += 1
        else:
            pair_agg[pair] = 1
    return pair_agg

N = int(input())
pair_agg = aggregate(N)
count = 0
for i in range(1, N + 1):
    pair = toHeadTail(i)
    pair_inverse = (pair[1], pair[0])
    if pair_inverse in pair_agg.keys():
        count += pair_agg[(pair[1], pair[0])]
print(count)
