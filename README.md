![Banner](https://github.com/SosaDevLab/.github/blob/main/profile/assets/banner.png?raw=true)

# ¿Qué es una API?

[Link del video](https://www.youtube.com/)

## Preparación del entorno

> **Nota:** El paso a paso de todas maneras lo iré explicando en el video.

Para poder seguir este tutorial necesitas tener instalado Python y algun editor de texto. En mi caso voy a usar Visual Studio Code.

### Instalación de Python

Para instalar Python debes instalarlo desde la página oficial de Python. [Link de descarga](https://www.python.org/downloads/)

### Instalación de Visual Studio Code

Para instalar Visual Studio Code debes instalarlo desde la página oficial de Visual Studio Code. [Link de descarga](https://code.visualstudio.com/)

## Cómo ejecutar el programa

> **Nota:** El paso a paso de todas maneras lo iré explicando en el video.

Para ejecutar el programa debes abrir una terminal y ejecutar el siguiente comando:

```bash
git clone https://github.com/SosaDevLab/api-example.git
cd api-example
```

Luego debes ejecutar el siguiente comando:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Finalmente debes ejecutar el siguiente comando:

```bash
python api.py
```

Y para el cliente debes ir al navegador y escribir la siguiente URL:

```bash
http://{la-ruta-de-tu-archivo}/client.html
# Ejemplo http://Repos/youtube/client.html
```
