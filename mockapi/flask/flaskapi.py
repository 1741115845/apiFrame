from flask import Flask,request
from mockapi.flask.sqldata import SQl
app=Flask(__name__)
sql=SQl()


class FlaskApi():
    @staticmethod
    @app.route('/get', methods=['get'])
    def get():
        '''
        查询用户接口，通过name和account查询
        :return: 返回查询结果
        '''
        name=request.args.get('name')
        account=request.args.get('account')
        datas=sql.selectUser(name=name,account=account)
        # datas在sql执行后进行了转类型为列表，然后在api中要进行组装json
        result={"code":200,"message":"查询成功","resurt":datas}
        #最后使用sql的进行关闭数据库
        # sql.close()
        return result

    @staticmethod
    @app.route('/post/insert',methods=['post'])
    def post():
        '''
        新增接口,json格式传参
        :return:
        '''
        data=request.get_json()
        name=data['name']
        account=data['account']
        phone=data['phone']
        email=data['email']
        id=sql.insertUser(name=name,account=account,phone=phone,email=email)
        result={"code":200,"message":"新增成功","data":{"id":id}}
        # 最后使用sql的进行关闭数据库
        # sql.close()
        return result
    @staticmethod
    @app.route('/post/update',methods=['post'])
    def update():
        '''
        更新接口，使用from表单格式，根据id更新
        :return:
        '''
        id=request.form.get('id')
        name=request.form.get('name')
        result={"code":200,"message":"{0}更新成功".format(name)}
        sql.update(id,name=name)
        # 最后使用sql的进行关闭数据库
        # sql.close()
        return result
    @staticmethod
    @app.route('/delete',methods=['delete'])
    def delete():
        id=request.form.get('id')
        sql.delete(id)
        result={"code":200,"meassge":"删除成功"}
        return result

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5001)





