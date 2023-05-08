from tkinter import *
from tkinter import messagebox

principal = Tk()

principal.title("Preguntas")
principal.geometry("300x200")
principal.config(bg="green")

def preguntas():
    respuesta = messagebox.askquestion("Pregunta", "Te gustan los perritos?")
    if respuesta == "yes":
        messagebox.showinfo("Respuesta", "Excelente")
    elif respuesta == "no":
        messagebox.showinfo("Respuesta", "Lo siento")
    else:
        messagebox.showwarning('respuesta', 'Ingresa una respuesta valida')

Button(principal, text="Pinchar aquí", command=preguntas).pack(pady=20)

principal.mainloop()