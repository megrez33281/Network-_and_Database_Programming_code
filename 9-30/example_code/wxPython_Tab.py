# see  https://pythonspot.com/wxpython-tabs/ for reference
import wx

class TabOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the first tab", (60,20))

class TabTwo(wx.Panel):
    def __init__(self, parent):                                                 #init 記得不是Init
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the second tab", (20,20))

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wxPython tabs example @pythonspot.com")
         
        # Creating the Tab holders: Panel and Notebook
        p = wx.Panel(self)
        nb = wx.Notebook(p)
        
        #Creating the Tab windows
        tab1 = TabOne(nb)
        tab2 = TabTwo(nb)


        # add Tabs to Notebook and give a name to the Tabs
        nb.AddPage(tab1, "Tab 1")
        nb.AddPage(tab2, "Tab 2")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

app = wx.App()
MainFrame().Show()
app.MainLoop()