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
