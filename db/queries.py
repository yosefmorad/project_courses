from soldier_courses_explorer import config
cnx = config.connect_to_db()
cursor = cnx.cursor()
cursor.execute('''SELECT id, institution, city, course, district, telephone, email
FROM courses
WHERE institution LIKE CONCAT('%', %s, '%')
LIMIT 50'''
)