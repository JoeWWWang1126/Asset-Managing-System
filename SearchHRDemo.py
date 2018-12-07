import xlrd
import os
import win32com.client
import win32com
import pyodbc


class readHR_IDExcel():
    conn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + "E:\App\MyDB2.mdb " + ";Uid=;Pwd=autof460;charset='utf-8';")
    cursor = conn.cursor()
    cursor.execute("select name,id,manager from sheet1")
    rows = cursor.fetchall()
    HRName = []
    HRID = []
    HRManager = []
    for row in rows:
        HRName.append(row.name)
        HRID.append(row.id)
        HRManager.append(row.manager)
    conn.close()
   
    def getHRIDByHRName(self,thisHRName):
        pos = self.HRName.index(thisHRName)
        return self.HRID[pos]
    def getHRManagerByHRName(self,thisHRName):
        pos = self.HRName.index(thisHRName)
        return self.HRManager[pos]
    def getHRNameByHRID(self,thisHRID):
        pos = self.HRID.index(thisHRID)
        return self.HRName[pos]
    def getHRManagerByHRID(self,thisHRID):
        pos = self.HRID.index(thisHRID)
        return self.HRManager[pos]

