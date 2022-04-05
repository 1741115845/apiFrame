from common.pubulic import *
import xlrd
import demjson3
from utlis.operationYaml import OpenYaml


class ExcelCols:
    caseID='用例编号'
    caseName='用例名称'
    url='请求地址'
    method='请求方法'
    data='请求参数'
    expect='预期结果'
    precondition='前置条件'
    run='是否用例执行'
    statuscode='响应状态码'
    writecontent='写入文件内容'
    dataType='请求体类型'

class ExcelValues:

    def getSheet(self,index=0):
        '''
        获取sheet
        :param index: 读取excel中的第几个sheet页
        :return:
        '''
        workbook=xlrd.open_workbook(filePath('data','text02.xls'))
        sheet=workbook.sheet_by_index(index)
        return sheet

    def getExcelDatas(self):
        '''
        读取excel中的所有数据
        :return: 以列表字典的形式返回excel中的每行数据[{"表头":"value"}]
        '''
        title=self.getSheet().row_values(0)
        caseListDatas = []
        for row in range(1,self.getSheet().nrows):
            data=dict(zip(title,self.getSheet().row_values(row)))
            caseListDatas.append(data)
        # print(caseListDatas)
        return caseListDatas

    def getRuns(self):
        '''
        :return: 返回可运行的测试用例
        '''
        excelcols=ExcelCols()
        runs=list()
        for data in self.getExcelDatas():
            run=data[excelcols.run]
            if run =='y':
                runs.append(data)
            else:pass
        return runs
    def precondition(self,caseID):
        '''
        根据用例编号查找出关联的用例，并返回用例数据
        :param caseID: 传入前置用例的编号
        :return: 以字典的形式返回关联的前置用例数据
        '''
        precase=None
        for casedate in self.getRuns():
            if casedate[ExcelCols.caseID] == caseID:
                precase=casedate
                break
        return precase
        # return None

    def getdata(self,key):
        data=str(OpenYaml().userdatas()[key])
        userID=readBookID()
        if "{userID}" in data:
            data=data.replace("{userID}",userID)
        # print(type(demjson3.decode(data)))
        return demjson3.decode(data)

    def detContent(self,content,code):
        '''
        将接口响应数据根据key返回数据
        :param content: 传入接口响应数据
        :param code: 传入字典对应的key值
        :return: 返回指定key的value值
        '''
        for i in range(len(code)):
            content=content[code[i]]
            print(content)
        return str(content)

if __name__ == '__main__':
    excvalue=ExcelValues()
    # dict01={"code": 200, "data": {"id": 319834}, "message": "新增成功"}
    print(excvalue.precondition('test002'))
