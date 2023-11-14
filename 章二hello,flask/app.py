from flask import Flask
app = Flask(__name__)  # 实例化
@app.route('/')  # 注册请求处理函数。@是装饰器，用于绑定对应URL，可以多个。/为根地址默认5000端口，URL 匹配的 URL 规则
@app.route('/home')
@app.route('/index')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
