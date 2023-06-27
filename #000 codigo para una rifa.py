#ultimo codigo generado


import random
import tkinter as tk
from datetime import datetime, timedelta

numeros_disponibles = list(range(1, 101))
numeros_vendidos = []

costo_tiquete = 1

def vender_tiquete():
    numero = int(entry_numero.get())
    if numero in numeros_disponibles:
        numeros_disponibles.remove(numero)
        numeros_vendidos.append(numero)
        label_mensaje.config(text=f"El tiquete número {numero} ha sido vendido.")
        label_monto_recolectado.config(text=f"Monto recolectado: ${len(numeros_vendidos) * costo_tiquete}")
        actualizar_tabla()
    else:
        label_mensaje.config(text=f"Lo siento, el tiquete número {numero} ya ha sido vendido o no está disponible.")

def realizar_sorteo():
    if len(numeros_vendidos) == 0:
        label_mensaje.config(text="No se pueden realizar el sorteo ya que no se han vendido tiquetes.")
    else:
        ganador = random.choice(numeros_vendidos)
        label_mensaje.config(text=f"El ganador del sorteo es el tiquete número {ganador}.")

def actualizar_tabla():
    for i in range(10):
        for j in range(10):
            numero = i * 10 + j + 1
            if numero in numeros_vendidos:
                tabla[i][j].config(bg="red", text=str(numero))
            else:
                tabla[i][j].config(bg="green", text=str(numero))

def actualizar_temporizador():
    fecha_sorteo = datetime.strptime(entry_fecha_sorteo.get(), "%Y-%m-%d %H:%M:%S")
    tiempo_restante = fecha_sorteo - datetime.now()
    dias, segundos_restantes = tiempo_restante.days, tiempo_restante.seconds
    horas = segundos_restantes // 3600
    minutos = (segundos_restantes // 60) % 60
    segundos = segundos_restantes % 60
    label_temporizador.config(text=f"Tiempo restante: {dias} días {horas} horas {minutos} minutos {segundos} segundos")
    root.after(1000, actualizar_temporizador)

root = tk.Tk()
root.title("Rifa")

label_numero = tk.Label(root, text="Número a jugar:")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

button_vender = tk.Button(root, text="Vender tiquete", command=vender_tiquete)
button_vender.pack()

button_sorteo = tk.Button(root, text="Realizar sorteo", command=realizar_sorteo)
button_sorteo.pack()

frame_tabla = tk.Frame(root)
frame_tabla.pack()

tabla = []
for i in range(10):
    fila = []
    for j in range(10):
        label_numero = tk.Label(frame_tabla, text=str(i * 10 + j + 1), bg="green", width=3)
        label_numero.grid(row=i, column=j)
        fila.append(label_numero)
    tabla.append(fila)

label_fecha_sorteo = tk.Label(root, text="Fecha del sorteo (YYYY-MM-DD HH:MM:SS):")
label_fecha_sorteo.pack()

entry_fecha_sorteo = tk.Entry(root)
entry_fecha_sorteo.pack()

label_temporizador = tk.Label(root, text="")
label_temporizador.pack()

root.after(1000, actualizar_temporizador)

label_monto_recolectado = tk.Label(root, text=f"Monto recolectado: $0")
label_monto_recolectado.pack()

label_mensaje = tk.Label(root, text="")
label_mensaje.pack()

root.mainloop()







































