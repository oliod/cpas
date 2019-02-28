from datetime import datetime

f = [1,2,3,4,5,8,9,78,4,52,1]


for m in f:
    print(m)
    if m == 78:
        print(" i found number 78")
    elif m== 5:
        print(" cool 5");
    else:
        print("-")

if 8 in f:
    print(" YES")
