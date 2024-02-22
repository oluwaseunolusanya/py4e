import re
# imsg = "My 2 favorite numbers are 19 and 42"
# omsg = re.findall("[0-9]+",imsg)    #[0-9]+ one or more digits made up of integer between 0 and 9.
# print(omsg)
# omsg_1 = re.findall("[AEIOU]+",imsg)
# print(omsg_1)  #Return an empty list

#Greedy pattern(* and +)
# imsg = "From: Using the: character"
# omsg = re.findall("^F.+:", imsg)
# print(omsg)

#Non-Greedy pattern(*? and +?)
# imsg = "From: Using the: character"
# omsg = re.findall("^F.+?:", imsg)
# print(omsg)

#Fine-tuning String Extraction
imsg = "From oolusanya@email.com Thu Feb 22 18:34 2024"
# omsg = re.findall("^From \S+@\S+", imsg)
omsg = re.findall("^From (\S+@\S+)", imsg)  #Demonstrating parentheses used to specify beginning and end of extraction.
print(omsg)