import csv

from soldier_courses_explorer import config
cursor =config.connect_to_db()
cnx = cursor.cursor()

with open ("../data/courses.csv" ,encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        cnx.execute("""INSERT INTO courses (institution, city, address, course,district, telephone, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",row)
cursor.commit()
cursor.close()
cnx.close()




