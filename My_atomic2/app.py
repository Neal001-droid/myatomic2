from flask import Flask, render_template, request, redirect, flash
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # This will render your homepage

# Route to render the login and signup form
@app.route('/login', methods=['GET', 'POST'])
def login_signup():
    return render_template('login.html')  # This will render your login/signup page

@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
