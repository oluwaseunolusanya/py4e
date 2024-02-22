import re
filehandle = open("mbox-short.txt")
confidence_list = list()
for line in filehandle:
    line = line.rstrip()
    confidence = re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
    
    if len(confidence) != 1:
        continue
    
    confidence_list.append(float(confidence[0]))

print("Maximum:",max(confidence_list))

    