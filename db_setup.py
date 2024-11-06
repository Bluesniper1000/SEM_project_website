import sqlite3

def create_db():
    conn = sqlite3.connect('food_data.db')
    c = conn.cursor()

    # Create users table for login functionality, with additional fields
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        name TEXT,
        gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
        age INTEGER CHECK(age > 0),
        height REAL CHECK(height > 0),  -- height in cm or inches
        weight REAL CHECK(weight > 0),  -- weight in kg or lbs
        disease1 TEXT,
        disease2 TEXT
    )''')

    # Create food suggestion table
    c.execute('''
    CREATE TABLE IF NOT EXISTS food_suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_name TEXT NOT NULL COLLATE NOCASE,
        health_condition TEXT NOT NULL COLLATE NOCASE
    )''')

    # Insert sample users with new fields
    c.execute("INSERT OR IGNORE INTO users (username, password, name, gender, age, height, weight, disease1, disease2) VALUES ('admin', 'admin123', 'Admin User', 'Male', 35, 175, 70, 'Hypertension', 'None')")
    c.execute("INSERT OR IGNORE INTO users (username, password, name, gender, age, height, weight, disease1, disease2) VALUES ('user', 'user123', 'Regular User', 'Female', 28, 160, 55, 'Diabetes', 'Asthma')")

    # Extensive list of food suggestions for various health conditions
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
        ('Yogurt', 'Gut health'),
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
        ('Beetroot', 'Blood pressure regulation'),
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
        ('Cranberries', 'Urinary tract health'),
        ('Bell peppers', 'Vitamin C boost'),
        ('Broccoli', 'Cancer prevention'),
        ('Basil', 'Antimicrobial support'),
        ('Seaweed', 'Thyroid health'),
        ('Quinoa', 'Protein deficiency'),
        ('Brown rice', 'Diabetes management'),
        ('Honey', 'Cough relief'),
        ('Flaxseed', 'Heart health'),
        ('Soy', 'Hormone balance'),
        ('Milk', 'Bone health'),
        ('Orange', 'Immune support'),
        ('Parsley', 'Detoxification'),
        ('Grapes', 'Heart health'),
        ('Peanut butter', 'Muscle gain'),
        ('Turmeric', 'Anti-inflammatory'),
        ('Apricots', 'Skin health'),
        ('Eggs', 'Protein boost'),
        ('Sesame seeds', 'Joint health'),
        ('Cloves', 'Anti-bacterial support'),
        ('Tuna', 'Omega-3s for heart health'),
        ('Cod liver oil', 'Vitamin D deficiency'),
        ('Berries', 'Brain function'),
        ('Sunflower seeds', 'Skin health'),
        ('Lamb', 'Anemia'),
        ('Chicken', 'Protein support'),
        ('Cinnamon', 'Blood sugar control'),
        ('Hemp seeds', 'Omega-3 and -6 balance'),
        ('Black beans', 'High fiber'),
        ('Green peas', 'Weight management'),
        ('Pecans', 'Skin health'),
        ('Macadamia nuts', 'Heart health'),
        ('Goji berries', 'Energy boost'),
        ('Rosemary', 'Memory enhancement'),
        ('Watercress', 'Cancer protection'),
        ('Turnips', 'Immune support'),
        ('Radishes', 'Liver health'),
        ('Mint', 'Digestive aid'),
        ('Bay leaves', 'Blood sugar management'),
        ('Sweet corn', 'Eye health'),
        ('Jackfruit', 'Antioxidants for immune system'),
        ('Fennel', 'Digestive health'),
        ('Anise', 'Respiratory support'),
        ('Artichokes', 'Liver function support'),
        ('Chard', 'Bone health'),
        ('Cauliflower', 'Heart health'),
        ('Leeks', 'Gut health'),
        ('Raspberries', 'Brain support'),
        ('Plums', 'Constipation relief'),
        ('Soy milk', 'Hormone regulation'),
        ('Barley', 'Cholesterol control'),
        ('Dates', 'Energy boost'),
        ('Mulberries', 'Liver support'),
        ('Pear', 'Colon health'),
        ('Okra', 'Blood sugar support'),
        ('Mustard greens', 'Detoxification')
    ]

    # Insert the food suggestions into the database
    c.executemany('INSERT OR IGNORE INTO food_suggestions (food_name, health_condition) VALUES (?, ?)', foods)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("Database setup complete with extensive food suggestions.")
