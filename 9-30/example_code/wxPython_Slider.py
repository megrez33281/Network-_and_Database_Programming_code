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


# +++++++++++ start of the Slider   +++++++++++++++++++



def OnSliderScroll(event):
    obj = event.GetEventObject() 
    val = obj.GetValue() 
    print (val)

# creating a panel in frame
panel=wx.Panel(frame, wx.ID_ANY)
# creating a slider  in panel
sld = wx.Slider(panel, value = 200, minValue = 1, maxValue = 500,
   style = wx.SL_HORIZONTAL|wx.SL_LABELS)

# bind the event handler "onRadioBox" to handle the selection
sld.Bind(wx.EVT_SLIDER, OnSliderScroll) 

# +++++++++++ RadioBox  +++++++++++++++++++

# show the frame
frame.Show()
#start to listen users' actions
app.MainLoop()