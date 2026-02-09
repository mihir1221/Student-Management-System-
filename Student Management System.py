import mysql.connector

print("=== Student Management System ===")

# ---------- CONNECT DATABASE ----------
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mihir@1221",
        database="student_db"
    )

    cursor = db.cursor()
    print("Database connected successfully!\n")

    while True:
        print("\n------ MENU ------")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Update Course")
        print("5. Delete Student")
        print("6. Edit Full Details")
        print("7. Add New Column")
        print("8. Remove Column")
        print("9. Exit")

        choice = input("Enter your choice: ")

        # ---------- ADD STUDENT ----------
        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll: ")
            course = input("Enter course: ")
            phone = input("Enter phone: ")

            sql = "INSERT INTO students (name, roll, course, phone) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (name, roll, course, phone))
            db.commit()

            print("Student added successfully!")

        # ---------- SHOW ALL ----------
        elif choice == "2":
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()

            print("\n--- Student List ---")
            for s in students:
                print(s)

        # ---------- SEARCH ----------
        elif choice == "3":
            roll = input("Enter roll to search: ")
            cursor.execute("SELECT * FROM students WHERE roll=%s", (roll,))
            result = cursor.fetchall()

            if result:
                print("Student Found:")
                for r in result:
                    print(r)
            else:
                print("No student found")

        # ---------- UPDATE COURSE ----------
        elif choice == "4":
            roll = input("Enter roll: ")
            new_course = input("Enter new course: ")

            cursor.execute("UPDATE students SET course=%s WHERE roll=%s",
                           (new_course, roll))
            db.commit()
            print("Course updated")

        # ---------- DELETE ----------
        elif choice == "5":
            roll = input("Enter roll to delete: ")
            cursor.execute("DELETE FROM students WHERE roll=%s", (roll,))
            db.commit()
            print("Student deleted")

        # ---------- EDIT FULL ----------
        elif choice == "6":
            roll = input("Enter roll to edit: ")
            cursor.execute("SELECT * FROM students WHERE roll=%s", (roll,))
            data = cursor.fetchall()

            if data:
                print("Old Details:", data[0])

                name = input("New name: ")
                course = input("New course: ")
                phone = input("New phone: ")

                sql = """UPDATE students 
                         SET name=%s, course=%s, phone=%s 
                         WHERE roll=%s"""
                cursor.execute(sql, (name, course, phone, roll))
                db.commit()
                print("Details updated")
            else:
                print("Student not found")

        # ---------- ADD COLUMN ----------
        elif choice == "7":
            col = input("Column name: ")
            dtype = input("Datatype (like VARCHAR(50) or INT): ")

            cursor.execute(f"ALTER TABLE students ADD {col} {dtype}")
            db.commit()
            print("Column added")

        # ---------- REMOVE COLUMN ----------
        elif choice == "8":
            col = input("Column name to delete: ")

            cursor.execute(f"ALTER TABLE students DROP COLUMN {col}")
            db.commit()
            print("Column removed")

        # ---------- EXIT ----------
        elif choice == "9":
            print("Program closed")
            break

        else:
            print("Wrong choice, try again")

except mysql.connector.Error as err:
    print("Database error:", err)

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("Database connection closed")