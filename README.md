# Web Scraping con BeautifulSoup

## Descripción
Este script de **web scraping** utiliza **Python** junto con la librería **BeautifulSoup** para obtener datos de una página web. En este caso, se extraen los títulos de los artículos que están dentro de las etiquetas `<h2>`. Se hace una solicitud HTTP a la página, se parsea el contenido HTML y se extrae la información deseada.

## Librerías Utilizadas
- **requests**: Se usa para hacer solicitudes HTTP y obtener el contenido de la página web.
- **BeautifulSoup** (del módulo `bs4`): Para parsear el HTML y navegar por los elementos del documento.

## Instalación
Las librerías necesarias se pueden instalar con el siguiente comando:

```bash
pip install requests beautifulsoup4
