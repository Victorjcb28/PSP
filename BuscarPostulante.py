#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# generated by wxGlade 0.7.1 on Fri Mar 17 20:28:21 2017
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
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Buscar Postulante"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Datos Personales"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Educacion"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("Nombres:"))
        self.txtNombre = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_9 = wx.StaticText(self, wx.ID_ANY, _("N. Educacion"))
        self.txtNEducacion = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Apellidos:"))
        self.txtApellido = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_10 = wx.StaticText(self, wx.ID_ANY, _("Especialidad:"))
        self.txtEspecialidad = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _(u"C\u00e9dula:"))
        self.txtCedula = wx.TextCtrl(self, wx.ID_ANY, "")
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/buscar.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/cancelar.png", wx.BITMAP_TYPE_ANY))
        self.label_12 = wx.StaticText(self, wx.ID_ANY, _("Idioma:"))
        self.cobIdioma = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _("Sexo:"))
        self.cobSexo = wx.ComboBox(self, wx.ID_ANY, choices=[_("M"), _("F")], style=wx.CB_DROPDOWN)
        self.label_11 = wx.StaticText(self, wx.ID_ANY, _("Estado:"))
        self.txtEstado = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_3_copy = wx.StaticText(self, wx.ID_ANY, _("Estatus"))
        self.label_11_copy = wx.StaticText(self, wx.ID_ANY, _("Municipio:"))
        self.txtMunicipio = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_9_copy = wx.StaticText(self, wx.ID_ANY, _("P. Salarial:"))
        self.txtPSalarial = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_11_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Parroquia:"))
        self.txtParroquia = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_9_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Vigente:"))
        self.cobVigente = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_8 = wx.StaticText(self, wx.ID_ANY, _(u"Direcci\u00f3n:"))
        self.txtDireccion = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_13 = wx.StaticText(self, wx.ID_ANY, _("Cargo:"))
        self.cobCargo = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Modificar"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Eliminar"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnPrincipal, self.principal)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnApe, self.txtNombre)
        self.Bind(wx.EVT_TEXT, self.OnLetras, self.txtNombre)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnCed, self.txtApellido)
        self.Bind(wx.EVT_TEXT, self.OnLetras, self.txtApellido)
        self.Bind(wx.EVT_TEXT, self.OnCedula, self.txtCedula)
        self.Bind(wx.EVT_BUTTON, self.OnBuscar, self.bitmap_button_1)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.bitmap_button_2)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEst, self.cobSexo)
        self.Bind(wx.EVT_BUTTON, self.OnModificar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnEliminar, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Buscar Postulante"))
        self.SetSize((604, 476))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txtNombre.SetMinSize((196, 32))
        self.txtNEducacion.SetMinSize((205, 32))
        self.txtApellido.SetMinSize((196, 32))
        self.txtCedula.SetMinSize((196, 32))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        self.cobSexo.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        vntPrincipal = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(12, 6, 0, 0)
        sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.txtNombre, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.txtNEducacion, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.txtApellido, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_10, 0, 0, 0)
        grid_sizer_1.Add(self.txtEspecialidad, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_6, 0, 0, 0)
        grid_sizer_1.Add(self.txtCedula, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.bitmap_button_1, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_2, 0, 0, 0)
        grid_sizer_1.Add(self.label_12, 0, 0, 0)
        grid_sizer_1.Add(self.cobIdioma, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_7, 0, 0, 0)
        grid_sizer_1.Add(self.cobSexo, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_11, 0, 0, 0)
        grid_sizer_1.Add(self.txtEstado, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3_copy, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.label_11_copy, 0, 0, 0)
        grid_sizer_1.Add(self.txtMunicipio, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9_copy, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.txtPSalarial, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_11_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.txtParroquia, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_9_copy_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobVigente, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_8, 0, 0, 0)
        grid_sizer_1.Add(self.txtDireccion, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_13, 0, 0, 0)
        grid_sizer_1.Add(self.cobCargo, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(5)
        sizer_1.Add(grid_sizer_1, 1, 0, 0)
        vntPrincipal.Add(sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(vntPrincipal)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnPrincipal(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Salir?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            Ventana=PA.Principal(self)
            Ventana.Show()
            self.Hide()
        dlg.Destroy()   

    def OnApe(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnApe' not implemented!"
        event.Skip()

    def OnLetras(self, event):  # wxGlade: Principal.<event_handler>
        pass

    def OnCed(self, event):  # wxGlade: Principal.<event_handler>
        pass

    def OnCedula(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
        Campo=frm.txtCedula.GetValue()
        if len(Campo)> 8:
            dlg=wx.MessageDialog(self,'La Cedula no debe ser mayor a 8 caracteres', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            if Campo.isdigit():
                pass
            else:
                dlg=wx.MessageDialog(self,'No puede Tener Letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy() 

    def OnBuscar(self, event):  # wxGlade: Principal.<event_handler>
        if self.Validate():
            #Cedula = self.txtCedula.GetValue()
            f.BuscarPostulantes(self)
            

    def OnLimpiar(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnLimpiar' not implemented!"
        event.Skip()

    def OnEst(self, event):  # wxGlade: Principal.<event_handler>
        pass

    def OnModificar(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnModificar' not implemented!"
        event.Skip()

    def OnEliminar(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnEliminar' not implemented!"
        event.Skip()

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

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App()
    #wx.InitAllImageHandlers()
    frame_1 = Principal(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()