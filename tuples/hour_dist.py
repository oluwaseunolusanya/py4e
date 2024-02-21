'''Program prompts user for mail box text file or uses 'mbox-short.txt' as default 
   for empty input and then outputs distribution of the hour in ascending order.'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_dist = dict()
for line in handle:
    line = line.rstrip()
    
    if not line.startswith("From "):
        continue
       
    time = line.split()[5]
    hour = time.split(":")[0]
    
    hour_dist[hour] = hour_dist.get(hour,0) + 1

for hour,count in sorted(hour_dist.items()):
    print(hour, count)

# print([hour, count for hour,count in sorted(hour_dist.items())])
