from selenium import webdriver
import csv

phno=[]

driver=webdriver.Chrome('C:\\webdrivers\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

file=input('Enter the DataBase name:')

#Opening csv files
f1=open("C:\\Users\\Sahas\\Desktop\\+file+")
csv_f1=csv.reader(f1)

#Extracting phone numbers
for row in csv_f1:
    phno.append(row[3])

msg=input('Enter your message:')

input('Enter anything after scanning')

for i in range(len(phno)):
    user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()
    msg_box=driver.find_element_by_class_name('_1Plpp')
    msg_box.send_keys(msg)
    button=driver.find_element_by_class_name('_35EW6')
    button.click()
