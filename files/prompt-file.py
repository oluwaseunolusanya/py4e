fname = input("Enter filename:")
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith("Subject:"):
        continue
    count += 1
print("There were", count, "subject lines in", fname)
