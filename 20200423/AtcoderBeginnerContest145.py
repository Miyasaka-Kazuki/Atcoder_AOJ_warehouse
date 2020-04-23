#!/usr/bin/env python
# coding: utf-8

# ・A - Circle

# In[3]:


PI = 3
base_area = 1 * 1 * PI

rad = int(input())
ans_area = rad * rad * PI

print(int(ans_area / base_area))


# ・B - Echo

# In[23]:


def isEcho(N, S):
    if N % 2 != 0: # 偶数じゃなければ
        return False
    
    first_S = S[0:int(N / 2)]
    last_S = S[int(N / 2):N]
    if first_S == last_S:
        return True
    return False

N = int(input())
S = input()
isTrue = isEcho(N, S)
if isTrue:
    print('Yes')
else:
    print('No')


# ・C - Average Length

# In[22]:


from itertools import permutations
from math import sqrt, pow, factorial

def length(a, b):
    x1, y1 = a
    x2, y2 = b
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

N = int(input())
xy = []
for i in range(N):
    xy.append(list(map(int, input().split())))
    
ans = 0
for order in permutations(range(N)): # 経路全探索
    tmp = 0
    for i in range(1, N):
        tmp += length(xy[order[i]], xy[order[i - 1]])
    ans += tmp
    
ans /= factorial(N)
print(ans)


# In[ ]:




