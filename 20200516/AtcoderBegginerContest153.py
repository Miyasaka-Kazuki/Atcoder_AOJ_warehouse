# ・A - Serval vs Monster
H, A = list(map(int, input().split()))
count = 0
while H > 0:
    H -= A
    count += 1
print(count)


# ・B - Common Raccoon vs Monster
H, N = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(N):
    H -= A[i]
if H <= 0:
    print('Yes')
else:
    print('No')


# ・C - Fennec vs Monster
N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

def calCount(h):
    if K > N:
        return 0
    return sum(h[K:])

H.sort(reverse=True)
print(calCount(H))


# ・D - Caracal vs Monster
H = int(input())

count = 0
monster_num = 1
monster_hp = H
while monster_hp != 0: #倍々で増えていく数列
    count += monster_num
    monster_num *= 2
    monster_hp //= 2
print(count)
