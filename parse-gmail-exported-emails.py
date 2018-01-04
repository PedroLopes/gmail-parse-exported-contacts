import re
import string

contacts = open("input.csv")
output = open("output.txt","w") 

for line in contacts:
    if len(line) == 1:
        break
    data = line.split(",")
    email = data[28]
    name = data[0].strip()
    name = re.sub(r'[^\x00-\x7f]',r'',name)
    if len(email) > 1:
        emails = email.split(":")
        for email in emails:
            if email.find("@") > 0:
                output.write('{0} <{1}>\n'.format(name.strip(),email.strip()))
                print('Name:{0}, email:{1}'.format(name.strip(),email.strip()))

output.close()
