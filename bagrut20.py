arr=[2,4,-7,8,1,2,4]
num=15
sum=0

for i in arr:
    sum+=i
    if sum>num:
        print(i)
        break
    else:
        continue

if sum<num:
    print(-1)