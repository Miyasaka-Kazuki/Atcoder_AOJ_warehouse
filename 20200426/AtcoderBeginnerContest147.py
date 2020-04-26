# ・A - Blackjack
As = list(map(int, input().split()))
print('bust' if sum(As) > 21 else 'win')


# ・B - Palindrome-philia
string = list(input())
reverse_string = string[-1::-1]

count = 0
for i in range(len(string)):
    if string[i] != reverse_string[i]:
        count += 1
print(int(count/2))

