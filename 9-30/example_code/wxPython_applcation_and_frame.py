# see the tutorial at https://pythonspot.com/wxpython-window/
# install instaltion manager pip in VS 
    # (1) download get-pip.py at https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    # (2) run get-pip.py scripy in VScode
    # (3) you migh have to add script directory " "  to path (從控制台==>系統==>進階系統設定 ==>環境變數==>Path 變數加入 C:/Users/Liu/AppData/Local/Programs/Python/Python38-32/)  
# install the library wxPython using "pip install -U wxPython" in console
# build the app with a frame with the stucture below

import wx 
# creating an app
app = wx.App()
# creating a frame with 'win.py as the caption of the frame '
frame=wx.Frame(None, -1, 'win.py')
# set the size of the  
frame.SetDimensions(0,0,640,480)  
# put the frame in the center of the screen
frame.Center() 
# show the frame
frame.Show()
#start to listen users' actions
app.MainLoop()


