from datetime import datetime, date, time, timedelta
dia=22
mes=04
ano=1989
d=date.today()
ano1= d.year-ano
cadena="hola"
if d.month <= mes:
	if d.day < dia:
		ano1=ano1-1	
print ano1
print cadena.center(50," ")
