#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.1 on Sun Apr  2 19:38:34 2017
#

import wx
import os
import FuncionesReportes as FR
import SeleccionPostulante as SP
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/ReporteUsuarios1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/home/victorjcb28/Psp-master/iconos/ReportePostulantes1.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnUsuarios, self.bitmap_button_1)
        self.Bind(wx.EVT_BUTTON, self.OnPostulantes, self.bitmap_button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Reportes"))
        self.bitmap_button_1.SetToolTip(wx.ToolTip(_("Reporte de Usuarios")))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_2.SetToolTip(wx.ToolTip(_("Reporte de Postulantes")))
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.bitmap_button_2, 0, wx.ALIGN_CENTER, 0)
        sizer_1.Add(grid_sizer_1, 1, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnUsuarios(self, event):  # wxGlade: Principal.<event_handler>
        FR.ReporUsuario(self)
        os.system('xdg-open "ReporteUsuarios.pdf"') #works for urls too

    def OnPostulantes(self, event):  # wxGlade: Principal.<event_handler>
        Ventana=SP.Principal(self)
        Ventana.Show()
        self.Hide()

# end of class Principal
