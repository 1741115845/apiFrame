import configparser
from mockapi.common.getPath import getPath

class Readconfig:
    def readconfig(self):
        mysqlInfo={"server":"","port":"","usrname":"","password":"","bd":""}
        config=configparser.ConfigParser()
        config.read(getPath('data','config.ini'))
        mysqlInfo['server']=config.get('mysql','server')
        mysqlInfo['port']=config.get('mysql','port')
        mysqlInfo['usrname']=config.get('mysql','usrname')
        mysqlInfo['password']=config.get('mysql','password')
        mysqlInfo['db'] = config.get('mysql', 'db')
        return mysqlInfo
