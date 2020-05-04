# ・A - A?C
contests = ['ABC', 'ARC']
S = input()
contests.remove(S)
print(contests[0])


# ・B - Trick or Treat
N, K = list(map(int, input().split()))
haves = [False for _ in range(N)]

def judge_Flag(flags):
    As = list(map(int, input().split()))
    for A in As:
        flags[A - 1] = True

for _ in range(K):
    people_num = int(input())
    judge_Flag(haves)
print(haves.count(False))
