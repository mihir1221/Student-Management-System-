# 🎓 Student Management System (Python + MySQL)

A simple **terminal-based Student Management System** built using **Python** and **MySQL**.  
This project helps manage student records such as adding, searching, updating, and deleting student details using a menu-driven approach.

---

## ✨ Features
✔ Add student  
✔View all students  
✔Search student by roll number  
✔Update student course  
✔Edit full student details   
✔Delete student record  
✔Add or remove columns from database  
✔ Menu-driven terminal system  

---

## 🛠 Technologies Used
- Python  
- MySQL  
- mysql-connector-python  
- VS Code  

---

## 🗂 Database Structure

### Create Database
```sql
CREATE DATABASE student_db;
CREATE TABLE students (
    name VARCHAR(50),
    roll VARCHAR(20) PRIMARY KEY,
    course VARCHAR(50),
    phone VARCHAR(15)
);
```
### ▶️ How to Run the Project

## 1️⃣ Install MySQL Connector
```install
pip install mysql-connector-python
```
## 2️⃣ Setup Database
- Open MySQL
- Create the database and table using the SQL commands above
## 3️⃣ Run the Program

```RUN
python "Student Management System.py"
```
# 🚀 Future Improvements

Login system 🔐
GUI version using Tkinter

Admin dashboard

Data encryption and cybersecurity features

---
 # 👨‍💻 Author

Mihir Chatterjee

Software Engineering Student | Python Developer

---




