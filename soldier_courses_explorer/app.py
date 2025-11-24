from db import queries
from db import load_csv
while True:
    menu = input(" 1.Load CSV into DB \n 2.Search records by institution name \n 3.Search records by course name \n 4.Find most/least common course \n 5.Show course count per district \n 6.Free SQL query \n 7.Exit")
    if menu == "1":
        load_csv.load_to_csv()
        # continue
    elif menu == "2":
        keyword = input("enter some word")
        queries.question_2(keyword)
        # continue

    elif menu == "3":
        keyword = input("enter name  course")
        queries.question_3(keyword)

    elif menu == "4":
        choice = input("choos most or least")
        if choice == "most":
            queries.question_4_a()
        elif choice == "least":
            queries.question_4_b()
        else:
            print("choice again")

    elif  menu == "5":
        queries.question_5()

    elif menu == "6":
        queries.question_6()

    elif menu == "7":
        break