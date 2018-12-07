import xlrd
import os
import win32com.client
import win32com
import pyodbc


class readHR_IDExcel():
    # FixedExcel = xlrd.open_workbook(r'E:\App\Human ID Form.xlsx')
    # sheet1_name = FixedExcel.sheet_names()[0]
    # shee1 = FixedExcel.sheet_by_index(0)
    conn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + "E:\App\MyDB2.mdb " + ";Uid=;Pwd=autof460;charset='utf-8';")
    cursor = conn.cursor()
    # rs_name = 'sheet2'
    cursor.execute("select name,id,manager from sheet1")
    rows = cursor.fetchall()
    # HRKey = []
    HRName = []
    HRID = []
    HRManager = []
    for row in rows:
        HRName.append(row.name)
        HRID.append(row.id)
        HRManager.append(row.manager)
    conn.close()
    # conn = win32com.client.Dispatch(r"ADODB.Connection")
    # DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = MyDB2.mdb'
    # conn.Open(DSN)
    # rs = win32com.client.Dispatch(r'ADODB.Recordset')
    # rs_name = 'sheet1'
    # rs.Open('[' + rs_name + ']', conn, 1, 3)
    # rs.MoveFirst()  # 光标移到首条记录
    # count = 0
    # NameList = []
    #
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
    # length = len(NameList)
    # col = 4
    # HRKey = []
    # HRName = []
    # HRID = []
    # HRManager = []
    # for i in range(length):
    #     if i % 4 == 0:
    #         HRKey.append(NameList[i])
    #     elif i % 4 == 1:
    #         HRName.append(NameList[i])
    #     elif i % 4 == 2:
    #         HRID.append(NameList[i])
    #     else:
    #         HRManager.append(NameList[i])
    # conn.Close()
    #
    # HRName=connectAcess.importFromMDB.
    # HRID=self.
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

#
# a=readHR_IDExcel()
# print(a.getHRManagerByHRID('88301648'))


