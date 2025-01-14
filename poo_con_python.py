class Personaje:
    #atributos de la clase
    def _init_(self, nombre, fuerza, inteligencia, vida, defensa):
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
    daño = self.daño(enemigo)
    enemigo.vida = enemigo.vida - daño
    print(self.nombre, "Ha Realizado", daño, "Punto de daño a", enemigo.nombre)
    print("Vida de", enemigo.nombre, "Es", enemigo.vida)


#variable del constructor vacío de la clase
mi_personaje = Personaje("Liam", 70, 60, 80, 50)
mi_enemigo = Personaje("Michael", 60, 90, 100, 40)
print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()

print("El nombre del personaje es", mi_personaje.nombre)
print("La fuerza del personaje es", mi_personaje.fuerza)
