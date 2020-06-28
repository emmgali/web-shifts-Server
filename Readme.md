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

### Migración a PostgreSQL

La base que se usa en heroku ya está cambiada a PostgreSQL. Asique mucho ojo con pegarle porque toda la información ahora persiste.
Para DEVELOP se sigue usando SQLite, ya que es más facil seguir trabajando así que obligarlos a instalar y levantar un servidor de postgres en local.

Para acceder de manera remota al bash de la base de heroku, seguir esta guia: https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

Para correr scripts que modifiquen la base de datos, contactar a @Trekkar. Si se quiere modificar la base y **no interesa borrarla toda y levantarla limpia de nuevo**, entonces agregar el script de cración en la carpeta *migrations*, pushear, y luego pegarle a la api por medio del *endpoint para reiniciar la base*
