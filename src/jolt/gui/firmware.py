# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyWizard1
###########################################################################

class MyWizard1 ( wx.adv.Wizard ):

	def __init__( self, parent ):
		wx.adv.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, bitmap = wx.NullBitmap, pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_pages = []

		self.m_wizPage1 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_wizPage1 )

		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer1 = wx.GridSizer( 1, 2, 0, 0 )

		board_selectChoices = [ u"Computer Board", u"Frontend Board" ]
		self.board_select = wx.RadioBox( self.m_wizPage1, wx.ID_ANY, u"Select Board\n", wx.DefaultPosition, wx.DefaultSize, board_selectChoices, 1, wx.RA_SPECIFY_COLS )
		self.board_select.SetSelection( 0 )
		gSizer1.Add( self.board_select, 0, wx.ALL, 5 )

		mode_selectChoices = [ u"Update Existing Firmware", u"Empty Board" ]
		self.mode_select = wx.RadioBox( self.m_wizPage1, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, mode_selectChoices, 1, wx.RA_SPECIFY_COLS )
		self.mode_select.SetSelection( 0 )
		gSizer1.Add( self.mode_select, 0, wx.ALL, 5 )


		fgSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"Select File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.file_select = wx.FilePickerCtrl( self.m_wizPage1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.file_select.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer2.Add( self.file_select, 0, wx.ALL, 5 )


		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.m_wizPage1.SetSizer( fgSizer1 )
		self.m_wizPage1.Layout()
		fgSizer1.Fit( self.m_wizPage1 )
		self.m_wizPage2 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_wizPage2 )

		fgSizer5 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.text_isp = wx.StaticText( self.m_wizPage2, wx.ID_ANY, u"ISP Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_isp.Wrap( -1 )

		fgSizer5.Add( self.text_isp, 0, wx.ALL, 5 )

		self.text_uploading = wx.StaticText( self.m_wizPage2, wx.ID_ANY, u"Uploading FW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_uploading.Wrap( -1 )

		fgSizer5.Add( self.text_uploading, 0, wx.ALL, 5 )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.output_box = wx.TextCtrl( self.m_wizPage2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_box.SetMinSize( wx.Size( 400,200 ) )

		fgSizer6.Add( self.output_box, 0, wx.ALL, 5 )

		self.scrollbar = wx.ScrollBar( self.m_wizPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_VERTICAL )
		self.scrollbar.SetMinSize( wx.Size( -1,200 ) )

		fgSizer6.Add( self.scrollbar, 0, wx.ALL, 5 )


		fgSizer5.Add( fgSizer6, 1, wx.EXPAND, 5 )


		self.m_wizPage2.SetSizer( fgSizer5 )
		self.m_wizPage2.Layout()
		fgSizer5.Fit( self.m_wizPage2 )
		self.m_wizPage3 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_wizPage3 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.text_complete = wx.StaticText( self.m_wizPage3, wx.ID_ANY, u"Installation complete!\n\nNow power cycle the device and restart the Jolt software.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_complete.Wrap( -1 )

		bSizer1.Add( self.text_complete, 0, wx.ALL, 5 )


		self.m_wizPage3.SetSizer( bSizer1 )
		self.m_wizPage3.Layout()
		bSizer1.Fit( self.m_wizPage3 )
		self.Centre( wx.BOTH )

	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)

	def __del__( self ):
		pass


