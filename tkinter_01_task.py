import tkinter as tk
from tkinter import messagebox

min_symbols = 2

# setup
root = tk.Tk()
root.title("Sign up form!")
root.geometry("800x600")
root.config(bg="#cfcfcf")

root.grid_columnconfigure(0, minsize=300)
root.grid_columnconfigure(1, minsize=500)

# title
label = tk.Label(root, text="Sign up form!", font=("Arial", 23), bg="#cfcfcf")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=50, sticky=tk.NSEW)

# Набор для "username"
username_label = tk.Label(root, text="username: ", font=("Arial", 17), bg="#cfcfcf")
username_entry = tk.Entry(root, width=30, font=("Arial", 17), bg="grey")
username_label.grid(row=1, column=0, padx=0, pady=10, sticky=tk.E)
username_entry.grid(row=1, column=1, padx=20, pady=10)

# Набор для "real name"
real_name_label = tk.Label(root, text="real name: ", font=("Arial", 17), bg="#cfcfcf")
real_name_entry = tk.Entry(root, width=30, font=("Arial", 17), bg="grey")
real_name_label.grid(row=2, column=0, padx=0, pady=10, sticky=tk.E)
real_name_entry.grid(row=2, column=1, padx=20, pady=10)

# Набор для "password"
password_label = tk.Label(root, text="password: ", font=("Arial", 17), bg="#cfcfcf")
password_entry = tk.Entry(root, width=30, font=("Arial", 17), bg="grey", show="*")
password_label.grid(row=3, column=0, padx=0, pady=10, sticky=tk.E)
password_entry.grid(row=3, column=1, padx=20, pady=10)

# Набор для "password confirmation"
password_confirmation_label = tk.Label(root, text="password confirmation: ", font=("Arial", 17), bg="#cfcfcf", justify=tk.RIGHT)
password_confirmation_entry = tk.Entry(root, width=30, font=("Arial", 17), bg="grey", show="*")
password_confirmation_label.grid(row=4, column=0, padx=0, pady=10, sticky=tk.E)
password_confirmation_entry.grid(row=4, column=1, padx=20, pady=10)

# кнопка
def submit():
    username_text = username_entry.get()
    real_name_text = real_name_entry.get()
    password_text = password_entry.get()
    password_confirmation_text = password_confirmation_entry.get()
    if len(username_text) >= min_symbols and len(real_name_text) >= min_symbols and len(password_text) >= min_symbols and password_text == password_confirmation_text:
        messagebox.showinfo("Successful", "You sign up successfuly!")
    else:
        messagebox.showerror("Error", "You have error in entering data!")
    
submit_button = tk.Button(root, text="SUBMIT", command=submit, width=20)
submit_button.config(
    font=("Arial", 14),
    activebackground="grey",      # установка цвета фона кнопки при нажатии
    relief="raised",             # установка внешнего вида рамки кнопки (raised - выступающая, sunken - погруженная)
)
submit_button.grid(row=5, column=0, columnspan=2, pady=30)


root.mainloop()