import pymysql
import datetime
import cryptography
import atnd_GUI.py
now=datetime.datetime.now()
db=pymysql.connect(host='localhost',user='root',password='sahas',db='login')
cursor=db.cursor();
print("USER LOGIN");
t=input("Enter your name:")
x=str(now.hour)
y=str(now.minute)
z=x+":"+y
sql="INSERT INTO " +t+ "(login) VALUES(%s)"
val=(z,)
cursor.execute(sql,val)
db.commit()
print(t+" LOGGED IN!!!!")
o=int(input("Enter 1 to logout:"))
if o==1:
    r=str(now.hour)
    s=str(now.minute)
    q=r+":"+s
    sql="update " +t+ " set logout=%s where login=%s"
    val=q,z
    cursor.execute(sql,val)
    db.commit()
    print(t+" LOGGED OUT!!!!")
    sql="select *from " +t+ ";"
    cursor.execute(sql)
    records=cursor.fetchall()
    for i in records:
        print(i[0]," ",i[1])
