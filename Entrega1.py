#Programa: "Busca el Tesoro"

#Usariamos el random para crear una coordenada nueva para el usuario cada juego (cuando cierre el programa)

#Este programa permite al usuario intentar encontrar un tesoro 
#escondido dentro de una cuadrícula (tablero) de tamaño definido.

#El tablero se representa con una lista de listas (una matriz).

#Las coordenadas del tesoro se guardan en un archivo de texto
#llamado "tesoro.txt". El programa usa estructuras de control como:

# if / elif / else para dar pistas sobre la ubicación (ejemplo: mas a la derecha o 10 unidades abajo)

# while para repetir los intentos hasta encontrar el tesoro 

#También usa funciones para organizar el código:

#  crear_archivo_tesoro(): crea el archivo con las coordenadas.
#  cargar_tesoro(): lee las coordenadas desde el archivo.
#  dibujar_tablero(): muestra el tablero en pantalla.
#  verificar_intento(): da pistas según la posición del intento.

#EXTRAA: Como se menciona al comienzo de los comentarios,
#pensamos implementar el import random para hacer más automatico el juego.

#CODIGO

#CONFIGURACIÓN GLOBAL
tamaño_tablero = 5
archivo_coordenadas = "tesoro.txt"
#Coordenadas del tesoro (fila, columna)
coordenadas_secretas = (4, 2)


#FUNCIONES AUXILIARES
#Esta funcion directamente escribe y crea el archivo de texto automaticamente
#sin que el jugador tenga que crearlo y ingresar las coordenadas a mano.
def crear_archivo_tesoro(nombre_archivo, coordenadas):
    """Crea el archivo donde se guardan las coordenadas del tesoro."""
    try:
        # Abre el archivo en modo escritura ('w')
        with open(nombre_archivo, 'w') as archivo:
            linea = f"{coordenadas[0]},{coordenadas[1]}\n"
            archivo.write(linea)
        print(f"Archivo '{nombre_archivo}' creado correctamente.")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

#Lee las coordenadas del teroso ubicadas en el archivo de texto. 
def cargar_tesoro(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            linea = archivo.readline().strip()

        if "," in linea:
            fila_str, col_str = linea.split(',')
            return (int(fila_str), int(col_str))
        else:
            return None
    except Exception as e:
        print(f"Ocurrió un error al cargar el tesoro: {e}")
        return None

#Dibuja el tablero en el consola de python. 
def dibujar_tablero(tablero):
    print("\n--- TABLERO DE JUEGO ---")
    print("   ", end="")
    for i in range(len(tablero[0])):
        print(f" {i}", end="")
    print(" (Columnas)")

    for i, fila in enumerate(tablero):
        print(f"{i} |", end="")
        for celda in fila:
            print(f" {celda}", end="")
        print(" |")
    print("(Filas)--------------------------")

#Sirve para verificar el intento y ayuda al jugador dandole una pisa.
def verificar_intento(intento_f, intento_c, tesoro_f, tesoro_c):
    if intento_f == tesoro_f and intento_c == tesoro_c:
        return True

    print("Pista:", end=" ")

    #Pistas verticales
    if intento_f < tesoro_f:
        print("Baja (el tesoro está más abajo).", end=" ")
    elif intento_f > tesoro_f:
        print("Sube (el tesoro está más arriba).", end=" ")
    else:
        print("Fila correcta.", end=" ")

    #Pistas horizontales
    if intento_c < tesoro_c:
        print("Ve a la derecha.")
    elif intento_c > tesoro_c:
        print("Ve a la izquierda.")
    else:
        print("Columna correcta.")

    return False


#FUNCIÓN PRINCIPAL DEL JUEGO
#Contiene la estructura y logica del juego
def jugar_tesoro():
    #Crea el archivo con las coordenadas del tesoro
    crear_archivo_tesoro(archivo_coordenadas, coordenadas_secretas)

    #Carga las coordenadas del archivo
    coordenadas_tesoro = cargar_tesoro(archivo_coordenadas)
    if coordenadas_tesoro is None:
        print("No se pudieron cargar las coordenadas.")
        return

    tesoro_fila, tesoro_col = coordenadas_tesoro
    print(f"El tesoro está escondido en un tablero de {tamaño_tablero}x{tamaño_tablero}.")

    #Crea el tablero (una matriz llena de '?')
    tablero = [['?' for _ in range(tamaño_tablero)] for _ in range(tamaño_tablero)]

    intentos = 0
    encontrado = False

    #Es el Ciclo principal del juego (bucle while)
    while not encontrado:
        dibujar_tablero(tablero)
        intentos += 1
        print(f"\n--- Intento #{intentos} ---")

        #Lee las fila y columna desde teclado
        try:
            intento_fila = int(input(f"Fila (0 a {tamaño_tablero - 1}): "))
            intento_col = int(input(f"Columna (0 a {tamaño_tablero - 1}): "))

            # Valida si las coordenadas están dentro del tablero
            if not (0 <= intento_fila < tamaño_tablero and 0 <= intento_col < tamaño_tablero):
                print("Coordenadas fuera del rango.")
                intentos -= 1
                continue
        except ValueError:
            print("Entrada no válida. Escribe solo números enteros.")
            intentos -= 1
            continue

        #Marcamos el intento en el tablero
        if tablero[intento_fila][intento_col] == '?':
            tablero[intento_fila][intento_col] = 'X'

        #Verificamos si encontró el tesoro
        encontrado = verificar_intento(intento_fila, intento_col, tesoro_fila, tesoro_col)

        #Si lo encontró, mostrar mensaje final
        if encontrado:
            tablero[intento_fila][intento_col] = 'T'
            dibujar_tablero(tablero)
            print(f"\n¡Felicidades! Encontraste el tesoro en ({intento_fila}, {intento_col}) después de {intentos} intentos.")


# INICIO DEL PROGRAMA 
if __name__ == "__main__":
    jugar_tesoro()
