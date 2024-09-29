# -*- coding: utf-8 -*-
from DataBase import clear, GetClassStudentGrade, InsertStudentGrade, InsertStudentClassData, InsertClassData, InsertStudentData, getAllStudentID, getAllCourse
from Output import MakeCSV
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

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

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
		self.m_radioBox2.SetSelection( 0 )
		wSizer2.Add( self.m_radioBox2, 0, wx.ALL, 5 )

		m_radioBox1Choices = [ u"男", u"女" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"性別", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		wSizer2.Add( self.m_radioBox1, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"新增學生資料", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button1, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer2, 1, wx.EXPAND, 5 )

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


		bSizer1.Add( wSizer3, 1, wx.EXPAND|wx.LEFT, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		m_comboBox3Choices = []
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"學號", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		wSizer4.Add( self.m_comboBox3, 0, wx.ALL, 5 )

		m_comboBox4Choices = []
		self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"課程代碼", wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, 0 )
		wSizer4.Add( self.m_comboBox4, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"MidScore：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		wSizer4.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"FinalScore：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		wSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"新增選課資料", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.m_button5, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer4, 1, wx.EXPAND, 5 )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"課程名稱", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		fgSizer5.Add( self.m_comboBox2, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"查詢總成績", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_bitmap2, 0, wx.ALL, 5 )


		wSizer5.Add( fgSizer5, 5, wx.EXPAND, 5 )


		bSizer1.Add( wSizer5, 5, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.StudentDataInsert )
		self.m_button2.Bind( wx.EVT_BUTTON, self.ClassDataInsert )
		self.m_button5.Bind( wx.EVT_BUTTON, self.StudentClassInsert )
		self.m_button7.Bind( wx.EVT_BUTTON, self.ScoreSearch )


	def __del__( self ):
		pass



	# Virtual event handlers, override them in your derived class
	#新增學生資料
	def StudentDataInsert( self, event ):
		studentID = self.m_textCtrl7.Value
		Name = self.m_textCtrl27.Value
		Fname = Name.split(" ")[0]
		Lname = Name.split(" ")[1]
		grade = self.m_radioBox2.GetString(self.m_radioBox2.GetSelection())
		sex = self.m_radioBox1.GetString(self.m_radioBox1.GetSelection())
		InsertStudentData(studentID, Fname, Lname, grade, sex)
		self.m_comboBox3.Append(studentID)
		self.m_textCtrl7.Value = ""
		self.m_textCtrl27.Value= ""


	#新增課程
	def ClassDataInsert( self, event ):
		CourseID = self.m_textCtrl12.Value
		CourseName = self.m_textCtrl13.Value
		InsertClassData(CourseID, CourseName)
		self.m_comboBox2.Append(CourseName)
		self.m_comboBox4.Append(CourseID)
		self.m_textCtrl12.Value = ""
		self.m_textCtrl13.Value = ""

	def StudentClassInsert( self, event ):
		StudentID = self.m_comboBox3.GetValue()
		CourseID = self.m_comboBox4.GetValue()
		MidScore = self.m_textCtrl23.Value
		FinalScore = self.m_textCtrl24.Value
		InsertStudentClassData(StudentID, CourseID, MidScore, FinalScore)
		self.m_textCtrl23.Value = ""
		self.m_textCtrl24.Value = ""
		

	def ScoreSearch( self, event ):
		CourseName = self.m_comboBox2.GetValue()
		grades = GetClassStudentGrade(CourseName)
		print("學號\t姓名\t總成績")
		for grade in grades:
			print(grade[0], grade[1], grade[2])
		print()
		#MakeCSV(CourseName + "_總成績", grades)

	def ComboBoxInit(self):
		#讀取資料庫中已有的資料
		studentIDs = getAllStudentID()
		for sID in studentIDs:
			self.m_comboBox3.Append(sID)
		
		Courses = getAllCourse()
		for course in Courses:
			self.m_comboBox2.Append(course[1])
			self.m_comboBox4.Append(course[0])
        

