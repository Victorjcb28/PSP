the_count = [1, 2, 3, 4, 5]
the_count2 = [1, 2, 3, 4, 5]
i=0
j=0
puntaje=0
# this first kind of for-loop goes through a list
for i in the_count:
    if i in the_count2:
    	puntaje=puntaje+10
    	
    else:
    	print "malo"
print puntaje