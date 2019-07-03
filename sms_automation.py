import csv
import webbrowser

#Creating empty lists and variables
reg=[]
phno=[]
new=2

#User input for msg date
month=input('Enter the month:')
date=(input('Enter the date:'))

#Opening csv files
f1=open("C:\\*path along with file name you want to create*")
csv_f1=csv.reader(f1)
f2=open("C:\\*database excel location*")
csv_f2=csv.reader(f2)

#Extracting registration numbers
for row in csv_f1:
    dob=[]
    dob.append(row[5])
    dob2=date+'-'+month
    if dob2 in dob[0]:
        reg.append(row[2])
print(reg)

#Extracting contact numbers
for i in range(len(reg)):
    for row2 in csv_f2:
        if reg[i]==row2[3]:
            phno.append(row2[10])
            break
print(phno)

'''#Sending messages
for i in range(len(phno)):
    url='http://softsms.in/app/smsapi/index.php?key=5c384d7e9588a&type=text&contacts=%s&senderid=GIFTER&msg=WE wish you a very Happy Birthday and prosperous future ahead                                @GIFTERIA'%phno[i]
    webbrowser.open(url,new=new)'''


