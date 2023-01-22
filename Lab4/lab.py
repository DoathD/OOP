import tkinter as tk
from tkinter import ttk


def change_Cbutton():
    if delivery.get():
        delivery_out["text"] = "Курьер до двери"
    elif not delivery.get():
        delivery_out["text"] = "Самовывоз"


def update_city(event):

    city = event.widget.get()
    city_out["text"] = f"Город {city}"

win = tk.Tk()
win.title("Lab4")
win.geometry("300x300")
win.resizable(False, False)

city = "Новосибирск"
delivery_out = tk.Label(win, text="Самовывоз")
city_out = tk.Label(win, text=f"Город {city}")

# Город
tk.Label(win, text="Выберите город").pack()
combo = ttk.Combobox(win,
                     values=[
                         "Новосибирск",
                         "Москва",
                         "Санкт-Петербург",
                         "Владивосток"])
combo.pack()
combo.bind("<<ComboboxSelected>>", update_city)

# Доставка
delivery = tk.IntVar()
tk.Checkbutton(win, text="Доставка до двери", variable=delivery, offvalue=False, onvalue=True,
               command=change_Cbutton).pack()

# Имя
name_out= tk.StringVar()
tk.Label(win, text="Ваше Имя").pack()
name = tk.Entry(win,textvariable=name_out)
name.pack()

# Вывод Итого
tk.Label(win, text="Итого:").pack()
city_out.pack()
delivery_out.pack()
tk.Label(win, textvariable=name_out).pack()

win.mainloop()
