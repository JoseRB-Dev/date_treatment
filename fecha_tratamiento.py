import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta


def calcular_fecha():
    fecha_inicio = entry_fecha.get_date()
    unidad = combo_unidad.get()
    cantidad_str = entry_cantidad.get()

    try:
        cantidad = int(cantidad_str)
    except ValueError:
        messagebox.showerror(
            "Error", "⚠️ Introduce un número entero para la duración.")
        return

    if unidad == "Días":
        delta = timedelta(days=cantidad)
    elif unidad == "Semanas":
        delta = timedelta(weeks=cantidad)
    else:
        messagebox.showerror(
            "Error", "⚠️ Selecciona una unidad de tiempo válida.")
        return

    fecha_fin = fecha_inicio + delta
    texto_resultado = f"✅ El tratamiento finaliza el {fecha_fin.strftime('%d-%m-%Y')}."
    resultado.set(texto_resultado)


def copiar_resultado():
    ventana.clipboard_clear()
    ventana.clipboard_append(resultado.get())
    ventana.update()  # Para que el portapapeles se actualice correctamente
    messagebox.showinfo("Copiado", "📋 Resultado copiado al portapapeles.")


def limpiar_campos():
    entry_fecha.set_date(datetime.today())
    entry_cantidad.delete(0, tk.END)
    combo_unidad.current(0)
    resultado.set("")


# Crear ventana
ventana = tk.Tk()
ventana.title("🩺 Calculadora de Tratamiento")
ventana.geometry("400x320")

# Variables
resultado = tk.StringVar()

# Widgets
tk.Label(ventana, text="📅 Fecha de inicio:").pack(pady=5)
entry_fecha = DateEntry(ventana, date_pattern='dd-mm-yyyy', locale='es_ES')
entry_fecha.pack()

tk.Label(ventana, text="⏱️ Unidad de duración:").pack(pady=5)
combo_unidad = ttk.Combobox(ventana, values=["Días", "Semanas"])
combo_unidad.pack()
combo_unidad.current(0)  # "Días" por defecto

tk.Label(ventana, text="💊 Cantidad:").pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Button(ventana, text="Calcular Fecha de Fin",
          command=calcular_fecha).pack(pady=10)
tk.Label(ventana, textvariable=resultado,
         font=("Arial", 10, "bold")).pack(pady=5)

tk.Button(ventana, text="📋 Copiar Resultado",
          command=copiar_resultado).pack(pady=5)
tk.Button(ventana, text="🧹 Limpiar", command=limpiar_campos).pack(pady=5)

# Iniciar loop
ventana.mainloop()
