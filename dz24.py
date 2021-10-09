s=input()
result = 0
for a in s:
    if "(" in a:
        result +=1
    elif ")" in a:
        result -= 1
    if result < 0:
        print("NO")
    if result > 0:
        print("YES")