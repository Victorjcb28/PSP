# -*- coding: cp1252 -*-
import os

#Obtenemos de platypus las clases Paragraph, para escribir p�rrafos Image, para insertar im�genes y SimpleDocTemplate para definir el DocTemplate. Adem�s importamos Spacer, para incluir espacios .

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
#Importamos clase de hoja de estilo de ejemplo.

from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet

#Se importa el tama�o de la hoja.

from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter, landscape

#Y los colores.

from reportlab.lib import colors
import sqlite3 as sq3

def conexion():
    con=sq3.connect('Sisep.s3db')
    con.text_factory=str #pa quitar la U
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return

def ReporUsuario(self):
    con, cur = conexion()


#Creamos un PageTemplate de ejemplo.

    estiloHoja = getSampleStyleSheet()

#Inicializamos la lista Platypus Story.

    story = []

#Definimos c�mo queremos que sea el estilo de la PageTemplate.

    cabecera = estiloHoja['Heading4']

#No se har� un salto de p�gina despu�s de escribir la cabecera (valor 1 en caso contrario).

    cabecera.pageBreakBefore=0

#Se quiere que se empiece en la primera p�gina a escribir. Si es distinto de 0 deja la primera hoja en blanco.

    cabecera.keepWithNext=0

#Color de la cabecera.

    cabecera.backColor=colors.cyan

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Usuarios ",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "primero.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Usuario","Clave","Tipo","Estado"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Usuarios order by Nombre')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Nombre from Usuarios order by Nombre')
            rs=cur.fetchall()
            cur.execute('Select Clave from Usuarios order by Nombre')
            rs1=cur.fetchall()
            cur.execute('Select Tipo from Usuarios order by Nombre')
            rs2=cur.fetchall()
            cur.execute('Select Estado from Usuarios order by Nombre')
            rs3=cur.fetchall()
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReporteUsuarios.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)

def Postulantes(self):
    con, cur = conexion()


#Creamos un PageTemplate de ejemplo.

    estiloHoja = getSampleStyleSheet()

#Inicializamos la lista Platypus Story.

    story = []

#Definimos c�mo queremos que sea el estilo de la PageTemplate.

    cabecera = estiloHoja['Heading4']

#No se har� un salto de p�gina despu�s de escribir la cabecera (valor 1 en caso contrario).

    cabecera.pageBreakBefore=0

#Se quiere que se empiece en la primera p�gina a escribir. Si es distinto de 0 deja la primera hoja en blanco.

    cabecera.keepWithNext=0

#Color de la cabecera.

    cabecera.backColor=colors.cyan

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = ""
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Caudal","Fluido","Densidad","Viscosidad","Diametro Nom"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
#Fila1
    cur.execute("Select * from variable order by oid DESC LIMIT 1 ")
    rs=cur.fetchone()

    fila4=[str(rs[1]),str(rs[2]),str(rs[3]),str(rs[4]),str(rs[5])]


    tabla = Table([fila4],colWidths=120)

    tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla)

    fila1=["Diametro In","Area Flu","Velocidad","Codo","Factor Friccion"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#Fila2
    cur.execute("Select * from variable order by oid DESC LIMIT 1 ")
    rs=cur.fetchone()

    fila4=[str(rs[6]),str(rs[7]),str(rs[8]),str(rs[14]),str(rs[0])]


    tabla1 = Table([fila4],colWidths=120)

    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla1)


#Fila3
    fila1=["Perdida","","","",""]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)
    cur.execute("Select * from variable order by oid DESC LIMIT 1 ")
    rs=cur.fetchone()

    fila4=[str(rs[15]),str(),str(),str(),str()]


    tabla3 = Table([fila4],colWidths=120)

    tabla3.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla3.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla3)

#Dejamos espacio.
    story.append(Spacer(0,80))
#Ahora incluimos una imagen.

    fichero_imagen = "codo.jpg"
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))


#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReporteCodo.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)