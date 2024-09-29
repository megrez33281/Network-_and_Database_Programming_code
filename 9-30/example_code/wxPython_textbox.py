# see the tutorial at https://pythonspot.com/wxpython-window/
# install the library wxPython using "pip install -U wxPython"
# build the app with a frame with the stucture below

import wx    

app = wx.App()
# creating a frame
frame=wx.Frame(None, -1, 'win.py')
# set the size of the frame
frame.SetDimensions(0,0,640,480)  
# put the frame in the center of the screen
frame.Center() 


# +++++++++++ start of the textbox   +++++++++++++++++++


def onKeyTyped(event):
    print (event.GetString())

# creating a panel in frame
panel=wx.Panel(frame, wx.ID_ANY)
# creating a Textbox  in panel
t1=wx.TextCtrl(panel)
# bind the event handler "onKeyTpyed" to handle the typing action
t1.Bind(wx.EVT_TEXT, onKeyTyped) 

# +++++++++++ Textbox  +++++++++++++++++++

# show the frame
frame.Show()
#start to listen users' actions
app.MainLoop()