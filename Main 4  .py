#Continuacion del ejercicio 4
from Cuentas import*
import datetime
from random import randint

#LAS FECHAS DE APERTURA DE CADA CUENTA SON:
fecha1 = datetime.datetime(randint(2000,2020), randint(1,12),randint(1,30))
fecha2 = datetime.datetime(randint(2000,2020), randint(1,12),randint(1,30))
fecha3 = datetime.datetime(randint(2000,2020), randint(1,12),randint(1,30))

'''ESTA ES LA FECHA DE VENCIMIENTO DE LA CUENTA A PLAZO FIJO:'''
fecha_vencimiento=datetime.datetime(randint(2000,2020), randint(1,12),randint(1,30))

#LOS NUMEROS DE CUENTA DE CADA CUENTA VIENEN DADOS POR:
numero1=randint(134567898765,987676543512)
numero2=randint(134567898765,987676543512)
numero3=randint(134567898765,987676543512)


#LOS TRES TIPOS DE CUENTA INICIALIZADAS
cuenta_normal=Cuenta(45,"Juan",fecha1,numero1,10000)
cuenta_vip=Cuenta_vip(56,"Jorge",fecha2,numero2,10000,-500)
cuenta_plazo_fijo=Plazo_fijo(78,"Ana",fecha3,numero3,10000,fecha_vencimiento)



#SE RETIRAN 78 EUROS DE CADA CUENTA
fecha_retirada=datetime.datetime(randint(2000,2020), randint(1,12),randint(1,30))
cuenta_normal.retirar(78)
cuenta_plazo_fijo.retirar(78,fecha_retirada)
cuenta_vip.retirar(78)
print("Saldo de la cuenta normal: ",cuenta_normal.saldo," Saldo de la cuenta plazo fijo: ",cuenta_plazo_fijo.saldo," Saldo cuenta vip: ",cuenta_vip.saldo)

#SE INGRESAN 575EUROS EN CADA CUENTA
cuenta_normal.ingresar(575)
cuenta_plazo_fijo.ingresar(575)
cuenta_vip.ingresar(575)
print("Saldo de la cuenta normal: ",cuenta_normal.saldo," Saldo de la cuenta plazo fijo: ",cuenta_plazo_fijo.saldo," Saldo cuenta vip: ",cuenta_vip.saldo)

#SE TRANSFIEREN 2000 EUROS:
cuenta_normal.transferir(cuenta_plazo_fijo,2000)
cuenta_plazo_fijo.transferir(cuenta_vip,2000)
cuenta_vip.transferir(cuenta_normal,2000)
print("Saldo de la cuenta normal: ",cuenta_normal.saldo," Saldo de la cuenta plazo fijo: ",cuenta_plazo_fijo.saldo," Saldo cuenta vip: ",cuenta_vip.saldo)

#ac
