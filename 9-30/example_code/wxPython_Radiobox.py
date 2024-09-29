# see the tutorial at https://www.tutorialspoint.com/wxpython/wxpython_major_classes.htm
# install the library wxPython using "pip install -U wxPython"
# build the app with a frame with the stucture below

import wx
from wx.core import RadioBox    

app = wx.App()
# creating a frame
frame=wx.Frame(None, -1, 'win.py')
# set the size of the frame
frame.SetDimensions(0,0,640,480)  
# put the frame in the center of the screen
frame.Center() 


# +++++++++++ start of the Radiobox   +++++++++++++++++++


def onRadioBox(event): 
   print (Rb.GetSelection()),

# creating a panel in frame
panel=wx.Panel(frame, wx.ID_ANY)
# creating a radiobox  in panelGetSelection()
lblList = ['Value X', 'Value Y', 'Value Z']    
Rb=RadioBox(panel,label = 'RadioBox', pos = (80,10), choices = lblList ,
   majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
# bind the event handler "onRadioBox" to handle the selection
Rb.Bind(wx.EVT_RADIOBOX, onRadioBox) 

# +++++++++++ RadioBox  +++++++++++++++++++

# show the frame
frame.Show()
#start to listen users' actions
app.MainLoop()