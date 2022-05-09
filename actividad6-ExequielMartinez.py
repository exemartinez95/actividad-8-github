class Cuenta:

    def __init__(self, titular, cantidad = 0):
      self.titular = titular
      self.cantidad = cantidad 



    def mostrar(self):
      return f"Mi nombre es {self.titular} y tengo en cuenta {self.cantidad} dolarucos"
  
    def ingresar(self, cantidad):
      self.cantidad += cantidad 
      return f"La cantidad ingresada es {cantidad} y el total es {self.cantidad} dolarucos"
      

    def retirar(self, retiro):
      self.cantidad -= retiro
      return f"Usted retiró {retiro} dolarucos y su total es:  {self.cantidad} "


persona = Cuenta("pepe", 10)
print(persona.mostrar())
print(persona.ingresar(10))
print(persona.mostrar())
print(persona.retirar(15))
print(persona.mostrar()) 

#usé print para que queden los cambios registrados