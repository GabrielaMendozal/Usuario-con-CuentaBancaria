from CuentaBancaria import CuentaBancaria

class Usuario:
    def __init__(self, name):
        self.name = name
        self.cuenta = {
            "cuentaB": CuentaBancaria(tasa_interés=0.02, balance=2000),
            "cuentaC": CuentaBancaria(tasa_interés=0.05, balance=3000)}

    def depósito (self):
        self.cuenta.depósito()
        return self

    def retiro (self):
        self.cuenta.retiro()
        return self

    def mostrar_info_cuenta (self):
        print (f'Usuario: {self.name}, cuentaB Balance: {self.cuenta["cuentaB"].mostrar_info_cuenta()}')
        print (f'Usuario: {self.name}, cuentaC Balance: {self.cuenta["cuentaC"].mostrar_info_cuenta()}')
        return self

    def transferir (self,monto,usuario):
        self.balance -= monto
        usuario.balance += monto
        self.mostrar_info_cuenta()
        usuario.mostrar_info_cuenta()
