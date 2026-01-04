from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production
CORS(app)

# Database setup
def init_db():
    conn = sqlite3.connect('decision_maker.db')
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # User profiles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            age INTEGER,
            occupation TEXT,
            location TEXT,
            monthly_income REAL,
            monthly_budget REAL,
            financial_goals TEXT,
            style_type TEXT,
            favorite_colors TEXT,
            body_type TEXT,
            interests TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    try:
        conn = sqlite3.connect('decision_maker.db')
        cursor = conn.cursor()
        
        # Check if user already exists
        cursor.execute('SELECT id FROM users WHERE email = ?', (data['email'],))
        if cursor.fetchone():
            return jsonify({'error': 'User already exists'}), 400
        
        # Create new user
        password_hash = generate_password_hash(data['password'])
        cursor.execute(
            'INSERT INTO users (email, password_hash, full_name) VALUES (?, ?, ?)',
            (data['email'], password_hash, data['fullName'])
        )
        
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        session['user_id'] = user_id
        return jsonify({'message': 'User created successfully', 'user_id': user_id}), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    try:
        conn = sqlite3.connect('decision_maker.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, password_hash FROM users WHERE email = ?', (data['email'],))
        user = cursor.fetchone()
        
        if user and check_password_hash(user[1], data['password']):
            session['user_id'] = user[0]
            return jsonify({'message': 'Login successful', 'user_id': user[0]}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/profile', methods=['POST'])
def save_profile():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    user_id = session['user_id']
    
    try:
        conn = sqlite3.connect('decision_maker.db')
        cursor = conn.cursor()
        
        # Check if profile exists
        cursor.execute('SELECT id FROM user_profiles WHERE user_id = ?', (user_id,))
        existing_profile = cursor.fetchone()
        
        if existing_profile:
            # Update existing profile
            cursor.execute('''
                UPDATE user_profiles SET
                age = ?, occupation = ?, location = ?, monthly_income = ?,
                monthly_budget = ?, financial_goals = ?, style_type = ?,
                favorite_colors = ?, body_type = ?, interests = ?
                WHERE user_id = ?
            ''', (
                data.get('age'), data.get('occupation'), data.get('location'),
                data.get('monthlyIncome'), data.get('monthlyBudget'),
                data.get('financialGoals'), data.get('styleType'),
                data.get('favoriteColors'), data.get('bodyType'),
                ','.join(data.get('interests', [])), user_id
            ))
        else:
            # Create new profile
            cursor.execute('''
                INSERT INTO user_profiles 
                (user_id, age, occupation, location, monthly_income, monthly_budget,
                 financial_goals, style_type, favorite_colors, body_type, interests)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id, data.get('age'), data.get('occupation'), data.get('location'),
                data.get('monthlyIncome'), data.get('monthlyBudget'),
                data.get('financialGoals'), data.get('styleType'),
                data.get('favoriteColors'), data.get('bodyType'),
                ','.join(data.get('interests', []))
            ))
        
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Profile saved successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    user_id = session['user_id']
    
    try:
        conn = sqlite3.connect('decision_maker.db')
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO expenses (user_id, description, amount, category) VALUES (?, ?, ?, ?)',
            (user_id, data['description'], data['amount'], data['category'])
        )
        
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Expense added successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user_id = session['user_id']
    
    try:
        conn = sqlite3.connect('decision_maker.db')
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT description, amount, category, date_added FROM expenses WHERE user_id = ? ORDER BY date_added DESC',
            (user_id,)
        )
        
        expenses = []
        for row in cursor.fetchall():
            expenses.append({
                'description': row[0],
                'amount': row[1],
                'category': row[2],
                'date_added': row[3]
            })
        
        conn.close()
        return jsonify({'expenses': expenses}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/dashboard-stats', methods=['GET'])
def get_dashboard_stats():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user_id = session['user_id']
    
    try:
        conn = sqlite3.connect('decision_maker.db')
        cursor = conn.cursor()
        
        # Get monthly spending
        cursor.execute('''
            SELECT SUM(amount) FROM expenses 
            WHERE user_id = ? AND date_added >= date('now', 'start of month')
        ''', (user_id,))
        monthly_spending = cursor.fetchone()[0] or 0
        
        # Get user budget
        cursor.execute('SELECT monthly_budget FROM user_profiles WHERE user_id = ?', (user_id,))
        budget_result = cursor.fetchone()
        monthly_budget = budget_result[0] if budget_result else 0
        
        # Get daily spending for the week
        cursor.execute('''
            SELECT DATE(date_added) as day, SUM(amount) as total
            FROM expenses 
            WHERE user_id = ? AND date_added >= date('now', '-7 days')
            GROUP BY DATE(date_added)
            ORDER BY day
        ''', (user_id,))
        
        daily_spending = []
        for row in cursor.fetchall():
            daily_spending.append({
                'day': row[0],
                'amount': row[1]
            })
        
        conn.close()
        
        return jsonify({
            'monthly_budget': monthly_budget,
            'monthly_spending': monthly_spending,
            'budget_remaining': monthly_budget - monthly_spending,
            'daily_spending': daily_spending
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)