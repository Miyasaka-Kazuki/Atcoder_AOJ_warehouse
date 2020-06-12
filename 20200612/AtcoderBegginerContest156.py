# ・A - Beginner
N, R = list(map(int, input().split()))
if N >= 10:
    print(R)
else:
    print(R + 100 * (10 - N))


# ・B - Digits
N, K = list(map(int, input().split()))
num = K
count = 1
while num <= N:
    num *= K
    count += 1
print(count)


# ・C - Rally
N = int(input())
X = list(map(int, input().split()))

p_max = 100
ans_min = 1000000 # 最大でも(100 - 1) ** 2 * 100だからそれを超えればいい
for p in range(1, p_max):
    sum_ = 0
    for x in X:
        sum_ += (x - p) ** 2
    ans_min = min(sum_, ans_min)
print(ans_min)