class CuentaBancaria:
    cuentas = []
    def __init__(self,tasa_interés,balance):
        self.tasa_interés =tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito (self, monto):
        self.balance += monto
        return self
        
    def retiro (self, monto):
        if (self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print ("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self 

    def mostrar_info_cuenta (self):
        return f'Balance: {self.balance}'
        

    def interes (self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self 

    @classmethod
    def imprimir (cls):
        for cuentas in cls.cuentas:
            cuentas.mostrar_info_cuenta()