import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Заказ")

def select_item():
    selected_item = combobox.get()
    selection_label.config(text=f"Выбрано: {selected_item}, руб")
items = {"Минет":100, "Анал":50, "Камшот":10, "Классика":30}

combobox = ttk.Combobox(root, values=list(items.items()))
selection_label = ttk.Label(root)
select_button = ttk.Button(root, text="Заказать", command=select_item)

combobox.pack()
selection_label.pack()
select_button.pack()

root.mainloop()