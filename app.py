from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 定义主页路由，返回至 index.html 页面
@app.route("/")
def home():
    return render_template("index.html")

# 定义注册页面路由，返回至 register.html 页面
@app.route("/register")
def register():
    return render_template("register.html")


# 定义 submit 路由和HTTP协议，接收前端提交数据，写入数据库后，返回至主页
@app.route("/register_ok", methods=["POST"])
def register_ok():
    # 1.接收用户提交数据
    # 左侧 user 为要存入数据库的变量名，右侧 user 为 form 表单提交数据的变量名
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    role = request.form.get("role")
    gender = request.form.get("gender")
    others = request.form.get("others")
    # 接收复选框  request.args.getlist()
    hobby = request.form.getlist("hobby")

    # 2.保存数据
    with open("users.txt", "a", encoding="utf-8") as f:
        line = f"{user}|{pwd}|{role}|{gender}|{hobby}|{others}\n"
        f.write(line)
    
    # 重定向到主页
    return redirect(url_for("home"))  # 此处 home 是主页视图函数

# 定义登录页面路由，返回至 login.html 页面
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()