#The program prompts user for a mail box text file and outputs the most frequent sender.

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhandle = open(fname)

senders = dict()

for line in fhandle:
    line = line.rstrip()
     
    if not line.startswith("From "):
        continue
    words = line.split()
    
    if len(words) < 1:
        continue
    
    sender = words[1]    
    
    # if sender not in senders:
    #     senders.update({sender: 1})
    # else:
    #     senders[sender] += 1

    senders[sender] = senders.get(sender,0) + 1
   
# for k, v in senders.items():
for sender in senders:
    if senders[sender] != max(senders.values()):
        continue
    print(sender, senders[sender])
    
  

   
        
    
    
    