# ・A - Round One
choice = [1, 2, 3]
wrongs = [0 for _ in range(2)]
wrongs[0] = int(input())
wrongs[1] = int(input())

choice.remove(wrongs[0])
choice.remove(wrongs[1])
print(choice[0])


# ・B - Strings with the Same Length
max_num = int(input())
S, T = list(input().split())

new = ''
for i in range(max_num):
    new += S[i]
    new+= T[i]
print(new)


# ・C - Snack
#python3.7.1だとmath.gcdだけどAtcoderの仕様が3.4.3だからこっちを使う
from fractions import gcd 

def lcm(x, y):
    return x * y // gcd(x, y)

A, B = map(int, input().split())
print(lcm(A, B))

