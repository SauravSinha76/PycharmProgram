n = int(input())
arr = input().split()

number = ''
count = 1
for x in arr:
    if count <= n/2:
        number += x[0]
    else:
        number += x[-1]
    count += 1

print(number)

if int(number) % 11 == 0:
    print("OUI")
else:
    print("NON")
