from soldier_courses_explorer import config
cnx = config.connect_to_db()
cursor= cnx.cursor()
def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
      id INT AUTO_INCREMENT PRIMARY KEY,
      institution VARCHAR(255) NOT NULL,   -- שם הגוף המכשיר
      city VARCHAR(255) NOT NULL,          -- ישוב
      address VARCHAR(255),                -- כתובת מלאה
      course VARCHAR(255) NOT NULL,        -- שם הקורס
      district VARCHAR(255),               -- מחוז (חיפה והצפון וכו')
      telephone VARCHAR(50),               -- טלפון / שלוחה
      email VARCHAR(255)                   -- כתובת מייל
    );
    ''')
    cnx.commit()
    cursor.close()
    cnx.close()
    return "table created"
print(create_table())