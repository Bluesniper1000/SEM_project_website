from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('food_data.db')
    conn.row_factory = sqlite3.Row  # To get dictionary-like rows
    return conn

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials, try again!'
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM food_suggestions WHERE health_condition LIKE ?', ('%' + search_term + '%',)).fetchall()
    conn.close()

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
