# -*- coding: UTF8-*-
import os
import wx
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
from datetime import datetime, date, time, timedelta
from time import time
import datetime


from reportlab.lib.pagesizes import LETTER #footer

def conexion():
    con=sq3.connect('Sisep.s3db')
    con.text_factory=str #pa quitar la U
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return



class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        con, cur = conexion()
        Fecha = str(datetime.date.today())
        cur.execute("Select Usuario from Bitacora order by Hora desc")
        rs=cur.fetchone()   
        page = "Page %s of %s" % (self._pageNumber, page_count)
        x = 500
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0]-x, 90,"Realizado por "+str(rs[0])+" en "+ Fecha)
        self.restoreState()

def ReporBitacora(self):
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

    parrafo = Paragraph("Reporte Bitacora ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Usuario","Fecha"]
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
            cur.execute('Select Usuario from Bitacora order by Usuario')
            rs=[r[0] for r in cur.fetchall()]
            
            cur.execute('Select Fecha from Bitacora order by Usuario')
            rs2=[r[0] for r in cur.fetchall()]
           
           

            fila4=[str(rs[i]),str(rs2[i])]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.

    
    
    

#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
    
    
    doc=SimpleDocTemplate("ReporteBitacora.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)

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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Usuario","Nombre","Apellido","Cedula","Tipo","Estado"]
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
            cur.execute('Select Usuario from Usuarios order by Cedula')
            rs=[r[0] for r in cur.fetchall()]
            
            cur.execute('Select Nombre from Usuarios order by Cedula')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Apellido from Usuarios order by Cedula')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Cedula from Usuarios order by Cedula')
            rs4=[r[0] for r in cur.fetchall()]
            cur.execute('Select Tipo from Usuarios order by Cedula')
            rs5=[r[0] for r in cur.fetchall()]
            cur.execute('Select Estado from Usuarios order by Cedula')
            rs6=[r[0] for r in cur.fetchall()]
            
            if rs6[i]==0:
                Valor="ACTIVO"
            else:
                Valor="BLOQUEADO"

            fila4=[str(rs[i]),str(rs2[i]),str(rs3[i]),str(rs4[i]),str(rs5[i]),Valor]

            i=i+1
            tabla = Table([fila4],colWidths=100)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.

    
    
    

#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
    
    
    doc=SimpleDocTemplate("ReporteUsuarios.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)

def PostulantesInternos(self):
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

    parrafo = Paragraph("Reporte Postulantes Internos",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))



#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Cargo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Experiencia where Vigente="SI"')
    rs1=cur.fetchall()
    
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen,Educacion,Experiencia where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cedula=Experiencia.Cedula and Experiencia.Vigente="SI" order by PUNTUACION DESC , MERITO ASC')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen,Educacion,Experiencia where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cedula=Experiencia.Cedula and Experiencia.Vigente="SI" order by PUNTUACION DESC , MERITO ASC')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen,Educacion,Experiencia where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cedula=Experiencia.Cedula and Experiencia.Vigente="SI" order by PUNTUACION DESC , MERITO ASC')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Examen.Cargo from Postulante,Examen,Educacion,Experiencia where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cedula=Experiencia.Cedula and Experiencia.Vigente="SI" order by PUNTUACION DESC , MERITO ASC')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Correo from Postulante,Examen,Educacion,Experiencia where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cedula=Experiencia.Cedula and Experiencia.Vigente="SI" order by PUNTUACION DESC , MERITO ASC')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesInternos.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.Nombre from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" order by PUNTUACION DESC , MERITO ASC')
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" order by PUNTUACION DESC , MERITO ASC')
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" order by PUNTUACION DESC , MERITO ASC')
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Sexo from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" order by PUNTUACION DESC , MERITO ASC')
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Correo from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" order by PUNTUACION DESC , MERITO ASC')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAdministrativo.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]
                      
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistenteAd.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))



#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesChofer.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesVigilante.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))



#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesGVentas.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Examen where Cargo="ASISTENTE VENTAS"')
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
            cur.execute('Select Postulante.correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAVentas.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesCajero.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))




#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAtencionCliente.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))




#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
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
            cur.execute('Select Postulante.correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" order by Examen.Puntuacion Desc')
            rs4=[r[0] for r in cur.fetchall()]           
            

     

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

            i=i+1
            tabla = Table([fila4],colWidths=125)

            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesRecursos.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)





def ReportePostulanteI(self):
    con, cur = conexion()
    frm=self
    Ce= frm.txtCedula.GetValue()

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

    parrafo = Paragraph("Reporte Postulantes",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))



    #Datos Personales
    cadena="Datos Personales"
    fila1=[cadena.center(200," ")]
    
    tabla9=Table([fila1],colWidths=600)
    tabla9.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla9.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla9.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla9)

    #fila 1
    fila1=["Nombre","Apellido","Cedula","Sexo","Edad"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select * from Postulante where Cedula=:Ce",{"Ce": Ce})
    rs1=cur.fetchone()


     

    fila4=[str(rs1[0]),str(rs1[1]),str(rs1[2]),str(rs1[3]),str(rs1[6])]

   
    tabla1 = Table([fila4],colWidths=120)

    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla1)

    #fila 2
    fila1=["Estado","Municipio","Parroquia","Direccion","Telefono"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select Estado.Nombre,Munic.Nombre,Parroquia.Nombre,Postulante.Direccion,Postulante.Telefono from Postulante,Estado,Munic,Parroquia where Estado.Id= Munic.Id and Munic.Id=Parroquia.Id and Parroquia.Id=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs2=cur.fetchone()
            

     

    fila4=[str(rs2[0]),str(rs2[1]),str(rs2[2]),str(rs2[3]),str(rs2[4])]

   
    tabla2 = Table([fila4],colWidths=120)

    tabla2.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla2.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla2)
    
    #Educacion
    cadena="Educacion"
    fila1=[cadena.center(200," ")]
    tabla10=Table([fila1],colWidths=600)
    tabla10.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla10.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla10.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla10)

    #fila 3 
    fila1=["Correo","Educacion","Titulo","Idioma","Paquete Office"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select Postulante.Correo,Educacion.NEducacion,Educacion.Titulo,Educacion.Idioma,Educacion.Office from Postulante, Educacion where Educacion.Cedula=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs3=cur.fetchone()
            

     

    fila4=[str(rs3[0]),str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4])]

   
    tabla3 = Table([fila4],colWidths=120)

    tabla3.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla3.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla3)

    #fila 4
    fila1=["Graduacion","Merito","Militar","Primeros Auxilios","Contabilidad"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select AGraduacion,Merito,Militar,PAuxilio,Contabilidad from Educacion where Cedula=:Ce",{"Ce": Ce})
    rs4=cur.fetchone()
            

     

    fila4=[str(rs4[0]),str(rs4[1]),str(rs4[2]),str(rs4[3]),str(rs4[4])]

   
    tabla4 = Table([fila4],colWidths=120)

    tabla4.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla4.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla4)
    
    #Experiencia
    cadena="Experiencia Laboral"
    fila1=[cadena.center(200," ")]
    tabla11=Table([fila1],colWidths=600)
    tabla11.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla11.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla11.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla11)

    #fila 5
    fila1=["Trabaja Empresa","Empresa","Años de Trabajo","Cargo",""]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select * from Experiencia where Cedula=:Ce",{"Ce": Ce})
    rs4=cur.fetchone()
            

     

    fila4=[str(rs4[0]),str(rs4[1]),str(rs4[2]),str(rs4[3]),""]

   
    tabla5 = Table([fila4],colWidths=120)

    tabla5.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla5.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla5)
    
    

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulanteIndividual.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)



def ReportePostulanteIP(self):
    con, cur = conexion()
    frm=self
    

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

    parrafo = Paragraph("Reporte Postulantes",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    
    #Cedula
    dato="Guardar Postulante"
    cur.execute("select max(hora),Variable from registro where operacion=:dato",{"dato": dato})
    rs6=cur.fetchone()
    
    
    Ce=str(rs6[1])

    
    
    

    #Datos Personales
    cadena="Datos Personales"
    fila1=[cadena.center(200," ")]
    
    tabla9=Table([fila1],colWidths=600)
    tabla9.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla9.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla9.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla9)

    #fila 1
    fila1=["Nombre","Apellido","Cedula","Sexo","Edad"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select * from Postulante where Cedula=:Ce",{"Ce": Ce})
    rs1=cur.fetchone()
            

     

    fila4=[str(rs1[0]),str(rs1[1]),str(rs1[2]),str(rs1[3]),str(rs1[6])]

   
    tabla1 = Table([fila4],colWidths=120)

    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla1)

    #fila 2
    fila1=["Estado","Municipio","Parroquia","Direccion","Telefono"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select Estado.Nombre,Munic.Nombre,Parroquia.Nombre,Postulante.Direccion,Postulante.Telefono from Postulante,Estado,Munic,Parroquia where Estado.Id= Munic.Id and Munic.Id=Parroquia.Id and Parroquia.Id=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs2=cur.fetchone()
            

     

    fila4=[str(rs2[0]),str(rs2[1]),str(rs2[2]),str(rs2[3]),str(rs2[4])]

   
    tabla2 = Table([fila4],colWidths=120)

    tabla2.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla2.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla2)
    
    #Educacion
    cadena="Educacion"
    fila1=[cadena.center(200," ")]
    tabla10=Table([fila1],colWidths=600)
    tabla10.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla10.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla10.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla10)

    #fila 3
    
    fila1=["Correo","Educacion","Titulo","Idioma","Paquete Office"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select Postulante.Correo,Educacion.NEducacion,Educacion.Titulo,Educacion.Idioma,Educacion.Office from Postulante, Educacion  where Educacion.Cedula=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs3=cur.fetchone()
            

     

    fila4=[str(rs3[0]),str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4])]

   
    tabla3 = Table([fila4],colWidths=120)

    tabla3.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla3.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla3)

    #fila 4
    fila1=["Graduacion","Merito","Militar","Primeros Auxilios","Contabilidad"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select AGraduacion,Merito,Militar,PAuxilio,Contabilidad from Educacion where Cedula=:Ce",{"Ce": Ce})
    rs4=cur.fetchone()
            

     

    fila4=[str(rs4[0]),str(rs4[1]),str(rs4[2]),str(rs4[3]),str(rs4[4])]

   
    tabla4 = Table([fila4],colWidths=120)

    tabla4.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla4.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla4)
    
    #Experiencia
    cadena="Experiencia Laboral"
    fila1=[cadena.center(200," ")]
    tabla11=Table([fila1],colWidths=600)
    tabla11.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla11.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla11.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla11)

    #fila 5
    fila1=["Trabaja Empresa","Empresa","Años de Trabajo","Cargo",""]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select * from Experiencia where Cedula=:Ce",{"Ce": Ce})
    rs4=cur.fetchone()
            

     

    fila4=[str(rs4[0]),str(rs4[1]),str(rs4[2]),str(rs4[3]),""]

   
    tabla5 = Table([fila4],colWidths=120)

    tabla5.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla5.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla5)
    
    
    

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulanteIndividualssss.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def ReportePostulanteIPM(self):
    con, cur = conexion()
    frm=self
    

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

    parrafo = Paragraph("Reporte Postulantes",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logo1.jpg" 
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    
    #Cedula
    dato="Modificar Postulante"
    cur.execute("select max(hora),Variable from registro where operacion=:dato",{"dato": dato})
    rs6=cur.fetchone()
    
    
    Ce=str(rs6[1])

    
    
    

    #Datos Personales
    cadena="Datos Personales"
    fila1=[cadena.center(200," ")]
    
    tabla9=Table([fila1],colWidths=600)
    tabla9.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla9.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla9.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla9)

    #fila 1
    fila1=["Nombre","Apellido","Cedula","Sexo","Edad"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select * from Postulante where Cedula=:Ce",{"Ce": Ce})
    rs1=cur.fetchone()
            

     

    fila4=[str(rs1[0]),str(rs1[1]),str(rs1[2]),str(rs1[3]),str(rs1[6])]

   
    tabla1 = Table([fila4],colWidths=120)

    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla1)

    #fila 2
    fila1=["Estado","Municipio","Parroquia","Direccion","Telefono"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select Estado.Nombre,Munic.Nombre,Parroquia.Nombre,Postulante.Direccion,Postulante.Telefono from Postulante,Estado,Munic,Parroquia where Estado.Id= Munic.Id and Munic.Id=Parroquia.Id and Parroquia.Id=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs2=cur.fetchone()
            

     

    fila4=[str(rs2[0]),str(rs2[1]),str(rs2[2]),str(rs2[3]),str(rs2[4])]

   
    tabla2 = Table([fila4],colWidths=120)

    tabla2.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla2.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla2)
    
    #Educacion
    cadena="Educacion"
    fila1=[cadena.center(200," ")]
    tabla10=Table([fila1],colWidths=600)
    tabla10.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla10.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla10.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla10)

    #fila 3
    
    fila1=["Correo","Educacion","Titulo","Idioma","Paquete Office"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select Postulante.Correo,Educacion.NEducacion,Educacion.Titulo,Educacion.Idioma,Educacion.Office from Postulante, Educacion  where Educacion.Cedula=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs3=cur.fetchone()
            

     

    fila4=[str(rs3[0]),str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4])]

   
    tabla3 = Table([fila4],colWidths=120)

    tabla3.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla3.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla3)

    #fila 4
    fila1=["Graduacion","Merito","Militar","Primeros Auxilios","Contabilidad"]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select AGraduacion,Merito,Militar,PAuxilio,Contabilidad from Educacion where Cedula=:Ce",{"Ce": Ce})
    rs4=cur.fetchone()
            

     

    fila4=[str(rs4[0]),str(rs4[1]),str(rs4[2]),str(rs4[3]),str(rs4[4])]

   
    tabla4 = Table([fila4],colWidths=120)

    tabla4.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla4.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla4)
    
    #Experiencia
    cadena="Experiencia Laboral"
    fila1=[cadena.center(200," ")]
    tabla11=Table([fila1],colWidths=600)
    tabla11.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)])
    tabla11.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla11.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla11)

    #fila 5
    fila1=["Vigente","Empresa","Años de Trabajo","Cargo",""]
    tabla1=Table([fila1],colWidths=120)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.white)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    

    cur.execute("Select * from Experiencia where Cedula=:Ce",{"Ce": Ce})
    rs4=cur.fetchone()
            

     

    fila4=[str(rs4[0]),str(rs4[1]),str(rs4[2]),str(rs4[3]),""]

   
    tabla5 = Table([fila4],colWidths=120)

    tabla5.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla5.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

    story.append(tabla5)
    
    
    

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulanteIndividualssss.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)



def PostulantesAsistentesFecha(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Asistentes",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="ASISTENTE" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistentesFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesAdministratativoFecha(self):
    con, cur = conexion()
    frm=self


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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="ADMINISTRACION" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAdministrativoFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesVigilanteFecha(self):
    con, cur = conexion()
    frm=self


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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="VIGILANTE" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesVigilanteFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesCajeroFecha(self):
    con, cur = conexion()
    frm=self


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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="CAJERO" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesCajeroFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesRecursosHFecha(self):
    con, cur = conexion()
    frm=self


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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="RECURSOS HUMANOS" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesRecursosHFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesChoferFecha(self):
    con, cur = conexion()
    frm=self


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

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="CHOFER" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesChoferFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesGerenteVentasFecha(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Gerente Ventas",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="GERENTE VENTAS" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesGerenteVentasFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesAsistenteVentasFecha(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Asistentes Ventas",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="ASISTENTE VENTAS" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistenteVentasFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesServicioCFecha(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Servicio al cliente",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Sexo","Correo"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    campo=frm.txtDesde.GetValue()
    campo2=frm.txtHasta.GetValue()
    fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
    fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=? and b.Cargo="SERVICIO AL CLIENTE" GROUP   BY b.cargo',(fecha1,fecha2))
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs1=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs2=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Sexo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs3=[r[0] for r in cur.fetchall()]
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and Postulante.Fecha>:fecha1 ORDER BY Examen.puntuacion desc',{"fecha1":fecha1} )
                rs4=[r[0] for r in cur.fetchall()]           
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesServicioCFecha.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesAdministratativoAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Administrativo Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="ADMINISTRACION" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAdministrativoAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesAsistenteAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Asistente Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="ASISTENTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistenteAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesChoferAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes ChoferAprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="CHOFER" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesChoferAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesCajeroAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Cajero Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="CAJERO" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesCajeroAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesVigilanteAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Vigilante Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=125)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="VIGILANTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=125)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesVigilanteAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesGerenteVAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Gentente en Ventas Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="GERENTE VENTAS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesGerenteVAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesAsistenteVAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Asistente en Ventas Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="ASISTENTE VENTAS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistenteVAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesAtencionCAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Atencion al Cliente Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="SERVICIO AL CLIENTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAtencionCAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesRecursosHAprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Recursos Humanos Aprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion>=50 and b.Cargo="RECURSOS HUMANOS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion>=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesRecursosHAprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesAdministrativoReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Administrativo Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="ADMINISTRACION" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAdministrativoReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesAsistenteReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Asistente Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="ASISTENTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistenteReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesChoferReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes ChoferReprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="CHOFER" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesChoferReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesCajeroReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Cajero Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="CAJERO" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesCajeroReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesVigilanteReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Vigilante Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="VIGILANTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesVigilanteReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)

def PostulantesGerenteVReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Gentente en Ventas Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="GERENTE VENTAS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesGerenteVReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesAsistenteVReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Asistente en Ventas Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="ASISTENTE VENTAS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAsistenteVReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesAtencionCReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Atencion al Cliente Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="SERVICIO AL CLIENTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesAtencionCReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


def PostulantesRecursosHReprobado(self):
    con, cur = conexion()
    frm=self


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

    parrafo = Paragraph("Reporte Postulantes Recursos Humanos Reprobado",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.


#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.
    
    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   b.Puntuacion<=50 and b.Cargo="RECURSOS HUMANOS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    if rs1:
        
        i=0
        l=0
        j=0
        
        
        for ol in rs1 :

            hola=ol[l]
            
            while i < hola:
                cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs=[r[0] for r in cur.fetchall()]
               
                
                cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs1=[r[0] for r in cur.fetchall()]
                
                
                cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs2=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs3=[r[0] for r in cur.fetchall()]
                
                cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.Puntuacion<=50 ORDER BY Examen.puntuacion desc')
                rs4=[r[0] for r in cur.fetchall()]   
                        
                

         

                fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i]),str(rs4[i])]

                i=i+1
                tabla = Table([fila4],colWidths=100)

                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])

                story.append(tabla)
    #else:
        #dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        #dlg.ShowModal()
        #dlg.Destroy()

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("ReportePostulantesRecursosHReprobado.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)
#Construimos el Platypus story.

    doc.build(story)


#<--------Reporte Seleccionados--------->

def ReportePostulantesAdministrativoSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Administrativos Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="ADMINISTRACION" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ADMINISTRACION" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesAdministrativoSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)


def ReportePostulantesAsistenteSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Asistentes Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="ASISTENTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesAsistenteSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)

def ReportePostulantesChoferSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Chofer Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="CHOFER" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CHOFER" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesChoferSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)


def ReportePostulantesCajeroSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Cajero Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="CAJERO" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="CAJERO" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesCajeroSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)

def ReportePostulantesVigilanteSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Vigilante Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="VIGILANTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="VIGILANTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesVigilanteSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)


def ReportePostulantesRecursosHSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Recursos Humanos Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="RECURSOS HUMANOS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="RECURSOS HUMANOS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesRecursosHSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)


def ReportePostulantesGerenteVSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Gerente en Ventas Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="GERENTE VENTAS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="GERENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesGerenteVSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)



def ReportePostulantesAtencionCSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Atencion Al Cliente Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="SERVICIO AL CLIENTE" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="SERVICIO AL CLIENTE" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesAtencionCSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)


def ReportePostulantesAsistenteVSeleccionados(self):
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

    parrafo = Paragraph("Reporte Postulantes Asistente en Ventas Seleccionados ",cabecera)
    

#Lo incluimos en el Platypus story.

    story.append(parrafo)

    


#Ahora incluimos una imagen.

    fichero_imagen = "iconos/Logonuevo1.png" #CAmbiar Loogo
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=300,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un p�rrafo. Vamos a crear un texto largo para demostrar c�mo se genera m�s de una hoja.
    #USuarios
    

#Damos un estilo BodyText al segundo p�rrafo, que ser� el texto a escribir.
    fila1=["Nombre","Apellido","Cedula","Correo","Telefono"]
    tabla1=Table([fila1],colWidths=100)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('SELECT  COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE    b.Seleccion="SI" and b.Cargo="ASISTENTE VENTAS" GROUP   BY b.cargo')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs=[r[0] for r in cur.fetchall()]
               
                
            cur.execute('Select Postulante.Apellido from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs1=[r[0] for r in cur.fetchall()]
                
                
            cur.execute('Select Postulante.Cedula from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs2=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.Correo from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
            rs3=[r[0] for r in cur.fetchall()]
                
            cur.execute('Select Postulante.telefono from Postulante,Examen where Postulante.Cedula=Examen.Cedula and Examen.Cargo="ASISTENTE VENTAS" and examen.seleccion="SI" ORDER BY Examen.puntuacion desc')
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
    
    
    doc=SimpleDocTemplate("ReportePostulantesAsistenteVSeleccionados.pdf",pagesize=landscape(letter),showBoundary=1)
    doc.multiBuild(story, canvasmaker=FooterCanvas)

#Construimos el Platypus story.

    doc.build(story)