# -*- coding: UTF8-*-
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

    cabecera.backColor=colors.white


#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Usuarios ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)
    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" #CAmbiar Loogo
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
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Clave from Usuarios order by Nombre')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Tipo from Usuarios order by Nombre')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Estado from Usuarios order by Nombre')
            rs3=[r[0] for r in cur.fetchall()]
            
     

            fila4=[str(unicode(rs[i])),str(rs1[i]),str(rs2[i]),str(rs3[i])]

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

def PostulantesAdministratativo(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Administrativo",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="ADMINISTRACION"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAdministrativo.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)


def PostulantesAsistenteA(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Asistente Administrativo",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="ASISTENTE"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistenteAd.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)


def PostulantesChofer(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Chofer",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="CHOFER"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesChofer.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)

def PostulantesVigilante(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Vigilante",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="VIGILANTE"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesVigilante.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)

def PostulantesVigilante(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Vigilante",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="VIGILANTE"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesVigilante.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)

def PostulantesGVentas(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Gerente en Ventas",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="GERENTE VENTAS"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesGVentas.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)

def PostulantesAVentas(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Asistente en Ventas",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="ASISTENTE VENTAS')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAVentas.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)


def PostulantesCajero(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Cajero",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="CAJERO"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesCajero.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)

def PostulantesAtencionC(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Atencion al Cliente",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="SERVICIO AL CLIENTE"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAtencionCliente.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)


def PostulantesRecursos(self):
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

    cabecera.backColor=colors.white

#Incluimos un Flowable, que en este caso es un p�rrafo.

    parrafo = Paragraph("Reporte Postulantes Recursos Humanos",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Puntuacion %"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="RECURSOS HUMANOS"')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" order by Examen.Puntuacion Desc')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" order by Examen.Puntuacion Desc')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" order by Examen.Puntuacion Desc')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" order by Examen.Puntuacion Desc')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Puntuacion from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesRecursos.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)

