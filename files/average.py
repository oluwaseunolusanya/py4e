'''Program prompts user for a text file, reads each line and returns 
   the average of a floating point number at the end of each line. '''
fname = input("Enter file name:")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = float(line[line.find(" "):])
    total += num
    # print(total)
    count += 1
    # print(count)
print("Average spam confidence:", total / count)


    