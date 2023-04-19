import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    pw_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_item():
    website = website_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    is_okay = messagebox.askokcancel(title="Website", message="Confirm saving?")
    if is_okay:
        try:
            with open("data.json", "r") as file:
                # Read data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Create data file
                json.dump(new_data, file, indent=4)
        else:
            # Amend data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Write data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            pw_entry.delete(0, tk.END)

# ---------------------------- Search --------------------------------- #
def search():
    website = website_entry.get()
    found = False
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                found = True
    except FileNotFoundError:
        pass

    print(found, website, data)
    if found:
        email = data[website]['email']
        password = data[website]['password']
        messagebox.showinfo("Found", f"Email: {email}\n Password: {password}")
    else:
        messagebox.showinfo("Not Found", f"Website not found")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email:")
email_label.grid(row=2, column=0)
pw_label = tk.Label(text="Password:")
pw_label.grid(row=3, column=0)

# Entry
website_entry = tk.Entry(width=30)
website_entry.grid(row=1, column=1)
# Get the cursor to the location at start
website_entry.focus()

email_entry = tk.Entry(width=30)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "yuangreg@hotmail.com")

pw_entry = tk.Entry(width=30)
pw_entry.grid(row=3, column=1)

# Button
generate_search_botton = tk.Button(text="Search", width=14, command=search)
generate_search_botton.grid(row=1, column=3)
generate_pw_botton = tk.Button(text="Generate Password", command=generate_password)
generate_pw_botton.grid(row=3, column=3)
add_button = tk.Button(text="Add Password to Store", width=52, command=add_item)
add_button.grid(row=4, column=0, columnspan=4)



window.mainloop()
