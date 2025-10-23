import os

# --- CONFIGURACIÓN GLOBAL ---
TAMAÑO_TABLERO = 5 
ARCHIVO_COORDENADAS = "tesoro.txt"
# LISTA que define las coordenadas del tesoro (Fila, Columna)
COORDENADAS_SECRETAS = (4, 2) 


# --- Funciones Auxiliares ---

def crear_archivo_tesoro(nombre_archivo, coordenadas):
    
    try:
        # Uso de Archivos: Abre el archivo en modo escritura ('w')
        with open(nombre_archivo, 'w') as archivo:
            # Convierte las coordenadas (3, 1) al formato de texto "3,1"
            linea = f"{coordenadas[0]},{coordenadas[1]}\n"
            archivo.write(linea)
    except Exception as e:
        print(f" Error al crear el archivo de coordenadas: {e}")

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

def dibujar_tablero(tablero):

    print("\n--- Tablero de Juego  ---")
    print("  ", end="")
    for i in range(len(tablero[0])):
        print(f" {i}", end="")
    print(" (Columna)")
    
    for i, fila in enumerate(tablero):
        print(f"{i} |", end="")
        for celda in fila:
            print(f" {celda}", end="")
        print(" |")
    print("(Fila)---------------------------")

def verificar_intento(intento_f, intento_c, tesoro_f, tesoro_c):

    # Condición de Victoria
    if intento_f == tesoro_f and intento_c == tesoro_c:
        return True
    
    print("Pista: ", end="")
    
    # Pistas de Fila (Vertical)
    if intento_f < tesoro_f:
        print("Sube (fila más alta).", end=" ")
    elif intento_f > tesoro_f:
        print("Baja (fila más baja).", end=" ")
    else: 
         print("Fila Correcta.", end=" ")
        
    # Pistas de Columna (Horizontal)
    if intento_c < tesoro_c:
        print("Ve a la Derecha.")
    elif intento_c > tesoro_c:
        print("Ve a la Izquierda.")
    else: 
         print("Columna Correcta.")
    
    return False

# --- Función Principal del Juego ---

def jugar_tesoro():
    """
    Ejecuta la lógica principal del juego.
    """
    # 1. Crear el archivo de texto usando la lista COORDENADAS_SECRETAS
    crear_archivo_tesoro(ARCHIVO_COORDENADAS, COORDENADAS_SECRETAS)
    
    # 2. Cargar las coordenadas del tesoro desde el archivo creado
    coordenadas_tesoro = cargar_tesoro(ARCHIVO_COORDENADAS)
    
    if coordenadas_tesoro is None:
        return 
        
    tesoro_fila, tesoro_col = coordenadas_tesoro
    print(f"¡El Tesoro está oculto en una cuadrícula de {TAMAÑO_TABLERO}x{TAMAÑO_TABLERO}!")

    # 3. Inicializar la Matriz (Tablero)
    tablero = [['?' for _ in range(TAMAÑO_TABLERO)] for _ in range(TAMAÑO_TABLERO)]

    intentos = 0
    encontrado = False

    # 4. Bucle Principal del Juego (Estructura while)
    while not encontrado:
        dibujar_tablero(tablero)
        intentos += 1
        
        print(f"\n--- Intento #{intentos} ---")
        
        # 5. Input y Validación
        try:
            intento_fila = int(input(f"Introduce la Fila (0 a {TAMAÑO_TABLERO - 1}): "))
            intento_col = int(input(f"Introduce la Columna (0 a {TAMAÑO_TABLERO - 1}): "))
            
            # Validación de Coordenadas
            if not (0 <= intento_fila < TAMAÑO_TABLERO and 0 <= intento_col < TAMAÑO_TABLERO):
                print(f"Coordenadas fuera de rango.")
                intentos -= 1 
                continue
                
        except ValueError:
            print("Entrada no válida. Introduce solo números enteros.")
            intentos -= 1
            continue
            
        # 6. Actualizar Tablero
        if tablero[intento_fila][intento_col] == '?':
             tablero[intento_fila][intento_col] = 'X'

        # 7. Verificar el Intento
        encontrado = verificar_intento(intento_fila, intento_col, tesoro_fila, tesoro_col)
        
        # 8. Condición de Victoria
        if encontrado:
            tablero[intento_fila][intento_col] = 'T' 
            dibujar_tablero(tablero)
            print(f"\n¡Felicidades! Encontraste el tesoro en la posición ({intento_fila}, {intento_col}) en **{intentos}** intentos.")

# --- INICIO DEL PROGRAMA ---
if __name__ == "__main__":
    jugar_tesoro()