import os

def filePath(directory,filename):
    '''
    :param directory: 文件父级目录名称
    :param filename: 文件名称
    :return: 返回文件当前路径
    '''
    basepath=os.path.dirname(os.path.dirname(__file__))
    filepath=os.path.join(basepath,directory,filename)
    return filepath

def writeUserID(content):
    '''
    :param content: 写入用户ID
    :return:
    '''
    with open(filePath('data','userID'),'w') as f:
        f.write(content)

def readBookID():
    '''
    :return: 返回写入的用户ID
    '''
    with open(filePath('data','userID'),'r') as f:
        return f.read()

