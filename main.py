from CuentaBancaria import CuentaBancaria
from Usuario import Usuario
#from Usuario import Usuario

#gaby = Usuario ('Gabriela')
#ronaldo = Usuario ('Ronaldo')

#gaby.depósito (100).retiro (50)
#ronaldo.depósito (20).retiro(5)

#gaby.mostrar_info_cuenta()
#ronaldo.mostrar_info_cuenta()


#gaby.transferir(10,ronaldo)

#usuario1 = CuentaBancaria (0.02, 1000)
#usuario2 = CuentaBancaria (0.05,2000)

#usuario1.depósito(100).depósito(200).depósito(300).retiro(50).interes().mostrar_info_cuenta()
#usuario2.depósito(500).depósito(600).retiro(50).retiro(60).retiro(70).retiro(80).interes().mostrar_info_cuenta()

#CuentaBancaria.imprimir()

usuario3 = Usuario('Lizeth')
#usuario3.cuenta.depósito(1000)


#usuario3.mostrar_info_cuenta()
#usuario3.cuenta.retiro (200)
#usuario3.mostrar_info_cuenta()

usuario3.cuenta['cuentaB'].depósito(200)
usuario3.cuenta['cuentaC'].depósito(300)
usuario3.mostrar_info_cuenta()
