import os

def getPath(directory,filename):
    '''

    :param directory: 读取文件的上级目录
    :param filename: 读取的文件名称
    :return: 返回文件当前路径
    '''
    basepath=os.path.dirname(os.path.dirname(__file__))
    path=os.path.join(basepath,directory,filename)
    return path

# print(getPath('data','config.ini'))