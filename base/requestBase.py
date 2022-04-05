import requests

class Request():
    '''
    这个是dev分支的备注
    '''
    def request(self,url,method,**kwargs):
        if method=='get':
            return requests.request(url=url,method='get',**kwargs)
        elif method=='post':
            return requests.request(url=url, method='post', **kwargs)
        elif method=='put':
            return requests.request(url=url, method='put', **kwargs)
        elif method=='delete':
            return requests.request(url=url, method='delete', **kwargs)

    def get(self,url,**kwargs):
        return self.request(url,method='get',**kwargs)

    def post(self,url,**kwargs):
        return self.request(url,method='post',**kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, method='delete', **kwargs)
# if __name__ == '__main__':
#     objrequest=Request()
#     data={"name":"dyy","age":18,"datas":[{"school":1},{"school":2}]}
#     r=objrequest.post('http://192.168.0.59:5000/post',json=data)
#     print(r.text)
