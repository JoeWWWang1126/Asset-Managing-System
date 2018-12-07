# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class Frame1
###########################################################################

class Frame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Asset Manager', pos=wx.DefaultPosition,
                          size=wx.Size(950, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # self.GetBackgroundColor()
        self.SetBackgroundColour((227,230,195))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        newitem = wx.MenuItem(fileMenu, wx.ID_NEW, text="ChangePassword", kind=wx.ITEM_NORMAL)

        fileMenu.Append(newitem)
        menubar.Append(fileMenu,'&Service')
        self.SetMenuBar(menubar)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txtEmployeeID = wx.StaticText(self, wx.ID_ANY, u"EmployeeID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtEmployeeID.Wrap(-1)
        # self.txtEmployeeID.SetBackgroundColour((230,180,80))
        gbSizer4.Add(self.txtEmployeeID, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.m_textCtrl1, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtEmployeeName = wx.StaticText(self, wx.ID_ANY, u"EmployeeName", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtEmployeeName.Wrap(-1)
        gbSizer4.Add(self.txtEmployeeName, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.m_textCtrl2, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtFixedAssertID = wx.StaticText(self, wx.ID_ANY, u"FixedAssertID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtFixedAssertID.Wrap(-1)
        gbSizer4.Add(self.txtFixedAssertID, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.m_textCtrl3, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        # self.btnApplyChange = wx.Button(self, wx.ID_ANY, u"PasswordService", wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer4.Add(self.btnApplyChange, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.txtOLDPassword = wx.TextCtrl(self, wx.ID_ANY, 'OriginalPassword', wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer4.Add(self.txtOLDPassword, wx.GBPosition(1, 4), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.txtNewPassword = wx.TextCtrl(self, wx.ID_ANY, 'NewPassword', wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer4.Add(self.txtNewPassword, wx.GBPosition(1, 5), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.btnConfirmChange = wx.Button(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer4.Add(self.btnConfirmChange, wx.GBPosition(1, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnSearch = wx.Button(self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btnSearch, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)
        self.btnSearch.SetBackgroundColour((230, 180, 80))


        self.btnClear = wx.Button(self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btnClear, wx.GBPosition(0, 7), wx.GBSpan(1, 1), wx.ALL, 5)
        self.btnClear.SetBackgroundColour((230, 180, 80))

        self.btnSafetyReport = wx.Button(self, wx.ID_ANY, u"SafetyReport", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btnSafetyReport, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        self.btnSafetyReport.SetBackgroundColour((153, 77, 82))

        self.NameOfAsset = wx.TextCtrl(self, wx.ID_ANY, 'Description', wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.NameOfAsset, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.code = wx.TextCtrl(self, wx.ID_ANY, 'Code', wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.code, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnAddNew = wx.Button(self, wx.ID_ANY, u"AddNew", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btnAddNew, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer2.Add(gbSizer4, 1, wx.EXPAND, 5)

        gbSizer5 = wx.GridBagSizer(0, 0)
        gbSizer5.SetFlexibleDirection(wx.BOTH)
        gbSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.txtEmployeeID1 = wx.StaticText(self, wx.ID_ANY, u"EmployeeID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtEmployeeID1.Wrap(-1)
        gbSizer5.Add(self.txtEmployeeID1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.showEmployeeID = wx.StaticText(self, wx.ID_ANY, u"_______________", wx.DefaultPosition, (100,50), 0)
        self.showEmployeeID.Wrap(-1)
        gbSizer5.Add(self.showEmployeeID, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtEmployeeName1 = wx.StaticText(self, wx.ID_ANY, u"EmployeName", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtEmployeeName1.Wrap(-1)
        gbSizer5.Add(self.txtEmployeeName1, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.showEmployeeName = wx.StaticText(self, wx.ID_ANY, u"__________", wx.DefaultPosition, (100,50), 0)
        self.showEmployeeName.Wrap(-1)
        gbSizer5.Add(self.showEmployeeName, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtManager = wx.StaticText(self, wx.ID_ANY, u"Manager", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtManager.Wrap(-1)
        gbSizer5.Add(self.txtManager, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.showManager = wx.StaticText(self, wx.ID_ANY, u"__________", wx.DefaultPosition, (100,50), 0)
        self.showManager.Wrap(-1)
        gbSizer5.Add(self.showManager, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.m_textCtrl9, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"FuzzySearch", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.m_button10, wx.GBPosition(0, 7), wx.GBSpan(1, 1), wx.ALL, 5)
        self.m_button10.SetBackgroundColour((230,180,80))

        self.txtEid1 = wx.StaticText(self, wx.ID_ANY, u"Employee ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtEid1.Wrap(-1)
        gbSizer5.Add(self.txtEid1, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.tcEID = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.tcEID, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtAid1 = wx.StaticText(self, wx.ID_ANY, u"Asset ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtAid1.Wrap(-1)
        gbSizer5.Add(self.txtAid1, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.tcAID = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.tcAID, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtDay= wx.StaticText(self, wx.ID_ANY, u"Period", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtDay.Wrap(-1)
        gbSizer5.Add(self.txtDay, wx.GBPosition(1, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.tcDay = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.tcDay, wx.GBPosition(1, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnGNRT = wx.Button(self, wx.ID_ANY, u"Get A PDF", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.btnGNRT, wx.GBPosition(1, 6), wx.GBSpan(1, 1), wx.ALL, 5)
        self.btnGNRT.SetBackgroundColour((230, 180, 80))

        bSizer2.Add(gbSizer5, 1, wx.EXPAND, 5)

        gbSizer6 = wx.GridBagSizer(0, 0)
        gbSizer6.SetFlexibleDirection(wx.BOTH)
        gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.listFixedAssert = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)


        # Grid
        self.listFixedAssert.CreateGrid(15, 4)
        self.listFixedAssert.EnableEditing(False)
        self.listFixedAssert.EnableGridLines(True)
        self.listFixedAssert.EnableDragGridSize(False)
        self.listFixedAssert.SetMargins(0, 0)

        # Columns
        self.listFixedAssert.EnableDragColMove(False)
        self.listFixedAssert.EnableDragColSize(True)
        self.listFixedAssert.SetColLabelSize(30)
        self.listFixedAssert.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        # self.listFixedAssert.AutoSizeColumns()
        # self.listFixedAssert.colLabels = [u'试卷名', u'制卷人', u'制卷人账号', u'考试成绩']
        self.listFixedAssert.SetColSize(0,60)
        self.listFixedAssert.SetColSize(1,200)
        self.listFixedAssert.SetColSize(2,80)
        self.listFixedAssert.SetColSize(3,80)

        # Rows
        self.listFixedAssert.EnableDragRowSize(True)
        self.listFixedAssert.SetRowLabelSize(30)
        self.listFixedAssert.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        # self.listFixedAssert.AutoSizeRows()


        # Label Appearance
        self.listFixedAssert.SetLabelTextColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.listFixedAssert.SetColLabelValue(0,'ID')
        self.listFixedAssert.SetColLabelValue(1,'Name')
        self.listFixedAssert.SetColLabelValue(2,'Status')
        self.listFixedAssert.SetColLabelValue(3,'User')

        # Cell Defaults
        self.listFixedAssert.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer6.Add(self.listFixedAssert, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        # self.listFixedAssert.SetBackgroundColour((217, 116, 43))

        self.listDailyAssert = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.listDailyAssert.CreateGrid(15, 4)
        self.listDailyAssert.EnableEditing(False)
        self.listDailyAssert.EnableGridLines(True)
        self.listDailyAssert.EnableDragGridSize(False)
        self.listDailyAssert.SetMargins(0, 0)

        # Columns
        # self.listDailyAssert.AutoSizeColumns()
        self.listDailyAssert.EnableDragColMove(False)
        self.listDailyAssert.EnableDragColSize(True)
        self.listDailyAssert.SetColLabelSize(30)
        self.listDailyAssert.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.listDailyAssert.SetColSize(0,100)
        self.listDailyAssert.SetColSize(1,160)
        self.listDailyAssert.SetColSize(2,60)
        self.listDailyAssert.SetColSize(3,60)

        # Rows
        # self.listDailyAssert.AutoSizeRows()
        self.listDailyAssert.EnableDragRowSize(True)
        self.listDailyAssert.SetRowLabelSize(80)
        self.listDailyAssert.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.listDailyAssert.SetColLabelValue(0,'ID')
        self.listDailyAssert.SetColLabelValue(1,'Name')
        self.listDailyAssert.SetColLabelValue(2,'Status')
        self.listDailyAssert.SetColLabelValue(3,'User')

        # Cell Defaults
        self.listDailyAssert.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer6.Add(self.listDailyAssert, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer2.Add(gbSizer6, 1, wx.EXPAND, 5)

        gbSizer7 = wx.GridBagSizer(0, 0)
        gbSizer7.SetFlexibleDirection(wx.BOTH)
        gbSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"Your ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        gbSizer7.Add(self.m_staticText10, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.m_textCtrl7, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Asset ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gbSizer7.Add(self.m_staticText11, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.m_textCtrl8, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"Borrow Time", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        gbSizer7.Add(self.m_staticText12, wx.GBPosition(1, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.m_textCtrl12, wx.GBPosition(1, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnBorrow = wx.Button(self, wx.ID_ANY, u"Borrow", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.btnBorrow, wx.GBPosition(1, 6), wx.GBSpan(1, 1), wx.ALL, 5)
        self.btnBorrow.Enable(True)
        self.btnBorrow.SetBackgroundColour((230, 180, 80))

        # self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"Email Address", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_staticText13.Wrap(-1)
        # gbSizer7.Add(self.m_staticText13, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer7.Add(self.m_textCtrl10, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.m_button6 = wx.Button(self, wx.ID_ANY, u"SendMail", wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer7.Add(self.m_button6, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)
        # self.m_button6.SetBackgroundColour((230, 180, 80))
        #
        # self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"Identify Code", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_staticText14.Wrap(-1)
        # gbSizer7.Add(self.m_staticText14, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer7.Add(self.m_textCtrl11, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.m_button7 = wx.Button(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer7.Add(self.m_button7, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 5)
        # self.m_button7.SetBackgroundColour((230, 180, 80))

        # self.themail = wx.TextCtrl(self, wx.ID_ANY, 'Themail', wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer7.Add(self.themail, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.thecode = wx.TextCtrl(self, wx.ID_ANY, 'thecode', wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer7.Add(self.thecode, wx.GBPosition(0, 7), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.checkBox = wx.Button(self, wx.ID_ANY, u"checkBox", wx.DefaultPosition, wx.DefaultSize, 0)
        # gbSizer7.Add(self.checkBox, wx.GBPosition(1, 7), wx.GBSpan(1, 1), wx.ALL, 5)
#-------------------------------------------------------------------------------------------------------------------------
        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"Your ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        gbSizer7.Add(self.m_staticText15, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.m_textCtrl13, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"Asset ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        gbSizer7.Add(self.m_staticText14, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.m_textCtrl14, wx.GBPosition(2, 3), wx.GBSpan(1, 1), wx.ALL, 5)



        self.btnReturn = wx.Button(self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.btnReturn, wx.GBPosition(2, 4), wx.GBSpan(1, 1), wx.ALL, 5)
        self.btnReturn.Enable(True )
        self.btnReturn.SetBackgroundColour((230, 180, 80))


        bSizer2.Add(gbSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events



    # Virtual event handlers, overide them in your derived class



