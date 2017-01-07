#! /usr/bin/env python
# -*- coding: CP1252-*-
#self.db.execute(SQL_STRING, (dork.decode('utf-8'), ))

import sqlite3 as sq3
import wx
import Entrada as E
import PrincipalAdmin as PA

#Conexion base de datos
def conexion():
    con=sq3.connect('Sisep.s3db')
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return

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
            cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='PROFESOR'",datos)
            rs2=cur.fetchone()
            if rs2:

                Ventana=P.Principal(self)
                Ventana.Show()
                self.Hide()
            else:
                cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='ESTUDIANTE'",datos)
                rs3=cur.fetchone()
                if rs3:
                    Ventana=PE.Principal(self)
                    Ventana.Show()
                    self.Hide()
                else:
                    dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()
