from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from datetime import datetime
import google.generativeai as genai
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True

# Configure CORS to allow credentials and all localhost origins
CORS(app, supports_credentials=True, origins=['http://localhost:4321', 'http://localhost:4322', 'http://localhost:3000', 'http://127.0.0.1:4321', 'http://127.0.0.1:4322'])

# Configure Gemini AI - Set your API key as environment variable GEMINI_API_KEY
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '').strip().strip('"')
print(f"GEMINI_API_KEY loaded: {'Yes' if GEMINI_API_KEY else 'No'}")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

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
    data = request.get_json()
    
    # If not authenticated, just return success (frontend uses localStorage)
    if 'user_id' not in session:
        print("Profile saved to localStorage only (no session)")
        return jsonify({'message': 'Profile data received', 'stored': 'localStorage'}), 200
    
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
        # Return empty data instead of 401 for better UX
        return jsonify({'expenses': []}), 200
    
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
        # Return default data instead of 401 for better UX
        return jsonify({
            'monthly_income': 0,
            'monthly_budget': 0,
            'monthly_spending': 0,
            'budget_remaining': 0,
            'daily_spending': []
        }), 200
    
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
        
        # Get user budget and income
        cursor.execute('SELECT monthly_budget, monthly_income FROM user_profiles WHERE user_id = ?', (user_id,))
        profile_result = cursor.fetchone()
        monthly_budget = profile_result[0] if profile_result and profile_result[0] else 0
        monthly_income = profile_result[1] if profile_result and profile_result[1] else 0
        
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
            'monthly_income': monthly_income,
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

@app.route('/api/outfit-recommendation', methods=['POST'])
def get_outfit_recommendation():
    data = request.get_json()
    
    occasion = data.get('occasion', 'casual')
    budget = data.get('budget', 5000)
    weather = data.get('weather', 'mild')
    travel_distance = data.get('travelDistance', 'local')
    style_preference = data.get('stylePreference', 'trendy')
    gender = data.get('gender', 'unisex')
    
    # Get user profile if authenticated
    user_profile = None
    if 'user_id' in session:
        try:
            conn = sqlite3.connect('decision_maker.db')
            cursor = conn.cursor()
            cursor.execute('SELECT style_type, favorite_colors, body_type FROM user_profiles WHERE user_id = ?', (session['user_id'],))
            profile = cursor.fetchone()
            if profile:
                user_profile = {
                    'style_type': profile[0],
                    'favorite_colors': profile[1],
                    'body_type': profile[2]
                }
            conn.close()
        except:
            pass
    
    # Build prompt for Gemini
    prompt = f"""You are a professional fashion stylist. Generate outfit recommendations based on the following criteria:

Occasion: {occasion}
Budget: ₹{budget} (Indian Rupees)
Weather: {weather}
Travel Distance: {travel_distance} (affects comfort needs)
Style Preference: {style_preference}
Gender: {gender}
"""
    
    if user_profile:
        prompt += f"""
User's Style Profile:
- Preferred Style: {user_profile.get('style_type', 'Not specified')}
- Favorite Colors: {user_profile.get('favorite_colors', 'Not specified')}
- Body Type: {user_profile.get('body_type', 'Not specified')}
"""
    
    prompt += """
Please provide exactly 4 outfit item recommendations. For each item, provide:
1. Item name (e.g., "Cotton Kurta", "Formal Blazer")
2. Suggested color
3. Estimated price in INR (within the budget)
4. A brief tip for styling this item

IMPORTANT: Respond ONLY with a valid JSON array in this exact format, no other text:
[
  {
    "item": "Item Name",
    "color": "Color",
    "price": 1500,
    "tip": "Styling tip here"
  }
]

Make sure recommendations are:
- Culturally appropriate for Indian context
- Within the total budget
- Suitable for the occasion and weather
- Practical for the travel distance (comfortable if long travel)
"""

    try:
        if not GEMINI_API_KEY:
            # Return fallback recommendations if no API key
            print("No GEMINI_API_KEY set, using fallback")
            return jsonify({
                'recommendations': get_fallback_recommendations(occasion, budget),
                'source': 'fallback',
                'style_tip': 'Configure GEMINI_API_KEY for personalized AI recommendations.'
            }), 200
        
        # Call Gemini API
        print(f"Calling Gemini API for {occasion} with budget {budget}")
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        
        # Parse the response
        response_text = response.text.strip()
        print(f"Gemini response: {response_text[:500]}...")  # Print first 500 chars
        
        # Try to extract JSON from the response
        recommendations = None
        if response_text.startswith('['):
            recommendations = json.loads(response_text)
        else:
            # Try to find JSON array in the response
            import re
            json_match = re.search(r'\[[\s\S]*?\]', response_text)
            if json_match:
                recommendations = json.loads(json_match.group())
            else:
                print("Could not find JSON in response, using fallback")
                raise ValueError("Could not parse AI response")
        
        print(f"Parsed {len(recommendations)} recommendations")
        
        # Generate a style tip based on occasion
        style_tips = {
            'wedding': 'For Indian weddings, don\'t shy away from rich colors and embellishments. Gold accessories complement most outfits.',
            'casual': 'Comfort is key for casual outings. Mix and match basics with one statement piece.',
            'work': 'Stick to well-fitted pieces in neutral colors. A good watch adds professionalism.',
            'interview': 'First impressions matter. Choose conservative colors and ensure everything is well-pressed.',
            'party': 'This is your time to shine! Add some sparkle or bold colors to stand out.',
            'festival': 'Embrace traditional elements with a modern twist. Comfortable footwear is essential.',
            'date': 'Choose something that makes you feel confident. A subtle fragrance completes the look.',
            'gym': 'Prioritize moisture-wicking fabrics and proper support. Style meets function.'
        }
        
        result = {
            'recommendations': recommendations,
            'source': 'gemini',
            'style_tip': style_tips.get(occasion, 'Choose pieces that make you feel confident and comfortable.')
        }
        print(f"Returning result: {result}")
        return jsonify(result), 200
        
    except Exception as e:
        print(f"Gemini API error: {str(e)}")
        import traceback
        traceback.print_exc()
        # Return fallback recommendations on error
        return jsonify({
            'recommendations': get_fallback_recommendations(occasion, budget),
            'source': 'fallback',
            'style_tip': 'AI recommendations temporarily unavailable. Showing curated suggestions.'
        }), 200

def get_fallback_recommendations(occasion, budget):
    """Fallback recommendations when Gemini API is unavailable"""
    fallback = {
        'wedding': [
            {'item': 'Silk Kurta Set', 'color': 'Royal Blue', 'price': int(budget * 0.4), 'tip': 'Pair with gold mojaris for a complete look'},
            {'item': 'Embroidered Dupatta/Stole', 'color': 'Gold', 'price': int(budget * 0.15), 'tip': 'Drape elegantly over one shoulder'},
            {'item': 'Ethnic Mojaris', 'color': 'Gold/Tan', 'price': int(budget * 0.25), 'tip': 'Break them in before the event'},
            {'item': 'Statement Watch', 'color': 'Gold Tone', 'price': int(budget * 0.2), 'tip': 'A classic accessory that elevates any outfit'}
        ],
        'casual': [
            {'item': 'Cotton T-Shirt', 'color': 'White', 'price': int(budget * 0.2), 'tip': 'A wardrobe essential that goes with everything'},
            {'item': 'Comfortable Jeans', 'color': 'Dark Blue', 'price': int(budget * 0.35), 'tip': 'Choose a slim fit for a modern look'},
            {'item': 'Canvas Sneakers', 'color': 'White', 'price': int(budget * 0.3), 'tip': 'Keep them clean for a fresh appearance'},
            {'item': 'Casual Watch', 'color': 'Brown Leather', 'price': int(budget * 0.15), 'tip': 'Adds sophistication to casual wear'}
        ],
        'work': [
            {'item': 'Formal Shirt', 'color': 'Light Blue', 'price': int(budget * 0.25), 'tip': 'Ensure proper fit around shoulders'},
            {'item': 'Formal Trousers', 'color': 'Navy', 'price': int(budget * 0.3), 'tip': 'Get them tailored for the perfect fit'},
            {'item': 'Leather Belt', 'color': 'Brown', 'price': int(budget * 0.15), 'tip': 'Match with your shoe color'},
            {'item': 'Oxford Shoes', 'color': 'Brown', 'price': int(budget * 0.3), 'tip': 'Polish regularly for a professional look'}
        ],
        'party': [
            {'item': 'Printed Shirt', 'color': 'Black with Print', 'price': int(budget * 0.25), 'tip': 'Let the shirt be the statement piece'},
            {'item': 'Slim Fit Chinos', 'color': 'Black', 'price': int(budget * 0.3), 'tip': 'Dark colors create a sleek silhouette'},
            {'item': 'Loafers', 'color': 'Black', 'price': int(budget * 0.3), 'tip': 'Comfortable for dancing all night'},
            {'item': 'Bracelet', 'color': 'Silver', 'price': int(budget * 0.15), 'tip': 'Subtle accessories add personality'}
        ]
    }
    
    return fallback.get(occasion, fallback['casual'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)