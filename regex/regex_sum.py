import re

filehandle = open("regex_sum_1979349.txt")
num = list()

for line in filehandle:
    line = line.rstrip()
    print(line)
    num_elem = re.findall("[0-9]+",line)
    print(num_elem)
    if len(num_elem) < 1:
        continue
    for elem in num_elem:
        num.append(int(elem))
        
print(sum(num))