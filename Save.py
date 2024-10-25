from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Giả lập cơ sở dữ liệu người dùng
users = {
    "admin": "password123",
    "user": "mypassword"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect("https://www.google.com")
    else:
        return "Tên đăng nhập hoặc mật khẩu không đúng!"

if __name__ == '__main__':
    app.run(debug=True)
