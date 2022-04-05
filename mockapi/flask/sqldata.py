from mockapi.common.baseMysql import OprationMysql
import random
class SQl():
    mysql=OprationMysql()
    def close(self):
        self.mysql.close()
    def selectUser(self,name=None,account=None):
        '''
        查询用户，支持姓名和编号的查询
        :param name: 查询人员的姓名
        :param account: 查询人员的编号
        :return:
        '''
        sql='select * from userinfo'
        params = ()
        if name!=None and account==None:
            sql=sql+' where name =%s'
            params=(name,)
        elif name==None and account!=None:
            sql = sql+' where account =%s'
            params=(account,)
            print('params:', params)
        elif account!=None and name!=None:
            sql=sql+' where name =%s and account=%s'
            params=(name,account)
        # 执行sql语句
        datas=self.mysql.select(sql,params)
        listdata = [list(data) for data in datas]
        # 关闭数据库
        # self.mysql.close()
        return listdata

    def insertUser(self,account,name=None,phone=None,email=None,):
        '''
        添加单个用户
        :param name: 用户姓名
        :param phone: 用户手机号
        :param email: 用户邮箱
        :param account: 用户编号
        :return:
        '''
        id=random.randint(1,1000000)
        data={"id":id,'name':name,'phone':phone,'email':email,'account':account}
        key=(',').join(data.keys())
        value=(',').join(['%s']*len(data))
        sql=f'insert into userinfo ({key}) values ({value})'.format(key=key,value=value)
        # print(data.values())
        params=tuple(data.values())
        # print(sql,params)
        self.mysql.sql(sql,params)
        # self.mysql.close()
        return id


    def update(self,id,**kwargs):
        '''
        更新操作
        :param id: 更新条件的id
        :param kwargs: 动态传入用户表中的列对应修改的值
        :return:
        '''
        keys=['name','phone','account','email']
        checkkeys=[False for c in kwargs if c not in keys]
        if checkkeys:
            return "传入的列名有误"

        setsql=''
        lenkwargs=len(kwargs)
        for key,value in kwargs.items():
            lenkwargs=lenkwargs-1
            if lenkwargs == 0:
                setvalue='{key}=\'{value}\''.format(key=key,value=value)
            else:
                setvalue = ', {key}=\'{value}\''.format(key=key, value=value)
            setsql=setvalue+setsql
        sql='update userinfo set '+setsql+' where id ={id}'.format(id=id)
        # print(sql)
        self.mysql.sql(sql)

    def delete(self,id):
        sql=f'delete from userinfo where id = \'{id}\''.format(id=id)
        # print(sql)
        self.mysql.sql(sql)


# user=SQl()
# print(user.delete(id=5))

