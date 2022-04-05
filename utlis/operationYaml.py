import yaml
from common.pubulic import filePath

class OpenYaml:
    def readYaml(self):
        '''
        :return: 返回yaml文件的用例信息,提供进行参数化用例执行
        '''
        with open(filePath('data','test.yaml'),'r',encoding='utf-8') as f:
            # 通过list转换后，读取的数据会成为列表的一个元素
            yamlfile=list(yaml.safe_load_all(f))
            return yamlfile
    def userdatas(self):
        '''
        :return: 返回excel用例中的用例参数数据,字典形式
        '''
        with open(filePath('config','userdatas.yaml'),'r',encoding='utf-8') as f:
            userdatas=yaml.safe_load(f)
            return userdatas

if __name__=='__main__':
    obj=OpenYaml()
    print(obj.userdatas()['test001'])