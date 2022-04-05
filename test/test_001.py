import pytest
from utlis.operationYaml import OpenYaml
from base.requestBase import Request
from common.pubulic import filePath

objyaml=OpenYaml()
objrequest=Request()

@pytest.mark.parametrize('data',objyaml.readYaml())
def test_post(data):

    r=objrequest.post(url=data['url'],json=data['data'])
    print('url:',data['url'],"data:",data['data'])
    resurt=r.json()
    assert  data['expect']['message'] in resurt['message']

if __name__=='__main__':
    pytest.main('-v','-s',filePath('test','test_001.py'))