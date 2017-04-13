#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# generated by wxGlade 0.7.1 on Sat Apr  1 10:14:50 2017
#

import wx
import funciones as f
import PrincipalAdmin as PA

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.vntPpal_BarraMenu = wx.MenuBar()
        self.archivo = wx.Menu()
        self.principal = wx.MenuItem(self.archivo, wx.ID_ANY, _("Principal"), _("Principal"), wx.ITEM_NORMAL)
        self.archivo.AppendItem(self.principal)
        self.vntPpal_BarraMenu.Append(self.archivo, _("Archivo"))
        self.SetMenuBar(self.vntPpal_BarraMenu)
        # Menu Bar end
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Postulante Asistente Administrativo"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfPor que quiere trabajar\ncon nosotros?"))
        self.cobExperiencia = wx.ComboBox(self, wx.ID_ANY, choices=[_("ESTA ES UNA EMPRESA CON BUENA REPUTACION EN PLENO CRECIMIENTO Y PUEDO APORTAR EXPERCIENCIAS LABORALES NUEVAS"), _("ES UNA BUENA OPORTUNIDAD PARA PONER EN PRACTICA MIS CONOCIMIENTOS Y CRECER COMO PROFESIONAL DENTRO DE MI CAMPO"), _("ESTOY DESEMPLEADO Y NECESITO TRABAJO")], style=wx.CB_DROPDOWN)
        self.label_9 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfSabe Trabajar en Equipo?"))
        self.cobMecanica = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO"), _("MUY POCO")], style=wx.CB_DROPDOWN)
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfTiene experiencia en esta\narea de trabajo?"))
        self.cobGTrabajo = wx.ComboBox(self, wx.ID_ANY, choices=[_("NO, PERO SOY UNA PERSONA QUE APRENDE RAPIDO Y MOTIVADA"), _("NO, PERO TENGO LA FORMACION ACADEMICA NECESARIA PARA EL CARGO"), _("SI")], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfTrabaja bajo presion?"))
        self.cobHoras = wx.ComboBox(self, wx.ID_ANY, choices=[_("NO, PERO TENER UNA FECHA LIMITE ES UN MAL NECESARIO QUE TENEMOS QUE AFRONTAR LA MAYORIA"), _("NO,CREO QUE LAS FECHAS LIMITE SON UNA PREOCUPACION Y PREFIERO PODER IR A MI PROPIO RITMO"), _("SI")], style=wx.CB_DROPDOWN)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfCuanto tiempo le gustaria\ntrabajar con nosotros?"))
        self.cobTFuera = wx.ComboBox(self, wx.ID_ANY, choices=[_("CUANTO MAS TIEMPO MEJOR"), _(u"NO MENOS DE TRES A\u00d1OS"), _("EL TIEMPO QUE REQUIERAN MIS SERVICIOS")], style=wx.CB_DROPDOWN)
        self.label_9_copy_copy = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfQue hace cuando se encuentra\nen una situacion de estres?"))
        self.cobNormas = wx.ComboBox(self, wx.ID_ANY, choices=[_("ANALIZA LA SITUACION Y ABORDA LOS PROBLEMAS DE LA MANERA MAS EFICIENTE Y EFICAZ"), _("DEJA QUE LOS DEMAS HAGAN EL TRABAJO POR USTED"), _("PIERDE EL CONTROL DE LA SITUACION Y NO SABE QUE HACER")], style=wx.CB_DROPDOWN)
        self.label_11_copy_1 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfHa vivido algun conflicto\nen su ultimo trabajo?"))
        self.cobLicencia = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO"), _("POCO")], style=wx.CB_DROPDOWN)
        self.label_13_copy = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfLlega puntual al \ntrabajo?"))
        self.cobNormasS = wx.ComboBox(self, wx.ID_ANY, choices=[_("RARA VEZ"), _("A VECEZ"), _("A MENUDO")], style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfPorque dejo su \nultimo trabajo?"))
        self.cobTransporte = wx.ComboBox(self, wx.ID_ANY, choices=[_("ME SENTIA UN POCO ESTANCADO Y DECIDI QUE NECESITABA NUEVOS RETOS QUE NO TENIA EN MI PUESTO ANTERIOR"), _("ESTOY INTEREADO EN UN PUESTO CON MAYOR RESPONSABILIDAD Y CREO QUE ESTE TRABAJO ME PUEDE OFRECER ESA OPORTUNIDAD"), _("NO ESTABA DE ACUERDO CON EL CARGO")], style=wx.CB_DROPDOWN)
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _(u"\u00bfTrabajaria horas extras?"))
        self.cobAccidente = wx.ComboBox(self, wx.ID_ANY, choices=[_("SI"), _("NO"), _("SEGUN SEA LA EMERGENCIA LABORAL")], style=wx.CB_DROPDOWN)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Guardar"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Limpiar"))
        
        self.__set_properties()
        self.cobExperiencia.SetValidator(ContieneDatos())#activa la validacion
        self.cobGTrabajo.SetValidator(ContieneDatos())#activa la validacion
        self.cobTFuera.SetValidator(ContieneDatos())#activa la validacion
        self.cobLicencia.SetValidator(ContieneDatos())#activa la validacion
        self.cobTransporte.SetValidator(ContieneDatos())#activa la validacion
        self.cobMecanica.SetValidator(ContieneDatos())#activa la validacion
        self.cobHoras.SetValidator(ContieneDatos())#activa la validacion
        self.cobNormas.SetValidator(ContieneDatos())#activa la validacion
        self.cobNormasS.SetValidator(ContieneDatos())#activa la validacion
        self.cobAccidente.SetValidator(ContieneDatos())#activa la validacion
        
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnPrincipal, self.principal)
        self.Bind(wx.EVT_BUTTON, self.OnGuardar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Postulante Chofer"))
        self.SetSize((688, 558))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.cobExperiencia.SetMinSize((156, 40))
        self.cobExperiencia.SetSelection(-1)
        self.cobMecanica.SetMinSize((156, 40))
        self.cobMecanica.SetSelection(-1)
        self.cobGTrabajo.SetMinSize((156, 40))
        self.cobGTrabajo.SetSelection(-1)
        self.cobHoras.SetMinSize((156, 40))
        self.cobHoras.SetSelection(-1)
        self.cobTFuera.SetMinSize((156, 40))
        self.cobTFuera.SetSelection(-1)
        self.cobNormas.SetMinSize((156, 40))
        self.cobNormas.SetSelection(-1)
        self.cobLicencia.SetMinSize((156, 40))
        self.cobLicencia.SetSelection(-1)
        self.cobNormasS.SetMinSize((156, 40))
        self.cobNormasS.SetSelection(-1)
        self.cobTransporte.SetMinSize((156, 40))
        self.cobTransporte.SetSelection(-1)
        self.cobAccidente.SetMinSize((156, 40))
        self.cobAccidente.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        vntPrincipal = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(12, 5, 0, 0)
        sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.cobExperiencia, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobMecanica, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, 0, 0)
        grid_sizer_1.Add(self.cobGTrabajo, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.cobHoras, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.cobTFuera, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9_copy_copy, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobNormas, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_11_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.cobLicencia, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_13_copy, 0, 0, 0)
        grid_sizer_1.Add(self.cobNormasS, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.cobTransporte, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_7, 0, 0, 0)
        grid_sizer_1.Add(self.cobAccidente, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(3)
        sizer_1.Add(grid_sizer_1, 1, 0, 0)
        vntPrincipal.Add(sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(vntPrincipal)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnPrincipal(self, event):  # wxGlade: Principal.<event_handler>
        pass

    def OnGuardar(self, event):  # wxGlade: Principal.<event_handler>
        if self.Validate():
            dlg = wx.MessageDialog(None, '¿Desea Guardar?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            f.GuardarAsistenteA(self)

            self.Hide()
        dlg.Destroy()  
        
    def OnLimpiar(self, event):  # wxGlade: Principal.<event_handler>
        pass

# end of class Principal
class ContieneDatos(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        """
        Note que todo validador debe implementar
        # el método Clone().
        """
        return ContieneDatos()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox("Este campo debe contener algún texto!",
                          "Error")
            textCtrl.SetBackgroundColour("red")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(
                               wx.SystemSettings_GetColour(
                               wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True
