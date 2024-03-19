import tkinter as tk
from tkinter import messagebox
import requests

def buscar_productos():
    # Obtiene el término de búsqueda ingresado por el usuario
    termino_busqueda = entry_busqueda.get()
    
    # URL de la API de Mercado Libre para buscar productos
    url = f'https://api.mercadolibre.com/sites/MLA/search?q={termino_busqueda}'
    
    try:
        # Realiza la solicitud GET a la API de Mercado Libre
        response = requests.get(url)
        data = response.json()
        
        # Muestra los resultados en una ventana de mensaje
        messagebox.showinfo("Resultados", f"Se encontraron {len(data['results'])} productos.")
        
        # Muestra los títulos de los productos encontrados en la consola
        for producto in data['results']:
            print(producto['title'])
    
    except Exception as e:
        # Muestra un mensaje de error si ocurre algún problema con la solicitud
        messagebox.showerror("Error", f"Ocurrió un error al buscar productos: {str(e)}")

# Crea la ventana principal
root = tk.Tk()
root.title("Búsqueda de Productos en Mercado Libre")

# Crea un cuadro de entrada para que el usuario ingrese el término de búsqueda
entry_busqueda = tk.Entry(root, width=50)
entry_busqueda.pack(pady=10)

# Crea un botón para iniciar la búsqueda de productos
btn_buscar = tk.Button(root, text="Buscar Productos", command=buscar_productos)
btn_buscar.pack()

# Ejecuta el bucle principal de la aplicación
root.mainloop()
