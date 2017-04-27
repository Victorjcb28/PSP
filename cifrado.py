import hashlib

h = "4d186321c1a7f0f354b297e8914ab240"
j=hashlib.md5("hola")
l=j.hexdigest()

print l
	
