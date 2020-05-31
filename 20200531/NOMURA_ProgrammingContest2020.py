# ・A - Study Scheduling
H1, M1, H2, M2, K = list(map(int, input().split()))
time = (H2 - H1) * 60 + M2 - M1
print(time - K)


# ・B - Postdocs
T = list(input())
for i in range(len(T)):
    if T[i] == '?':        
        T[i] = 'D'
print(''.join(T))

