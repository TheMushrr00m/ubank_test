# Test API

Para inciializar la Base de datos es necesario acceder desde una sesión interactiva en la consola de Python y ejecutar los siguientes comandos.

```
>>> from api.infraestructure.database import database
>>> database.db.connect()
True
>>> from api.domain.models.user import User
>>> User.create_table(True)
>>> database.db.close()
```
## Iniciar el API
```
$ gunicorn -c gunicorn_cfg.py api.application:app.api
```

### El API cuenta con los siguientes endpoints

```
/
    GET
/users
    GET
    POST
/users/:id
    GET
    PATCH
    DELETE
```

#### GET /
Devuelve el estado del API (verificar que el servicio se encuentra activo)
```
{
    "status": "Running correctly"
}
```


#### GET /users
Devuelve una lista de registros en la DB.
```
[
    {
        "active": true,
        "some_date": "2018-08-09",
        "id": 2,
        "name": "Gabo",
        "description": "Admin",
        "age": 23,
        "email": "admin@gcueto.com"
    },
    {
        "active": true,
        "some_date": "2018-08-09",
        "id": 3,
        "name": "John Doe",
        "description": "Admin",
        "age": 23,
        "email": "john@gcueto.com"
    }
]
```

#### POST /users
Crea un nuevo registro en la DB y lo devuelve en la respuesta. Ejemplo de payload para request:
```
{
	"name": "John Doe",
	"email": "john@gcueto.com",
	"description": "Admin",
	"age": 23,
	"some_date": "2018-08-09",
	"some_datetime": "2018-08-09T21:59:00.019077+00:00"
}
```

#### GET /users/:id
Devuelve un registro en especifico

```
{
    "active": true,
    "some_date": "2018-08-09",
    "id": 2,
    "name": "Gabo",
    "description": "Admin",
    "age": 23,
    "email": "admin@gcueto.com"
}
```
#### PATCH /users/:id
Modifica información de un registro y devuelve:
```
{
    "updated_rows": 1
}
```
#### DELETE /users/:id
Elimina un registro y devuelve:
```
{
    "deleted_rows": 1
}
```