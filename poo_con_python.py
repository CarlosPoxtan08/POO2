class Personaje:
    #atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
#variable del constructor vacío de la clase
mi_personaje = Personaje()
mi_personaje.nombre = 'damaris'
mi_personaje.fuerza = 9000
mi_personaje.vida = 100
print("El nombre del personaje es: ", mi_personaje.nombre)
print("La fuerza de mi personaje es: " , mi_personaje.fuerza)
print("La vida de mi personaje es: ", mi_personaje.vida )