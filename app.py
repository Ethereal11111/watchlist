from flask import Flask, render_template  # 这个函数识别并调用Jinja2语句，返回渲染模版
app = Flask(__name__)  # 实例化
# @app.route('/')  # 注册请求处理函数。@是装饰器，用于绑定对应URL，可以多个。/为根地址默认5000端口，URL 匹配的 URL 规则
# @app.route('/home')
name = 'Ethereal'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
