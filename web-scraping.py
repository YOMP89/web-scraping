# Importar las librerías necesarias
# requests: Para hacer solicitudes HTTP a la página web
# BeautifulSoup: Para parsear el contenido HTML
import requests
from bs4 import BeautifulSoup

# Definir la URL de la página web que deseamos scrapear
# Puedes cambiar 'https://example.com' por cualquier otra página
url = 'https://example.com'

# Realizar una solicitud GET a la página web para obtener su contenido
# La función requests.get() devuelve la respuesta del servidor
response = requests.get(url)

# Verificar que la solicitud fue exitosa (el código 200 significa éxito)
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    # El contenido de la respuesta (response.content) se pasa a BeautifulSoup
    # Usamos el parser 'html.parser' para analizar el HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscar todas las etiquetas <h2> en la página web
    # Supongamos que los títulos de los artículos están dentro de etiquetas <h2>
    titles = soup.find_all('h2')

    # Recorrer la lista de títulos y extraer el texto de cada etiqueta <h2>
    # get_text() extrae solo el texto dentro de la etiqueta HTML
    for index, title in enumerate(titles):
        # Mostrar el título de cada artículo en la consola
        print(f"{index + 1}. {title.get_text()}")

else:
    # Si la solicitud no fue exitosa, mostramos el código de error
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
