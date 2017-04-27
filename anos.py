from datetime import datetime, date, time, timedelta
d=date.today()
j=int(d.year)+1
i=int(d.year)-100
while j>i:
	ano1=j-1 
	print ano1
	j=j-1