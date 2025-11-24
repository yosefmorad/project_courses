import csv
from soldier_courses_explorer import config

def load_to_csv():

    cnx =config.connect_to_db()
    cursor = cnx.cursor()

    with open ("../data/courses.csv" ,encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            cursor.execute("""INSERT INTO courses (institution, city, address, course,district, telephone, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""",row)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("load data")
    return "load data"
print(load_to_csv())



