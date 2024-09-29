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


# +++++++++++ start of the button  +++++++++++++++++++

#建立button
def onButton(event):
    print ("Button pressed.")

# creating a panel in frame
panel=wx.Panel(frame, wx.ID_ANY)
# creating a button in panel
button=wx.Button(panel, wx.ID_ANY, 'my_button', (10, 10))
# bind the event handler "onButton" to handle the press action
button.Bind(wx.EVT_BUTTON, onButton)


# +++++++++++ button  +++++++++++++++++++

# show the frame
frame.Show()
#start to listen users' actions
app.MainLoop()