# API para Códigos postales de España

Sencilla API para obtener información de los códigos postales de España. Obteniendo información como:

- Código postal.
- Población.
- Latitud.
- Longitud.

## Llamadas

### Obtener todos los datos de un código postal

``` bash
localhost/api/v1/postal_code/{numero}
```

Ejemplo

``` bash
curl localhost/api/v1/postal_code/46017
```

``` json
[
  {
    "index": 461021,
    "postal_code": 46017,
    "poblacion": "Santa Margarida de Montbui",
    "lat": 41.55659597,
    "lng": 1.60489809
  },
  {
    "index": 461022,
    "postal_code": 46017,
    "poblacion": "Pampliega",
    "lat": 42.20619881,
    "lng": -3.98797885
  },
  {
    "index": 461023,
    "postal_code": 46017,
    "poblacion": "Villanueva de Guadamejud",
    "lat": 40.22470982,
    "lng": -2.50703229
  },
  ...
]
```

### Obtener por index (indice)

``` bash
curl localhost/api/v1/index/{indice}
```

Ejemplo

``` bash
curl localhost/api/v1/index/461021
```

``` json
[
  {
    "index": 461021,
    "postal_code": 46017,
    "poblacion": "Santa Margarida de Montbui",
    "lat": 41.55659597,
    "lng": 1.60489809
  }
]
```

## Instalación

```bash
pipenv install
pipenv shell
```

Después solo debes arrancarlo.

```bash
python3 app.py
```
