import re

data = open("data.txt")
sum=0
for x in data:
    #print(x)
    y = re.findall('[0-9]', x)
    print(y[0] + y[-1])
    sum += int(y[0] + y[-1])
    print(sum)


data.close()