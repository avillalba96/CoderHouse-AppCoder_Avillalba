# leeme.md

## INSTALACION INICIAL

- Creamos el proyecto y la aplicacion

```bash
django-admin startproject AppCoder_Avillalba
cd AppCoder_Avillalba
python manage.py startapp MiSitio
```

- Ejecutamos el sitio

```bash
python manage.py runserver
```

- Editamos los archivos necesarios en el orden indicado si queremos agregar mas modulos

```bash
MiSitio/models.py
MiSitio/forms.py
MiSitio/views.py
MiSitio/admin.py
MiSitio/urls.py
MiSitio/templates/example.html
```

- Aplicamos cambios en la DB *(por editar models.py)*

```bash
python manage.py makemigrations
python manage.py migrate
```

