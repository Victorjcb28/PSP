import sqlite3 as sq3
def conexion():
    con=sq3.connect('Sisep.s3db')
    con.text_factory=str #pa quitar la U
    cur = con.cursor()
    return con, cur

hola=30
i=0
while i < hola:
	con,cur=conexion()
	cur.execute('Select Nombre from Usuarios order by Nombre')
	rs=[r[0] for r in cur.fetchall()]
	print(rs)
    

    
            

