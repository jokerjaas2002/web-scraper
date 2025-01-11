import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la tienda en línea (ejemplo)
url = 'https://bienchicve.com/'

# Realiza la solicitud HTTP
response = requests.get(url)

# Verifica que la solicitud fue exitosa
if response.status_code == 200:
    # Analiza el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra los elementos que contienen la información deseada
    productos = soup.find_all('div', class_='producto')

    # Lista para almacenar los datos
    datos_productos = []

    for producto in productos:
        nombre = producto.find('h2', class_='nombre').text
        precio = producto.find('span', class_='precio').text
        datos_productos.append({'Nombre': nombre, 'Precio': precio})

    # Crea un DataFrame de pandas para organizar los datos
    df = pd.DataFrame(datos_productos)

    # Muestra los datos
    print(df)

else:
    print(f'Error al acceder a la página: {response.status_code}')