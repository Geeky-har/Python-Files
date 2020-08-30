import re

str1 = '''
This is a sample string which I am writing to store the numbers which have origin from india 
+917836952729 this is my number but dont call alright? +919818678491 this adis number you can call here
+914582348023 I dont know whose number this is but still good. +929846305738 this is a pak number
stay alert!! Now here comes numbers from the united states of america: +1-555-748-1098 its john cena's number, +1-444-979-7071 this is randy ortons number, +1-999-100-0001 this is bill gates number, call now to contact him..
'''

numbers_ind = re.findall(r'\b91\d{10}\b', str1)
numbers_pak = re.findall(r'\b92\d{10}\b', str1)
numbers_us = re.findall(r'\b1-\d{3}-\d{3}-\d{4}\b', str1)
print(f" Numbers from India are: {numbers_ind}")
print(f" Numbers from Pakistan are: {numbers_pak}")
print(f" Numbers from United States are: {numbers_us}")