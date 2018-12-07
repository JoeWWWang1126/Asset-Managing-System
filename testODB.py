import win32com.client
import win32com
import wx
import pyodbc

class makeODB:
    def __init__(self,sheetName):
        # self.conn = win32com.client.Dispatch(r"ADODB.Connection")
        # self.DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = MyDB2.mdb'
        # self.conn.Open(self.DSN)
        # self.rs = win32com.client.Dispatch(r'ADODB.Recordset')
        self.conn = pyodbc.connect(
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + "E:\App\MyDB2.mdb " + ";Uid=;Pwd=autof460;charset='utf-8';")
        cursor = self.conn.cursor()
        # self.rs.open('[' + 'sheet4 '+ ']', self.conn, 1, 3)
        # old = self.rs.Fields[0].Value
        # self.rs.close('[' + 'sheet4 '+ ']')
        # self.rs.open('[' + 'sheet3 ' + ']', self.conn, 1, 3)
        # new = self.rs.RecordCount
        # if new!=old:
        #     wx.MessageBox('You Got New Message! Please Check it! ')
        # # self.rs.close('[' + 'sheet3 ' + ']')

        # old=self.rs.Fields[0].Value
        # new=self.rs.RecordCount


        # rs.Open('[' + rsName + ']', conn, 1, 3)

        self.rsName = sheetName
        # self.rs.Open('[' + self.rsName + ']', self.conn, 1, 3)
        # self.rs.Open("SELECT * from sheet2 FixedID = '465210003212'")
    def Exit(self):
        self.conn.close()
    def addToSheet4(self,MailAddress,Identify,Time):
        sentence = "VALUES ('" + MailAddress + "','" + Identify + "','" + Time + "')"
        sql = "Insert Into " + self.rsName + "([MailAddress],[Identify],[Time])" + sentence

        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()




    def addNewLine(self,HRID,HRName,FixedID,AssetName,TimeLimit,NowTime,MailAddress):
        sentence = "VALUES ('" + HRID+"','"+HRName+"','"+FixedID+"','"+AssetName+"','"+TimeLimit+"','"+NowTime+"','"+MailAddress+"')"
        # print(self.rs.RecordCount)



        sql="Insert Into "+self.rsName+"([ID],[Name],[AssetID],[AssetInfo],[More],[LocalTime],[MailAddress])"+sentence
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def testADD(self,NowTime):
        sentence= "VALUES ('" + NowTime+"')"
        sql = "Insert Into " + self.rsName + "(LocalTime)" + sentence
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def UpadateBorrow(self,AssetID,UserID,User,TimeLimit,LocalTime):
        # sentence = "UPDATE "+self.rsName+" SET [User]= '" +UserID + "', [UserName] = '"+ User+"', TimeLimit = "+ TimeLimit+"', LocalTime = '"+ LocalTime+"'," +" WHERE FixedID = " + AssetID
        sql = "UPDATE sheet7 SET [User] = '%s',[UserName] = '%s', TimeLimit = '%s', LocalTime= '%s', [Status] = 'Not in Stock'  WHERE [FixedID] = '%s'" % (
        UserID, User, TimeLimit, LocalTime, AssetID)
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def UpdateReturn(self,AssetID,LocalTime):
        sql = "UPDATE sheet7 SET  [User] = '%s',[UserName] = '%s', TimeLimit = '%s', LocalTime= '%s', [Status] = 'In Stock'  WHERE [FixedID] = '%s'" % (
        'None', '', '', LocalTime, AssetID)
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def testUpdate(self,AssetID,UserID,User,TimeLimit,LocalTime):
        # sentence = "Update " + self.rsName + " Set User = '" + UserID+"' WHERE FixedID = '" + AssetID+"'"
        sql="UPDATE sheet2 SET [User] = '%s',[UserName] = '%s', TimeLimit = '%s', LocalTime= '%s' WHERE [FixedID] = '%s'" % (UserID,User,TimeLimit,LocalTime,AssetID)
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def testThisUp(self):
        # sql = "Update " + self.rsName + " Set User = 88303409 where FixedID = 465210003212"
        sql = "Update " + self.rsName + " Set [User] = '88303409',TimeLimit = '30',[UserName] = 'Joe', [LocalTime] = '2018 9 17 ' where [FixedID] = '465210003212'"
        # sql = "UPDATE Sheet2 SET ID = '465210005844' WHERE AssetID = '465210004626'"
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def selectThis(self):
        pass

        # sql = "SELECT * from sheet2 FixedID = '465210003212'"
        # self.conn.Execute(sql)
        # self.rs.open(sql)
        # self.rs.Fields('aaa')
# A=makeODB('Sheet2')
# A.UpadateBorrow('465210003212','88301648','CHEN GANG','30','time')
# A.testUpdate('465210003212','88301648','CHEN GANG','30','time')

    # def closeThis(self):
    #     # sql="UPDATE Sheet4 SET Count = 0 "
    #     # self.conn.Execute(sql)
    #
    #     self.conn.close()

    # def checkThis(self):
    #     MaxRecords


# A=makeODB('sheet3')
# # # A.addNewLine('88301648','465210003212')
# # # # A.addNewLine()
# # A.testADD('time')
# # A=makeODB('sheet3')
# A.addNewLine('a','a','a','a','a','hhhh')
# A.checkThis()
