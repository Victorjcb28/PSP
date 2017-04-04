#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.1 on Mon Apr  3 23:43:11 2017
#

import wx
import os
import FuncionesReportes as FR
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/Administrativo1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_4 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_5 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_6 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3_copy = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3_copy_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3_copy_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3_copy_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("chofer1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3_copy_4 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/chofer1.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnAdministrativo, self.bitmap_button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Seleccion de Postulantes"))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_3.SetSize(self.bitmap_button_3.GetBestSize())
        self.bitmap_button_4.SetSize(self.bitmap_button_4.GetBestSize())
        self.bitmap_button_5.SetSize(self.bitmap_button_5.GetBestSize())
        self.bitmap_button_6.SetSize(self.bitmap_button_6.GetBestSize())
        self.bitmap_button_3_copy.SetSize(self.bitmap_button_3_copy.GetBestSize())
        self.bitmap_button_3_copy_1.SetSize(self.bitmap_button_3_copy_1.GetBestSize())
        self.bitmap_button_3_copy_2.SetSize(self.bitmap_button_3_copy_2.GetBestSize())
        self.bitmap_button_3_copy_3.SetSize(self.bitmap_button_3_copy_3.GetBestSize())
        self.bitmap_button_3_copy_4.SetSize(self.bitmap_button_3_copy_4.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(3, 9, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_1, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_4, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_5, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_6, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3_copy, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3_copy_1, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3_copy_2, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3_copy_3, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_button_3_copy_4, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnAdministrativo(self, event):  # wxGlade: Principal.<event_handler>
        FR.PostulantesAdministratativo(self)
        os.system('xdg-open "ReportePostulantesAdministrativo.pdf"') #works for urls too

# end of class Principal
