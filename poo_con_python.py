class Personaje:
    #atributos de la clase
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre)
        print("-fuerza: ", self.fuerza)
        print("-inteligencia: ", self.inteligencia)
        print("-defensa: ", self.defensa)
        print("-vida: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha Muerto")

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha Realizado", daño, "Punto de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "Es", enemigo.vida)

#creando clase "guerrero" que hereda de su clase padre "personaje"
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #llamar a la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    #pedirle al usuario escoger un arma
    def cambiar_arma(self):
        opcion = int (input("Elige un arma: (1) Espada de plata, daño 10, (2) Espada de bronce, daño 8, "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Valor incorrecto")
    #sobreescribir metodo
    def atributos(self):
        super().atributos()
        print("-Espada: ", self.espada)
    #sobreescribir el calculo del año
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
#creando clase "Mago"
class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        #llamar a la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #sobreescribir metodo
    def atributos(self):
        super().atributos()
        print("-Libro: ", self.libro)
    
    #sobreescribir el calculo del daño
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa


trakalosa = Personaje("La trakalosa de monterrey", 20, 15,10,100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)

#imprimir atributos antes del ataque
trakalosa.atributos
hercules.atributos
diosito.atributos
#ataques
trakalosa.atacar(hercules)
hercules.atacar(diosito)
diosito.atacar(trakalosa)
#imprimir

#hercules.cambiar_arma()
hercules.atributos()
#print(hercules.espada)


#variable del constructor vacío de la clase
#mi_personaje = Personaje("Liam", 70, 60, 80, 50)
#mi_enemigo = Personaje("Michael", 60, 90, 100, 40)
#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()

#print("El nombre del personaje es", mi_personaje.nombre)
#print("La fuerza del personaje es", mi_personaje.fuerza)
