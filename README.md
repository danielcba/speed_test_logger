
# Speed Test Logger

Este script en Python utiliza la biblioteca `speedtest` para medir la velocidad de Internet y guardar los resultados en un archivo CSV. Es ideal para monitorear el rendimiento de tu conexión a lo largo del tiempo.

## Características

- Realiza pruebas de velocidad de descarga, subida y latencia (ping).
- Selecciona automáticamente el servidor con mejor latencia.
- Guarda los resultados en un archivo CSV con formato estructurado.

## Requisitos

- Python 3.7 o superior
- Bibliotecas necesarias:
  - `speedtest`
  - `csv` (incluida en la instalación de Python)
  - `os` (incluida en la instalación de Python)

Para instalar la biblioteca `speedtest`, ejecuta:

```bash
pip install speedtest-cli
```

## Uso

1. Descarga o clona este repositorio.
2. Ejecuta el script:

```bash
python speed_test_logger.py
```

3. Los resultados se guardarán automáticamente en el archivo `speedtest_results.csv`.

## Estructura del archivo CSV

El archivo contiene las siguientes columnas:

| Columna          | Descripción                                           |
|-------------------|-------------------------------------------------------|
| Server ID         | Identificador único del servidor                     |
| Sponsor           | Nombre del patrocinador del servidor                 |
| Server Name       | Nombre del servidor                                  |
| Timestamp         | Fecha y hora de la prueba                            |
| Distance          | Distancia al servidor (en km)                        |
| Ping              | Latencia en milisegundos (ms)                        |
| Download          | Velocidad de descarga (en bits/s)                    |
| Upload            | Velocidad de subida (en bits/s)                      |
| Share             | URL para compartir los resultados                    |
| IP Address        | Dirección IP del cliente                             |

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, por favor abre un issue o un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
