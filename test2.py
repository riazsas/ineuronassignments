import mysql.connector as conn

mydb = conn.connect(host ="localhost", user="root", passwd="Inf29nity!")
cursor = mydb.cursor()

cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")
cursor.execute("insert into riaz.ineuron1 values(1,'riaz','riaz@gmail.com',100,30)")

mydb.commit()
cursor.execute("select * from riaz.ineuron1")
for i in cursor.fetchall():
    print (i)