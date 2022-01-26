word = input("Enter word: ")

z = 0
o = 0
for x in word:
    if x == 'z':
        z += 1
    elif x == 'o':
        o += 1
    else:
        print("Invalid value :" + x)

if z * 2 == o:
    print("YES")
else:
    print("NO")

