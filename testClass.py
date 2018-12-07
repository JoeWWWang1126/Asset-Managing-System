import xlrd
import os
from collections import defaultdict
import win32com.client
import win32com
import io
import wx
import sys
import pyodbc
import re





class ReadExcel:
    # conn = pyodbc.connect(
    #             r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + "E:\App\MyDB2.mdb "+ ";Uid=;Pwd=autof460;charset='utf-8';")
    conn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + "E:\App\MyDB2.mdb " + ";Uid=;Pwd=autof460;charset='utf-8';")
    cursor = conn.cursor()
    # rs_name = 'sheet2'
    cursor.execute("select status,fixedid,fixedinfo,user,username,timelimit,localtime from sheet7")
    rows = cursor.fetchall()
    FixedID = []
    FixedInfo = []
    FixedStatus = []
    FixedUser = []
    FixedUserName = []
    FixedTimeLimit = []
    FixedLocalTime = []
    for row in rows:
        FixedID.append(row.fixedid)
        FixedInfo.append(row.fixedinfo)
        FixedStatus.append(row.status)
        FixedUser.append(row.user)
        FixedUserName.append(row.username)
        FixedTimeLimit.append(row.timelimit)
        FixedLocalTime.append(row.localtime)
    conn.close()
    # conn = win32com.client.Dispatch(r"ADODB.Connection")
    # DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE =MyDB2.mdb;User Id=;Jet OLEDB:Database Password=autof460;'
    # conn.Open(DSN)
    # rs = win32com.client.Dispatch(r'ADODB.Recordset')
    # rs_name = 'sheet2'
    # rs.Open('[' + rs_name + ']', conn, 1, 3)
    # rs.MoveFirst()  # 光标移到首条记录
    # count = 0
    # NameList = []
    # print('rs.Fields:')
    # print(rs.Fields[2].Value)
    # while True:
    #     if rs.EOF:
    #         break
    #     else:
    #         for i in range(rs.Fields.Count):
    #             # 字段名：字段内容
    #             NameList.append(rs.Fields[i].Value)
    #             # print(NameList)
    #
    #             # print(rs.Fields[i].Name, "：", rs.Fields[i].Value)
    #             # print(i)
    #         count += 1
    #         # print(count)
    #     rs.MoveNext()
    # # print(NameList)
    # print(NameList)
    # length = len(NameList)
    # col = 8
    # finalKey = []
    # FixedID = []
    # FixedInfo = []
    # FixedStatus = []
    # FixedUser = []
    # FixedUserName=[]
    # FixedTimeLimit=[]
    # FixedLocalTime=[]
    # for i in range(length):
    #     if i % col == 0:
    #         finalKey.append(NameList[i])
    #     elif i % col == 1:
    #         FixedID.append(NameList[i])
    #     elif i % col == 2:
    #         FixedInfo.append(NameList[i])
    #     elif i % col == 3:
    #         FixedStatus.append(NameList[i])
    #     elif i % col == 4:
    #         FixedUser.append(NameList[i])
    #     elif i % col == 5:
    #         FixedTimeLimit.append(NameList[i])
    #     elif i % col == 6:
    #         FixedLocalTime.append(NameList[i])
    #     else:
    #         FixedUserName.append(NameList[i])
    # # print(FixedInfo)
    # conn.Close()

    def getInfoByFixedID(self,thisFixedID):
        pos = self.FixedID.index(thisFixedID)
        return self.FixedInfo[pos]

    def getStatusByFixedID(self,thisFixedID):
        pos = self.FixedID.index(thisFixedID)
        return self.FixedStatus[pos]

    def getUserByFixedID(self,thisFixedID):
        pos = self.FixedID.index(thisFixedID)
        return self.FixedUser[pos]
    def getTimeLimitByFixedID(self,thisFixedID):
        pos = self.FixedID.index(thisFixedID)
        if self.FixedTimeLimit[pos]=='':
            print('hhh')
        return self.FixedTimeLimit[pos]
    def getUserNameByFixedID(self,thisFixedID):
        pos = self.FixedID.index(thisFixedID)
        return self.FixedUserName[pos]
    def getLocalTimeByFixedID(self,thisFixedID):
        pos = self.FixedID.index(thisFixedID)
        return self.FixedLocalTime[pos]
    def findReapeted(self,thislist,target):
        d = defaultdict(list)
        for k,va in [(v,i) for i,v in enumerate(thislist)]:
            d[k].append(va)
        return d[target]
    def getFixedIDByUser(self,thisUser):    
        newList=self.findReapeted(self.FixedUser,thisUser)
        length=len(newList)
        n=0
        IDlist=[]
        for x in newList :
            # print(x)
            # print(self.FixedID)
            # print(self.FixedID[x])
            IDlist.append(self.FixedID[x])
            n+=1
        return IDlist

    def getFixedIDByFixedInfo(self, AssetName):
        # print(self.FixedInfo)
        a = r'.*' + AssetName + r'.*'
        def check_name(K):

            # print(a)
            # print(re.findall('\.*'+AssetName+'\.*',i,re.I))
            if re.findall(a,K,re.I)==[]:
                return 'none'
            else:
                return re.findall(a,K,re.I)[0]


        count=0
        posi=[]
        for i in self.FixedInfo:
            # print(i,a)
            # print(re.findall('.*755.*',str(i),re.I))
            if check_name(str(i))=='none':
                pass
            else:
                posi.append(count)
            count+=1
        IDlist=[]

        for k in posi:
            IDlist.append(self.FixedID[k])
        return IDlist

        # newList=[i for i, x in enumerate(self.FixedInfo) if x.find(AssetName) != -1]
        # if newList!=[]:
        #     quantity = len(newList)
        #     n = 0
        #     IDlist = []
        #     for x in newList:
        #
        #         IDlist.append(self.FixedID[x])
        #         n += 1
        #     return IDlist
        # else:
        #     return []
    def checkSafety(self,event):
        SaftyReport='    Safety Stock Report  '

        for x in self.FixedInfo:

            if len(self.getFixedIDByFixedInfo(x)) <= 2:
                quantity=str(len(self.getFixedIDByFixedInfo(x)))

                SaftyReport+="\n"+'Warning: '  +x +' '+quantity
        f = open("Safety Stock Report.txt",'w',encoding='utf-8')
        f.write(SaftyReport)
        f.close()
        wx.MessageBox('Safety Stock Report.txt Has Created, Please Check it...')

        # print(SaftyReport)










