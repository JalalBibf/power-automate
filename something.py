completerNums = []
for i in range(1000, 700000):
    if(len(str(i))%2)==0:
        num = list(map(int, str(i)))
        if len(num) == 4:
            if (num[0] + num [3]) == (num[1] + num[2]):
                completerNums.append(i)
        elif len(num) == 6:
            if (num[0] + num [5]) == (num[1] + num[4]) == (num[2] + num[3]):
                completerNums.append(i)
print(completerNums)
print(len(completerNums))

