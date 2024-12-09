from flask import Flask, render_template, request, redirect, flash
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = '233456'

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('/My_atomic2/N_database.db')  # Replace with your database file
    conn.row_factory = sqlite3.Row
    return conn

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # This will render your homepage

# Route to render the login and signup form
@app.route('/login', methods=['GET', 'POST'])
def login_signup():
    return render_template('login.html')  # This will render your login/signup page

# Route to handle sign-up form submission
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db_connection()
    try:
        # Insert the user data into the database
        conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hashed_password))
        conn.commit()
        conn.close()
        flash('Account created successfully!')
        return redirect('/login')
    except sqlite3.IntegrityError:
        conn.close()
        flash('Email already exists. Please use a different one.')
        return redirect('/login')

# Route to handle login form submission
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, hashed_password)).fetchone()
    conn.close()

    if user:
        flash('Login successful!')
        return redirect('/')
    else:
        flash('Invalid credentials. Please try again.')
        return redirect('/login')

@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
