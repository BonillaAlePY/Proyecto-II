# Proyecto II, hecho por Alexander Bonilla Figueroa y Adrián Rodríguez Quirós 

import random
import time

# Función que introduce al usuario al contexto de la simulación, se utiliza el módulo "time" para facilitar la lectura del usuario (prueba)

def Intro(textos, ini = 0, ind = 0, res = ""):
    # Se verifica si aún hay elementos en la lista
    if ini < len(textos):
        # Se verifica si aún hay caracteres por imprimir 
        if ind < len(textos[ini]):
            # Se imprime el caracter actual
            print(res + textos[ini][ind], end = "", flush = True)
            # Se da un intervalo de tiempo antes de imprimir el siguiente caracter
            time.sleep(0.04)
            # Se pasa al siguiete caracter
            return Intro(textos, ini, ind + 1, res)
        else:
            # Se imprime un salto de línea si ya se imprimió al menos un caracter (end == "") 
            print("\n" if ind > 0 else "", end = "")
            # Llamada recursiva para pasar al siguiente texto
            return Intro(textos, ini + 1, 0, res)
    else:
        # Retorna el texto completo una vez que se han impreso todas las frases
        return res

print() # Salto de línea

# Variable que almacena los textos de introducción a la simulación

Introduccion = [" (-_-) ¡Hola! Soy ........... no te voy a decir mi nombre aún, tendrás que descubrirlo, pero si puedo decirte que seré tu guía durante esta simulación.", 
                " \n (-_-) Podes reconocerme fácilmente ya que al inicio de cada oración aparece esta cara: (-_-).", 
                " \n (-_-) Estoy guapo ¿verdad? (-_.) (eso fue un guiño jeje).", 
                " \n (-_-) Para iniciar, quiero darte un poco de contexto.", 
                " \n (-_-) Estas en una simulación en la cual, con mi ayuda, podes viajar a diversas zonas verdes y dentro de ellas, interactuar con distintas personas.",
                " \n (-_-) El principal objetivo o misión es que disfrutes de estas zonas y que interactues con los demás.",  
                " \n (-_-) Gracias a las interacciones irás acumulando puntos de experiencia, al llegar a diez mil, podrás saber mi nombre jeje.",
                " \n (*u*) ¡Iniciemos entonces!", " \n (-_-) Primero debes decidir la cantidad de zonas verdes que quieres habilitar para tu visita."]

print(Intro(Introduccion)) # Se imprime la función Intro tomando la lista de textos como parámetros

# Primeros nombres de las zonas verdes

Primeros_nombres = ["Parque", "Recinto", "Zona protegida", "Parque Nacional", "Área Natural", "Área Silvestre", 
       "Refugio de Vida", "Santuario", "Bosque Nacional", "Reserva Natural", "Área de Conservación", 
       "Hábitat Protegido", "Refugio de Fauna", "Área de Protección", "Área de Preservación", "Refugio Natural", 
       "Humedal Protegido", "Reserva Ecológica", "Parque Ecológico", "Reserva de Biodiversidad", "Área de Recreación", 
       "Área de Restauración", "Área de Rehabilitación", "Refugio de Flora", "Refugio de Aves", "Área de Vida Silvestre", 
       "Zona de Conservación", "Área de Bosque", "Refugio de Especies", "Área de Repoblación", "Área de Restauración Ecológica"]

# Segundos nombres de las zonas verdes

Segundos_nombres = [" Monteverde", " La Selva", " Tortuguero", " Corcovado", " Manuel Antonio", " Irazú", " Poás", " La Amistad", " Barra Honda", 
                    " Santa Rosa", " Guanacaste", " Carara", " Caño Negro", " Rincón de la Vieja", " Arenal", " Chirripó", " La Paz", " Los Quetzales", 
                    " Tapantí", " Turrialba", " Río Celeste", " Montezuma", " Volcán Tenorio", " Los Santos", " Osa", " Las Cruces", " San Pablo", 
                    " El Escambray", " Las Sierras", " Cartago", " Moín", " Uvita", " San Blas"]

# Nombres de las personas

Nombres = ["Sofía", "Mateo", "Valentina", "Sebastián", "Luciana", "Dylan", "Camila", "Martín", "Isabella", "Matías", "María José", "Nicolás", 
           "Mía", "Juan José", "Emilia", "Diego", "Valeria", "Gabriel", "Victoria", "Thiago", "Ana Sofía", "Leonardo", "Juliana", "Alexander", 
           "Sara", "José Daniel", "Regina", "Andrés", "Isabel", "Carlos", "Carolina", "Esteban"]

# Apellidos de las personas

Apellidos = [" González", " Rodríguez", " Fernández", " Hernández", " López", " Martínez", " Pérez", " Gómez", " Díaz", " Torres", " Flores", " Sánchez", 
             " Romero", " Álvarez", " Ruiz", " Ramírez", " Suárez", " Gutiérrez", " García", " Navarro", " Moreno", " Chaves", " Morales", " Jiménez", 
             " Arias", " Castro", " Herrera", " Vargas", " Villalobos", " Campos", " Mora", " Guerrero"]

# Lista de diálogos

Dialogos = [ "No me hables, estoy descansando", " ¡esta zona es la mejor para conectar con la naturaleza!", "¡Qué maravilla respirar aire puro y estar rodeado de árboles!", 
            "¿En qué año estamos?", "¡Vamos a plantar más árboles para cuidar nuestro planeta!", "¡Este lugar es perfecto para meditar y recargar energías!", 
            "¡Miren qué lindas flores hay aquí, son una inspiración!", "¿Qué tal si hacemos un safari fotográfico para documentar la biodiversidad?",
            "¡No olviden recoger la basura y mantener limpio este hermoso lugar!", "¿Alguien trajo semillas para intercambiar y enriquecer nuestros jardines?",
            "¡Hagamos un concurso de avistamiento de aves, a ver quién encuentra más especies!", "¡Estoy tan agradecido de poder disfrutar de la naturaleza en buena compañía!",
            "¡El sonido del viento entre las hojas es música para el alma!", "¡Vamos a explorar y descubrir nuevos rincones de esta maravillosa zona verde!", 
            "¿Qué opinan de organizar un taller de reciclaje creativo para niños?", "¡Este es el lugar perfecto para hacer yoga y conectarse con uno mismo!",
            "Parece que lloverá", "Linux > Windows, factos", 
            "¿Han visto qué hermoso atardecer se puede apreciar desde aquí?", "¡Cuidemos cada planta y animal como si fuera parte de nuestra familia!", 
            "¡Me encanta ver cómo la vida florece en cada rincón de este lugar!", "¿Alguien trajo binoculares? Podemos observar aves desde lejos sin molestarlas.", 
            "¡Recuerden llevar agua y mantenernos hidratados mientras disfrutamos de la naturaleza!","¡Cada árbol cuenta su historia, vamos a escucharlas y aprender juntos!",
            "¿Qué opinan de organizar una jornada de limpieza y restauración de senderos?", "¡Hoy es un buen día para agradecer a la tierra por darnos tanto!", 
            "¡Funda se para! pero cada acción eco-amigable suma para un mundo mejor."]

# Puntos de experiencia

Experiencia = 0

# Lista de números para inicializar

Números_inicio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                  26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
                  49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 
                  72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 
                  95, 96, 97, 98, 99, 100]

# Caractres ASCII para validar el input (no incluye los números)

ASCII_charts =  [ "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", 
                 "@", "[", "\\",  "]", "^", "_", "`", "{", "|", "}", "\"", "~", "A", "B", "C", "D", "E", "F", "G", 
                 "H", "I", "J", "K", "L", "M",  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", 
                 "b", "c", "d", "e", "f", "g", "h", "i", "j",  "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", 
                 "v", "w", "x", "y", "z", " ", ""]
    
# Función que verifica que no hayan letras dentro de un texto (necesaria para la función Intro)
# Sí la cadena es muy grande, la pila se desborda (limitación de esta función) (si pudiéramos usar in...)

def Verificar(texto, asc = ASCII_charts):

    return Verificar_aux(texto, asc, 0, 0, len(texto), len(asc))

def Verificar_aux(texto, asc, ini_txt, ini_asc, fin_txt, fin_asc):
    
    # Casos especiales:
    if texto == "0" or texto == "": 
        return False
    # Ya se verificaron todos los caractres de la lista ASCII_charts con cada caracter del texto
    elif ini_asc == fin_asc: 
        return True
    # Ya se verificaron todos los caracteres del texto con el primer caracter de ASCII_charts
    elif ini_txt == fin_txt: 
        return Verificar_aux(texto, asc, 0, ini_asc + 1, fin_txt, fin_asc)
    # Se pasa a comparar el siguiente caracter de texto
    elif texto[ini_txt] != asc[ini_asc]:
        return Verificar_aux(texto, asc, ini_txt + 1, ini_asc, fin_txt, fin_asc)
    # Hay algún caracter de ASCII_charts en texto
    else:
        return False

# Función que solicita el número de zonas verdes que se inicializarán

def Intro(texto, num = Números_inicio, ini = 0, fin = len(Números_inicio)):

    # Llamada a la función Verificar, que indica si hay valores ASCII, no números en el input
    if Verificar(texto) == True: 
        # Se verifica que el número esté dentro del rango establecido (1-100)
        if int(texto) < 0 or int(texto) > 100:  
            return Intro(input(" (0_0) ¡Estás digitando un número fuera de rango! ---> "), num, ini, fin)
        # Se retorna el número si se encuentra en la posición ini de num (lista de números del 1 al 100)
        elif int(texto) == num[ini]:
            return int(texto)
        # Se pasa a la siguiente posición de la lista de números (num)
        else:
            return Intro(texto, num, ini + 1, fin)
    # Hay valores ASCII no números en el input, se repregunta    
    else:
        return Intro(input(" (0_0) ¡Estás digitando un caracter inválido! Inténtalo de nuevo ---> "), num, ini, fin)
    
# Variable que almacena la cantidad de zonas verdes que se inicializarán

Número_zonas = Intro(input(" (-_-) ¿Cuantas zonas verdes deseas habilitar? ---> ")) 

# Función que construye la cantidad de zonas verdes que el usuario le indicó

def Ini_zonas(pr = Primeros_nombres, se = Segundos_nombres, num = Número_zonas, res = []):

    # Ya se almacenaron todas las listas (print vacío para salto de línea)
    if num == 0:
        print()
        return res
    # Se siguen almacenando listas
    else:
        # Índice random de la lista pr
        ran_pr = pr[random.randint(0, len(pr)-1)]
        # Índice random de la lista se
        ran_se = se[random.randint(0, len(se)-1)]
        # Se retorna la suma del res actual y la siguiente zona verde
        return Ini_zonas(pr, se, num-1,  res + [[ran_pr + ran_se]])

# Variable que almacena la lista de zonas verdes

Zonas = Ini_zonas()

# Función que enumera las zonas verdes

def Enum_elem(zon = Zonas, num = Números_inicio, ini = 0, fin = len(Zonas), res = []):

    # Se enumeraron todas las zonas
    if ini == fin:
        return res
    # Se mezcla la lista de números con la de zonas
    else:
        return Enum_elem(zon, num, ini + 1, fin, res + [[num[ini]] + Zonas[ini]])

# Variable que almacena las zonas enumeradas

Enum = Enum_elem() 

# Función que muestra las zonas verdes separadas por saltos de línea

def Saltos(lista = Enum, ini = 0, fin = len(Enum)):

    # Se retorna un texto vacío al final para que no sea visible
    if ini == fin:
        return ""
    # Se imprime un salto de línea antes de imprimir la siguiente zona
    else:
        print()
        print(lista[ini])
        # Se pasa a la siguiente zona verde
        return Saltos(Enum, ini + 1, fin)
    
# Se imprimen las zonas que se inicializaron

print(Saltos())

# Función que selecciona una de las zonas verdes

def Selección(texto, num = Número_zonas):

    # Se llama a la función Verificar para validar posibles errores
    if Verificar(texto) == True: 
        # La zona seleccionada debe estar entre cero y el número de zonas habilitadas
        if 0 < int(texto) <= num:
            return int(texto)
        # Si se digitó un número fuera de rango, se repregunta
        else:
            return Selección(input("\n (0_0) ¡Estás digitando un número fuera de rango! Inténtalo de nuevo ---> "), num)
    # Si se digitó un caracter ASCII no número, se repregunta
    else:
        return Selección(input("\n (0_0) ¡Estás digitando un caracter inválido! Inténtalo de nuevo ---> "), num)

# Función que muestra la zona seleccionada

def Mostrar_zona(Num_zona_sele, Zonas = Enum): 

    # Solamente retorna la posición
    return Zonas[Num_zona_sele-1] # OJO AQUÍ PA --- la variable necesita definirse hasta después

# Función que inicializa los nombres de las personas 
# Se inicializan tres veces la cantidad de nombres de zonas para distribuir de manera más uniforme

def Ini_nombres(num = Número_zonas, fin = 0, nomb = Nombres, ape = Apellidos, res = []):

    # Si se llega a esta condición, formaron todos los nombres
    if num <= 0:
        return res
    # Se forman los nombres
    else:
         # Índice random de la lista nomb
         ran_nomb = nomb[random.randint(1, len(nomb)-1)]
         # Índice random de la lista ape
         ran_ape = ape[random.randint(1, len(ape)-1)]
         # Se forma el siguiente nombre y se resta 0.33 al num
         return Ini_nombres(num - 0.33, fin, nomb, ape, res + [ran_nomb + ran_ape])

# Variable que almacena la lista con los nombres de las personas

Nombres_personas = Ini_nombres()

# Función que introduce los nombres de las personas a cada zona verde

def Ini_zonas_nombres(zon = Enum, nom = Nombres_personas, ini = 0, ind = 0, res = []):

    if ini == len(zon):
        return res
    else:
        return Ini_zonas_nombres(zon, nom, ini + 1, ind + 3, res + [[zon[ini]] + [[nom[ind], nom[ind + 1], nom[ind + 2]]]])
    
# Variable que almacena a la función que junta la lista de zonas con la lista de nombres
    
Lista_completa = Ini_zonas_nombres()
  
# Función que selecciona el número de zona a visitar

def Selección_zona(texto, num = Número_zonas):

    # Se llama a la función Verificar para validar posibles errores
    if Verificar(texto) == True: 
        # La zona seleccionada debe estar entre cero y el número de zonas habilitadas
        if 0 < int(texto) <= num:
            return int(texto)
        # Si se digitó un número fuera de rango, se repregunta
        else:
            return Selección_zona(input("\n (0_0) ¡Estás digitando un número fuera de rango! Inténtalo de nuevo ---> "), num)
    # Si se digitó un caracter ASCII no número, se repregunta
    else:
        return Selección_zona(input("\n (0_0) ¡Selecciona un número de zona!---> "), num)

# Función que muestra la zona seleccionada

def Mostrar_sele_zona(Sele_zona, List = Lista_completa):

    # Solamente retorna la posición
    return List[Sele_zona-1] # OJO AQUÍ PA --- la variable necesita definirse hasta después

# Función que enumera a las personas para seleccionarlas de manera más sencillas

def Enum_per(Mostrar_se, fin, ini = 0, res=[]):

    if ini == fin:
        return [Mostrar_se[0]] + [res]
    else:
        return Enum_per(Mostrar_se, fin, ini + 1, res + [str(ini + 1) + "." + Mostrar_se[1][ini]])

    
# Función que selecciona una de las personas y despliega un diálogo

def Diálogo_per(texto, personas_enum, dia = Dialogos):

    global Experiencia

    if texto == "1":
        texto = int(texto)
	
        print(personas_enum[1][texto-1] + " :" + dia[random.randint(0, len(dia)-1)])
        Experiencia = Experiencia + 5
        return Diálogo_per(input("\n (.w.) Si deseas seguir interactuando, selecciona el número de persona, pero si deseas salir de la zona, digita (s) ---> "), personas_enum, Dialogos)
    elif texto == "2":
        texto = int(texto)
        Experiencia = Experiencia + 5
        print(personas_enum[1][texto-1] + " :" + dia[random.randint(0, len(dia)-1)])
        return Diálogo_per(input("\n (.w.) Si deseas seguir interactuando, selecciona el número de persona, pero si deseas salir de la zona, digita (s) ---> "), personas_enum, Dialogos)
    elif texto == "3":
        texto = int(texto)
        print(personas_enum[1][texto-1] + " :" + dia[random.randint(0, len(dia)-1)])
        Experiencia = Experiencia + 5
        return Diálogo_per(input("\n (.w.) Si deseas seguir interactuando, selecciona el número de persona, pero si deseas salir de la zona, digita (s) ---> "), personas_enum, Dialogos)
    elif texto == "s" or texto == "S":
        Experiencia = Experiencia + 2
        return Simulación(input(" (-_-) Selecciona (y) para continuar la simulación o (x) para finalizar la simulación  ---> "))
    else:
        return Diálogo_per(input("\n (0_0) ¡Estás digitando un caracter inválido! Inténtalo de nuevo ---> "), personas_enum, Dialogos)
    
# Función simulación que incluye todas las demás funciones

def Simulación(texto):

    # Variable global para sumar la experiencia 

    global Experiencia

    if texto == "y" or texto == "Y":
       
        print("::::::::::::........................................................................::::::")
        print(":::::::::.............................................................................::::")
        print("::::::..................................................................................::")
        print("::::........................................-=--..........................................")
        print("::.......................................:=+*###*+-:......................................")
        print(":.....................................:+######%#####*+=:  ................................")
        print(".................................:.-*=+#####%%%%%%%###****=.   ...........................")
        print("............................:.. =#**#*#%%%%%%#%%##+######***=-.  .........................")
        print("........................=:+*#***###*##*###%%####*####%%#######=   ........................")
        print("........................==*+##################*#*#####*####*#**=..........................")
        print("........................ -**#%%#####%####%%%%%%%%####%########+..:........................")
        print("........................+##%#%%%%%%%%%#%%#%%%%%%##*########%%##*##=.......................")
        print(".......................=##%%%%%%%@@%@@%##%##%%%%%#%%##%%%#%#######*+--:...................")
        print("......................:##*#%%%%%%%%%##%#%%%###%%%%@%%%%%#############*-...................")
        print("......................:###%%%%%###*##*#@@##%%%%%%%%%%@%##############*....................")
        print("......................=+*#%%#%%########%%%###%%%###%%%%##%##%#######**....................")
        print("......................+*%%%#*#########*#%#*##*#%#####%%%#%%%%####*###--...................")
        print(".......................-*%%######%%#####%##*##*####*#%%%##%%%%###***#+=...................")
        print("..::::................:=##%%#%#%%%%%##@@@@%#%##%%%%#*#######%%%%###+=-....................")
        print("*****+++*++++======---:-#%%%%%#####%%@@%@@%@%%##%%###***###**+=#**+-..::::::::::::::::::::")
        print("+++++++++++++++++++=====+%%%%%#####*=%@@%@%%##*##%########*===-------=-----============+==")
        print("------------------------*+*-+%#*++***@@@@@%##*##+*#*==#+**#=======+=======================")
        print("--------------:::::::::::::+##*=+=---@@@@@%####*+-========+===============+++++++===+++===")
        print("---------------------------*+==------%%%%%=+*===------=========+==++++++++++++++++=====+++")
        print("------------==++************########%%%%%%#######********+++++++++++++++++++++==++++++++++")
        print("-----------=+=+==++++****###############%#####*##***+++++++++++++++++++++=++++++++++++++++")
        print("------------------===+++++**++++++++++++*++++++++++*++*+++++++++++++++++++++++++++++++++++")
        print("------------===+++====+++++=======+++++++++++++++***++++++++++=++++++++++++++++++++++++*+*")
        print("---====+++===++++++++++=========+===+++++++++++++++++=+++++++++++++++=++++++++++++++++++++")
        print("+++++++=+==+++=++=++=====++==+==+==========++=++=++++++===+==+++++++++++++++++**+++*+++***")
        print(Saltos())
        print(" (-_-) Arriba están las zonas que puedes visitar.")
        print(" (-_-) Experiencia actual:", Experiencia)

        Zona_seleccionada = Selección_zona(" (-_-) ¿Qué zona deseas visitar? ---> ")
        print()
        print(Enum_per(Mostrar_sele_zona(Zona_seleccionada), len(Mostrar_sele_zona(Zona_seleccionada))+1))
        print()
        Personas_enumeradas = Enum_per(Mostrar_sele_zona(Zona_seleccionada), len(Mostrar_sele_zona(Zona_seleccionada)) + 1)
        print(Diálogo_per(input(" (-_-) ¿Con qué persona desea interactuar? ---> "), Personas_enumeradas))
        print()
  
    elif texto == "x" or texto == "X":

        print()
        print("                                 :-=+*#%%@@@@@@@@%%#*+=-:.                                ")
        print("                           .-+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*=:                           ")
        print("                       .-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=:                       ")
        print("                    :+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*-                    ")
        print("                 :*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:                 ")
        print("               -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=               ")
        print("             =%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.            ")
        print("           =%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+           ")
        print("         -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-         ")
        print("        +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*        ")
        print("       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.      ")
        print("     .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:     ")
        print("    .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-    ")
        print("   :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-   ")
        print("  .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:  ")
        print("  -***********##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%  ")
        print("                  .-==++++*****###%%@@@@@@@@@@@%%###****+++++*#%@@@@@@@@@@@@@@@@@@@@@@@@+ ")
        print("                                      .::-==**                     ..::-=+*%@@@@@@@@@@@@@.")
        print("                                             :=                              .-+#@@@@@@@@=")
        print("                                             .%                                   .-+#@@@*")
        print("                                             -=      ..                                .==")
        print("                    .                  .     @.       +                                   ")
        print("                   =.                .-     .#      : =*.:.                               ")
        print("       .:-==++=:.-#.          ..::.-#+:--.  -=      :+---%-.             :                ")
        print(" :-+#%@@@@@@@@%-==+*+=-:  :+*%@@*  -.-.     +:      ==   %-             -.                ")
        print("*@@@@@@@@@@@@@@+            :-=*%.    ::    @     .. . :-              +%-                ")
        print("-@@@@@@@@@@@@@@@%-         .*::::-=+--::::::*:     .:::            .=*@@@@@*::.           ")
        print(" %@@@@@@@@@@@@@@@@@*-.::.     -=-#--====+=. -@@%@@=             :+#@@@@@@@@@@*:           ")
        print(" =@@@@@@@@@@@@@@@@@@@@@+:.    .: .      -@@@@@@@@=::         -*@@@@@@@@@@@@@@@@#:         ")
        print("  %@@@@@@@@@@@@@@@@@@@@@@%=.        -#%%@@@@@@@@@- :+.   .-*@@@@@@@@@@@@@@@@@@@@@#-       ")
        print("  .@@@@@@@@@@@@@@@@@@@@@@@@@%*-.-   .=@@@@@@@@@@@@*==###@@@@@@@@@@@@@@@@@@@@@@@@@@@%+.    ")
        print("   :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-   ")
        print("    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=    ")
        print("     :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=     ")
        print("      .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-      ")
        print("        *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.       ")
        print("         -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=         ")
        print("           +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.          ")
        print("            .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:            ")
        print("              .+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:              ")
        print("                 -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=                 ")
        print("                    =#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=.                   ")
        print("                       :+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*-.                      ")
        print("                          .-+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+-.                          ")
        print("                                :-=+*##%%@@@@@@@@%%##*+=-:.                               ")
        print()
        
        print("(-_-) Simulación finalizada, gracias por jugar")

        if Experiencia >= 10000:
            return " (-_-) Mi nombre es ... no tengo xd"
        else:
            print()
            return " (-_-) No alcanzaste los 10000 puntos."

    else:
        return Simulación(input(" (-_-) Digitaste un caracter inválido, ¡Inténtalo de nuevo! ---> "))

print(Simulación(input(" (-_-) Selecciona (y) para iniciar la simulación, y (x) para finalizar la simulación  ---> ")))