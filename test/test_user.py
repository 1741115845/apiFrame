import pytest
from utlis.operationExcel import OperationExcel
from base.requestBase import Request
import json
from common.pubulic import *

class Test_User():
    excelobj=OperationExcel()
    requestobj=Request()

    def resurt(self,r,row):
        '''
        接口断言校验
        :param r: 请求对象
        :param row: 校验的预期结果的行数
        :return:
        '''
        assert r.status_code==200
        assert self.excelobj.getExpect(row=row) in json.dumps(r.json(), ensure_ascii=False)

    def test_select_user(self):
        '''
        :return: 查询用户
        '''
        r=self.requestobj.get(url=self.excelobj.getUrl(1),params=self.excelobj.getData(1))
        # print(type(r.text),json.dumps(r.json(),ensure_ascii=False))
        self.resurt(r,row=1)

    def test_001add(self):
        # data=self.excelobj.getData(2)
        # print(data,type(data))
        r=self.requestobj.post(url=self.excelobj.getUrl(2),json=self.excelobj.getData(2))
        print(type(r.json()),r.json()['data']['id'])
        writeUserID(str(r.json()['data']['id']))
        self.resurt(r,row=2)

    def test_002update(self):
        r=self.requestobj.post(url=self.excelobj.getUrl(3),data=self.excelobj.getData(3))
        print(readBookID())
        self.resurt(r,row=3)
    #
    def test_003delete(self):
        r=self.requestobj.delete(url=self.excelobj.getUrl(4),data=self.excelobj.getData(4))
        self.resurt(r,row=4)


if __name__ == '__main__':
    pytest.main(['-v','-s','test_user.py::Test_User'])