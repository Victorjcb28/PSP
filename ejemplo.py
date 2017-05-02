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
    
    Op="Postulante Administracion"
    
    dato="ADMINISTRACION"
    con, cur = conexion()


    cur.execute("Select count(*) from Examen where Cargo=:dato",{"dato": dato})
    rs5=cur.fetchone()
    i=0
    j=0
    l=0
    lista3=[]
    cur.execute("Select max(id) from Examen")
    rs2=cur.fetchone()
    lista4=[str(rs2[0])]
    
    
            
    
        if rs5:
            while l< int(rs5[0]):
                cur.execute("Select * from Examen where Cargo=:dato order by puntuacion desc",{"dato": dato})
                rs1=[r[0] for r in cur.fetchall()]

                lista3.append(str(rs1[l]))
                l=l+1
        while lista4[0] != lista3[j]:
            j=j+1

        Pu=str(j+1)
    
    

        
            
    dlg=wx.MessageDialog(self,'Datos Guardados\n'+
    'Su puntuacion fue de: '+pp+'%\n'+
    'Su Posicion es:'+ID+
    'Su Posicion es:'+Pu
    , 'Atencion', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()
                    
                    
                 
        

        
        

          
    cur.close()
    con.close()