#导入flask拓展
from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import SelectField,PasswordField,StringField
#创建flask应用程序
app = Flask(__name__)
app.secret_key='1223'
#定义路由及视图函数
@app.route('/',methods = ['GET','POST'])  #默认get请求
def hello_world():

    url='www.baidu.com'
    #return 'Hello World!'
    return render_template('index.html',url=url)

@app.route('/order/<int:order_id>')
def get_order_id(order_id):
    flash(u'参数不完整')
    return 'order is'%order_id

if __name__ == '__main__':
    app.run()


