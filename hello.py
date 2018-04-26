from flask import Flask      #导入类Flask，第一个参数是应用模块的名称，如果使用的是单   
                             #一的模块，第一个参数应该使用__name__,
app = Flask(__name__)        #该类的实例，传递给他模块或包的面过程

@app.route('/')               #装饰器route（）告诉Flask哪个URL才能触发我们的函数
def hello_world():            #定义函数，函数名用来给特定函数生成UPLs，并返回信息
    return 'Hello World!'

@app.route('/shiyanlou')
def show_name():
    return 'Guangxia'

@app.route('/user/<username>')    #显示用户名称
def show_user_profile(username): 
    return 'User %s' % username

@app.route('/post/<int:post_id>')   #显示提交整形的用户“id"的结果，int:输入字符串形式转换为整形数据
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return 'sum %d' %(a+b)


if __name__=='__main__':       #确保服务器只会在该脚本被Python解释器运行应用
    app.run(debug=True)        #run（）启动本地服务器运行应用。app.debug =True;app.run() >>> app.run(debug = True)

