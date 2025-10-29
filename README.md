#Student Management System (Flask Project)

This is a simple Student Management System built using Flask, HTML, CSS, and Jinja2 templates.
It allows the admin to add, view, update, and delete student records.
The admin can also log in and log out securely.

# Features

Admin Login and Logout
Add New Student.
View All Students.
Update Student Details.
Delete Student.
User Session Management.

# Technologies Used
Frontend: HTML, CSS, Jinja2 Templates .
Backend: Python Flask.
Database: MySQL.
Server: Flask Development Server.

# Database Connectivity
In the project, database connection is handled using mysql.connector.

You can set your own MySQL credentials in the connection section:
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'your_Mysql_password',
    database = 'your_database_name'
)

Make sure to replace:
your_Mysql_password → with your MySQL password
your_database_name → with your database name

# Steps to Run the Project
1) Clone or Download the Project
git clone <your_repository_link>
cd StudentManagementSystem

2) Install Requirements
Make sure you have Python installed, then run:
pip install -r requirements.txt

3) Create Database in MySQL
CREATE DATABASE college;
USE college;
CREATE TABLE admin (
  username VARCHAR(50),
  email VARCHAR(50),
  password VARCHAR(50)
);

CREATE TABLE student (
  Roll_No INT PRIMARY KEY,
  Name VARCHAR(50),
  Branch VARCHAR(50),
  Year VARCHAR(10),
  Mark INT
);

4) Run the Flask Application
python app.py

5) Open in Browser

Go to:
👉 http://127.0.0.1:3000/

# requirements.txt
The project uses the following dependencies:
Flask==3.0.0
mysql-connector-python==9.0.0

(You can update versions as per your installed packages.)


# Author

Shivanand Kailas Dabhade
🎓 BE Computer Engineering, SPPU
📍 Nashik, Maharashtra
