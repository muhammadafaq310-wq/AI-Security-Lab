# 🔐 AI Security Lab – Access Control System

A beginner-friendly cybersecurity project built with Python to demonstrate how authentication, role-based access control, authorization, and security logging work in a simple access control system.

This project was created as part of my hands-on cybersecurity learning journey.

## 🚀 Features

- User authentication with username and password
- SHA-256 password hashing for educational purposes
- Hidden password input using `getpass`
- Role-based access control (RBAC)
- Multiple access levels
- Access granted/denied based on permissions
- Failed login attempt tracking
- Account lockout after 3 failed attempts
- Input validation
- Security event logging with timestamps
- GRANTED and DENIED activity records

- ## 👥 Roles & Access Levels

| Role | Access Level | Confidential Report |
|---|---:|---|
| Administrator | 5 | Granted ✅ |
| Security Analyst | 3 | Granted ✅ |
| Student | 1 | Denied ❌ |

## ⚙️ How It Works

1. The program loads user data from `users.json`.
2. The user enters a username and password.
3. The password is hashed and compared with the stored hash.
4. The system verifies the user's role and access level.
5. Access is granted or denied based on the required permission level.
6. Login activity is recorded in `access_log.txt`.
7. After 3 invalid login attempts, the account is locked for the current session.

## 🛠️ Technologies Used

- Python
- JSON
- hashlib
- getpass
- datetime
- File Handling

## 🔒 Security Note

This project is designed for educational purposes. SHA-256 is used to demonstrate password hashing concepts. In a production system, passwords should be stored using dedicated password-hashing algorithms such as Argon2 or bcrypt with proper salting.

## 📚 What I Learned

Through this project, I gained hands-on experience with:

- Python conditions, loops, and functions
- Working with JSON data
- Authentication and authorization concepts
- Role-Based Access Control (RBAC)
- Password hashing concepts
- Security event logging
- Input validation and failed login handling
- Debugging and testing a Python security application

