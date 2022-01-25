n = int(input())
s = input()

if 'HH' in s:
    print("No")
else:
    print("YES")
    print(s.replace('.', 'B'))
