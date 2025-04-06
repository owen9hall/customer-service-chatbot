import sqlite3

# This file contains all queries used to create and populate SQLite database.
# users table contains the user's name, email, and id
# packages table contains various package data for each order

connection = sqlite3.connect('chatbot_database.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS users")
#cursor.execute("DROP TABLE IF EXISTS packages")


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
   user_name TEXT NOT NULL,
   email TEXT UNIQUE
)              
""")

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

cursor.execute("""
INSERT INTO users (user_name, email)
VALUES (?, ?)
""", ("Ashutosh Roy", "ashutosh.roy123@gmail.com"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (1, "Zenify Ultra 6ft Phone Charger", "Shipped", 
#       "San Francisco, CA", "San Jose, CA", "On-time.", "2025-03-28"))

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


# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (2, "AquaPure Water Filter", "In Transit",
#       "Denver, CO", "Austin, TX",
#       "Delayed due to weather conditions.", "2025-03-27"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (2, "EcoClean Detergent - 2L", "Delivered",
#       "Austin, TX", "Austin, TX",
#       "Delivered on time. Left at doorstep.", "2025-03-20"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (3, "SonicBass Wireless Headphones", "Shipped",
#       "Chicago, IL", "Miami, FL",
#       "Package is on schedule.", "2025-03-29"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (1, "ThermaCup Insulated Mug", "Delayed",
#       "Phoenix, AZ", "San Jose, CA",
#       "Expected to arrive in 2 days.", "2025-03-28"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (1, "SmartGlow Night Light", "Delivered",
#       "San Diego, CA", "San Jose, CA",
#       "Delivered. Signed by recipient.", "2025-03-25"))

# # User 2
# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (2, "ZenMat Yoga Mat", "Shipped",
#       "Dallas, TX", "Austin, TX",
#       "Package has left the facility.", "2025-03-30"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (2, "GreenScape Planter Set", "Processing",
#       "N/A", "Austin, TX",
#       "Order received and is being prepared.", "2025-03-31"))

# # User 3
# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (3, "LumiTech LED Strip Lights", "In Transit",
#       "Nashville, TN", "Miami, FL",
#       "Package moving through network.", "2025-03-28"))

# cursor.execute("""
# INSERT INTO packages (user_id, product_name, shipping_status,
#                      package_location, package_destination,
#                      shipping_description, order_date)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """, (3, "PulseTrack Fitness Band", "Delivered",
#       "Miami, FL", "Miami, FL",
#       "Delivered. Left in mailbox.", "2025-03-26"))

connection.commit()
connection.close()