# -*- coding: utf-8 -*-
from FrontEndCommand import clear, GetClassStudentGrade, InsertStudentClassData, InsertClassData, getCnameFromEnrollment, getCIDFromEnrollment,  getSIDFromEnrollment,  InsertStudentData, getAllStudentID, getAllCourse, UpdateGrade, getPicture
from ChoosePicture import ChoosePicture, ReadPictureToBinary, BinaryToPicture
###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc



Search_Result = 1000

###########################################################################
## Class MyFrame1
###########################################################################


class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1073,587 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		###Create Tab###
		p = wx.Panel(self)
		self.notebook1 = wx.Notebook(p)
		#建立分頁
		tab1 = MyPanel3(self.notebook1)
		tab2 = MyPanel4(self.notebook1)
		tab3 = MyPanel5(self.notebook1)
		tab4 = AddScore(self.notebook1)
		tab7 = MyPanel7(self.notebook1)

		#將建立的分頁加入Frame，並給予名稱
		self.notebook1.AddPage(tab1, "新增學生資料")
		self.notebook1.AddPage(tab2, "新增課程資料")
		self.notebook1.AddPage(tab3, "新增選課資料")
		self.notebook1.AddPage(tab4, "輸入成績")
		self.notebook1.AddPage(tab7, "查詢總成績")

		#建立切換分頁的監聽
		self.notebook1.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_changed)

		#設定layout
		sizer = wx.BoxSizer()
		sizer.Add(self.notebook1, 1, wx.EXPAND)
		p.SetSizer(sizer)
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def on_tab_changed(self, event):
		selected_page = self.notebook1.GetSelection()
		if selected_page == 2 or selected_page == 3:
			MyPanel = self.notebook1.GetPage(selected_page)
			studentIDs = 0
			Courses = 0
			if selected_page == 2:
				studentIDs = getAllStudentID()
				Courses = getAllCourse()
			else:
				studentIDs = getSIDFromEnrollment()
				Courses = []
	
		
			MyPanel.SIDList.Clear()
			MyPanel.SIDList.SetValue("學號")
			for sID in studentIDs:
				MyPanel.SIDList.Append(sID)

			
			MyPanel.CIDList.Clear()
			if selected_page == 2:
				MyPanel.CIDList.SetValue("課程代碼")
			else:
				MyPanel.CIDList.SetValue("課程名稱")
			for courses in Courses:
				MyPanel.CIDList.Append(courses[0])

		elif selected_page == 4:
			MyPanel = self.notebook1.GetPage(selected_page)
			Courses = getAllCourse()
			MyPanel.m_comboBox2.Clear()
			MyPanel.m_comboBox2.SetValue("課程名稱")
			for courses in Courses:
				MyPanel.m_comboBox2.Append(courses[1])
		#print(selected_page)
    	



###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 459,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"學號：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		wSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"姓名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		wSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_textCtrl27, 0, wx.ALL, 5 )

		m_radioBox2Choices = [ u"1", u"2", u"3", u"4" ]
		self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, u"年級", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox2.SetSelection( 2 )
		wSizer2.Add( self.m_radioBox2, 0, wx.ALL, 5 )

		m_radioBox1Choices = [ u"男", u"女" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"性別", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		wSizer2.Add( self.m_radioBox1, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Email：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		wSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl71 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_textCtrl71, 0, wx.ALL, 5 )

		self.Picture_Name = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.Picture_Name.Wrap( -1 )

		wSizer2.Add( self.Picture_Name, 0, wx.ALL, 5 )

		self.FilePath = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FilePath.Wrap( -1 )

		self.FilePath.Hide()

		wSizer2.Add( self.FilePath, 0, wx.ALL, 5 )

		self.Choose_Picture = wx.Button( self, wx.ID_ANY, u"選擇照片", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.Choose_Picture, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"新增學生資料", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button1, 0, wx.ALL, 5 )


		self.SetSizer( wSizer2 )
		self.Layout()

		# Connect Events
		self.Choose_Picture.Bind( wx.EVT_BUTTON, self.HandleChoosePicture )
		self.m_button1.Bind( wx.EVT_BUTTON, self.StudentDataInsert )


	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class
	def StudentDataInsert( self, event ):
		studentID = self.m_textCtrl7.Value
		Name = self.m_textCtrl27.Value
		Fname = Name.split(" ")[0]
		Lname = Name.split(" ")[1]
		grade = self.m_radioBox2.GetString(self.m_radioBox2.GetSelection())
		sex = self.m_radioBox1.GetString(self.m_radioBox1.GetSelection())
		email = self.m_textCtrl71.Value
		filePath = self.FilePath.GetLabel()
		photo = ReadPictureToBinary(filePath)	#byte形式
		InsertStudentData(studentID, Fname, Lname, grade, sex, email, photo)
		self.m_textCtrl7.Value = ""
		self.m_textCtrl27.Value= ""
		self.m_textCtrl71.Value = ""
		self.Picture_Name.SetLabel("")

	def HandleChoosePicture( self, event ):
		file_path = ChoosePicture()
		if file_path == 0:
			return 
		fileName = file_path.split("/")[-1]
		self.Picture_Name.SetLabel(fileName)
		self.FilePath.SetLabel(file_path)
		print(fileName)


###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"課程號碼：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		wSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"課名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		wSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"新增課程資料", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.m_button2, 0, wx.ALL, 5 )


		self.SetSizer( wSizer3 )
		self.Layout()

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.ClassDataInsert )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ClassDataInsert( self, event ):
		CourseID = self.m_textCtrl12.Value
		CourseName = self.m_textCtrl13.Value
		InsertClassData(CourseID, CourseName)
		self.m_textCtrl12.Value = ""
		self.m_textCtrl13.Value = ""


###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		SIDListChoices = []
		self.SIDList = wx.ComboBox( self, wx.ID_ANY, u"學號", wx.DefaultPosition, wx.DefaultSize, SIDListChoices, 0 )
		wSizer4.Add( self.SIDList, 0, wx.ALL, 5 )

		CIDListChoices = []
		self.CIDList = wx.ComboBox( self, wx.ID_ANY, u"課程代碼", wx.DefaultPosition, wx.DefaultSize, CIDListChoices, 0 )
		wSizer4.Add( self.CIDList, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"新增選課資料", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.m_button5, 0, wx.ALL, 5 )


		self.SetSizer( wSizer4 )
		self.Layout()

		# Connect Events
		self.SIDList.Bind( wx.EVT_COMBOBOX, self.SIDChoose)
		self.m_button5.Bind( wx.EVT_BUTTON, self.StudentClassInsert )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def SIDChoose( self, event ):
		StudentID = self.SIDList.GetValue()
		CIDs = getCIDFromEnrollment(StudentID)
		AllCID = getAllCourse()
		self.CIDList.Clear()
		self.CIDList.SetValue("課程代碼")
		for courses in AllCID:
			cid = courses[0]
			inStCid = 0
			for stCid in CIDs:
				if cid == stCid[0]:
					inStCid = 1
			if inStCid == 0:
				self.CIDList.Append(cid)
		
	def StudentClassInsert( self, event ):
		StudentID = self.SIDList.GetValue()
		CourseID = self.CIDList.GetValue()
		StudentID = self.SIDList.GetValue()
		CIDs = getCIDFromEnrollment(StudentID)
		AllCID = getAllCourse()
		self.CIDList.Clear()
		self.CIDList.SetValue("課程代碼")
		for courses in AllCID:
			cid = courses[0]
			inStCid = 0
			for stCid in CIDs:
				if cid == stCid[0]:
					inStCid = 1
			if inStCid == 0 and cid != CourseID:
				self.CIDList.Append(cid)
		InsertStudentClassData(StudentID, CourseID)

###########################################################################
## Class MyPanel7
###########################################################################

class MyPanel7 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 866,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		fgSizer5 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"課程名稱", wx.DefaultPosition, wx.Size( 150,-1 ), m_comboBox2Choices, 0 )
		fgSizer5.Add( self.m_comboBox2, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"查詢總成績", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button7, 0, wx.ALL, 5 )


		wSizer5.Add( fgSizer5, 8, wx.EXPAND, 50 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer2.SetMinSize( wx.Size( 1000,1000 ) )
		self.ScrolledWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.ScrolledWindow.SetScrollRate( 0, 10 )
		fgSizer3 = wx.FlexGridSizer( 0, 7, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		
		self.ScrolledWindow.SetSizer( fgSizer3 )
		self.ScrolledWindow.Layout()
		fgSizer3.Fit( self.ScrolledWindow )
		bSizer2.Add( self.ScrolledWindow, 1, wx.EXPAND |wx.ALL, 5 )


		wSizer5.Add( bSizer2, 8, wx.EXPAND, 6 )


		self.SetSizer( wSizer5 )
		self.Layout()

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.ScoreSearch )


	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ScoreSearch( self, event ):
		CourseName = self.m_comboBox2.GetValue()
		InitializeStaticText(self)
		grades = GetClassStudentGrade(CourseName)
		for grade in grades:
			pic = BinaryToPicture(getPicture(grade['photo']))
			image = wx.Image(pic, wx.BITMAP_TYPE_PNG)
			AddStaticBitmap(self, image)
			#"照片", "學號", "姓名", "期中成績", "期末成績", "總成績", "email"
			labels = [grade['SID'], grade['Name'], str(grade['MidScore']), str(grade['FinalScore']), str(grade['TotalScore']), grade['Email']]
			print("labels= ", labels)
			heights = [-1, 150, -1, -1, -1, 300]
			widths = [100, 100, 100, 100, 100, 100]
			AddStaticText(self, labels, heights, widths)

	




###########################################################################
## Class AddScore
###########################################################################

class AddScore ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 712,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		SIDListChoices = []
		self.SIDList = wx.ComboBox( self, wx.ID_ANY, u"學號", wx.DefaultPosition, wx.DefaultSize, SIDListChoices, 0 )
		wSizer5.Add( self.SIDList, 0, wx.ALL, 5 )

		CIDListChoices = []
		self.CIDList = wx.ComboBox( self, wx.ID_ANY, u"課程名稱", wx.DefaultPosition, wx.DefaultSize, CIDListChoices, 0 )
		wSizer5.Add( self.CIDList, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"MidScore：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		wSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.MidScore = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.MidScore, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"FinalScore：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		wSizer5.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.FinalScore = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.FinalScore, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"輸入成績", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.m_button6, 0, wx.ALL, 5 )


		self.SetSizer( wSizer5 )
		self.Layout()

		# Connect Events
		self.SIDList.Bind( wx.EVT_COMBOBOX, self.SIDChoose )
		self.m_button6.Bind( wx.EVT_BUTTON, self.HandleAddScore )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def SIDChoose(self, event):
		StudentID = self.SIDList.GetValue()
		Courses = getCnameFromEnrollment(StudentID)
		self.CIDList.Clear()
		self.CIDList.SetValue("課程名稱")
		for courses in Courses:
			self.CIDList.Append(courses)

	def HandleAddScore( self, event ):
		MidScore = self.MidScore.Value
		FinalScore = self.FinalScore.Value
		StudentID = self.SIDList.GetValue()
		CourseID = self.CIDList.GetValue()
		UpdateGrade(StudentID, CourseID, MidScore, FinalScore)
		self.MidScore.Value = ""
		self.FinalScore.Value = ""




def AddStaticText(self, labels, widths, heights):
	#查詢總成績時用於添加Text資料
	fgSizer = self.ScrolledWindow.GetSizer()
	for i in range(0, len(labels)):
		print("label=", labels[i])
		name = "TextInScroll" + str(i+1)
		new_static_text = wx.StaticText( self.ScrolledWindow, wx.ID_ANY, labels[i], wx.DefaultPosition, wx.Size( widths[i],heights[i] ), 0)
		new_static_text.Wrap( -1 )
		fgSizer.Add( new_static_text, 0, wx.ALL, 5 )
	fgSizer.Layout()
	self.ScrolledWindow.Layout()
	self.Layout()


def AddStaticBitmap(self, image):
	#查詢總成績時用於添加圖片
	bitmap = wx.StaticBitmap( self.ScrolledWindow, wx.ID_ANY, image, wx.DefaultPosition, wx.Size(100, 100), 0 )
	fgSizer = self.ScrolledWindow.GetSizer()
	fgSizer.Add( bitmap, 0, wx.ALL, 5 )
	fgSizer.Layout()
	self.ScrolledWindow.Layout()
	self.Layout()

def InitializeStaticText(self):
	#初始化查詢總成績
	fgSizer = wx.FlexGridSizer( 0, 7, 0, 0 )
	fgSizer.SetFlexibleDirection( wx.BOTH )
	fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
	childrens = self.ScrolledWindow.GetChildren()
	for child in childrens:
		child.Destroy()
	self.ScrolledWindow.SetSizer(None)
	self.ScrolledWindow.SetSizer(fgSizer)
	labels = ["照片", "學號", "姓名", "期中成績", "期末成績", "總成績", "email"]
	widths = [100, -1, 150, -1, -1, -1, 300]
	heights = [-1, -1, -1, -1, -1, -1, -1]
	AddStaticText(self, labels, widths, heights)



