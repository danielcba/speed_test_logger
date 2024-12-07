import speedtest  # Biblioteca para realizar pruebas de velocidad de red
import csv  # Biblioteca para manejar archivos CSV
import os  # Biblioteca para interactuar con el sistema de archivos


def test_speed():
    """
    Realiza la prueba de velocidad de Internet utilizando la biblioteca speedtest.

    Retorna:
        dict: Diccionario con los resultados de la prueba, incluyendo velocidad de 
        descarga, subida, latencia (ping) y detalles del servidor.
    """
    s = speedtest.Speedtest(
        secure=True)  # Inicializa el objeto Speedtest con conexión segura
    s.get_servers()  # Descarga la lista de servidores disponibles
    s.get_best_server()  # Selecciona el servidor con mejor latencia
    s.download()  # Ejecuta la prueba de velocidad de descarga
    s.upload()  # Ejecuta la prueba de velocidad de subida
    results = s.results.dict()  # Obtiene los resultados en formato de diccionario
    return results


def save_results_to_csv(filename, data):
    """
    Guarda los resultados de la prueba de velocidad en un archivo CSV.

    Parámetros:
        filename (str): Nombre del archivo CSV donde se guardarán los resultados.
        data (dict): Diccionario con los datos de la prueba de velocidad.

    Notas:
        - Si el archivo no existe, se agrega un encabezado con las columnas.
        - Los valores nulos se manejan para evitar errores al escribir los datos.
    """
    # Verifica si el archivo ya existe en el sistema
    file_exists = os.path.isfile(filename)

    # Abre el archivo en modo "a" (append), permitiendo agregar datos al final
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Escribe el encabezado si el archivo es nuevo
        if not file_exists:
            writer.writerow([
                "Server ID", "Sponsor", "Server Name", "Timestamp", "Distance",
                "Ping", "Download", "Upload", "Share", "IP Address"
            ])

        # Escribe una fila con los resultados de la prueba, manejando valores nulos
        writer.writerow([
            data.get("server", {}).get("id", ""),  # ID del servidor
            data.get("server", {}).get("sponsor", ""),  # Patrocinador
            data.get("server", {}).get("name", ""),  # Nombre del servidor
            data.get("timestamp", ""),  # Fecha y hora de la prueba
            data.get("server", {}).get("d", ""),  # Distancia al servidor
            data.get("ping", ""),  # Latencia en ms
            data.get("download", ""),  # Velocidad de descarga en bits/s
            data.get("upload", ""),  # Velocidad de subida en bits/s
            data.get("share", ""),  # URL para compartir los resultados
            data.get("client", {}).get("ip", ""),  # Dirección IP del cliente
        ])


# Ejecuta la prueba de velocidad
print("Realizando prueba de velocidad...")
results = test_speed()

# Guarda los resultados en un archivo CSV
print("Guardando resultados en 'speedtest_results.csv'...")
save_results_to_csv("speedtest_results.csv", results)
print("Resultados guardados exitosamente.")
