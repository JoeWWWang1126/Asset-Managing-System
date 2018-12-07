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
    #pyodbc is used here as a major to connect Access.
    #Plus, connecting can be a success if you don't enter the Uid.
    #This is used when it don't have username but password. 
    conn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + "E:\App\MyDB2.mdb " + ";Uid=;Pwd=autof460;charset='utf-8';")
    cursor = conn.cursor()
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










