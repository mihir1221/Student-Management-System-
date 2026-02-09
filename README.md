Student Management System (Python + MySQL)

A simple terminal-based Student Management System built using Python and MySQL.  
This project helps manage student records like adding, searching, updating, and deleting student details.

Features
✔ Add Student  
✔ View All Students  
✔ Search Student by Roll  
✔ Update Course  
✔ Edit Full Student Details  
✔ Delete Student  
✔ Add/Remove Column from Database  
✔ Menu-driven system  

 Technologies Used
- Python
- MySQL
- mysql-connector-python
- VS Code
 💻 How to Run Project

1. Install MySQL connector:pip install mysql-connector-python
2. CREATE DATABASE student_db;
3.  Create table:
    CREATE TABLE students(
name VARCHAR(50),
roll VARCHAR(20) PRIMARY KEY,
course VARCHAR(50),
phone VARCHAR(15)
);

4. Run program:
python "Student Management System.py"


 Future Improvements
- Login system 🔐  
- GUI version (Tkinter)  
- Admin dashboard  
- Cybersecurity encryption  

Author
**Mihir Chatterjee**  
software engineering Student | Python Developer


