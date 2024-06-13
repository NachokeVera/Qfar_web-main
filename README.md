Comandos en la terminal.
1.- para arrancar la pagina web hay que crear el entorno virtual de python:
-python -m venv env

2.- posterior entrar al entorno virtual:
- .\env\Scripts\activate

3.- instalar las dependencias (si no se instalan estan todas en los requiremts.txt)
- pip install -r requirements.txt
(sino es )
- pip install 'La_dependencia_correspondiente'

4.- migrar la base de datos:
-python manage.py migrate
5.- y ejecutar!
-python manage.py runserver

