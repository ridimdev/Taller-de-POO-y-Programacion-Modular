### Ejercicio
"""
Del ejercicio avanzado añade lo siguiente

- Crear un método para retirar dinero
- Crear un método para depositar dinero
- Crear un método para mostrar un balance (Nombre y Saldo)
- **Bonus: Crea un método para transferir dinero.**
"""

class User:
    def __init__(self,nombre,dinero):
        self.dinero=dinero
        self.nombre=nombre
    def depositar(self, monto):
        # self.dinero = self.dinero + monto
        self.dinero+=monto
        print(self.dinero)

    def retirar(self, monto):
        self.dinero-=monto
        print(self.dinero)

    def mostrarBalance(self):
        return f'Usuario: {self.nombre} - Saldo: {self.dinero}'
    
    def transferir(self,destino):
        monto = input('Ingrese la cantidad a depositar: ')
        money = int(monto)
        self.retirar(money)
        destino.depositar(money)

objElias = User("Elias", 100)
objJhomar = User("Jhomar", 100)
# Depositamos 50 soles en la cuenta de mi usuario
# objElias.depositar(50)
# objElias.depositar(5)
# Retiramos 4 soles para un helado
# objElias.retirar(4)
objElias.transferir(objJhomar)

# Mostramos el balance
respuestaBalanceElias=objElias.mostrarBalance()
respuestaBalanceJhomar=objJhomar.mostrarBalance()
print("{a} {b}".format(a=str(respuestaBalanceElias),b=str(respuestaBalanceJhomar)))
