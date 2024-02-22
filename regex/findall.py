import re
imsg = "My 2 favorite numbers are 19 and 42"
omsg = re.findall("[0-9]+",imsg)    #[0-9]+ one or more digits.
print(omsg)