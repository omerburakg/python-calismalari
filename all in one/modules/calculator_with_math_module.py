import math
import tkinter as tk

print(
    """
*****************************
        HESAP MAKİNESİ
*****************************
"""
)
sonuc = 0


def topla():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        answer.configure(text=str(s1 + s2))


def cikar():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        answer.configure(text=str(s1 - s2))


def carp():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        answer.configure(text=str(s1 * s2))


def bolme():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        answer.configure(text=str(s1 / s2))


window = tk.Tk()
window.title("Hesap Makinesi")
screen_width = window.winfo_screenwidth() // 2 - 240
screen_height = window.winfo_screenheight() // 2 - 300
window.geometry("480x600+{}+{}".format(screen_width, screen_height))

answer = tk.Label(window, text=sonuc, font="Arial 16 bold", width=30, justify="center")
answer.place(x=40, y=40)
sayi1 = tk.Entry(window, font="Arial 16 bold", width=15, justify="right")
sayi1.place(x=150, y=90)
sayi2 = tk.Entry(window, font="Arial 16 bold", width=15, justify="right")
sayi2.place(x=150, y=120)

tus1 = tk.Button(window, text="+", width=10, command=topla)
tus1.place(x=150, y=200)
tus2 = tk.Button(window, text="-", width=10, command=cikar)
tus2.place(x=150, y=250)
tus3 = tk.Button(window, text="*", width=10, command=carp)
tus3.place(x=250, y=200)
tus4 = tk.Button(window, text="/", width=10, command=bolme)
tus4.place(x=250, y=250)
sayi1.focus()
window.mainloop()
