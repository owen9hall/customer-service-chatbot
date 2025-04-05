import sqlite3

# Connect to database
connection = sqlite3.connect('chatbot_database.db')
cursor = connection.cursor()

# cursor.execute("DROP TABLE IF EXISTS users")
# cursor.execute("DROP TABLE IF EXISTS packages")


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#    user_name TEXT NOT NULL,
#    email TEXT UNIQUE
# )              
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS packages (
#    tracking_number INTEGER PRIMARY KEY AUTOINCREMENT,
#    user_id INTEGER,
#    product_name TEXT,
#    shipping_status TEXT,
#    package_location TEXT,
#    package_destination TEXT,
#    shipping_description TEXT,
#    order_date TEXT,
#    FOREIGN KEY (user_id) REFERENCES users(user_id)
# )              
# """)

# cursor.execute("""
# INSERT INTO users (user_name, email)
# VALUES (?, ?)
# """, ("Ashutosh Roy", "ashutosh.roy123@gmail.com"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (1, "Zenify Ultra 6ft Phone Charger", "Shipped", 
#       "San Francisco, CA", "Los Angeles, CA", "On-time.", "2025-03-28"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (1, "SmartX Light Bulbs - 10 pack", "Exception",
#       "Eugene, OR", "San Jose, CA", 
#       "The package was damaged during delivery. Re-delivery scheduled. ETA: 3 days late.",
#       "2025-03-30"))

cursor.execute("""
INSERT INTO users (user_name, email)
VALUES (?, ?)
""", ("Jessica Nguyen", "jess.nguyen89@gmail.com"))

cursor.execute("""
INSERT INTO users (user_name, email)
VALUES (?, ?)
""", ("Mark Ramirez", "mark.ramirez22@yahoo.com"))

cursor.execute("""
INSERT INTO users (user_name, email)
VALUES (?, ?)
""", ("Tina Thompson", "tina.t.thompson@example.com"))

cursor.execute("""
INSERT INTO packages (user_id, product_name, shipping_status,
                     package_location, package_destination,
                     shipping_description, order_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (2, "AquaPure Water Filter", "In Transit",
      "Denver, CO", "Austin, TX",
      "Delayed due to weather conditions.", "2025-03-27"))

cursor.execute("""
INSERT INTO packages (user_id, product_name, shipping_status,
                     package_location, package_destination,
                     shipping_description, order_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (2, "EcoClean Detergent - 2L", "Delivered",
      "Austin, TX", "Austin, TX",
      "Delivered on time. Left at doorstep.", "2025-03-20"))

# For Carlos (user_id = 3)
cursor.execute("""
INSERT INTO packages (user_id, product_name, shipping_status,
                     package_location, package_destination,
                     shipping_description, order_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (3, "SonicBass Wireless Headphones", "Shipped",
      "Chicago, IL", "Miami, FL",
      "Package is on schedule.", "2025-03-29"))

connection.commit()
connection.close()