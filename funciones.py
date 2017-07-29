#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#self.db.execute(SQL_STRING, (dork.decode('utf-8'), ))

import sqlite3 as sq3
import wx
import os
import FuncionesReportes as FR
import hashlib

import entrada as E
import PrincipalAdmin as PA
import PrincipalSecretaria as PS

import GuardarPostulante as GP
import BuscarPostulante as BP1
import BuscarPostulante2 as BP2

import EChofer as EC
import EChoferM as ECM

import EAdministracion as EA
import EAdministracionM as EAM

import EAsistenteA as EAA
import EAsistenteAM as EAAM

import ECajero as ECA
import ECajeroM as ECAM

import EServicioC as ESC
import EServicioCM as ESCM


import ERecursosH as ERH
import ERecursosHM as ERHM

import ECompraVenta as ECV
import ECompraVentaM as ECVM

import ECompraVenta1 as ECV1
import ECompraVenta1M as ECV1M

import EVigilante as EV
import EVigilanteM as EVM


from datetime import datetime, date, time, timedelta
from time import time
import datetime

import numpy as na
import matplotlib.pyplot as plt


#Conexion base de datos
def conexion():
    con=sq3.connect('Sisep.s3db')
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return


#funciones nuevas.
def UsuarioFecha(frm):
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    self=frm
    con, cur=conexion()

    cur.execute("select usuario from bitacora order by hora desc")
    rs=cur.fetchone()
    if rs:

        self.txtUsuario.SetValue(str(rs[0]))
        self.txtFecha.SetValue(str(Fecha))
    else:
        self.txtUsuario.SetValue(" ")
        self.txtFecha.SetValue(" ") 

def Edad(frm):
    self=frm
    dia=int(frm.cobDia.GetValue())
    mes=int(frm.cobMes.GetValue())
    ano=int(frm.cobAno.GetValue())

    d=date.today()
    ano1=d.year-ano
    if ano1<18:
        dlg=wx.MessageDialog(self,'No puede ser menor a 18 años', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        self.txtEdad.Clear()
    else:
        if d.month <= mes:
            if d.day < dia:
                ano1=ano1-1 
        self.txtEdad.SetValue(str(ano1))

def Ano(frm):
    self=frm
    d=date.today()
    j=int(d.year)+1
    i=int(d.year)-100
    while j>i:
        ano1=j-1 
        self.cobAno.Append(str(ano1))
        j=j-1
        
#Funciones nuevas para levantar examen al momento de guardar Postulante !!Pedido por profesor!!
def Administrativo(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="ADMINISTRACION"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def Chofer(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="CHOFER"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def Cajero(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="CAJERO"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def Vigilante(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="VIGILANTE"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def GerenteVentas(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="GERENTE VENTAS"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def AsistenteVentas(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="ASISTENTE VENTAS"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def Asistente(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="ASISTENTE"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def ServicioCliente(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="SERVICIO AL CLIENTE"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()

def RecursosHumanos(frm):

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Seleccionar Postulante"
    Nom="RECURSOS HUMANOS"
    self=frm
    con, cur=conexion()
    cur.execute("Select Usuario from Bitacora order by hora")
    rs2=cur.fetchone()
    if rs2:
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
        con.commit()
#Fin funciones examen-Guardar      
                    

#fin funciones nuevas        

def Bitacora(frm):
    Usu=frm.txtUsuario.GetValue()
    En=Usu.upper()
    
    Hora=datetime.datetime.now()
    
    Fecha = datetime.date.today()
    datos=(En,Fecha,Hora)

    con,cur=conexion()


    cur.execute("Insert into Bitacora (Usuario,Fecha,Hora) Values (?,?,?)", (En,Fecha,Hora))
    

    con.commit()
    cur.close()
    con.close()

def Entrada(frm):

    Usu=frm.txtUsuario.GetValue()
    En=Usu.upper()
    Cl=hashlib.md5(frm.txtClave.GetValue())
    Cla=Cl.hexdigest()
    datos=(En,Cla)

    con,cur=conexion()
    self=frm

    cur.execute("Select Estado from Usuarios where Estado= 1 and Usuario=:En",{"En":En})
    rs=cur.fetchone()

    if rs:
        dlg=wx.MessageDialog(self,'Usuario Bloqueado', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    else:
        cur.execute("Select * from Usuarios Where Usuario=? and Clave=? and Tipo='ADMINISTRADOR'",datos)
        rs1=cur.fetchone()

        if rs1:

            Ventana=PA.Principal(self)
            Ventana.Show()
            self.Hide()
        else:
            cur.execute("Select * from Usuarios Where Usuario=? and Clave=? and Tipo='SECRETARIA'",datos)
            rs2=cur.fetchone()
            if rs2:

                Ventana=PS.Principal(self)
                Ventana.Show()
                self.Hide()
            
            else:
                dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()


#<------Usuarios-------->
def Bloquear(frm):
    self=frm
    con,cur=conexion()
    U=frm.txtNombre.GetValue()
    Usu=U.upper()
    dato=Usu
    cur.execute('select usuario from bitacora order by hora desc')
    rs1=cur.fetchone()
    Usuario=str(rs1[0])

    cur.execute("Select Estado from Usuarios where Usuario=:dato",{"dato":dato})
    
    rs=cur.fetchone() 
    N=int(rs[0])
    if N ==1:
        wx.MessageBox('Error, El usuario ya estaba bloqueado', 'Caja de mensaje')
    else:
        if Usu==Usuario:
            dlg=wx.MessageDialog(self,'No se puede bloquear el usuario actual', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:

            cur.execute("Update  Usuarios set Estado= 1 where Usuario=:dato",{"dato":dato})
            wx.MessageBox('Usuario Bloqueado Satisfactoriamente', 'Caja de mensaje')
            con.commit()

            self.txtNombre.Clear()
            self.txtClave.Clear()
            self.cobTipo.Clear()

def Desbloquear(frm):
    self=frm
    con,cur=conexion()
    U=frm.txtNombre.GetValue()
    Usu=U.upper()
    dato=Usu
    cur.execute("Select Estado from Usuarios where Usuario=:dato",{"dato":dato})
    rs=cur.fetchone()
    N=int(rs[0])
    if N ==0:
        wx.MessageBox('Error, El usuario no esta bloqueado', 'Caja de mensaje')
    else:
        cur.execute("Update  Usuarios set Estado= 0 where Usuario=:dato",{"dato":dato})
        wx.MessageBox('Usuario Desbloqueado Satisfactoriamente', 'Caja de mensaje')
        con.commit()

        self.txtNombre.Clear()
        self.txtClave.Clear()
        self.cobTipo.Clear()


def GuardarUsuario(frm):
    No=frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap=frm.txtApellido.GetValue()
    Ape=Ap.upper()
    Ce=frm.txtCedula.GetValue()
    Usuario=frm.txtUsuario.GetValue()
    Usu=Usuario.upper()
    dato=Usu
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Guardar Usuario"
    Cl=hashlib.md5(frm.txtClave.GetValue())
    Cla=Cl.hexdigest()
    Ti=frm.cobTipo.GetValue()
    Es=0

    datos1=(Nom,Cla,Ti,Es,Ape,Ce,Usu)
    self=frm
    con, cur=conexion()
    # Saber si es menor de 8 caracteres
    if len(Cla)< 8:
        dlg=wx.MessageDialog(self,'La clave debe ser mayor a 8 caracteres', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        self.txtClave.Clear()
        self.txtClave.SetFocus()
    else:#isdigit solo numeros isalpha solo letras.... comparacion alfanumerica
        if Cla.isdigit()or Cla.isalpha() : #isdigit puros numeros, isalpha puras letras
            dlg=wx.MessageDialog(self,'La Clave Debe Contener Datos Alfanumericos', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.txtClave.Clear()
            self.txtClave.SetFocus()
        
        else:
            cur.execute("Select Usuario from Usuarios where Usuario=:dato",{"dato":dato})
    
            rs=cur.fetchone() 
            
            if rs:
                wx.MessageBox('Error, El usuario ya esta Registrado ', 'Caja de mensaje')
            else:       
                cur.execute('INSERT INTO Usuarios (Nombre,Clave,Tipo, Estado,Apellido,Cedula,Usuario) VALUES (?,?,?,?,?,?,?)',(datos1))
                wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')
                con.commit()
            
                cur.execute("Select usuario from Bitacora order by hora desc")
                rs2=cur.fetchone()
                if rs2:
        
                    N=(str(rs2[0]))
                    cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
                    con.commit()
                
                    
                    
                        
                    self.Hide()
                        
                
                self.txtNombre.Clear()
                self.txtClave.Clear()
                #self.cobTipo.Clear()
                self.txtNombre.SetFocus()
            
                cur.close()
                con.close()

def BuscarU(frm):#Buscar de modificar
    con,cur=conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Usuario"
    dato1=frm.txtUsuario.GetValue()
    dato=dato1.upper()
    cur.execute("Select * from Usuarios where Usuario=:dato",{"dato":dato})
    
    rs=cur.fetchone()
    self=frm
    if rs:
        self.txtNombre.SetValue(str(rs[0]))
        self.txtClave.SetValue(str(rs[1]))
        self.txtClave2.SetValue(str(rs[1]))
        self.cobTipo.SetValue(str(rs[2]))
        self.txtApellido.SetValue(str(rs[4]))
        self.txtCedula.SetValue(str(rs[5]))

        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato1,Hora,Op))
            con.commit()
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

def BuscarU1(frm):#Buscar de Buscar
    con,cur=conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Usuario"
    dato1=frm.txtUsuario.GetValue()
    dato=dato1.upper()
    cur.execute("Select * from Usuarios where Usuario=:dato",{"dato":dato})
    
    rs=cur.fetchone()
    self=frm
    

    if rs:
        Estado=str(rs[3])
        
        if Estado=="1":
            
            self.txtEstado.SetValue("BLOQUEADO")
        else:
            self.txtEstado.SetValue("ACTIVO")



        self.txtNombre.SetValue(str(rs[0]))
        self.txtClave.SetValue(str(rs[1]))
        self.cobTipo.SetValue(str(rs[2]))
        self.txtApellido.SetValue(str(rs[4]))
        self.txtCedula.SetValue(str(rs[5]))
        self.txtUsuario.SetValue(str(rs[6]))
            
        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato1,Hora,Op))
            con.commit()
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

def BuscarU2(frm):#Buscar de Bloquear
    con,cur=conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Usuario"
    dato1=frm.txtNombre.GetValue()
    dato=dato1.upper()
    cur.execute("Select * from Usuarios where Usuario=:dato",{"dato":dato})
    rs=cur.fetchone()
    self=frm
    if rs:
    

  


        
        self.txtClave.SetValue(str(rs[1]))
        self.cobTipo.SetValue(str(rs[2]))
            
                
            
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
            
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato1,Hora,Op))
            con.commit()
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    



def ModificarUsuario(frm):
    self=frm
    No=frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap=frm.txtApellido.GetValue()
    Ape=Ap.upper()
    Ce=frm.txtCedula.GetValue()
    Usuario=frm.txtUsuario.GetValue()
    Usu=Usuario.upper()
    dato=Usu
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Cl=hashlib.md5(frm.txtClave.GetValue())
    Cla=Cl.hexdigest()
    Ti=frm.cobTipo.GetValue()
    
    
    Op="Modificar Usuario"
    con,cur=conexion()

    cur.execute('UPDATE Usuarios Set  Clave=?, Tipo=?,Nombre=?,Apellido=?,Cedula=? WHERE Usuario=?',(Cla,Ti,Nom,Ape,Ce,Usu))
    wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
    con.commit()
    cur.execute("Select usuario from Bitacora order by hora desc")
    rs2=cur.fetchone()
    if rs2:

        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,No,Hora,Op))
        con.commit()
    self.txtNombre.Clear()
    self.txtClave.Clear()
    self.txtClave2.Clear()
    self.cobTipo.Clear()
    cur.close()
    con.close()
    return

#No eliminar Usuario a peticion del profesor.
def EliminarUsuario(frm):
    self=frm
    dato=frm.txtNombre.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Eliminar Usuario"
    con,cur=conexion()

    cur.execute("Delete from Usuarios where Nombre=:dato",{"dato":dato})
    wx.MessageBox('Eliminado Satisfactoriamente', 'Caja de mensaje')
    con.commit()
    self.txtNombre.Clear()
    self.txtClave.Clear()
    self.cobTipo.Clear()
    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato,Hora,Op))
        con.commit()  
    cur.close()
    con.close()
    return
        
#<-----Postulante------->

def GuardarPostulante(frm):
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap= frm.txtApellidos.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.CobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Est= Es.upper()
    Mu=frm.cobMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.cobParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    Edad=frm.txtEdad.GetValue()
    Corr=frm.txtCorreo.GetValue()
    Tele=frm.txtTelefono.GetValue()
    dia=frm.cobDia.GetValue()
    mes=frm.cobMes.GetValue()
    anno=frm.cobAno.GetValue()
    Fna=dia + "/"+mes+ "/"+ anno
    
    Ed=frm.cobEducacion.GetValue()
    Ti=frm.txtTitulo.GetValue()
    Id=frm.cobIdioma.GetValue()
    AG=frm.txtAnoG.GetValue()
    Me=frm.txtMerito.GetValue()
    Off=frm.cobOffice.GetValue()
    Con=frm.cobContabilidad.GetValue()
    Curso=frm.txtCurso.GetValue()
    Mili=""
    PAu=""
    

    Educacion=(Ed,Ti,Id,AG,Me,Off,Con,Curso,Mili,PAu,Ce)

    Sa=frm.cobSalario.GetValue()
    Emp=frm.txtEmpresaT.GetValue()
    AT=frm.cobAtrabajo.GetValue()
    Car=frm.cobCargo.GetValue()
    Experiencia=(Sa,Emp,AT,Car,Ce)

    

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Guardar Postulante"
    
    
    con, cur = conexion()
    dato=frm.txtCedula.GetValue()
    #datos=(Car,Sec)
    cur.execute("Select Variable from registro order by hora desc")
    rs3=cur.fetchone()
    if rs3:
        
        Ca=(str(rs3[0]))
        Seleccion="NO"

    cur.execute("select Cedula from Postulante where Cedula=:dato",{"dato": dato})
    rs=cur.fetchone()
    if rs:
       wx.MessageBox('Cedula Repetida', 'Caja de mensaje') 
    else:
        
                
        cur.execute('INSERT INTO Postulante (Nombre,Apellido,Cedula,Sexo,Direccion,Fecha,Edad,Telefono,Correo,FNacimiento) VALUES (?,?,?,?,?,?,?,?,?,?)',(Nom,Ape,Ce,Se,Dir,Hora,Edad,Tele,Corr,Fna))
        cur.execute('INSERT INTO Educacion (NEducacion,Titulo,Idioma,AGraduacion,Merito,Office,Contabilidad,Curso,Militar,PAuxilio,Cedula) VALUES (?,?,?,?,?,?,?,?,?,?,?)',Educacion)
        cur.execute('INSERT INTO Experiencia (Vigente,EmpresaV,ATrabajo,Cargo,Cedula) VALUES (?,?,?,?,?)',Experiencia)
        cur.execute('INSERT INTO Estado (Nombre,Id) VALUES (?,?)',(Est,Ce))
        cur.execute('INSERT INTO Munic (Nombre,Id) VALUES (?,?)',(Mun,Ce))
        cur.execute('INSERT INTO Parroquia (Nombre,Id) VALUES (?,?)',(Par,Ce))
        cur.execute('INSERT INTO Examen (Cargo,Cedula,Seleccion) VALUES (?,?,?)',(Ca,Ce,Seleccion))
        wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')       
        con.commit()        


        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
            con.commit()

        
            

        if Ca=="ADMINISTRACION":
                Ventana=EA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE":
                Ventana=EAA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CAJERO":
                Ventana=ECA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CHOFER":
                Ventana=EC.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="VIGILANTE":
                Ventana=EV.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="GERENTE VENTAS":
                Ventana=ECV.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE VENTAS":
                Ventana=ECV1.Principal(self)
                Ventana.Show()
                self.Hide()               
        if Ca=="SERVICIO AL CLIENTE":
                Ventana=ESC.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="RECURSOS HUMANOS":
                Ventana=ERH.Principal(self)
                Ventana.Show()
                self.Hide()
        

    self.txtNombre.Clear()
    self.txtApellidos.Clear()
    self.txtCedula.Clear()
        
    
    self.cobMunicipio.Clear()
    self.cobParroquia.Clear()
    self.txtDireccion.Clear()

    self.txtTitulo.Clear()
   
    self.txtNombre.SetFocus()        
    cur.close()
    con.close()
    return

def GuardarPostulante2(frm):
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap= frm.txtApellidos.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.CobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Est= Es.upper()
    Mu=frm.cobMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.cobParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    Edad=frm.txtEdad.GetValue()
    Corr=frm.txtCorreo.GetValue()
    Tele=frm.txtTelefono.GetValue()
    dia=frm.cobDia.GetValue()
    mes=frm.cobMes.GetValue()
    anno=frm.cobAno.GetValue()
    Fna=dia + "/"+mes+ "/"+ anno
    
    Ed=frm.cobEducacion.GetValue()
    Ti=frm.txtTitulo.GetValue()
    Id=frm.cobIdioma.GetValue()
    AG=frm.txtAnoG.GetValue()
    Me=frm.txtMerito.GetValue()
    Off=""
    Con=""
    Curso=frm.txtCurso.GetValue()
    Mili=frm.cobMilitar.GetValue()
    PAu=""
    

    Educacion=(Ed,Ti,Id,AG,Me,Off,Con,Curso,Mili,PAu,Ce)

    Sa=frm.cobSalario.GetValue()
    Emp=frm.txtEmpresaT.GetValue()
    AT=frm.cobAtrabajo.GetValue()
    Car=frm.cobCargo.GetValue()
    Experiencia=(Sa,Emp,AT,Car,Ce)

    

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Guardar Postulante"
    
    
    con, cur = conexion()
    dato=frm.txtCedula.GetValue()
    #datos=(Car,Sec)
    cur.execute("Select Variable from registro order by hora desc")
    rs3=cur.fetchone()
    if rs3:
        
        Ca=(str(rs3[0]))
        Seleccion="NO"

    cur.execute("select Cedula from Postulante where Cedula=:dato",{"dato": dato})
    rs=cur.fetchone()
    if rs:
       wx.MessageBox('Cedula Repetida', 'Caja de mensaje') 
    else:
        
                
        cur.execute('INSERT INTO Postulante (Nombre,Apellido,Cedula,Sexo,Direccion,Fecha,Edad,Telefono,Correo,FNacimiento) VALUES (?,?,?,?,?,?,?,?,?,?)',(Nom,Ape,Ce,Se,Dir,Hora,Edad,Tele,Corr,Fna))
        cur.execute('INSERT INTO Educacion (NEducacion,Titulo,Idioma,AGraduacion,Merito,Office,Contabilidad,Curso,Militar,PAuxilio,Cedula) VALUES (?,?,?,?,?,?,?,?,?,?,?)',Educacion)
        cur.execute('INSERT INTO Experiencia (Vigente,EmpresaV,ATrabajo,Cargo,Cedula) VALUES (?,?,?,?,?)',Experiencia)
        cur.execute('INSERT INTO Estado (Nombre,Id) VALUES (?,?)',(Est,Ce))
        cur.execute('INSERT INTO Munic (Nombre,Id) VALUES (?,?)',(Mun,Ce))
        cur.execute('INSERT INTO Parroquia (Nombre,Id) VALUES (?,?)',(Par,Ce))
        cur.execute('INSERT INTO Examen (Cargo,Cedula,Seleccion) VALUES (?,?,?)',(Ca,Ce,Seleccion))
        wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')       
        con.commit()        


        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
            con.commit()

        
            

        if Ca=="ADMINISTRACION":
                Ventana=EA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE":
                Ventana=EAA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CAJERO":
                Ventana=ECA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CHOFER":
                Ventana=EC.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="VIGILANTE":
                Ventana=EV.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="GERENTE VENTAS":
                Ventana=ECV.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE VENTAS":
                Ventana=ECV1.Principal(self)
                Ventana.Show()
                self.Hide()               
        if Ca=="SERVICIO AL CLIENTE":
                Ventana=ESC.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="RECURSOS HUMANOS":
                Ventana=ERH.Principal(self)
                Ventana.Show()
                self.Hide()
        

    self.txtNombre.Clear()
    self.txtApellidos.Clear()
    self.txtCedula.Clear()
        
    
    self.cobMunicipio.Clear()
    self.cobParroquia.Clear()
    self.txtDireccion.Clear()

    self.txtTitulo.Clear()
   
    self.txtNombre.SetFocus()        
    cur.close()
    con.close()
    return

#Busca el postulante Modulo BuscarUsuario.
def BuscarPostulantespaso1(frm):
    self=frm
    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Postulante"
    Ce= frm.txtCedula.GetValue()
    cur.execute("Select Postulante.Cedula,Examen.Cargo from Postulante,Examen where Examen.Cedula=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs1=cur.fetchone()
    if rs1:
        Ca=(str(rs1[1]))

        if Ca=="ADMINISTRACION":
                Ventana=BP1.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE":
                Ventana=EAA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CAJERO":
                Ventana=ECA.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="CHOFER":
                Ventana=BP2.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="VIGILANTE":
                Ventana=BP2.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="GERENTE VENTAS":
                Ventana=ECV.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="ASISTENTE VENTAS":
                Ventana=ECV1.Principal(self)
                Ventana.Show()
                self.Hide()               
        if Ca=="SERVICIO AL CLIENTE":
                Ventana=ESC.Principal(self)
                Ventana.Show()
                self.Hide()
        if Ca=="RECURSOS HUMANOS":
                Ventana=ERH.Principal(self)
                Ventana.Show()
                self.Hide()

    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    cur.execute("Select usuario from bitacora order by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
        con.commit()

#se carga en el archivo BuscarPostulante.py
def BuscarPostulantes(frm):
    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Postulante"
    Ce= frm.txtCedula.GetValue()
    cur.execute("Select Postulante.Nombre,Postulante.Apellido,Postulante.Cedula,Postulante.Sexo,Postulante.Direccion,Postulante.Edad,Postulante.Correo,Postulante.Telefono,Postulante.FNacimiento,Estado.Nombre,Munic.Nombre,Parroquia.Nombre, Educacion.NEducacion,Educacion.Titulo,Educacion.Idioma,Educacion.Office,Educacion.Curso,Educacion.AGraduacion, Educacion.Merito,Educacion.Contabilidad,Experiencia.Vigente,Experiencia.EmpresaV,Experiencia.ATrabajo,Experiencia.Cargo,Educacion.Militar,Examen.Cargo from Postulante,Estado, Munic, Parroquia, Educacion,Experiencia,Examen where Examen.Cedula=Experiencia.Cedula and  Experiencia.Cedula=Educacion.Cedula and Educacion.Cedula=Estado.Id and Estado.Id=Munic.Id and Munic.Id=Parroquia.Id and Parroquia.Id=Postulante.Cedula and Postulante.Cedula=:Ce",{"Ce": Ce})
    rs = cur.fetchone()
    self=frm
    if rs:  
        FNacimiento=str(rs[8])
        
        
        self.txtNombre.SetValue(str(rs[0]))
        self.txtApellidos.SetValue(str(rs[1]))
        self.txtCedula.SetValue(str(rs[2]))
        self.CobSexo.SetValue(str(rs[3]))
        self.txtDireccion.SetValue(str(rs[4]))
        self.txtEdad.SetValue(str(rs[5]))
        self.txtCorreo.SetValue(str(rs[6]))
        self.txtTelefono.SetValue(str(rs[7]))
        self.cobDia.SetValue(FNacimiento[0]+FNacimiento[1])
        self.cobMes.SetValue(FNacimiento[3]+FNacimiento[4])
        self.cobAno.SetValue(FNacimiento[6]+FNacimiento[7]+FNacimiento[8]+FNacimiento[9])
        self.cobEstado.SetValue(str(rs[9]))
        self.cobMunicipio.SetValue(str(rs[10]))
        self.cobParroquia.SetValue(str(rs[11])) 
        self.cobEducacion.SetValue(str(rs[12])) 
        self.txtTitulo.SetValue(str(rs[13]))
        self.cobIdioma.SetValue(str(rs[14]))
        self.cobOffice.SetValue(str(rs[15]))
        self.txtCurso.SetValue(str(rs[16]))
        self.txtAnoG.SetValue(str(rs[17]))
        self.txtMerito.SetValue(str(rs[18]))
        self.cobContabilidad.SetValue(str(rs[19]))
        self.cobSalario.SetValue(str(rs[20]))
        self.txtEmpresaT.SetValue(str(rs[21]))
        self.cobAtrabajo.SetValue(str(rs[22]))
        self.cobCargo.SetValue(str(rs[23]))
        self.cobMilitar.SetValue(str(rs[24]))
        self.cobCargoP.SetValue(str(rs[25]))
        if str(rs[20])=="NO":
            self.label_22.Enable(True)
            
            self.cobCargo.Enable(True)
            self.label_3.Enable(True)
            
            self.txtEmpresaT.Enable(True)
            self.label_4.Enable(True)
            
            self.cobAtrabajo.Enable(True)

        self.txtNombre.Enable(True)        
        self.txtApellidos.Enable(True)             
        self.CobSexo.Enable(True)        
        self.txtDireccion.Enable(True)        
        #self.txtEdad.Enable(True)        
        self.txtCorreo.Enable(True)        
        self.txtTelefono. Enable(True)       
        self.cobDia.Enable(True)
        self.cobMes.Enable(True)
        self.cobAno.Enable(True)
        self.cobEstado.Enable(True)        
        self.cobMunicipio.Enable(True)
        self.cobParroquia.Enable(True) 
        self.cobEducacion. Enable(True)
        self.txtTitulo.Enable(True)
        self.cobIdioma.Enable(True)
        self.txtCurso.Enable(True)
        self.txtAnoG.Enable(True)
        self.txtMerito.Enable(True)
        self.cobSalario.Enable(True)
        self.cobCargoP.Enable(True)

        cur.execute("Select Cargo from Examen where Cedula=:Ce",{"Ce": Ce})
        rs1 = cur.fetchone()
        
        if rs1:
            Cargo=str(rs1[0])  
            if Cargo=="CHOFER" or Cargo=="VIGILANTE": 
                self.cobMilitar.Enable(True)
                                   
            else:
                self.cobOffice.Enable(True)
                self.cobContabilidad.Enable(True)
    else:
            
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        self.txtCedula.Clear()

def BuscarPostulantesSeleccion(frm):
    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    self=frm
    Op="Buscar Postulante Seleccion"
    Cargo= frm.cobCargo.GetValue()
    cur.execute('Select count(*) from Examen where Cargo=:Cargo and Seleccion="NO"',{"Cargo": Cargo})
    rs1=cur.fetchall()
    
    i=0
    l=0
    j=0
    listaNombre=[]
    listaApellido=[]
    listaCedula=[]
    listaMerito=[]
    listaCurso=[]
    for ol in rs1 :

        hola=ol[l]

        while i < hola:
            cur.execute('Select Postulante.Nombre from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo=:Cargo and seleccion="NO" order by PUNTUACION DESC , MERITO ASC',{"Cargo": Cargo})
            rs=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Apellido from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo=:Cargo and seleccion="NO" order by PUNTUACION DESC , MERITO ASC',{"Cargo": Cargo})
            rs1=[r[0] for r in cur.fetchall()]
            cur.execute('Select Postulante.Cedula from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo=:Cargo and seleccion="NO" order by PUNTUACION DESC , MERITO ASC',{"Cargo": Cargo})
            rs2=[r[0] for r in cur.fetchall()]
            cur.execute('Select Educacion.Merito from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo=:Cargo and seleccion="NO" order by PUNTUACION DESC , MERITO ASC',{"Cargo": Cargo})
            rs3=[r[0] for r in cur.fetchall()]
            cur.execute('Select Educacion.Curso from Postulante,Examen,Educacion where Postulante.Cedula=Examen.Cedula and Educacion.Cedula=Examen.Cedula and Examen.Cargo=:Cargo and seleccion="NO" order by PUNTUACION DESC , MERITO ASC',{"Cargo": Cargo})
            rs4=[r[0] for r in cur.fetchall()]
                      
            listaNombre.append(str(rs[i]))
            listaApellido.append(str(rs1[i]))             
            listaCedula.append(str(rs2[i]))
            listaMerito.append(str(rs3[i]))             
            listaCurso.append(str(rs4[i]))    

            i=i+1

    if len(listaNombre)<1:
        dlg=wx.MessageDialog(self,'No hay registros', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    else:
        self.txtNombre1.SetValue(listaNombre[0])
        self.txtApellido1.SetValue(listaApellido[0])
        self.txtCedula.SetValue(listaCedula[0])
        self.txtMerito.SetValue(listaMerito[0])
        self.txtCurso.SetValue(listaCurso[0])
        if len(listaNombre)<2:
            dlg=wx.MessageDialog(self,'Solo hay un postulante', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:

            self.txtNombre2.SetValue(listaNombre[1])
            self.txtApellido2.SetValue(listaApellido[1])
            self.txtCedula2.SetValue(listaCedula[1])
            self.txtMerito1.SetValue(listaMerito[1])
            self.txtCurso1.SetValue(listaCurso[1])
            if len(listaNombre)<3:
                dlg=wx.MessageDialog(self,'Solo hay 2 postulantes', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
            else:

                self.txtNombre3.SetValue(listaNombre[2])
                self.txtApellido3.SetValue(listaApellido[2])
                self.txtCedula3.SetValue(listaCedula[2])
                self.txtMerito3.SetValue(listaMerito[2])
                self.txtCurso3.SetValue(listaCurso[2])
                if len(listaNombre)<4:
                    dlg=wx.MessageDialog(self,'Solo hay 3 postulantes', 'Atencion', wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()
                else:

                    self.txtNombre4.SetValue(listaNombre[3])
                    self.txtApellido4.SetValue(listaApellido[3])
                    self.txtCedula4.SetValue(listaCedula[3])
                    self.txtMerito4.SetValue(listaMerito[3])
                    self.txtCurso4.SetValue(listaCurso[3])
                    if len(listaNombre)<5:
                        dlg=wx.MessageDialog(self,'Solo hay 4 postulantes', 'Atencion', wx.OK)
                        dlg.ShowModal()
                        dlg.Destroy()
                    else:

                        self.txtNombre5.SetValue(listaNombre[4])
                        self.txtApellido5.SetValue(listaApellido[4])
                        self.txtCedula5.SetValue(listaCedula[4])
                        self.txtMerito5.SetValue(listaMerito[4])
                        self.txtCurso5.SetValue(listaCurso[4])
    
        

       
   

    
def ModificarPostulante(frm):
    
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap= frm.txtApellidos.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.CobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Est= Es.upper()
    Mu=frm.cobMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.cobParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    Edad=frm.txtEdad.GetValue()
    Corr=frm.txtCorreo.GetValue()
    Tele=frm.txtTelefono.GetValue()
    dia=frm.cobDia.GetValue()
    mes=frm.cobMes.GetValue()
    anno=frm.cobAno.GetValue()
    Fna=dia + "/"+mes+ "/"+ anno
    
    Ed=frm.cobEducacion.GetValue()
    Ti=frm.txtTitulo.GetValue()
    Id=frm.cobIdioma.GetValue()
    AG=frm.txtAnoG.GetValue()
    Me=frm.txtMerito.GetValue()
    Off=frm.cobOffice.GetValue()
    Con=frm.cobContabilidad.GetValue()
    Curso=frm.txtCurso.GetValue()
    Mili=frm.cobMilitar.GetValue()
    PAu=""
    Educacion=(Ed,Ti,Id,AG,Me,Off,Con,Curso,Mili,PAu,Ce)

    Sa=frm.cobSalario.GetValue()
    Emp=frm.txtEmpresaT.GetValue()
    AT=frm.cobAtrabajo.GetValue()
    Car=frm.cobCargo.GetValue()
    
    Experiencia=(Sa,Emp,AT,Car,Ce)

    Ca=frm.cobCargoP.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    
    
    
    con, cur = conexion()
      
    Op="Modificar Postulante"
   
     

    cur.execute('UPDATE Postulante Set Nombre=?, Apellido=?, Sexo=?, Direccion=?, Edad=?,Telefono=?,Correo=?,FNacimiento=? WHERE Cedula=?',(Nom,Ape,Se,Dir,Edad,Tele,Corr,Fna,Ce))
    cur.execute('UPDATE Educacion set NEducacion=?, Titulo=?, Idioma=?, AGraduacion=?, Merito=?, Office=?, Contabilidad=?, Curso=?, Militar=?, PAuxilio=? where cedula=?',Educacion)
    cur.execute('UPDATE Experiencia set Vigente=?,EmpresaV=?,ATrabajo=?,Cargo=? where Cedula=?',Experiencia)
    cur.execute('UPDATE Estado Set Nombre=? WHERE Id=?',(Est,Ce))
    cur.execute('UPDATE Munic Set Nombre=? WHERE Id=?',(Mun,Ce))
    cur.execute('UPDATE Parroquia Set Nombre=? WHERE Id=?',(Par,Ce))
    cur.execute('UPDATE Examen Set Cargo=? WHERE Cedula=?',(Ca,Ce))
    

    wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
    con.commit()

    cur.execute("Select Usuario from Bitacora order by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
        con.commit()

    if Ca=="ADMINISTRACION": 
        Ventana=EAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="ASISTENTE": 
        Ventana=EAAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="CAJERO": 
        Ventana=ECAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="CHOFER": 
        Ventana=ECM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="VIGILANTE": 
        Ventana=EVM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="GERENTE VENTAS": 
        Ventana=ECVM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="ASISTENTE VENTAS": 
        Ventana=ECV1M.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="SERVICIO AL CLIENTE": 
        Ventana=ESCM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="RECURSOS HUMANOS": 
        Ventana=ERHM.Principal(self)
        Ventana.Show()
        self.Hide()
    cur.close()
    con.close()
    return


def ModificarPostulante1(frm): #Peticiion del profesor
    
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap= frm.txtApellidos.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.CobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Est= Es.upper()
    Mu=frm.cobMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.cobParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    Edad=frm.txtEdad.GetValue()
    Corr=frm.txtCorreo.GetValue()
    Tele=frm.txtTelefono.GetValue()
    dia=frm.cobDia.GetValue()
    mes=frm.cobMes.GetValue()
    anno=frm.cobAno.GetValue()
    Fna=dia + "/"+mes+ "/"+ anno
    
    Ed=frm.cobEducacion.GetValue()
    Ti=frm.txtTitulo.GetValue()
    Id=frm.cobIdioma.GetValue()
    AG=frm.txtAnoG.GetValue()
    Me=frm.txtMerito.GetValue()
    Off=frm.cobOffice.GetValue()
    Con=frm.cobContabilidad.GetValue()
    Curso=frm.txtCurso.GetValue()
    Mili=""
    PAu=""
    Educacion=(Ed,Ti,Id,AG,Me,Off,Con,Curso,Mili,PAu,Ce)

    Sa=frm.cobSalario.GetValue()
    Emp=frm.txtEmpresaT.GetValue()
    AT=frm.cobAtrabajo.GetValue()
    Car=frm.cobCargo.GetValue()
    
    Experiencia=(Sa,Emp,AT,Car,Ce)

    

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    
    
    
    con, cur = conexion()
      
    Op="Modificar Postulante"
    cur.execute("Select Variable from registro order by hora desc")
    rs3=cur.fetchone()
    if rs3:
        
        Ca=(str(rs3[0]))
     

    cur.execute('UPDATE Postulante Set Nombre=?, Apellido=?, Sexo=?, Direccion=?, Edad=?,Telefono=?,Correo=?,FNacimiento=? WHERE Cedula=?',(Nom,Ape,Se,Dir,Edad,Tele,Corr,Fna,Ce))
    cur.execute('UPDATE Educacion set NEducacion=?, Titulo=?, Idioma=?, AGraduacion=?, Merito=?, Office=?, Contabilidad=?, Curso=?, Militar=?, PAuxilio=? where cedula=?',Educacion)
    cur.execute('UPDATE Experiencia set Vigente=?,EmpresaV=?,ATrabajo=?,Cargo=? where Cedula=?',Experiencia)
    cur.execute('UPDATE Estado Set Nombre=? WHERE Id=?',(Est,Ce))
    cur.execute('UPDATE Munic Set Nombre=? WHERE Id=?',(Mun,Ce))
    cur.execute('UPDATE Parroquia Set Nombre=? WHERE Id=?',(Par,Ce))
    cur.execute('UPDATE Examen Set Cargo=? WHERE Cedula=?',(Ca,Ce))
    

    wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
    con.commit()

    cur.execute("Select Usuario from Bitacora order by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
        con.commit()

    if Ca=="ADMINISTRACION": 
        Ventana=EAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="ASISTENTE": 
        Ventana=EAAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="CAJERO": 
        Ventana=ECAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="CHOFER": 
        Ventana=ECM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="VIGILANTE": 
        Ventana=EVM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="GERENTE VENTAS": 
        Ventana=ECVM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="ASISTENTE VENTAS": 
        Ventana=ECV1M.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="SERVICIO AL CLIENTE": 
        Ventana=ESCM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="RECURSOS HUMANOS": 
        Ventana=ERHM.Principal(self)
        Ventana.Show()
        self.Hide()
    cur.close()
    con.close()
    return

def ModificarPostulante2(frm): #Peticiion del profesor
    
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap= frm.txtApellidos.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.CobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Est= Es.upper()
    Mu=frm.cobMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.cobParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    Edad=frm.txtEdad.GetValue()
    Corr=frm.txtCorreo.GetValue()
    Tele=frm.txtTelefono.GetValue()
    dia=frm.cobDia.GetValue()
    mes=frm.cobMes.GetValue()
    anno=frm.cobAno.GetValue()
    Fna=dia + "/"+mes+ "/"+ anno
    
    Ed=frm.cobEducacion.GetValue()
    Ti=frm.txtTitulo.GetValue()
    Id=frm.cobIdioma.GetValue()
    AG=frm.txtAnoG.GetValue()
    Me=frm.txtMerito.GetValue()
    Off=""
    Con=""
    Curso=frm.txtCurso.GetValue()
    Mili=frm.cobMilitar.GetValue()
    PAu=""
    Educacion=(Ed,Ti,Id,AG,Me,Off,Con,Curso,Mili,PAu,Ce)

    Sa=frm.cobSalario.GetValue()
    Emp=frm.txtEmpresaT.GetValue()
    AT=frm.cobAtrabajo.GetValue()
    Car=frm.cobCargo.GetValue()
    
    Experiencia=(Sa,Emp,AT,Car,Ce)

    

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    
    
    
    con, cur = conexion()
      
    Op="Modificar Postulante"
    cur.execute("Select Variable from registro order by hora desc")
    rs3=cur.fetchone()
    if rs3:
        
        Ca=(str(rs3[0]))
     

    cur.execute('UPDATE Postulante Set Nombre=?, Apellido=?, Sexo=?, Direccion=?, Edad=?,Telefono=?,Correo=?,FNacimiento=? WHERE Cedula=?',(Nom,Ape,Se,Dir,Edad,Tele,Corr,Fna,Ce))
    cur.execute('UPDATE Educacion set NEducacion=?, Titulo=?, Idioma=?, AGraduacion=?, Merito=?, Office=?, Contabilidad=?, Curso=?, Militar=?, PAuxilio=? where cedula=?',Educacion)
    cur.execute('UPDATE Experiencia set Vigente=?,EmpresaV=?,ATrabajo=?,Cargo=? where Cedula=?',Experiencia)
    cur.execute('UPDATE Estado Set Nombre=? WHERE Id=?',(Est,Ce))
    cur.execute('UPDATE Munic Set Nombre=? WHERE Id=?',(Mun,Ce))
    cur.execute('UPDATE Parroquia Set Nombre=? WHERE Id=?',(Par,Ce))
    cur.execute('UPDATE Examen Set Cargo=? WHERE Cedula=?',(Ca,Ce))
    

    wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
    con.commit()

    cur.execute("Select Usuario from Bitacora order by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
        con.commit()

    if Ca=="ADMINISTRACION": 
        Ventana=EAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="ASISTENTE": 
        Ventana=EAAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="CAJERO": 
        Ventana=ECAM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="CHOFER": 
        Ventana=ECM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="VIGILANTE": 
        Ventana=EVM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="GERENTE VENTAS": 
        Ventana=ECVM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="ASISTENTE VENTAS": 
        Ventana=ECV1M.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="SERVICIO AL CLIENTE": 
        Ventana=ESCM.Principal(self)
        Ventana.Show()            
        self.Hide()
    if Ca=="RECURSOS HUMANOS": 
        Ventana=ERHM.Principal(self)
        Ventana.Show()
        self.Hide()
    cur.close()
    con.close()
    return

# Examenes
#Cargar datos momento de modificar examen
def CargarDatos(frm):
    con, cur = conexion()   

    cur.execute("select variable,fecha,hora from registro where Operacion='Modificar Postulante' order by hora desc" )
    rs = cur.fetchone()
    
    self=frm
    if rs:
        dato=(str(rs[0]))
        
        
        cur.execute("Select * from Examen where Cedula=:dato",{"dato": dato})
        rs1 = cur.fetchone()
        if rs1:
            
            self.cobExperiencia.SetValue(str(rs1[0]))
            self.cobGTrabajo.SetValue(str(rs1[1]))
            self.cobTFuera.SetValue(str(rs1[2]))
            self.cobLicencia.SetValue(str(rs1[3]))
            self.cobTransporte.SetValue(str(rs1[4]))
            self.cobMecanica.SetValue(str(rs1[5]))
            self.cobHoras.SetValue(str(rs1[6]))
            self.cobNormas.SetValue(str(rs1[7]))
            self.cobNormasS.SetValue(str(rs1[8]))
            self.cobAccidente.SetValue(str(rs1[9]))      

        
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

#Buscar Examenes (posiblemente no usar)
def BuscarExamen(frm):

    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Examen"
    Ce= frm.txtCedula.GetValue()

    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
        con.commit()

    cur.execute("Select Cargo from Examen where Cedula=:Ce",{"Ce": Ce})
    rs = cur.fetchone()
    self=frm
    if rs:
        Campo=(str(rs[0]))

        if Campo=="ADMINISTRACION": 
            Ventana=EAM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="ASISTENTE": 
            Ventana=EAAM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="CAJERO": 
            Ventana=ECAM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="CHOFER": 
            Ventana=ECM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="VIGILANTE": 
            Ventana=EVM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="GERENTE VENTAS": 
            Ventana=ECVM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="ASISTENTE VENTAS": 
            Ventana=ECV1M.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="SERVICIO AL CLIENTE": 
            Ventana=ESCM.Principal(self)
            Ventana.Show()            
            self.Hide()
        if Campo=="RECURSOS HUMANOS": 
            Ventana=ERHM.Principal(self)
            Ventana.Show()

                
       
            
            self.Hide() 

        
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

#Chofer
def GuardarChofer(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Chofer"
    
    dato="CHOFER"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select id from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]
                    if rs1:

                        lista3.append(str(rs1[l]))
                        l=l+1
                    else:
                        l=0
            #nuevo codigo
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j) 

            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()  

                            
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()


def ModificarChofer(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Chofer"
    
    dato="CHOFER"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:

        Id=(str(rs2[0])) 
        
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by examen.puntuacion and Educacion.Merito desc",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
            while Id != lista3[j]:
                j=j+1

            Pu=str(j+1)
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIPM(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()  

                            
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()


#Administacion

def GuardarAdministrador(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Administrativo"
    
    dato="ADMINISTRACION"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select * from Examen ,educacion where  examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]
                    if rs1:

                        lista3.append(str(rs1[l]))
                        l=l+1
                    else:
                        l=0
            #nuevo codigo
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j) 
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    'Su Numero de Registro es:'+Id+ '\n'+
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIP(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()  

                            
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()

def ModificarAdministrador(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Administrativo"
    
    dato="ADMINISTRACION"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:

        Id=(str(rs2[0])) 
        
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
            while Id != lista3[j]:
                j=j+1

            Pu=str(j+1)
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIPM(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()  

                            
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()




#Asistente Administrativo

def GuardarAsistenteA(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Asistente Administrativo"
    
    dato="ASISTENTE"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select * from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]
                    if rs1:

                        lista3.append(str(rs1[l]))
                        l=l+1
                #nuevo codigo
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)             
                     
            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()  

                            
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

def ModificarAsistenteA(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Asistente Administrativo"
    
    dato="ASISTENTE"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]
                    if rs1:

                        lista3.append(str(rs1[l]))
                        l=l+1
                #nuevo codigo
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)             
                     
            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIPM(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()  

                            
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()
#Cajero

def GuardarCajero(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Cajero"
    
    dato="CAJERO"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select * from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
            #nuevo codigo
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)

            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()  

                            
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

def ModificarCajero(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Cajero"
    
    dato="CAJERO"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]
                    if rs1:

                        lista3.append(str(rs1[l]))
                        l=l+1
                #nuevo codigo
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)             
                     
            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIPM(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()  

                            
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

#Servicio al Cliente

def GuardarServicioC(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Servicio al Cliente"
    
    dato="SERVICIO AL CLIENTE"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select * from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
            #nuevo codigo
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j) 

            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()  

                            
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

def ModificarServicioC(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Servicio al Cliente"
    
    dato="SERVICIO AL CLIENTE"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:

        Id=(str(rs2[0])) 
        
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
            while Id != lista3[j]:
                j=j+1

            Pu=str(j+1)
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIPM(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()  

                            
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()

#Vigilante

def GuardarVigilante(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Vigilante"
    
    dato="VIGILANTE"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)

            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()  

                            
                 
        

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

def ModificarVigilante(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Vigilante"
    
    dato="VIGILANTE"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:

        Id=(str(rs2[0])) 
        
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
            while Id != lista3[j]:
                j=j+1

            Pu=str(j+1)
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIPM(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()  

                            
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()
#Recursos Humanos

def GuardarRecursosH(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Recursos Humanos"
    
    dato="RECURSOS HUMANOS"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)

            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()                          
                 
        

        
        cur.execute("Select usuario from Bitacora order by fecha desc")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

def ModificarRecursosH(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Recursos Humanos"
    
    dato="RECURSOS HUMANOS"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:

        Id=(str(rs2[0])) 
        
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
            while Id != lista3[j]:
                j=j+1

            Pu=str(j+1)
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIP(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()  

                            
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()
#Gerente Ventas

def GuardarGVentas(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Compra y Ventas"
    
    dato="GERENTE VENTAS"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)

            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()                          
                 
        

        
        cur.execute("Select usuario from Bitacora order by fecha desc")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

def ModificarGVentas(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Gerente Ventas"
    
    dato="GERENTE VENTAS"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:

        Id=(str(rs2[0])) 
        
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
            while Id != lista3[j]:
                j=j+1

            Pu=str(j+1)
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIP(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()                             
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()
#Asistente Ventas

def GuardarAVentas(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Asistente en ventas"
    
    dato="ASISTENTE VENTAS"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute("Select max(id) from Examen where Cargo=:dato",{"dato": dato})
    rs2=cur.fetchone()
    if rs2:
        Id=(str(rs2[0])) 
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
        

            pp=str(puntaje)
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Id=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,pp,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                for i in lista4:
                    for i in lista3:
                
                        j=j+1

                Pu=str(j)

            dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
            'Su puntuacion fue de: '+pp+'%\n'+
            'Su Numero de Registro es:'+Id+ '\n'+
            'Su Posicion es:'+Pu,
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

            if dlg.ShowModal()==wx.ID_OK:
                FR.ReportePostulanteIP(self)
                os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
                self.Hide()
            dlg.Destroy()                          
                 
        

        
        cur.execute("Select usuario from Bitacora order by fecha desc")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
            con.commit()

          
    cur.close()
    con.close()

def ModificarAVentas(frm):
    self=frm
    puntaje=0
    #Años de Experiencia=P1
    AE=frm.cobExperiencia.GetValue()
    #Se integra facilmente a grupos de trabajo=P2
    GT=frm.cobGTrabajo.GetValue()
    #Tendria incoveniente en trabajar fuera de la ciudad=P3
    TF=frm.cobTFuera.GetValue()
    #Que tipo de licencia posee=P4
    LI=frm.cobLicencia.GetValue()
    #Que tipo de Transporte ha manejado=P5
    TA=frm.cobTransporte.GetValue()
    #Posee conocimientos en mecanica basica=P6
    ME=frm.cobMecanica.GetValue()
    #Esta dispuesto a trabajas horas extras=P7
    HE=frm.cobHoras.GetValue()
    #Acepta las normas de la empresa=P8
    NE=frm.cobNormas.GetValue()
    #Acepta las normas de sus superores=P9
    NS=frm.cobNormasS.GetValue()
    #Ha tenido accidentes de transito=P10
    AC=frm.cobAccidente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Postulante Asistente Ventas"
    
    dato="ASISTENTE VENTAS"
    con, cur = conexion()
    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    
    m=0
    j=0
    l=0
    lista3=[]

    cur.execute('Select variable from registro where Operacion="Modificar Postulante" order by hora desc')
    rs2=cur.fetchone()
    if rs2:

        Id=(str(rs2[0])) 
        
        lista4=[str(rs2[0])]
        cur.execute("select * from Respuestas where Cargo=:dato",{"dato": dato})
        rs3=cur.fetchone()
        if rs3:
            lista1=[AE,GT,TF,LI,TA,ME,HE,NE,NS,AC]
            lista2=[str(rs3[1]),str(rs3[2]),str(rs3[3]),str(rs3[4]),str(rs3[5]),str(rs3[6]),str(rs3[7]),str(rs3[8]),str(rs3[9]),str(rs3[10]),]
            puntaje=0
            mal=0
            pu=str(0)

            for i in lista1:
                if i in lista2:
                    puntaje=puntaje+10
               

            ppa=int(puntaje)
            pp=str(puntaje)
            
            cur.execute('UPDATE Examen Set  P1=?,P2=?,P3=?,P4=?,P5=?,P6=?,P7=?,P8=?,P9=?,P10=?,Puntuacion=? WHERE Cedula=?',(AE,GT,TF,LI,TA,ME,HE,NE,NS,AC,ppa,Id))
            
                 
    
            if rs5:
                while l< int(rs5[0]):
                    cur.execute("Select examen.cedula from Examen ,educacion where examen.cedula=educacion.cedula and Cargo=:dato order by PUNTUACION DESC , MERITO ASC",{"dato": dato})
                    rs1=[r[0] for r in cur.fetchall()]

                    lista3.append(str(rs1[l]))
                    l=l+1
                
            while Id != lista3[j]:
                j=j+1

            Pu=str(j+1)
            

    dlg = wx.MessageDialog(None, 'Desea Imprimir la Planilla\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    
    'Su Posicion es:'+Pu,
            
                    'Dialogo de Mensage', wx.OK|wx.CANCEL|
                    wx.ICON_QUESTION)
        #dlg.ShowModal()
        

    if dlg.ShowModal()==wx.ID_OK:
        FR.ReportePostulanteIP(self)
        os.system('xdg-open "ReportePostulanteIndividualssss.pdf"') #works for urls too
        self.Hide()
    dlg.Destroy()                             
                 
        

        
    cur.execute("Select Usuario from Bitacora ORDER by hora desc")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Id,Hora,Op))
        con.commit()

          
    cur.close()
    con.close()

#Fin examenes

#Direcciones
def BuscarM(frm):
    
    dato=frm.cobEstado.GetValue()
       
    self=frm

    
    i=0
    
    Merida=["Alberto Adriani","Andres Bello","Antonio Pinto Salinas","Aricagua","Arzobispo Chacon","Campo Elias","Caracciolo Parra Olmedo","Cardenal Quintero","Guaraque","Julio Cesar","Justo Briceno","Libertador","Miranda","Obispo Ramos de Lora","Padre Noguera","Pueblo Llano","Rangel","Rivas Davila","Santos Marquina","Sucre","Tovar","Tulio Febres Cordero","Zea"]
    Sucre=["Bermudez","Sucre","Benitez","Cruz Salmeron Acosta","Bolivar","Arismendi","Ribero","Valdez","Montes","Mejia","Marino","Libertador","Andres Mata","Andres Eloy Blanco","Cajigal"]
    if dato=="Merida":
        self.cobMunicipio.Clear()
        while i <len(Merida):
            self.cobMunicipio.Append(Merida[i])
            i=i+1
    elif dato=="Sucre":
        self.cobMunicipio.Clear()
        while i <len(Sucre):
            self.cobMunicipio.Append(Sucre[i])
            i=i+1

def BuscarP(frm):
    
    dato=frm.cobMunicipio.GetValue()

    self=frm
    i=0
    #Listas de las Parroquias (problemas con el unicode)
    Bermudez=["Santa Catalina","Santa Rosa","Santa Teresa", "Bolivar", "Macarapana"]
    Sucre=["San Juan","Altagracia","Ayacucho","Gran Mariscal","Raul Leoni","Valentin Valiente"]
    Benitez=["El Pilar","El Rincon","General Francisco Antonio Vazquez","Guaraunos","Tunapuicito","Union"]
    Cruz_Salmeron_Acosta=["Cruz Salmeron Acosta", "Chacopata","Manicuare"]
    Bolivar=["Mariguitar"]
    Arismendi=["Antonio Jose de Sucre","El Morro de Puerto Santo","Puerto Santo","Rio Caribe","San Juan de las Galdonas"]
    Ribero=["Catuaro","Rendon","Santa Cruz","Santa Maria","Villa Frontado"]
    Valdez=["Bideau","Cristobal Colon","Guiria","Punta de Piedras"]
    Montes=["Arenas","Aricagua","Cocollar","Cumanacoa","San Fernando","San Lorenzo"]
    Mejia=["Mejia"]
    Marino=["Irapa","Campo Claro","Maraval","San Antonio de Irapa","Soro"]
    Libertador=["Tunapuy","Campo Elias"]
    Andres_Mata=["San Jose de Aerocuar","Tavera Acosta"]
    Andres_Eloy_Blanco=["Marino","Romulo Gallegos"]
    Cajigal=["Libertad","ElPaujil","Yaguaraparo"]
    
    if dato=="Bermudez":
        self.cobParroquia.Clear()
        while i<len(Bermudez):
            self.cobParroquia.Append(Bermudez[i])
            i=i+1
    if dato=="Sucre":
        self.cobParroquia.Clear()
        while i<len(Sucre):
            self.cobParroquia.Append(Sucre[i])
            i=i+1
    if dato=="Benitez":
        self.cobParroquia.Clear()
        while i<len(Benitez):
            self.cobParroquia.Append(Benitez[i])
            i=i+1
    if dato=="Cruz Salmeron Acosta":
        self.cobParroquia.Clear()
        while i<len(Cruz_Salmeron_Acosta):
            self.cobParroquia.Append(Cruz_Salmeron_Acosta[i])
            i=i+1
    if dato=="Bolivar":
        self.cobParroquia.Clear()
        while i<len(Bolivar):
            self.cobParroquia.Append(Bolivar[i])
            i=i+1
    if dato=="Arismendi":
        self.cobParroquia.Clear()
        while i<len(Arismendi):
            self.cobParroquia.Append(Arismendi[i])
            i=i+1
    if dato=="Ribero":
        self.cobParroquia.Clear()
        while i<len(Ribero):
            self.cobParroquia.Append(Ribero[i])
            i=i+1
    if dato=="Valdez":
        self.cobParroquia.Clear()
        while i<len(Valdez):
            self.cobParroquia.Append(Valdez[i])
            i=i+1
    if dato=="Montes":
        self.cobParroquia.Clear()
        while i<len(Montes):
            self.cobParroquia.Append(Montes[i])
            i=i+1
    if dato=="Mejia":
        self.cobParroquia.Clear()
        while i<len(Mejia):
            self.cobParroquia.Append(Mejia[i])
            i=i+1
    if dato=="Marino":
        self.cobParroquia.Clear()
        while i<len(Marino):
            self.cobParroquia.Append(Marino[i])
            i=i+1
    if dato=="Libertador":
        self.cobParroquia.Clear()
        while i<len(Libertador):
            self.cobParroquia.Append(Libertador[i])
            i=i+1
    if dato=="Andres Mata":
        self.cobParroquia.Clear()
        while i<len(Andres_Mata):
            self.cobParroquia.Append(Andres_Mata[i])
            i=i+1
    if dato=="Andres Eloy Blanco":
        self.cobParroquia.Clear()
        while i<len(Andres_Eloy_Blanco):
            self.cobParroquia.Append(Andres_Eloy_Blanco[i])
            i=i+1
    if dato=="Andres Mata":
        self.cobParroquia.Clear()
        while i<len(Andres_Mata):
            self.cobParroquia.Append(Andres_Mata[i])
            i=i+1



def ano():
    self.cobAno.Clear()
    i=0
    ano=time.strftime("%Y")
    ano1=int(ano)-101

    while ano1 < int(ano):
        ano1=ano1+1
        #print ano1

def ReporUD(self):
        #conn = sqlite3.connect('Simulacion.s3db')
        #c = conn.cursor()
        con,cur=conexion()
    #c.execute('drop table if exists failed_banks')
    #c.execute('create table failed_banks(id integer primary key autoincrement, name text, city text, state text, zip integer, close_date text, updated_date text)')
        
    
        
    # Get failed banks by year, for fun
        cur.execute("Select strftime('%m',Fecha),count(*) from Bitacora   group by 1;")
        #cur.execute("Select cargo,count(*) from examen   group by cargo;")
        years = []
        failed_banks = []
        for row in cur:
            years.append(row[0])
            failed_banks.append(row[1])

    # Plot the data, for fun


        values = tuple(failed_banks)
        ind = na.array(range(len(values))) + 0.5
        width = 0.35
        plt.bar(ind, values, width, color='r')
        plt.ylabel("Cantidad de Usuarios")
        plt.xlabel("Tiempo en Meses")
        plt.title('Reporte de Usuarios por Mes\n Leyenda:Registro de Acceso de usuarios en los diferentes meses')
        plt.xticks(ind+width/2, tuple(years))
        plt.show()

    # Clean up
        cur.close()

def ReporPostulantes(self):
        #conn = sqlite3.connect('Simulacion.s3db')
        #c = conn.cursor()
        con,cur=conexion()
    #c.execute('drop table if exists failed_banks')
    #c.execute('create table failed_banks(id integer primary key autoincrement, name text, city text, state text, zip integer, close_date text, updated_date text)')
        
    
        
    # Get failed banks by year, for fun
        #cur.execute("Select strftime('%m',Fecha),count(*) from Bitacora   group by 1;")
        cur.execute("Select cargo,count(*) from examen   group by cargo;")
        years = []
        failed_banks = []
        for row in cur:
            years.append(row[0])
            failed_banks.append(row[1])

    # Plot the data, for fun


        values = tuple(failed_banks)
        ind = na.array(range(len(values))) + 0.5
        width = 0.35
        plt.bar(ind, values, width, color='r')
        plt.ylabel("Cantidad de Postulantes")
        plt.xlabel("Cargos")
        plt.title('Reporte Postulantes por Cargo\n Leyenda:Registro de la Totalidad de Postulantes por Cargo')
        plt.xticks(ind+width/2, tuple(years))
        plt.show()

    # Clean up
        cur.close()


def ReporPostulantesFecha(self):
        #conn = sqlite3.connect('Simulacion.s3db')
        #c = conn.cursor()
        frm=self
        con,cur=conexion()
    #c.execute('drop table if exists failed_banks')
    #c.execute('create table failed_banks(id integer primary key autoincrement, name text, city text, state text, zip integer, close_date text, updated_date text)')
        
    
        
    # Get failed banks by year, for fun
        #cur.execute("Select strftime('%m',Fecha),count(*) from Bitacora   group by 1;")
        campo=frm.txtDesde.GetValue()
        campo2=frm.txtHasta.GetValue()
        fecha1=campo[6]+campo[7]+campo[8]+campo[9]+"-"+campo[3]+campo[4]+"-"+campo[0]+campo[1]
        fecha2=campo2[6]+campo2[7]+campo2[8]+campo2[9]+"-"+campo2[3]+campo2[4]+"-"+campo2[0]+campo2[1]
        cur.execute('SELECT  Cargo,COUNT(*) TotalCount FROM    postulante a INNER JOIN examen b  ON a.cedula = b.cedula WHERE   a.fecha>=? and a.fecha<=?  GROUP   BY b.cargo',(fecha1,fecha2))
        
        #cur.execute("Select cargo,count(*) from examen where fecha  group by cargo;")
        years = []
        failed_banks = []
        for row in cur:
            years.append(row[0])
            failed_banks.append(row[1])

    # Plot the data, for fun


        values = tuple(failed_banks)
        ind = na.array(range(len(values))) + 0.5
        width = 0.35
        plt.bar(ind, values, width, color='r')
        plt.ylabel("Cantidad de Postulantes")
        plt.xlabel("Cargos")
        plt.title('Reporte Postulantes por Cargo\n Leyenda:Registro de la Totalidad de Postulantes por Cargo')
        plt.xticks(ind+width/2, tuple(years))
        plt.show()

    # Clean up
        cur.close()