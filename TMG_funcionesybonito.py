# Requisitos funcionales: Iniciales.

# La pantalla base de nuestro STEMgotchi mostrará el estado del mismo,
# con el nivel de Felicidad  y  Saciedad (hambren’t)
# y el número de Cacas que ha hecho.
# Inicialmente todos estos valores estarán a 0.
# Tanto la Felicidad como la Saciedad pueden ir de 0 a 4.
# El número de cacas puede llegar a 6.

# Felicidad: ❤️❤️❤️❤️
# Saciedad: 🍙🍙🍙🍙 
# Cacas: 💩💩💩💩💩

# Inicialmente tendremos a nuestra disposición tres posibles acciones o actividades: 
# dar de comer, jugar y limpiar la caca,
# que se mostrará en forma de menú para poder elegir la acción a realizar.

# Como manera de gestionar el tiempo, 
#  vamos a considerar la realización de cualquiera de las acciones o actividades como una iteración temporal ⏱️. 



# 🍙🍡 DAR DE COMER 🍡🍙 

# El STEMgotchi no puede comer si hay alguna caca 💩 a su alrededor: ¡Qué asco!

# Podemos darle dos tipos de alimento:
# 🍙 Comida 🍙: Al comer sube de nivel de saciedad (+1🍙)
# 🍡 Dulce 🍡: Al comer un dulce sube el nivel de saciedad (+1🍙) y el nivel de felicidad (+1❤️).

# 🕹️ JUGAR 🕹️
# Cuando el STEMgotchi juega 🕹️ sube el nivel de felicidad (+1❤️) y baja el nivel de saciedad (-1🍙).
# No puede jugar si hay más de tres (3) cacas 💩💩💩 a su alrededor.

# 💩 LIMPIAR LA CACA 💩

# Cuando le limpias la caca 💩, simplemente dejará de tener caca. Seguramente se ponga más contento, pero es tu obligación como cuidador, así que no aumentará el nivel de felicidad.
# Cuando se interaccione tres (3) veces ⏱️⏱️⏱️ con el STEMgotchi, este hará una caca (+1💩) y bajará  el nivel de felicidad (-1❤️).

# corazon = "❤️"
# comida = "🍙"
# caca = "💩"

def contartiempo(cacas, felicidad, cuentaTiempo):
    cuentaTiempo += 1
    if cuentaTiempo == 3:
        cacas += 1
        felicidad -= 1
        cuentaTiempo = 0
    return cacas, felicidad, cuentaTiempo

def funComer(cacas, saciedad, felicidad, cuentaTiempo):
    if cacas>0:
            print("\nQué asco, con caca no se come")

    else:
        eligeComida = int(input ("\nElige comida (1) o dulce (2): "))
        if eligeComida == 1:
            print ("\n¡Mmmmm comidita riquita!")
            saciedad += 1
        elif eligeComida == 2:
            print ("\n¡Chuches! Una vez al año no hace daño, ¡viva!")
            saciedad += 1
            felicidad += 1

    cacas, felicidad, cuentaTiempo = contartiempo(cacas, felicidad, cuentaTiempo)
    
    return cacas, saciedad, felicidad,cuentaTiempo

def funJugar (cacas, saciedad, felicidad, cuentaTiempo):
    
    if cacas <numCacasValido:
        print ("\n¡Qué emoción, todo es diversión!")
        felicidad += 1
        saciedad -= 1
    else: 
        print ("\nCON CACA NO SE JUEGAAAA")

    cacas, felicidad, cuentaTiempo = contartiempo(cacas, felicidad, cuentaTiempo)

    return cacas, saciedad, felicidad,cuentaTiempo
    
def funLimpiarCacas(cacas, felicidad, cuentaTiempo):
    cacas = 0
    print ("\n¡Limpio como una patena!")
    cacas, felicidad, cuentaTiempo = contartiempo(cacas, felicidad, cuentaTiempo)
    return cacas, felicidad, cuentaTiempo

#CODIGO PRINCIPAL

felicidad = 0
saciedad= 0
cacas = 0
cuentaTiempo = 0 
numCacasValido = 4

while cacas < numCacasValido + 1:

    accion = int(input("\n¡Tienes tres opciones para interactuar con tu bebesitotchi! \n\n(1)Comer, \n(2)Jugar, \n(3)Limpiar caca. \n\nElige lo que quieres hacer: "))

    if accion == 1:
        print ("\n¡A comeeer!")
        cacas, saciedad, felicidad, cuentaTiempo= funComer(cacas, saciedad, felicidad, cuentaTiempo)

    elif accion == 2:
        print ("\n¡A jugar!")
        cacas, saciedad, felicidad, cuentaTiempo= funJugar (cacas, saciedad, felicidad, cuentaTiempo)

    elif accion == 3:
        print ("\nVamo a limpiar.")
        cacas, felicidad, cuentaTiempo = funLimpiarCacas(cacas, felicidad, cuentaTiempo)
    
    else :
        print("¿Te gusta ser tonte? Introduce una accion correcta.")

    
    print(f"\nEl estado de tu StemGotchi es: \n\nFelicidad = {felicidad}. \nSaciedad = {saciedad}. \nCacas = {cacas}.")

print("\nSa morio D.E.P")
    


# proebas de caca
#kjhxskvghxkvjkxfd
















