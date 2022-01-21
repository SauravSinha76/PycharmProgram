n = int(input())
arr = input().split()

number = ''
for x in arr:
    number += x[-1]

print(number)
if int(number) % 10 == 0 :
    print('Yes')
else:
    print('No')
