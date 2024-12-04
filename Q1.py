import tkinter as tk
from tkinter import messagebox
import random
PRESET_PASSWORD = "1234"

def check_password(entry, target_password):
    if entry.get() == target_password:
        messagebox.showinfo("結果", "密碼正確")
    else:
        messagebox.showerror("結果", "密碼錯誤")

def clear_entry(entry):
    entry.delete(0, tk.END)

def create_random_buttons(root, entry):
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    numbers.append(0)
    btn_grid = [[numbers.pop(0) for _ in range(3)] for _ in range(3)]
    btn_grid.append(['C', '', 'OK']) 
    for i, row in enumerate(btn_grid):
        for j, value in enumerate(row):
            if value == "C":
                btn = tk.Button(root, text=value, font=("Arial", 20), command=lambda: clear_entry(entry))
                btn.grid(row=i+1, column=j, sticky=tk.NSEW)
            elif value == "OK":
                btn = tk.Button(root, text=value, font=("Arial", 20), command=lambda: check_password(entry, PRESET_PASSWORD))
                btn.grid(row=i+1, column=j, sticky=tk.NSEW)
            elif value != '':
                btn = tk.Button(root, text=value, font=("Arial", 20),
                                command=lambda val=value: entry.insert(tk.END, str(val)))
                btn.grid(row=i+1, column=j, sticky=tk.NSEW)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("隨機數字鍵盤")
    root.geometry("300x400+200+100") 
    for i in range(4): 
        root.grid_rowconfigure(i, weight=1)
    for i in range(3): 
        root.grid_columnconfigure(i, weight=1)
    entry = tk.Entry(root, font=("Arial", 20), justify="right")
    entry.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
    create_random_buttons(root, entry)
    root.mainloop()
