# ・A - A?C
contests = ['ABC', 'ARC']
S = input()
contests.remove(S)
print(contests[0])


# ・B - Trick or Treat
N, K = list(map(int, input().split()))
haves = [False for _ in range(N)]
 
def judge_Flag(flags, num):
    As = list(map(int, input().split()))
    for i in range(num):
        flags[As[i] - 1] = True
        
for _ in range(K):
    people_num = int(input())
    judge_Flag(haves, people_num)
print(haves.count(False))


# ・C - Peaks
N, M = list(map(int, input().split()))
tenbodai = [H for H in list(map(int, input().split()))]
tenbodai_trail = [set() for i in range(len(tenbodai))]
 
for _ in range(M): #展望台と繋がる道のリストを作成
    trail = list(map(int, input().split()))
    tenbodai_trail[trail[0] - 1].add(trail[1] - 1)
    tenbodai_trail[trail[1] - 1].add(trail[0] - 1)
    
count = 0
for i in range(len(tenbodai)): #全探索
    flag = True
    for trail in tenbodai_trail[i]: # i:現在の展望台の番号, trail:繋がる展望台の番号
        if tenbodai[i] <= tenbodai[trail]:
            flag = False
            break
    if flag:
        count += 1
print(count)

