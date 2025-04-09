import tkinter as tk
import random
import string

def generate ():
    length = int(spinbox.get())
    numbers = var1.get()
    special = var2.get()
    spaces = var3.get()
    
    characters = string.ascii_letters

    if special:
        characters += string.punctuation
    if spaces:
        characters += ' '
    if numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for i in range(length))
    textbox.delete(0, tk.END)
    textbox.insert(0, password)







root = tk.Tk()
root.geometry("500x200")
root.title("Cписок дел")

spinbox_var = tk.StringVar(value=7)

spinbox = tk.Spinbox(from_=1.0, to=100.0, textvariable=spinbox_var)
spinbox.pack(pady=10)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

checkbox1 = tk.Checkbutton(root, text='Включять цифры', variable=var1)
checkbox1.pack()
checkbox1 = tk.Checkbutton(root, text='Включять спец символы', variable=var2)
checkbox1.pack()
checkbox1 = tk.Checkbutton(root, text='Включять пробелы', variable=var3)
checkbox1.pack()

add_button = tk.Button(root, text="Сгенерировать", command=generate)
add_button.pack(pady=20)

textbox = tk.Entry(root, font=("Arial", 14))
textbox.pack(pady=5)

root.mainloop()