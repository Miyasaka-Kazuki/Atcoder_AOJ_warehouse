#!/usr/bin/env python
# coding: utf-8

# ・C - Buy an Integer

# In[26]:


left = 0
right = 10 ** 9 + 1
a, b, x = map(int, input().split())

keta = lambda num: len(str(num))
f = lambda mid: a * mid + b * keta(mid)
while right - left > 1:
    mid = (left + right) // 2
    if f(mid) <= x:
        left = mid
    else:
        right = mid
        
print(left)

