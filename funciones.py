#! /usr/bin/env python
# -*- coding: CP1252-*-
#self.db.execute(SQL_STRING, (dork.decode('utf-8'), ))

import sqlite3 as sq3
import wx
import entrada as E
import PrincipalAdmin as PA

from time import time
import datetime

#Conexion base de datos
def conexion():
    con=sq3.connect('Sisep.s3db')
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return

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
    Cla=frm.txtClave.GetValue()
    datos=(En,Cla)

    con,cur=conexion()
    self=frm

    cur.execute("Select Estado from Usuarios where Estado= 1 and Nombre=:En",{"En":En})
    rs=cur.fetchone()

    if rs:
        dlg=wx.MessageDialog(self,'Usuario Bloqueado', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    else:
        cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='ADMINISTRADOR'",datos)
        rs1=cur.fetchone()

        if rs1:

            Ventana=PA.Principal(self)
            Ventana.Show()
            self.Hide()
        else:
            cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='SECRETARIA'",datos)
            rs2=cur.fetchone()
            if rs2:

                Ventana=P.Principal(self)
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
    
    cur.execute("Select Estado from Usuarios where Nombre=:dato",{"dato":dato})
    
    rs=cur.fetchone() 
    N=int(rs[0])
    if N ==1:
        wx.MessageBox('Error, El usuario ya estaba bloqueado', 'Caja de mensaje')
    else:
        cur.execute("Update  Usuarios set Estado= 1 where Nombre=:dato",{"dato":dato})
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
    cur.execute("Select Estado from Usuarios where Nombre=:dato",{"dato":dato})
    rs=cur.fetchone()
    N=int(rs[0])
    if N ==0:
        wx.MessageBox('Error, El usuario no esta bloqueado', 'Caja de mensaje')
    else:
        cur.execute("Update  Usuarios set Estado= 0 where Nombre=:dato",{"dato":dato})
        wx.MessageBox('Usuario Desbloqueado Satisfactoriamente', 'Caja de mensaje')
        con.commit()

        self.txtNombre.Clear()
        self.txtClave.Clear()
        self.cobTipo.Clear()


def GuardarUsuario(frm):
    No=frm.txtNombre.GetValue()
    Nom=No.upper()
    dato=Nom
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Guardar Usuario"
    Cla=frm.txtClave.GetValue()
    Ti=frm.cobTipo.GetValue()
    Es=0

    datos1=(Nom,Cla,Ti,Es)
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
            cur.execute("Select Nombre from Usuarios where Nombre=:dato",{"dato":dato})
    
            rs=cur.fetchone() 
            
            if rs:
                wx.MessageBox('Error, El usuario ya esta Registrado ', 'Caja de mensaje')
            else:       
                cur.execute('INSERT INTO Usuarios (Nombre,Clave,Tipo, Estado) VALUES (?,?,?,?)',(datos1))
                wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')
                con.commit()
            
                cur.execute("Select min(Usuario) from Bitacora")
                rs2=cur.fetchone()
                if rs2:
        
                    N=(str(rs2[0]))
                    cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
                    con.commit()
                
                    dlg = wx.MessageDialog(None, '¿Desea Agregar Otro Usuario?',
                            'Dialogo de Mensage', wx.OK|wx.CANCEL|
                             wx.ICON_QUESTION)
                
                    if dlg.ShowModal()==wx.ID_OK:
                        pass
                    else:
                    
                     Ventana=PA.Principal(self)
                     Ventana.Show()
                     self.Hide()
                    dlg.Destroy()
                
                self.txtNombre.Clear()
                self.txtClave.Clear()
                #self.cobTipo.Clear()
                self.txtNombre.SetFocus()
            
                cur.close()
                con.close()

def BuscarU(frm):
    con,cur=conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Usuario"
    dato1=frm.txtNombre.GetValue()
    dato=dato1.upper()
    cur.execute("Select * from Usuarios where Nombre=:dato",{"dato":dato})
    
    rs=cur.fetchone()
    self=frm
    if rs:
        self.txtNombre.SetValue(str(rs[0]))
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

    Cla=frm.txtClave.GetValue()
    Ti=frm.cobTipo.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Modificar Usuario"
    con,cur=conexion()

    cur.execute('UPDATE Usuarios Set  Clave=?, Tipo=? WHERE Nombre=?',(Cla,Ti,No))
    wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
    con.commit()
    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:

        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,No,Hora,Op))
        con.commit()
    self.txtNombre.Clear()
    self.txtClave.Clear()
    self.cobTipo.Clear()
    cur.close()
    con.close()
    return

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
    Ap= frm.txtApellido.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.cobSexo.GetValue()
    Es=frm.txtEstado.GetValue()
    Est= Es.upper()
    Mu=frm.txtMunicipio.GetValue()
    Mun=Mu.upper()
    Pa=frm.txtParroquia.GetValue()
    Par=Pa.upper()
    Di=frm.txtDireccion.GetValue()
    Dir=Di.upper()
    
    Ed=frm.txtNEducacion.GetValue()
    Es=frm.txtEspecialidad.GetValue()
    Id=frm.cobIdioma.GetValue()

    Sa=frm.txtPSalarial.GetValue()
    Vi=frm.cobVigente.GetValue()

    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    
    Op="Guardar Postulante"
    
    datos1=(Nom,Ape,Ce,Se)
    con, cur = conexion()
    dato=frm.txtCedula.GetValue()
    #datos=(Car,Sec)
    cur.execute("select Cedula from Postulante where Cedula=:dato",{"dato": dato})
    rs=cur.fetchone()
    if rs:
       wx.MessageBox('Cedula Repetida', 'Caja de mensaje') 
    else:
        
                
        cur.execute('INSERT INTO Postulante (Nombre,Apellido,Cedula,Sexo,Direccion,Neducacion,Especialidad,Idioma,PSalarial,Vigente) VALUES (?,?,?,?,?,?,?,?,?,?)',(Nom,Ape,Ce,Se,Dir,Ed,Es,Id,Sa,Vi))
        cur.execute('INSERT INTO Estado (Nombre,Id) VALUES (?,?)',(Est,Ce))
        cur.execute('INSERT INTO Munic (Nombre,Id) VALUES (?,?)',(Mun,Ce))
        cur.execute('INSERT INTO Parroquia (Nombre,Id) VALUES (?,?)',(Par,Ce))
        wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')       
        con.commit()

        
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
            con.commit()

    self.txtNombre.Clear()
    self.txtApellido.Clear()
    #self.txtCedula.Clear()
   
    self.txtNombre.SetFocus()        
    cur.close()
    con.close()
    return

def BuscarPostulantes(frm):
    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Estudiante"
    dato= frm.txtCedula.GetValue()
    cur.execute("Select Postulante.Nombre,Postulante.Apellido, Postulante.Sexo,Postulante.Direccion,Postulante.Neducacion, Postulante.Especialidad, Postulante.Idioma, Postulante.Psalarial, Postulante.Vigente,Munic.Nombre,Parroquia.Nombre, Estado.Nombre  from Postulante, Munic, Parroquia, Estado where Postulante.Cedula=Munic.Id and Munic.Id=Parroquia.Id and Parroquia.Id=Estado.Id and Postulante.Cedula=:dato",{"dato": dato})
    rs = cur.fetchone()
    self=frm
    if rs:
        
        self.txtNombre.SetValue(str(rs[0]))
        self.txtApellido.SetValue(str(rs[1]))
        #self.txtCedula.SetValue(int(rs[2]))
        self.cobSexo.SetValue(str(rs[2]))
        self.txtDireccion.SetValue(str(rs[3]))
        self.txtNEducacion.SetValue(str(rs[4]))
        self.txtEspecialidad.SetValue(str(rs[5]))
        self.cobIdioma.SetValue(str(rs[6]))
        self.txtPSalarial.SetValue(str(rs[7]))
        self.cobVigente.SetValue(str(rs[8]))
        self.txtMunicipio.SetValue(str(rs[9]))
        self.txtParroquia.SetValue(str(rs[10]))
        self.txtEstado.SetValue(str(rs[11]))
        self.txtNombre.SetFocus()
        
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()










