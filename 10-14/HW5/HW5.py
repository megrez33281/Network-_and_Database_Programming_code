# -*- coding: utf-8 -*-


from my_GUI import MyFrame1
import wx
import wx.xrc
from FrontEndCommand import clear, GetClassStudentGrade, InsertStudentClassData, InsertClassData, InsertStudentData



if __name__ == '__main__':
    #clear()
    app = wx.App()
    frm = MyFrame1(None)
    frm.Show()
    app.MainLoop()