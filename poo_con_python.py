class Personaje:
    #atributos de la clase
    def _init_(self, nombre, fuerza, inteligencia, vida, defensa):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

def atributos(self):
    print(self.__nombre)
    print("-fuerza: ", self.__fuerza)
    print("-inteligencia: ", self.__inteligencia)
    print("-defensa: ", self.__defensa)
    print("-vida: ", self.__vida)

def subir_nivel(self, fuerza, inteligencia, defensa):
    self.fuerza += fuerza
    self.inteligencia += inteligencia
    self.defensa += defensa

def esta_vivo(self):
    return self.__vida > 0

def morir(self):
    self.vida = 0
    print(self.__nombre, "Ha Muerto")

def dañar(self, enemigo):
    return self.fuerza - enemigo.defensa if self.fuerza > enemigo.defensa else 0

def atacar(self, enemigo):
    daño = self.dañar(enemigo)
    enemigo.vida = enemigo.vida - daño
    print(self.__nombre, "Ha Realizado", daño, "Punto de daño a", enemigo.__nombre)
    if not enemigo.esta_vivo():
        enemigo.morir()
    print("Vida de", enemigo.__nombre, "Es", enemigo.vida)

def get_fuerza(self):
    return self.__fuerza

def set_fuerza(self, fuerza):
    self.__fuerza = fuerza



#variable del constructor vacío de la clase
mi_personaje = Personaje("Trakalosa dd monterrey", 70, 60, 80, 50)
mi_enemigo = Personaje("La arrolladora banda limon", 60, 90, 100, 40)
print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()

print("El .__nombre del personaje es", mi_personaje.__nombre)
print("La fuerza del personaje es", mi_personaje.fuerza)
#prueba 1. Sin acceso al atributo fuerza
print(mi_personaje.fuerza)
