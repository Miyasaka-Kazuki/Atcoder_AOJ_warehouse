# ・A - Five Variables
X = list(map(int, input().split()))
print(X.index(0) + 1)


# ・B - Crane and Turtle
X, Y = list(map(int, input().split())) # 匹数, 足の本数
kame = 4
turu = 2

def flag():
    if Y % 2 != 0:
        return False
    
    for i in range(X + 1): #単調増加
        kame_num = i
        turu_num = X - i
        temp_sum = turu_num * turu + kame_num * kame
        if temp_sum == Y:
            return True
        elif temp_sum > Y:
            break
    return False

flag = flag()
print('Yes') if flag else print('No')


# ・C - Forbidden List
X, N = list(map(int, input().split()))
P = list(map(int, input().split()))

min_ = 100
for i in range(0, 102):
    cur = i 
    if cur in P:
        continue
    diff = abs(X - cur)
    if diff < min_:
        min_ = diff

front = X - min_
back = X + min_
if front not in P:
    print(front)
else:
    print(back)


#別解法
X, N = list(map(int, input().split()))
P = list(map(int, input().split()))

min_ = 0
while True:
    front = X - min_
    back = X + min_
    if front in P and back in P:
        min_ += 1
    else:
        break

front = X - min_
back = X + min_
if front not in P:
    print(front)
else:
    print(back)

