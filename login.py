import tkinter as tk
from tkinter import messagebox
import json
import os

USER_FILE = "users.json"
LOCKOUT_SECONDS = 10

# Load users from JSON or use default
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"admin": "admin123", "user": "user123"}

def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f)

users = load_users()
login_attempts = 0
locked_out = False

def login_screen():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Login System")
    tk.Label(root, text="Login System", font=("Arial", 20), bg=bg).pack(pady=20)

    tk.Label(root, text="Username:", font=("Arial", 12), bg=bg).pack()
    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:", font=("Arial", 12), bg=bg).pack()
    password_entry = tk.Entry(root, font=("Arial", 12), show='*')
    password_entry.pack(pady=5)

    show_var = tk.IntVar()
    def toggle_password():
        if show_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")
    tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password, bg=bg).pack()

    # Use login_attempts from global scope
    def login():
        nonlocal username_entry, password_entry
        global login_attempts, locked_out

        if locked_out:
            messagebox.showwarning("Locked Out", "Too many failed attempts! Try again soon.")
            return

        username = username_entry.get().strip()
        password = password_entry.get()

        if username in users and users[username] == password:
            login_attempts = 0
            welcome_screen(username)
        else:
            login_attempts += 1
            if login_attempts >= 3:
                locked_out = True
                messagebox.showerror("Locked Out", f"Too many failed attempts! Try again in {LOCKOUT_SECONDS} seconds.")
                root.after(LOCKOUT_SECONDS * 1000, unlock_login)
            else:
                messagebox.showerror("Login Failed", f"Invalid username or password.\n{3-login_attempts} attempts left.")

    def register():
        registration_screen()

    def forgot():
        messagebox.showinfo("Forgot Password", "Password recovery is not available in this demo.\nPlease contact admin.")

    tk.Button(root, text="Login", command=login, font=("Arial", 12), width=12, bg="#4caf50", fg="black").pack(pady=7)
    tk.Button(root, text="Register", command=register, font=("Arial", 12), width=12, bg="#1976d2", fg="white").pack()
    tk.Button(root, text="Forgot Password?", command=forgot, font=("Arial", 10), bg=bg).pack(pady=3)

def unlock_login():
    global locked_out, login_attempts
    locked_out = False
    login_attempts = 0

def registration_screen():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Register")
    tk.Label(root, text="Register New User", font=("Arial", 20), bg=bg).pack(pady=17)

    tk.Label(root, text="Choose Username:", font=("Arial", 12), bg=bg).pack()
    new_user_entry = tk.Entry(root, font=("Arial", 12))
    new_user_entry.pack(pady=5)

    tk.Label(root, text="Choose Password:", font=("Arial", 12), bg=bg).pack()
    new_pass_entry = tk.Entry(root, font=("Arial", 12), show="*")
    new_pass_entry.pack(pady=5)

    show_var = tk.IntVar()
    def toggle_password():
        if show_var.get():
            new_pass_entry.config(show="")
        else:
            new_pass_entry.config(show="*")
    tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password, bg=bg).pack()

    def register_newuser():
        username = new_user_entry.get().strip()
        password = new_pass_entry.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
            return
        users[username] = password
        save_users(users)
        messagebox.showinfo("Success", "Account created! You can now log in.")
        login_screen()

    tk.Button(root, text="Register", command=register_newuser, font=("Arial", 12), width=12, bg="#4caf50", fg="black").pack(pady=10)
    tk.Button(root, text="Back to Login", command=login_screen, font=("Arial", 12), width=12, bg="#f44336", fg="black").pack()

def welcome_screen(username):
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Welcome")
    tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 20, "bold"), bg=bg, fg="#388e3c").pack(pady=32)
    tk.Button(root, text="Logout", command=login_screen, font=("Arial", 12), width=15, bg="#f44336", fg="white").pack(pady=18)

bg = "#f0f4c3"
root = tk.Tk()
root.geometry("400x320")
root.configure(bg=bg)
login_screen()
root.mainloop()