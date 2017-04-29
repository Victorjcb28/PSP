import sqlite3 as sq3
def conexion():
    con=sq3.connect('prueba.s3db')
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return


con,cur=conexion()
dato="ADMINISTRACION"
cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
rs2=cur.fetchone()
i=0
j=0
lista2=[]
cur.execute("select max(id) from examen")
rs4=cur.fetchone()
lista1=[str(rs4[0])]
j=0
if rs2:
	while i<4:
		cur.execute("Select * from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
		rs1=[r[0] for r in cur.fetchall()]

		lista2.append(str(rs1[i]))
		i=i+1		

while lista1[0] != lista2[j]:
	j=j+1
print j+1

print lista2



