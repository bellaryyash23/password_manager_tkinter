from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_output.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        web_input.get(): {
            "email": username_input.get(),
            "password": password_output.get()
        }
    }

    if len(web_input.get()) == 0 or len(password_output.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty !")

    # Method to add and save data to data.txt file. Later version updated to use data in json format.
    # The use of json to stored data in data.json file allows for effective searching and storage than a txt file.
    # else:
    #     is_ok = messagebox.askokcancel(title=f"{web_input.get()}",
    #                                    message=f"You have entered these details:\nEmail: {username_input.get()}\n"
    #                                    "Password:{password_output.get()}\nClick OK to add.")
    #       if is_of:
    #           with open("data.txt", "a") as data:
    #     #        data.write(f"{web_input.get()} | {username_input.get()} | {password_output.get()} \n")

    else:
        try:
            with open("data.json", "r") as data:
                # Reading old data
                old_data = json.load(data)
                # Update old data
                old_data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            with open("data.json", "w") as data:
                # Saving updated data
                json.dump(old_data, data, indent=4)

        web_input.delete(0, END)
        password_output.delete(0, END)
        web_input.focus()


# --------------------------- Search Password ------------------------- #

def search_password():
    find_website = web_input.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        try:
            email = data[find_website]["email"]
            password = data[find_website]["password"]
        except KeyError:
            messagebox.showwarning(title="Error", message="No Details for Website exist !")
        else:
            is_ok = messagebox.askokcancel(title=f"{find_website}",
                                           message=f"E-Mail: {email}\nPassword: {password}")
            if is_ok:
                pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

web_input = Entry(width=18)
web_input.grid(row=1, column=1)
web_input.focus()

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)

username_input = Entry(width=36)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "yash@email.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_output = Entry(width=18)
password_output.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", width=14, command=generate_password)
generate_btn.grid(row=3, column=2)

search_btn = Button(text="Search", width=14, command=search_password)
search_btn.grid(row=1, column=2)

add_btn = Button(text="Add", width=31, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
