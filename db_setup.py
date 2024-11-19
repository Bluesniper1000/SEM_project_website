from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('food_data.db')
    conn.row_factory = sqlite3.Row  # To get dictionary-like rows
    return conn

# Index route with conditional login redirect
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']  # Store user ID in session
            return redirect(url_for('index'))  # Redirect to homepage after login
        else:
            return 'Invalid credentials, try again!'
    
    return render_template('login.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        existing_user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        if existing_user:
            return 'Username already exists, please choose another one.'
        
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        
        return redirect(url_for('login'))  # Redirect to login page after successful signup
    
    return render_template('signup.html')

# Profile creation and update route
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    user_id = session['user_id']

    if request.method == 'POST':
        name = request.form['name']
        sex = request.form['sex']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        
        conn.execute(''' 
            INSERT OR REPLACE INTO profiles (user_id, name, sex, age, height, weight)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, name, sex, age, height, weight))
        conn.commit()

    profile_data = conn.execute('SELECT * FROM profiles WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()

    return render_template('profile.html', profile=profile_data)

# Combined logout route
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()  # Clears the session data
    return redirect(url_for('login'))  # Redirects to the login page after logout

# Search suggestions route
@app.route('/search_suggestions', methods=['GET'])
def search_suggestions():
    query = request.args.get('query', '')
    if len(query) < 3:
        return jsonify([])  # No suggestions if query is too short

    conn = get_db_connection()
    health_conditions = conn.execute(
        'SELECT DISTINCT health_condition FROM food_suggestions WHERE health_condition LIKE ?', ('%' + query + '%',)
    ).fetchall()
    conn.close()

    suggestions = [{"health_condition": hc["health_condition"]} for hc in health_conditions]
    return jsonify(suggestions)

# Main search route for food suggestions
@app.route('/search', methods=['POST'])
def search():
    query = request.form['search_term']

    conn = get_db_connection()
    food_suggestions = conn.execute(
        'SELECT food_name, health_condition FROM food_suggestions WHERE health_condition LIKE ?', ('%' + query + '%',)
    ).fetchall()
    conn.close()

    return render_template('index.html', results=food_suggestions)

if __name__ == '__main__':
    app.run(debug=True)

