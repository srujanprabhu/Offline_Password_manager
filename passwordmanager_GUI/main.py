import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for y in range(nr_symbols)]
    password_num = [random.choice(numbers) for z in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_num

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_in_file():
    website_entry_val = website_entry.get()
    email_entry_val = email_entry.get()
    password_entry_val = password_entry.get()
    new_data = {
        website_entry_val: {
            "email": email_entry_val,
            "password": password_entry_val
        }
    }

    if len(website_entry_val) and len(password_entry_val) > 0:

        is_ok = messagebox.askokcancel(title=website_entry_val, message=f"These are the details entered: \nWebsite: {website_entry_val}\nEmail: {email_entry_val}\nPassword: {password_entry_val} \nIs it Ok to save?")
        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except json.JSONDecodeError:
                # Handle the case where the file is empty
                with open("passwords.json", "w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)

                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

    else:
        messagebox.showinfo(title="Enter something")

# ---------------------------- SEARCH JSON FOR PASSWORDS ------------------------------- #
def search():
    website_entry_val = website_entry.get()
    try:
        with open("passwords.json", 'r') as file:
            data = json.load(file)

            if website_entry_val in data:
                item = data[website_entry_val]
                email = item.get("email")
                passw = item.get("password")
                messagebox.showinfo(title="hey", message=f"FOUND!\nEmail - {email}\nPassword - {passw}")

            elif website_entry_val not in data:
                messagebox.showinfo(title="hey", message="No details found, sorry")

    except:
        messagebox.showinfo(title="hey", message="No data available!\nAdd some")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(600, 600)
window.title("Password Manager")
window.config(padx=20, pady=20, bg="light pink")
window.grid()
canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(10, 10, image=myimg, anchor='nw')
# canvas.grid(row=0,column=1)
canvas.place(x=175, y=10)
website_label = Label(text="Website", font=("Courier", 10))
website_label.place(x=30, y=250)
email_label = Label(text="Email/Username", font=("Courier", 10))
email_label.place(x=30, y=280)
password_label = Label(text="Password", font=("Courier", 10))
password_label.place(x=30, y=310)

# Entries
website_entry = Entry(width=35)
website_entry.place(x=180, y=250)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.place(x=180, y=280)
password_entry = Entry(width=35)
password_entry.place(x=180, y=310)

# buttons
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.place(x=220, y=350)
add_button = Button(text="Add", width=10, command=save_in_file)
add_button.place(x=420, y=310)
search_button = Button(text="search", width=10, height=1, command=search)
search_button.place(x=420, y=250)

window.mainloop()
