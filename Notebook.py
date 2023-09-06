from tkinter import*
from tkinter import messagebox
from tkinter import ttk

def add_button_click():

    title = title_entry.get()
    name = name_entry.get()
    issue = issue_entry.get()
    age = age_entry.get()


    is_ok = messagebox.askokcancel(title="Website", message=f"Эти данные введены: \nНазвание:{title} \nАвтор:{name}\nИздательство:{issue} \nГод:{age} \nВсе правильно?")
    saved_text = f"{title} /{name} /{issue} /{age}\n"

    if is_ok:
        with open("КнигииАниме.txt", mode="a") as file:
            file.write(saved_text)
        title_entry.delete(0, END)
        name_entry.delete(0, END)
        issue_entry.delete(0, END)
        age_entry.delete(0, END)

window = Tk()
window.title("Архив")

window.config(padx=50, pady=50, bg="white")

title_lab = Label(text="Название:", bg="white", fg="black", highlightthickness=0)
title_lab.grid(row=1, column=0)

name_lab = Label(text="Автор:", bg="white", fg="black", highlightthickness=0)
name_lab.grid(row=2, column=0)

issue_lab = Label(text="Издательство:", bg="white", fg="black", highlightthickness=0)
issue_lab.grid(row=3, column=0)

age_lab = Label(text="Год:", bg="white", fg="black", highlightthickness=0)
age_lab.grid(row=4, column=0)

title_entry = Entry(width=36, bg="white", fg="black", highlightthickness=0, insertbackground="black")
title_entry.grid(row=1, column=1, columnspan=2)
title_entry.focus()
name_entry = Entry(width=36, bg="white", fg="black", highlightthickness=0, insertbackground="black")
name_entry.grid(row=2, column=1, columnspan=2)

issue_entry = Entry(width=19, bg="white", fg="black", highlightthickness=0, insertbackground="black")
issue_entry.grid(row=3, column=1)
age_entry = Entry(width=19, bg="white", fg="black", highlightthickness=0, insertbackground="black")
age_entry.grid(row=4, column=1)

add_button = Button(text="Add", width=33, bg="grey", highlightthickness=0, highlightbackground="white", command=add_button_click)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()