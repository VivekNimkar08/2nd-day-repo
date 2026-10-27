import tkinter as tk
from time import strftime


def update_clock():
    clock_label.config(text=strftime("%H:%M:%S"))
    clock_label.after(1000, update_clock)


window = tk.Tk()
window.title("Digital Clock")
window.configure(bg="black")

clock_label = tk.Label(
    window,
    font=("Arial", 48, "bold"),
    bg="black",
    fg="lime",
)
clock_label.pack(padx=30, pady=20)

update_clock()
window.mainloop()