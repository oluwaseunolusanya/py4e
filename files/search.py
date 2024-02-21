fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    # if line.startswith("From:"):
    #     print(line)
    if not line.startswith("From:"):
        continue
    print(line)