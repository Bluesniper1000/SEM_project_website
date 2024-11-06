import sqlite3

def create_db():
    conn = sqlite3.connect('food_data.db')
    c = conn.cursor()

    # Create users table for login functionality
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')

    # Create food suggestion table
    c.execute('''
    CREATE TABLE IF NOT EXISTS food_suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_name TEXT NOT NULL,
        health_condition TEXT NOT NULL
    )''')

    # Insert some sample users
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('user', 'user123')")

    # Insert extensive food suggestions for various health conditions
    foods = [
        ('Carrot', 'Vision problems'),
        ('Spinach', 'Anemia'),
        ('Banana', 'Fatigue'),
        ('Apple', 'Digestive issues'),
        ('Salmon', 'Heart disease'),
        ('Tomato', 'Cancer prevention'),
        ('Olive oil', 'Inflammation'),
        ('Garlic', 'High blood pressure'),
        ('Ginger', 'Nausea'),
        ('Yogurt', 'Probiotics for gut health'),
        ('Oats', 'High cholesterol'),
        ('Chia seeds', 'Heart health'),
        ('Avocado', 'Weight loss'),
        ('Blueberries', 'Memory enhancement'),
        ('Sweet potato', 'Diabetes'),
        ('Almonds', 'Muscle recovery'),
        ('Mango', 'Immune boosting'),
        ('Kiwi', 'Asthma'),
        ('Cucumber', 'Hydration'),
        ('Kale', 'Cancer prevention'),
        ('Lemon', 'Detoxification'),
        ('Watermelon', 'Hydration and vitamin C'),
        ('Turmeric', 'Joint health'),
        ('Beetroot', 'Detoxification'),
        ('Green tea', 'Metabolism boosting'),
        ('Coconut water', 'Hydration'),
        ('Pumpkin seeds', 'Prostate health'),
        ('Eggplant', 'Blood sugar regulation'),
        ('Cabbage', 'Cancer prevention'),
        ('Lentils', 'Iron deficiency'),
        ('Cherries', 'Anti-inflammatory'),
        ('Pineapple', 'Digestive health'),
        ('Chia seeds', 'Omega-3 fatty acids'),
        ('Brussels sprouts', 'Antioxidants'),
        ('Peppermint', 'Digestive issues'),
        ('Cilantro', 'Heavy metal detox'),
        ('Pomegranate', 'Heart health'),
        ('Coconut oil', 'Brain function'),
        ('Papaya', 'Stomach ulcers'),
        ('Grapefruit', 'Weight loss'),
        ('Asparagus', 'Antioxidants'),
        ('Mushrooms', 'Immune system support'),
        ('Zucchini', 'Digestive health'),
        ('Figs', 'Bone health'),
        ('Blackberries', 'Antioxidants'),
        ('Walnuts', 'Brain health'),
        ('Pistachios', 'Lowering cholesterol'),
        ('Chickpeas', 'Diabetes'),
        ('Cranberries', 'Urinary tract health')
    ]
    
    # Insert the food suggestions into the database
    c.executemany('INSERT OR IGNORE INTO food_suggestions (food_name, health_condition) VALUES (?, ?)', foods)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("Database setup complete with extensive food suggestions.")
