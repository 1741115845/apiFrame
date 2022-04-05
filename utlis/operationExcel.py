import json
import demjson3
import xlrd
from utlis.operationYaml import OpenYaml
from common.pubulic import *

class ExcelCols:
    caseID=0
    caseName=1
    url=2
    method=3
    data=4
    expect=5

    @property
    def getCaseId(self):
        ''':return:获取CaseID'''
        return  self.caseID
    @property
    def getCaseName(self):
        ''':return:获取用例名称'''
        return self.caseName
    @property
    def getUrl(self):
        '''return:获取请求方式'''
        return self.url
    @property
    def getMethod(self):
        '''return:获取请求方式'''
        return self.method
    @property
    def getData(self):
        return self.data
    @property
    def getExpect(self):
        '''return:请求预期结果'''
        return self.expect

class OperationExcel:
    def getSheet(self,index=0):
        '''
        获sheet,默认读取第一个sheet
        :return: 返回sheet
        '''
        workbook=xlrd.open_workbook(filePath('data','test.xls'))
        sheet=workbook.sheet_by_index(index)
        return sheet
    def getrows(self,index=0):
        '''
        :return: 返回sheet的总行数
        '''
        sheet=self.getSheet(index)
        rowsnumb=sheet.nrows
        return rowsnumb
    def getcors(self,index=0):
        '''
        :index:传入读取的sheet的序号,默认不传为0
        :return: 返回sheet的总列数
        '''
        sheet=self.getSheet(index)
        colsnumb=sheet.ncols
        return colsnumb
    def cellvaule(self,rowx,colx,index=0):
        '''
        读取单元格数据
        :index：传入读取的sheet的序号,默认不传为0
        :param rowx: 传入需要读取单元格所在位置的第几行
        :param colx: 传入需要读取单元格所在位置的第几列
        :return: 返回单元格数据
        '''
        sheet=self.getSheet(index)
        cell=sheet.cell_value(rowx=rowx,clox=colx)
        return cell
    def getCaseID(self,row,index=0):
        '''
        :param row: 传入获取用例编号的行数，例如第1行
        :param index: 传入读取的sheet的序号,默认不传为0
        :return: 返回指定行的用例编号
        '''
        sheet=self.getSheet(index)
        return sheet.cell_value(row,ExcelCols().getCaseId)
    def getCaseName(self,row,index=0):
        '''
        获取用例名
        :param row: 传入获取用例名称的行数，例如第1行
        :param index: 传入读取的sheet的序号,默认不传为0
        :return: 返回指定行的用例名称
        '''
        sheet=self.getSheet(index)
        return sheet.cell_value(row,ExcelCols().getCaseName)
    def getUrl(self,row,index=0):
        '''
        获取用例请求地址
        :param row: 传入获取用例请求地址的行数，例如第1行
        :param index: 传入读取的sheet的序号,默认不传为0
        :return: 返回指定行的用例接口请求地址
        '''
        sheet=self.getSheet(index)
        return sheet.cell_value(row,ExcelCols().getUrl)
    def getMethod(self,row,index=0):
        '''
        获取用例请求方法
        :param row: 传入获取用例请求方式的行数，例如第1行
        :param index: 传入读取的sheet的序号,默认不传为0
        :return: 返回指定行的用例接口请求方式
        '''
        sheet=self.getSheet(index)
        return sheet.cell_value(row,ExcelCols().getMethod)
    def getData(self,row,index=0):
        '''
        获取用例请求参数
        :param row: 传入获取用例请求参数标识的行数，例如第1行
        :param index: 传入读取的sheet的序号,默认不传为0
        :return: 返回指定行的用例接口请求参数的标识
        '''
        sheet=self.getSheet(index)
        datanum=sheet.cell_value(row,ExcelCols().getData)
        datas=str(OpenYaml().userdatas()[datanum])
        if "{userID}" in datas:
            userID = readBookID()
            datas=datas.replace('{userID}',userID)
        else:
            datas=datas
        return demjson3.decode(datas)
    def getExpect(self,row,index=0):
        '''
        获取用例期望结果
        :param row: 传入获取用例请求预期结果的行数，例如第1行
        :param index: 传入读取的sheet的序号,默认不传为0
        :return: 返回指定行的用例接口请求的预期结果
        '''
        sheet=self.getSheet(index)
        return sheet.cell_value(row,ExcelCols().getExpect)

# if __name__ == '__main__':
#     objexcel=OperationExcel()
#     # print(ExcelCols().getCaseName)
#     print(type(objexcel.getData(2)),objexcel.getData(2))
