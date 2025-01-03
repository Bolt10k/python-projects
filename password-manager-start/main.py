from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    pass_word_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = pass_word_letters+password_numbers+password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    # password =""
    # for char in password_list:
    #     password+=char
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website =website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message = "You left an field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"these details entered: \n Email:{email}"
                                                             f"\nPassword:{password} \n Is ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Add the logo image
logo_img = PhotoImage(file='logo.png')  # Ensure 'logo.png' is in the same directory
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website input
website_label = Label(text='Website')
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email/username input
email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,'ankitdongare2004@gmail.com')

# Password input
password_label = Label(text='Password')
password_label.grid(row=3, column=0)


password_input = Entry(width=35)  # Adjusted width to align with other fields
password_input.grid(column=1, row=3, columnspan=2)


# Generate Password button
generate_password = Button(text='Generate Password',command=generate_pass)
generate_password.grid(column=2, row=3, sticky="E")  # Button stays aligned to the right

# Add button
add_button = Button(text='Add', width=36,command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Run the main loop
window.mainloop()





