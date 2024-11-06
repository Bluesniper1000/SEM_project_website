from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('food_data.db')
    conn.row_factory = sqlite3.Row  # To get dictionary-like rows
    return conn

# Route for home page
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?', (username, password)
        ).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials, try again!'
    
    return render_template('login.html')

# Route for signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        existing_user = conn.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        
        if existing_user:
            return 'Username already exists, please choose another one.'
        
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        
        return redirect(url_for('login'))
    
    return render_template('signup.html')

# Route for logout functionality
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Route to provide health condition suggestions for autocomplete
@app.route('/search_suggestions', methods=['GET'])
def search_suggestions():
    query = request.args.get('query', '').strip().lower()
    if len(query) < 3:
        return jsonify([])  # No suggestions if query is too short

    conn = get_db_connection()
    health_conditions = conn.execute(
        'SELECT DISTINCT health_condition FROM food_suggestions WHERE LOWER(health_condition) LIKE ?', ('%' + query + '%',)
    ).fetchall()
    conn.close()

    suggestions = [{"health_condition": hc["health_condition"]} for hc in health_conditions]
    return jsonify(suggestions)

# Route to search for food suggestions based on a health condition
@app.route('/search', methods=['POST'])
def search():
    query = request.form['search_term'].strip().lower()

    conn = get_db_connection()
    food_suggestions = conn.execute(
        'SELECT food_name, health_condition FROM food_suggestions WHERE LOWER(health_condition) LIKE ?', ('%' + query + '%',)
    ).fetchall()
    conn.close()

    return render_template('index.html', results=food_suggestions)

if __name__ == '__main__':
    app.run(debug=True)
