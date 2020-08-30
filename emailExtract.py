import re

samp_str = '''This is a sample string in which i will keep some email addresses and by re module in python I will extract the email addresses of various people. My email: abc@gmail.com,
padosi email: padosi@gmail.com, bhabhi email: bhabhiji@gmail.com, chahcha email: 
chachabh@ymail.com, kutta email: kuttabhai@hotmail.com. these are some of the emails of those people whom i personally know and all of them are totally fake. Kaisa laga mjak.... Chal ab niklo yaha se.'''

email = re.findall(r'\S+@\S+', samp_str)
print(email)