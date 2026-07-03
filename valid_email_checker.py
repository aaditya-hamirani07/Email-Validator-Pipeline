import csv
import re

list1=[]
list2=[]
valid=0
invalid=0

def validator(x):
    global valid,invalid
    pattern = r'^[A-Za-z0-9](?:[\w.%+-]*[A-Za-z0-9])?@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z]{2,4})+$'
    if (re.match(pattern,x)):
            list1.append(x)
            # print(x)
            valid += 1
    else:
         list2.append(x)
        #  print(x)
         invalid += 1

with open('fake_dataset.csv','r') as file:
    a = csv.reader(file)
    for row in a:
        rows = "".join(row)
        rows = rows.strip()
        validator(rows)

print("Valid email",valid)
print("Invalid email",invalid)

with open('valid_emails.csv','a',newline="") as vf:
    writer = csv.writer(vf)
    for email in list1:
        writer.writerow([email])

with open('invalid_emails.csv','a',newline="") as invf:
     writer = csv.writer(invf)
     for invemail in list2:
          writer.writerow([invemail])