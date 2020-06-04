# Web Shifts Server


Para el correcto setteo lean el blog de miguelito:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Tecnicamente lo unico que necesitan es crear la carpeta VENV y configurar su terminal para que les tome los comandos.

### Crear el virtual environment

Pararse en el proyecto. O sea, al mismo nivel que app, main. Luego, en la terminal escribir:

`python3 -m venv venv` (puede ser _py_ o _python_ en lugar de _python3_ según cada instalación)

El comando previo les deberia crear la carpeta VENV y todo lo que contiene. Ahora hace falta setearlo:

- en terminal linux: `source venv/bin/activate`
- en terminal windows: `venv\Scripts\activate`

El comando les deberia cambiar la consola y crarles un ambiente, tipo asi: `(venv) $ _`

### Instalar flask y todas las bibliotecas que utiliza la aplicación

Ejecutar los siguientes comandos en la consola (dentro del _venv_):

```
pip install flask
pip install flask-cors
pip install flask-sqlalchemy
pip install flask-migrate
```

### Correr las migraciones de la base de datos

`flask db upgrade`

### Setear variables de environment

Lo siguiente es necesario si desean correr el server en el environment _development_

- en windows (powershell): `$env:FLASK_ENV = "development"`
- en linux: `export FLASK_ENV=development`

### Levantar el server local

`flask run`

