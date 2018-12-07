import win32com.client
import win32com
import wx
import pyodbc

class makeODB:
    def __init__(self,sheetName):
        self.conn = pyodbc.connect(
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + "E:\App\MyDB2.mdb " + ";Uid=;Pwd=autof460;charset='utf-8';")
        cursor = self.conn.cursor()
        self.rsName = sheetName
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
       
        sql="UPDATE sheet2 SET [User] = '%s',[UserName] = '%s', TimeLimit = '%s', LocalTime= '%s' WHERE [FixedID] = '%s'" % (UserID,User,TimeLimit,LocalTime,AssetID)
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def testThisUp(self):
        sql = "Update " + self.rsName + " Set [User] = '88303409',TimeLimit = '30',[UserName] = 'Joe', [LocalTime] = '2018 9 17 ' where [FixedID] = '465210003212'"
 
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()
    def selectThis(self):
        pass
