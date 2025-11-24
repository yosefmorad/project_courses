from soldier_courses_explorer import config

cux = config.connect_to_db()
cursor = cux.cursor()

def question_2(keyword):

    cursor.execute("""SELECT id, institution, city, course, district, telephone, email
FROM courses
WHERE institution LIKE CONCAT('%', %s, '%')
LIMIT 50;""", (keyword  ,))
    return cursor.fetchall()
# print(question_2("חיפה"))

def question_3(keyword):
    cursor.execute("""SELECT id, institution, city, course, district, telephone, email
    FROM courses
    WHERE institution LIKE CONCAT('%', %s, '%')
    LIMIT 50;""", (keyword,))
    return cursor.fetchall()
# print(question_3("הצלה בבריכות שחיה סוג 1"))

def question_4_a():
    cursor.execute("""SELECT course, COUNT(*) AS num
    FROM courses
    GROUP BY course
    ORDER BY num DESC
    LIMIT 1;"""
    )

    return cursor.fetchall()


def question_4_b():
    cursor.execute("""select course ,count(*) as num from courses group by course order by num limit 1""")

    return cursor.fetchall()


def question_5():
    cursor.execute('''
SELECT district, COUNT(*) AS num_courses
FROM courses
GROUP BY district
ORDER BY num_courses DESC;
''')
    return cursor.fetchall()

def question_6(query_user):

    if "select" == query_user.split()[0]:
        cursor.execute(query_user)
    return cursor.fetchall()
#
# print(question_6("select * from courses"))


