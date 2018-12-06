import wx
import demoFrame1
# import testSearchDemo
import xlrd
import os
import testClass
import SearchHRDemo
from xGridTable import StudentInfoGridTable
from collections import defaultdict
import wx.grid
import pdfDemo
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
import testODB
import time
import testTime
import TestSendMail
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
import testPOPemail
import dealthis




class showFrame(demoFrame1.Frame1,testClass.ReadExcel,SearchHRDemo.readHR_IDExcel,pdfDemo.MakingPdf,testODB.makeODB,testTime.TimeDemo,TestSendMail.sendMail,testPOPemail.popMail,dealthis.getpdf):
    #建立主类，并继承其他相关的函数
    def __init__(self,parent):
        demoFrame1.Frame1.__init__(self,parent)
        #--------------------------------------------------------------
        self.btnSearch.Bind(wx.EVT_BUTTON,self.search)
        self.btnClear.Bind(wx.EVT_BUTTON,self.clear)
        self.btnBorrow.Bind(wx.EVT_BUTTON,self.borrow)
        self.btnReturn.Bind(wx.EVT_BUTTON, self.returnThis)
        self.m_button10.Bind(wx.EVT_BUTTON,self.fuzzySearch)
        self.m_textCtrl9.Bind(wx.EVT_TEXT_ENTER, self.fuzzySearch)
        self.Bind(wx.EVT_CLOSE, self.closeAll)
        self.btnGNRT.Bind(wx.EVT_BUTTON,self.Get_a_pdf)
        # self.m_button6.Bind(wx.EVT_BUTTON,self.sendEmailDemo)
        # self.m_textCtrl10.Bind(wx.EVT_TEXT_ENTER, self.sendEmailDemo)
        # self.m_button7.Bind(wx.EVT_BUTTON,self.checkCode)
        # self.m_textCtrl11.Bind(wx.EVT_TEXT_ENTER, self.checkCode)
        self.m_textCtrl1.Bind(wx.EVT_TEXT_ENTER,self.search)
        self.m_textCtrl2.Bind(wx.EVT_TEXT_ENTER, self.search)
        self.m_textCtrl3.Bind(wx.EVT_TEXT_ENTER, self.search)
        # self.checkBox.Bind(wx.EVT_BUTTON,self.checkTheMail)
        password = '123456'

        # self.checkSafty
        # print('hh')
        self.btnSafetyReport.Bind(wx.EVT_BUTTON,self.checkSafety)
        #--------------------------------------------------------------
        #绑定事件与函数
        # print(isinstance(self.ppp(), str))
        PWDDialog = wx.TextEntryDialog(self, 'Enter Your Password', 'Password')
        if PWDDialog.ShowModal() == wx.ID_OK and PWDDialog.GetValue() == password:
            pass

        else:
            PWDDialog.Destroy()
            self.btnReturn.Enable(False)
            self.btnBorrow.Enable(False)
            # wx.Exit()

        #建立登陆密码，设置开始方式

    # def checkTheMail(self,event):
    #     mailaddress=self.themail.GetLineText(0)
    #     thecodde= self.thecode.GetLineText(0)
    #     self.main_(mailaddress,thecodde)
    #     print(self.judge)
    #     if self.judge:
    #         self.btnReturn.Enable(True)
    #         self.btnBorrow.Enable(True)

    # def sendEmailDemo(self,event):
    #     #发邮件函数，触发SENDIT函数
    #
    #     # self.receieve = self.m_textCtrl10.GetLineText(0)
    #     # if 'siemens.com' in self.receieve :
    #     #     self.code = str(random.randint(1000, 9999))
    #     #     self.sendIT(self.receieve, self.code)
    #     # else:
    #     #     wx.MessageBox('Please User the Mail End with @siemens.com~')
    #
    #     self.receieve = self.m_textCtrl10.GetLineText(0)
    #
    #     self.code = str(random.randint(1000, 9999))
    #     self.sendIT(self.receieve, self.code)

    # def checkCode(self,event):
    #     #检查并核对返回的验证码
    #     checkCode = self.m_textCtrl11.GetLineText(0)
    #     if checkCode==self.code:
    #         wx.MessageBox('Email Confirmed!')
    #         self.btnBorrow.Enable(True)
    #         self.btnReturn.Enable(True)
    #         sheet4 = testODB.makeODB('sheet4')
    #         nowTime=self.ppp()
    #         sheet4.addToSheet4(self.receieve,'Match',nowTime)
    #         # self.receieve='TBC'
    #         self.code='TBC'
    #     else:
    #         wx.MessageBox('Your Code is Not Correct! Try another time~')
    #         self.btnBorrow.Enable(False)
    #         self.btnReturn.Enable(False)

    def closeAll(self,event):
        wx.Exit()
        #关闭主窗口（但可能造成进程退出不完全）


        # PWDDialog = wx.TextEntryDialog(self, 'Enter Your Password', 'Password')
        # if PWDDialog.ShowModal() == wx.ID_OK and PWDDialog.GetValue() == '123456':
        #     pass
        #
        # else:
        #     PWDDialog.Destroy()
        #     wx.Exit()
            # self.App.OnExit()
        # self.Frame

    def fuzzySearch(self, event):
        # for i in range(20):
        #     for n in range(4):
        #         self.listDaliyAssert.SetCellValue(i, n, '')
        #模糊搜索，并触发fillAssetInfo函数，填充表格

        Asset = self.m_textCtrl9.GetLineText(0)
        self.fillAssetInfo(Asset)

    def fillAssetInfo(self,AssetName):
        #填充表格，将searchAllAsset所取得的信息全部填入表格
        gridDatas = self.searchAllAsset(AssetName)
        if gridDatas!=[]:
            b = 0
            for i in range(15):
                for n in range(4):
                    self.listDailyAssert.SetCellValue(i, n, '')
            for aList in gridDatas:
                if len(aList) > 15:
                    wx.MessageBox('TOO MANY DATA! PLEASE DECREASE IT !')
                    break
                else:
                    a = 0
                    for Element in aList:
                        self.listDailyAssert.SetCellValue(a, b, Element)
                        a += 1

                b += 1
        else:
            # wx.MessageBox('This is not in the LIST! Please enter an invalid value!')
            pass

        # for i in range(20):
        #     for n in range(4):
        #         self.listDaliyAssert.SetCellValue(i, n, '')

    def returnThis(self,event):
        #此函数为归还按键所触发的函数
        HRID = self.m_textCtrl13.GetLineText(0)
        AssetID = self.m_textCtrl14.GetLineText(0)
        if (HRID in self.HRID) and (AssetID in self.FixedID) :
            HRName = self.getHRNameByHRID(HRID)
            # print(AssetID)
            AssetName = self.getInfoByFixedID(AssetID)
            # AssetStatus = self.getStatusByFixedID(AssetID)
            AssetUser=self.getUserByFixedID(AssetID)
            if AssetUser==HRID:
                Sheet3 = testODB.makeODB('sheet3')
                NowTime = self.ppp()
                self.receieve='true'
                Sheet3.addNewLine(HRID, HRName, AssetID, AssetName, 'Return', NowTime, self.receieve)
                Sheet2 = testODB.makeODB('sheet2')
                Sheet2.UpdateReturn(AssetID,NowTime)
                wx.MessageBox('Application Sent!')
                self.btnReturn.Enable(False)
            else:
                wx.MessageBox('You cannot return it ')

        else:
            wx.MessageBox("Please Enter The Right HRID AND AssetID!")

    def Get_a_pdf(self,event):

        HRID = self.tcEID.GetLineText(0)
        AssetID = self.tcAID.GetLineText(0)
        if (HRID in self.HRID) and (AssetID in self.FixedID) :
            HRName = self.getHRNameByHRID(HRID)
            # print(AssetID)
            AssetName = self.getInfoByFixedID(AssetID)
            AssetStatus = self.getStatusByFixedID(AssetID)
            if AssetStatus == 'In Stock':
                # wx.MessageBox('youc can borrow')
                # pdfName = canvas.Canvas("Application Sheet.pdf")

                TimeLimit = self.tcDay.GetLineText(0)
                wildcard = "PDF File (.pdf)|.pdf"

                dlg = wx.FileDialog(self, message='Save', defaultDir=os.getcwd(), defaultFile="", wildcard=wildcard,
                                    style=wx.FD_SAVE)
                dlg.ShowModal()
                save_padth=dlg.GetPath()

                self.gpdf(HRID, HRName, AssetID, AssetName, TimeLimit,save_padth)
                dlg.Destroy()
                # Sheet.Exit()
                # Sheet.closeThis()
                # self.pdfMaker(pdfName, HRID, HRName, AssetID, AssetName, TimeLimit)
                # pdfName.showPage()
                # pdfName.save()

                wx.MessageBox('PDF Generated!')


            else:
                wx.MessageBox('you cannot borrow it ')
        pass

    def borrow(self,event):
        #此函数为借阅按键所触发的函数
        HRID = self.m_textCtrl7.GetLineText(0)
        AssetID = self.m_textCtrl8.GetLineText(0)
        if (HRID in self.HRID) and (AssetID in self.FixedID) :
            HRName = self.getHRNameByHRID(HRID)
            # print(AssetID)
            AssetName = self.getInfoByFixedID(AssetID)
            AssetStatus = self.getStatusByFixedID(AssetID)
            if AssetStatus == 'In Stock':
                # wx.MessageBox('youc can borrow')
                # pdfName = canvas.Canvas("Application Sheet.pdf")
                self.receieve='none'
                TimeLimit = self.m_textCtrl12.GetLineText(0)
                Sheet3 = testODB.makeODB('sheet3')
                NowTime = self.ppp()
                Sheet3.addNewLine(HRID, HRName, AssetID, AssetName, TimeLimit, NowTime, self.receieve)
                Sheet2 = testODB.makeODB('sheet7')
                Sheet2.UpadateBorrow(AssetID, HRID, HRName, TimeLimit, NowTime)
                # wildcard = "PDF File (.pdf)|.pdf"
                #
                # dlg = wx.FileDialog(self, message='Save', defaultDir=os.getcwd(), defaultFile="", wildcard=wildcard,
                #                     style=wx.FD_SAVE)
                # dlg.ShowModal()
                # save_padth=dlg.GetPath()
                #
                # self.gpdf(HRID, HRName, AssetID, AssetName, TimeLimit,save_padth)
                # dlg.Destroy()
                # Sheet.Exit()
                # Sheet.closeThis()
                # self.pdfMaker(pdfName, HRID, HRName, AssetID, AssetName, TimeLimit)
                # pdfName.showPage()
                # pdfName.save()

                wx.MessageBox('Application Sent!')
                self.btnBorrow.Enable(False)

            else:
                wx.MessageBox('you cannot borrow it ')
            # pdfName = canvas.Canvas("Application Sheet.pdf")
            # TimeLimit = self.m_textCtrl12.GetLineText(0)
            # Sheet3=testODB.makeODB('sheet3')
            # NowTime =self.ppp()
            # Sheet3.addNewLine(HRID, HRName, AssetID, AssetName, TimeLimit,NowTime,self.receieve)
            # Sheet2=testODB.makeODB('sheet2')
            # Sheet2.UpadateBorrow(AssetID,HRID,HRName,TimeLimit,NowTime)
            # # Sheet.Exit()
            # # Sheet.closeThis()
            # # self.pdfMaker(pdfName, HRID, HRName, AssetID, AssetName, TimeLimit)
            # # pdfName.showPage()
            # # pdfName.save()
            # wx.MessageBox('Application Sent!')
            # self.btnBorrow.Enable(False)

        else:
            wx.MessageBox("Please Enter The Right HRID AND AssetID!")

    def fillData(self,thisHRID):
        for i in range(15):
            for n in range(4):
                self.listFixedAssert.SetCellValue(i, n, '')
        gridDatas = self.searchAsset(thisHRID)
        b=0
        for aList in gridDatas:
            a=0
            if len(aList)<=15:
                for Element in aList:
                    self.listFixedAssert.SetCellValue(a, b, Element)
                    a += 1
                b += 1
            else:
                wx.MessageBox('Too Many Data!')
                break

    def search(self,event):
        HRID = self.m_textCtrl1.GetLineText(0)
        HRName = self.m_textCtrl2.GetLineText(0)
        IDmessage = self.m_textCtrl3.GetLineText(0)
        if (HRID and HRName) and (not IDmessage):
            if (HRID in self.HRID) and (HRName in self.HRName) and (self.getHRNameByHRID(HRID)==HRName):
                self.showEmployeeID.SetLabel(HRID)
                self.showEmployeeName.SetLabel(HRName)
                self.showManager.SetLabel(self.getHRManagerByHRID(HRID))
                self.fillData(HRID)
            else:
                wx.MessageBox('HR Name and HR ID NOT match!'+'\n'+'Please Choose ONLY ONE to Enter')
        elif ((HRID)and(not HRName)) and (not IDmessage):
            if HRID in self.HRID:
                self.showEmployeeID.SetLabel(HRID)
                self.showEmployeeName.SetLabel(self.getHRNameByHRID(HRID))
                self.showManager.SetLabel(self.getHRManagerByHRID(HRID))
                self.fillData(HRID)
            else:
                wx.MessageBox('This HR ID is not in the list!' + '\n' + 'Please Enter a Right ID')
        elif ((HRName)and(not HRID)) and (not IDmessage):
            if HRName in self.HRName:
                self.showEmployeeID.SetLabel(self.getHRIDByHRName(HRName))
                self.showEmployeeName.SetLabel(HRName)
                self.showManager.SetLabel(self.getHRManagerByHRName(HRName))
                self.fillData(self.getHRIDByHRName(HRName))
            else:
                wx.MessageBox('This HR Name is not in the list!'+'\n' + 'Please Enter a Right Name')
        elif (not (HRName or HRID)) and (IDmessage):
            if IDmessage in self.FixedID:
                # wx.MessageBox(self.getInfoByFixedID(IDmessage),'hello',wx.OK)
                wx.MessageBox(
                    ('Fixed Assert:  ' + IDmessage + '\n' + 'Information:  ' + self.getInfoByFixedID(IDmessage) +
                     '\n' + 'Status:  ' + self.getStatusByFixedID(IDmessage) + '\n' + 'User:  ' + self.getUserByFixedID(
                                IDmessage)), 'Information', wx.OK)
            else:
                wx.MessageBox('This ID is not in the list! ' + '\n' + 'Please enter a right ID')
        else:
            wx.MessageBox('Please Choose Only One to Search !')

    def clear(self,event):
        self.m_textCtrl1.SetLabel('')
        self.m_textCtrl2.SetLabel('')
        self.m_textCtrl3.SetLabel('')
        self.showEmployeeID.SetLabel('__________')
        self.showEmployeeName.SetLabel('__________')
        self.showManager.SetLabel('__________')

        for i in range(15):
            for n in range(4):
                self.listFixedAssert.SetCellValue(i, n, '')

    def searchAsset(self,thisHRID):
        IDList = self.getFixedIDByUser(thisHRID)
        n=0
        InfoList=[]
        StatusList=[]
        TimeList=[]
        for x in IDList:
            A=self.getLocalTimeByFixedID(x)
            if A is None:
                A=''

            InfoList.append(self.getInfoByFixedID(x))
            StatusList.append(self.getStatusByFixedID(x))
            TimeList.append(A)
            n+=1

        return [IDList,InfoList,StatusList,TimeList]

    def GenerNew(self,event):
        descriName=self.NameOfAsset.GetLineText(0)
        codeName=self.code.GetLineText(0)
        if codeName=='' or codeName=='Code':
            pass

    def searchAllAsset(self,AssetName):

            IDList = self.getFixedIDByFixedInfo(AssetName)
            if IDList!=[]:
                n = 0
                InfoList = []
                StatusList = []
                UserList = []
                for x in IDList:
                    InfoList.append(self.getInfoByFixedID(x))
                    StatusList.append(self.getStatusByFixedID(x))
                    UserList.append(self.getUserByFixedID(x))
                    n += 1

                return [IDList, InfoList, StatusList, UserList]
            else:

                wx.MessageBox('Please enter an valid Value!')
                return []





























app = wx.App(False)
frame =  showFrame(None)
frame.Show(True)
app.MainLoop()


