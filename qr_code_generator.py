import pyqrcode
import pymysql
db=pymysql.connect(host='localhost',user='root',password='*******',db='*********')
cursor=db.cursor();
cursor.execute("select *from abc")
numrows=cursor.rowcount
for i in range(numrows):
    row=cursor.fetchone()
    a=str(row)
    qr=pyqrcode.create(''+a+'')
    qr.png('qr_code'+str(i)+'.png',scale=7)
