import mysql.connector
localhost="bgztsjor72h6ardjo4uy-mysql.services.clever-cloud.com"
user="uvxcb2zoflv3tn5v"
password="QtU7GUWYZ2rwSdQ38Sco"
database="bgztsjor72h6ardjo4uy"


def select(q):
	con=mysql.connector.connect(user=user,password=password,host=localhost,database=database,port=3306)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	result=cur.fetchall()
	cur.close()
	con.close()
	return result

def insert(q):
	con=mysql.connector.connect(user=user,password=password,host=localhost,database=database,port=3306)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.lastrowid
	cur.close()
	con.close()
	return result

def update(q):
	con=mysql.connector.connect(user=user,password=password,host=localhost,database=database,port=3306)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	res=cur.rowcount
	cur.close()
	con.close()
	return res

def delete(q):
	con=mysql.connector.connect(user=user,password=password,host=localhost,database=database,port=3306)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.rowcount
	cur.close()
	con.close()
	return result