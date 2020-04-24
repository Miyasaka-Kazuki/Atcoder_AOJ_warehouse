#!/usr/bin/env python
# coding: utf-8

# ・A - Can't Wait for Holiday

# In[4]:


days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'NEXT_SUN'] #末尾までどのくらい遠いか

today_day = input()
today_index = days.index(today_day)
nextsun_index = days.index('NEXT_SUN')
print(nextsun_index - today_index)


# ・B - ROT N

# In[19]:


shift_num = int(input())
string = list(input())

for i, char in enumerate(string):
    current_ord = (ord(char)+shift_num-ord('A')) % 26
    new = chr(current_ord + ord('A'))
    string[i] = new
    
print(''.join(string))


# ・C - Buy an Integer

# In[ ]:




