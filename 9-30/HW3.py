# -*- coding: utf-8 -*-


from my_GUI import MyFrame1
import wx
import wx.xrc
from DataBase import clear, GetClassStudentGrade, InsertStudentGrade, InsertStudentClassData, InsertClassData, InsertStudentData



if __name__ == '__main__':
    #clear()
    app = wx.App()
    frm = MyFrame1(None)
    frm.Show()
    frm.ComboBoxInit()
    app.MainLoop()