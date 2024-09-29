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



# creating a panel in frame

def onButton(event):
    print ("Button pressed.")


panel=wx.Panel(frame, wx.ID_ANY)
# creating a button in panel
button1=wx.Button(panel, wx.ID_ANY, 'my_button', (10, 10))
# bind the event handler "onButton" to handle the press action
button1.Bind(wx.EVT_BUTTON, onButton)

# +++++++++++ start of the BMPbutton  +++++++++++++++++++

# 記得反斜線要用另一反斜線來註明是反斜線
bmp=wx.Bitmap("C:\\Users\\Liu\\Desktop\\2024 Python\\7. wxPython\\pdf.png", wx.BITMAP_TYPE_ANY)
button2=wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp, size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
button2.Bind(wx.EVT_BUTTON, onButton)
button2.SetPosition((160, 20))

# +++++++++++ button  +++++++++++++++++++

# show the frame
frame.Show()
#start to listen users' actions
app.MainLoop()