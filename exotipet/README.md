# sandbox

Pasos de configuracion:

1. Crea entorno virtual propio:
En la carpeta i+d+i_exotipet/exotipet

Remove-Item -Recurse -Force venv
rmdir /S /Q venv

2. Crea un Nuevo Entorno Virtual:
python -m venv venv

3. Activa el Nuevo Entorno Virtual: 
.\venv\Scripts\activate

4. Instala las Dependencias desde requirements.txt
pip install -r requirements.txt

5. Crear base de datos
Usar el archivo veterinaria.sql para la BD

6. Cambiar información de conexión en config.py
Cambiar de acuerdo a usuario y clave




Cambiar Interprete

1. Abre la paleta de comandos:

Presiona Ctrl + Shift + P (o Cmd + Shift + P en Mac) para abrir la paleta de comandos.

Busca y selecciona “Python: Select Interpreter”:

2. Escribe Python: Select Interpreter y selecciónalo en la lista.