from tkinter import *
from tkinter import messagebox

principal = Tk()

principal.title("Primer Ejemplo")
principal.geometry("300x300")
principal.config(bg="#5FB691")

def genera_mensajes():
    messagebox.showinfo("Mensaje", "Hola Mundo")
    messagebox.showerror('Error Fatal', 'El programa se cerrara')

Button(principal, text="Pinchame", command=genera_mensajes).pack(pady=50)

principal.mainloop()