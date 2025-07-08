class Coche:
  # Constructor: se utiliza para inicializar los atributos del objeto
  def __init__(self, marca, modelo, anio):
      self.marca = marca       # Atributo público
      self.modelo = modelo     # Atributo público
      self.__anio = anio       # Atributo privado (encapsulado)

  # Método para mostrar la información del coche
  def mostrar_informacion(self):
      print(f"Coche: {self.marca} {self.modelo}, Año: {self.__anio}")

  def arrancar(self):
      print("el coche esta arrancando")

# Creación de un objeto (instancia de la clase)
mi_coche = Coche("Toyota", "Corolla", 2020)

mi_coche.mostrar_informacion()
mi_coche.arrancar()
