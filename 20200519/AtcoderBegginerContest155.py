# ・A - Poor
A, B, C = list(map(int, input().split()))
print('Yes' if len(set([A, B, C])) == 2 else 'No')


# ・B - Papers, Please
N = int(input())
A = list(map(int, input().split()))
A_even = [i for i in A if i % 2 == 0]
flag_list = list(map(lambda x: (x % 3 == 0) or (x % 5 == 0), A_even))
print('APPROVED' if False not in flag_list else 'DENIED')
