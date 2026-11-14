
# Actividad formativa 3: Herencia
# Programa de empleados utilizando Programación Orientada a Objetos.

# Clase base
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    # Método que pueden utilizar las clases derivadas
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo: ${self.sueldo}")


# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    # Sobrescritura del método de la clase base
    def mostrar_informacion(self):
        print("=== GERENTE ===")
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

    # Método exclusivo de Gerente
    def dirigir_equipo(self):
        print(f"{self.nombre} está dirigiendo su equipo.")


# Clase derivada Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje):
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje

    # Sobrescritura del método de la clase base
    def mostrar_informacion(self):
        print("=== DESARROLLADOR ===")
        super().mostrar_informacion()
        print(f"Lenguaje de programación: {self.lenguaje}")

    # Método exclusivo de Desarrollador
    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")


# Programa principal: creación de objetos
if __name__ == "__main__":

    gerente1 = Gerente("Carlos", 25000, "Administración")
    desarrollador1 = Desarrollador("Ana", 18000, "Python")

    # Probar los métodos heredados y propios
    gerente1.mostrar_informacion()
    gerente1.dirigir_equipo()

    print()

    desarrollador1.mostrar_informacion()
    desarrollador1.programar()
