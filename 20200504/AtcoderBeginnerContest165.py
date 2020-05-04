# ・A - We Love Golf
K = int(input())
A, B = list(map(int, input().split()))

a = A // K
b = B // K
a_amari = A % K
b_amari = B % K
amari = min(a_amari, b_amari)
if (b - a) >= 1 or amari == 0:
    print('OK')
else:
    print('NG')


# ・B - 1%
X = int(input())

save = 100
count = 0
while save < X:
    save += int(save * 0.01)
    count += 1
print(count)
