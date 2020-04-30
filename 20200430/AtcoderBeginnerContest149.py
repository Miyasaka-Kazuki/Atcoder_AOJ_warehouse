# ・A - Strings
S, T = input().split()
print(T+S)


# ・B - Greedy Takahashi
A, B, K = list(map(int, input().split()))

a = max(A - K, 0)
K -= A - a
b = max(B - K, 0)
print(a, b)


# ・C - Next Prime
X = int(input())

def is_prime(x): #素数判定
    flag = True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

cur = X 
while True:
    if is_prime(cur):
        break
    cur += 1
print(cur)