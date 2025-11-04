# 🔐 Tkinter Login & Registration System

A modern GUI authentication app built in Python with Tkinter. Supports user registration (with persistent storage), password show/hide toggle, login lockout after repeated failures, “Forgot Password” notification, and a personal welcome screen.

---

## ✨ Features

- **Register new users:** Username + password, stored in `users.json`.
- **Login with lockout:** After 3 failed attempts, login blocks for 10 seconds.
- **Password show/hide toggle** for all password fields.
- **“Forgot Password?”** button displays help (no real recovery in demo).
- **Welcome screen** after login and easy logout.
- **User data persists** across runs; default users: admin/admin123 and user/user123.

---

## 🚀 How to Run

1. Requires Python 3.x (Tkinter library included).
2. Save as `login.py` in your chosen folder.
3. Run in your terminal or command prompt: `python login.py`

---

## 🧑‍💻 How to Use

- **Login:** Enter username and password. (admin/admin123 and user/user123 work from default install.)
- **Show Password:** Tick box to reveal/hide password.
- **Register:** Click “Register” to create a new account. Pick username & password.
- **Lockout:** After 3 failed login attempts, login is blocked for 10 seconds.
- **Forgot Password?** Click for a simple help message.
- **Welcome Screen:** Get a personalized greeting after successful login. Logout back to login screen.

---

## 📁 Data Storage

- User credentials are saved in `users.json` (created automatically).
- On registration, data is updated and changes persist.

---

## 📄 License

MIT License — free for educational and personal use.

---

Perfect for learning authentication, GUI design, and secure user flow in Python!
