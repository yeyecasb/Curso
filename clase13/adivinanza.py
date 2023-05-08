import random
import tkinter as tk
from tkinter import messagebox

intentos = 0
numero_en_mente = random.randint(1, 100)

def verificar_numero():
    global intentos
    intentos += 1
    numero_ingresado = int(numero_entry.get())
    if numero_ingresado < numero_en_mente:
        resultado_label.config(text=f"El numero buscado es mayor que {numero_ingresado}")
    elif numero_ingresado > numero_en_mente:
        resultado_label.config(text=f"El numero buscado es menor que {numero_ingresado}")
    else:
        messagebox.showinfo('Bien', f'Felicidades, lo lograste en {intentos} intentos')
        reiniciar_juego()

def reiniciar_juego():
    global intentos, numero_en_mente
    intentos = 0
    numero_en_mente = random.randint(1, 100)
    numero_entry.delete(0, tk.END)
    resultado_label.config(text="")

#configuraacion tkinter
ventana = tk.Tk()
ventana.title('Adivinanza de Numeros')

#labels
instrucciones_label = tk.Label(ventana, text="Tengo un numero de 1 a 100, intenta adivinarlo").pack()
resultado_label = tk.Label(ventana)
resultado_label.pack()

#entry
numero_entry = tk.Entry(ventana)
numero_entry.pack()

#boton
verificar_btn = tk.Button(ventana, text="Verificar", command=verificar_numero).pack()

ventana.mainloop()
