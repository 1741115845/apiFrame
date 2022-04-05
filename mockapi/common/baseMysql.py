import pymysql
from mockapi.flask.readConfig import Readconfig

class OprationMysql():
    def __init__(self):
        self.mysqlinfo = Readconfig().readconfig()
        print(self.mysqlinfo['port'])
        # try:
        self.connt=pymysql.connect(host=self.mysqlinfo['server'],
                              port=int(self.mysqlinfo['port']),
                              user=self.mysqlinfo['usrname'],
                              password=self.mysqlinfo['password'],
                                   db=self.mysqlinfo['db'])
        # except BaseException as e:
        #     e.args
        # else:
        self.curse=self.connt.cursor()
    def close(self):
        self.curse.close()
        self.connt.close()
    def select(self,sql,params=None):
        '''
        执行sql语句
        :param sql: 编写查询执行的sql语句
        :param params: 传入sql中的参数
        :return: 无
        '''
        # self.conten()
        print(sql, params)
        self.curse.execute(sql,params)
        datas=self.curse.fetchall()
        return datas
    def sql(self,sql,params=None):
        '''
        执行sql语句
        :param sql: 编写非查询执行的sql语句
        :param params: 传入sql中的参数
        :return: 无
        '''
        # self.conten()
        self.curse.execute(sql,params)
        self.connt.commit()


