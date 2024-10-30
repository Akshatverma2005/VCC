from flask import Flask, render_template, redirect, url_for, flash, request, session
# import mysql.connector

app = Flask(__name__)
app.secret_key = 'mysecretkey123'

@app.route('/')
def login_page():
    return render_template('index.html')