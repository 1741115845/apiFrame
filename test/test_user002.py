import json

import allure
import pytest
from base.requestBase import Request
from utlis.operationExcel02 import *


class RequestMethod():
    # 获取所有可运行的用例
    testdatas = ExcelValues().getRuns()
    requestobj = Request()
    excleCols = ExcelCols()
    excelValue = ExcelValues()

    def requestmethod(self, data):
        datanum = data[self.excleCols.data]
        reperationcase = self.excelValue.precondition(data[self.excleCols.caseID])
        #get请求的时候执行这个
        if data[self.excleCols.method]=='get':
            # pass
            r=self.requestobj.get(url=data[self.excleCols.url],params=self.excelValue.getdata(datanum))
            print(json.dumps(r.json(),ensure_ascii=False))
        #postt请求
        elif data[self.excleCols.method]=='post':
            if data[self.excleCols.dataType]=='json':
                r=self.requestobj.post(url=data[self.excleCols.url],json=self.excelValue.getdata(datanum))
            elif data[self.excleCols.dataType]=='form':
                r = self.requestobj.post(url=data[self.excleCols.url], data=self.excelValue.getdata(datanum))
            print(json.dumps(r.json(),ensure_ascii=False))
        #delete请求
        elif data[self.excleCols.method]=='delete':
            if data[self.excleCols.dataType]=='json':
                r=self.requestobj.delete(url=data[self.excleCols.url],json=self.excelValue.getdata(datanum))
            elif data[self.excleCols.dataType]=='form':
                r = self.requestobj.delete(url=data[self.excleCols.url], data=self.excelValue.getdata(datanum))
            print(json.dumps(r.json(),ensure_ascii=False))
        #判断是否需要写入文件数据
        if data[self.excleCols.writecontent] != "":
            # str(data[self.excleCols.writecontent]).split(',')是将excel文件中的数据转换成列表，调用方法进行获取数据
            writeUserID(self.excelValue.detContent(r.json(), str(data[self.excleCols.writecontent]).split(',')))
        return r

@allure.feature('用户的测试类执行')
class Test_user:
    #获取所有可运行的用例
    testdatas=ExcelValues().getRuns()
    requestobj=Request()
    excleCols=ExcelCols()
    excelValue=ExcelValues()
    # @allure.feature("用户表增删改查接口执行")
    # @allure.step('操作步骤')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('用户表增删改查接口执行')
    @pytest.mark.parametrize('data',testdatas)
    def test_user(self,data):
        #执行用例前先判断是否有前置条件用例需要执行，如果有则先执行前置用例
        with allure.step('方法内的操作步骤描述：执行前置用例'):
            if data[self.excleCols.precondition]!="" and self.excelValue.precondition(data[self.excleCols.precondition]) !=None:
                RequestMethod().requestmethod(self.excelValue.precondition(data[self.excleCols.precondition]))
            else: pass
        #执行用例
        r=RequestMethod().requestmethod(data)
        assert data[self.excleCols.expect] in json.dumps(r.json(),ensure_ascii=False)

if __name__ == '__main__':
    pytest.main(['-s','test_user002.py',"--alluredir=../resport/result"])
    import subprocess
    subprocess.call('allure generate ../resport/result/ -o ../resport/html --clean',shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 5055 ../resport/html',shell=True)