import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("250x150")
root.title("Подсчет слов и символов")

def lenght():
    sentence = sentence_entry.get("1.0", "end-1c")
    words = len(sentence.split())
    characters = len(sentence)
    words_label.config(text=f"Количество слов: {words}")
    characters_label.config(text=f"Количество символов: {characters}")

sentence_entry = tk.Text(root, height=3, wrap="word")
words_label = ttk.Label(root)
characters_label = ttk.Label(root)
count_button = ttk.Button(root, text="Подсчитать", command=lenght)

sentence_entry.pack()
words_label.pack()
characters_label.pack()
count_button.pack()

root.mainloop()
