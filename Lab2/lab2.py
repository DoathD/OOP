import tkinter
from tkinter import messagebox


def final_equal():
    if (type_pizza.get() != 500) and (type_pizza.get() != 700):
        error_choice()
        final_string.set(f"")
        return 0
    if not count.get().isdigit():
        error_count()
        final_string.set(f"")
        return 0
    res = int(count.get()) * (type_pizza.get() + radius_pizza.get() + korka_pizza.get())
    final_string.set(f"Общая стоимость равна {res} руб.")


def error_choice():
    messagebox.showerror("Ошибка", "Выберите тип теста!")


def error_count():
    messagebox.showerror("Ошибка", "Введите целое число!")


win = tkinter.Tk()
win.title("Pizza")
win.geometry("300x300")
win.resizable(False, False)

type_pizza = tkinter.IntVar()
radius_pizza = tkinter.IntVar()
korka_pizza = tkinter.IntVar()
final_string = tkinter.StringVar()

tkinter.Label(win, text="Выберите тип теста").pack()
tkinter.Radiobutton(win, text="Традиционное", variable=type_pizza, value=500).pack()
tkinter.Radiobutton(win, text="Тонкое (+200р)", variable=type_pizza, value=700).pack()

tkinter.Label(win, text="Выберите размер").pack()
tkinter.Radiobutton(win, text="30см", variable=radius_pizza, value=0).pack()
tkinter.Radiobutton(win, text="35см (+250р)", variable=radius_pizza, value=250).pack()
tkinter.Radiobutton(win, text="40см (+500р)", variable=radius_pizza, value=500).pack()

tkinter.Checkbutton(win, text="Чесночно-сырная корочка (+100р)", variable=korka_pizza, offvalue=0, onvalue=100).pack()

tkinter.Label(win, text="Введите количество").pack()
count = tkinter.Entry(win)
count.pack()

tkinter.Button(win, text="Расчёт", command=final_equal).pack()
tkinter.Label(win, textvariable=final_string).pack()

win.mainloop()
