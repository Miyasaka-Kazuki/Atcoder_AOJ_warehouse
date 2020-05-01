# ・A - 500 Yen Coins
K, X = list(map(int, input().split()))
print('Yes' if 500 * K >= X else 'No')


# ・B - Count ABC
N = input()
S = input()
print(S.count('ABC'))


# ・C - Count Order
from itertools import permutations

N = int(input())
P = int(''.join(input().split()))
Q = int(''.join(input().split()))

# 順列の単調増加リスト作成
perms = []
for order in permutations(list(map(lambda x:x + 1, range(N)))):
    order = map(str, list(order))
    perms.append(int(''.join(order)))

def binary_search(x):
    left_index = 0
    right_index = len(perms)
    while right_index - left_index > 1:
        mid_index = (left_index + right_index) // 2
        if perms[mid_index] <= x:
            left_index = mid_index
        else:
            right_index = mid_index
    return left_index + 1 # インデックスTo番目は＋１する必要がある

print(abs(binary_search(P) - binary_search(Q)))
