class Cuenta():

    def __init__(self,id,propietario,fecha,numero,saldo):
        self.id=id #ID de la cuenta bancaria
        self.propietario=propietario
        self.fecha=fecha #Fecha de apertura
        self.numero=numero #numero de cuenta
        self.saldo=saldo

    def retirar(self,cantidad):
        '''El argumento cantidad indica cuanto dinero quieres sacar.
         La funcion solo modifica el atributo saldo,si se cumple la condicion
         del if;Que cantidad sea menor que el saldo de la cuenta'''
        
        if (cantidad<self.saldo):
            self.saldo=self.saldo-cantidad

    def ingresar(self,cantidad):
        '''El argumento cantidad indica cuanto dinero quieres ingresar.
         La funcion solo modifica el atributo saldo'''
        
        self.saldo=self.saldo+cantidad

    def transferir(self,cuenta,cantidad):
        '''El argumento cantidad indica cuanto dinero quieres transferir a otra cuenta.
        El atributo cuenta se trata de un objeto de la clase cuenta.
        La funcion solo modifica el atributo de instancia saldo de cada clase
        si se cumple la condicion del if;Que cantidad sea menor que el saldo de la cuenta'''
        
        if (cantidad<self.saldo):
            self.saldo=self.saldo-cantidad
            cuenta.saldo=cuenta.saldo+cantidad

    

class Plazo_fijo(Cuenta):
    
    def __init__(self, id, propietario, fecha, numero, saldo,vencimiento):
        super().__init__(id, propietario, fecha, numero, saldo)
        self.vencimiento=vencimiento#Fecha de vencimiento 
    
    def retirar(self, cantidad,fecha):
        '''El atributo fecha se refiere a la fecha en la que se ha retirado el dinero.
        Si esta fecha es anterior a la fecha de vencimiento se aplica una penalizacion.'''
        
        if (cantidad<self.saldo):
            
            if (fecha<self.vencimiento):
                self.saldo=(self.saldo-cantidad)-(0.05*cantidad)

            else:
                self.saldo=self.saldo-cantidad

                

        

    




class Cuenta_vip(Cuenta):
    
    def __init__(self, id, propietario, fecha, numero, saldo,negativo):
        super().__init__(id, propietario, fecha, numero, saldo)
        self.negativo=negativo

    def retirar(self, cantidad):
        
        if (cantidad>self.saldo) and((self.saldo-cantidad)>self.negativo):
            #En este caso si cantidad es mayor que el saldo de la cuenta pero al quitar esa cantidad el saldo
            #negativo que te queda esta por debajo del limite,puedes sacar esa cantidad.
            self.saldo=self.saldo-cantidad
        
        elif(cantidad<self.saldo) and((self.saldo-cantidad)>self.negativo):
            #Si la cantidad a retirar es menor que el saldo que tiene la cuenta,se puede retirar sin problema,
            #siempre que no se supere el saldo negativo limite.
            
            self.saldo=self.saldo-cantidad

        else:
            #Esta opcion solo se ejecuta cuando la cantidad a retirar es mayor que el saldo de la cuenta y el limite negativo
            #maximo se supera
            print("No puedes retirar dinero")

    
    def transferir(self, cuenta, cantidad):
        if (cantidad>self.saldo) and((self.saldo-cantidad)>self.negativo):
            #En este caso si cantidad es mayor que el saldo de la cuenta pero al quitar esa cantidad el saldo
            #negativo que te queda esta por debajo del limite,puedes sacar esa cantidad y por lo tanto realizar
            #la tranferencia.
            
            self.saldo=self.saldo-cantidad
            cuenta.saldo=cuenta.saldo+cantidad
        
        elif(cantidad<self.saldo) and((self.saldo-cantidad)>self.negativo):
            #Si la cantidad a retirar es menor que el saldo que tiene la cuenta,se puede retirar sin problema,
            #siempre que no se supere el saldo negativo limite;Por lo tanto se pude transferir dinero sin problema.
            
            self.saldo=self.saldo-cantidad
            cuenta.saldo=cuenta.saldo+cantidad

        else:
            #Esta opcion solo se ejecuta cuando la cantidad a retirar es mayor que el saldo de la cuenta y el limite negativo
            #maximo se supera y por lo tanto la transferencia no puede realizarse.
            print("No puedes realizar la tranferencia")

#Actua
       
