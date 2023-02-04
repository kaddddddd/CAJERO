class Cajerito:
    money=350000
    
    def inicio(self):
      password=12345
      print("=========================================")
      nombre=input("Ingrese su nombre: ")
      p=int(input("Ingrese su contraseña: "))
      if p==password:
        print("Accediendo...")
      else:
        print("Error, inténtalo otra vez")
        p=int(input("Ingrese su contraseña: "))
      if p==password:
        print("Accediendo...")
      else:
        print("Error, tienes una útlima oportunidad, inténtalo otra vez")  
        p=int(input("Ingrese su contraseña: "))
      if p==password:
        print("Accediendo...")
      else:
        print("Tú tarjeta ha sido bloqueada")
        print("=========================================") 
        self.inicio()
        
      
    
    def numeritos(self):
        self.number = int(input("""
        =============================================
        "BIENVENIDO A CAJERITO RAYO MCQUEEN"
        Digite el número de lo que desea hacer...
        1. Verificar dinero
        2. Retirar dinero
        3. Depositar saldo
        4. Solicitar avance
        5. Dona para mejorar nuestro servicio
        6. Salir
        ============================================="""))
        self.cajero=0
        while self.cajero==0:
            if self.number==1:
                self.verificar()
            elif self.number==2:
                self.retiradita()
            elif self.number==3:
                self.depositar()
            elif self.number==4:
                self.avance()  
            elif self.number==5:
                self.donar()    
            elif self.number==6:  
                self.cajero=1
                self.salir()
            else:
                print("No existe :( inténtalo de nuevo")
                self.numeritos()

    def verificar(self):
        print("Tienes disponible $", self.money)
        self.numeritos()

    def retiradita(self):
        self.retiradita = int(input("¿Qué cantidad de dinero desea retirar de su cuenta?"))
        while self.cajero==0:
            if self.retiradita > self.money:
                print("Lo siento, no tienes el suficiente dinero para retirar ¡Inténtalo otra vez!")
                self.retiradita = int(input("¿Qué cantidad de dinero desea retirar de su cuenta?"))
            elif self.retiradita<= self.money:
                self.money=self.money-self.retiradita
                self.verificar()    

    def depositar(self):
        self.deposito = int(input("¿Qué cantidad de dinero desea depositar a su cuenta?"))
        print("Confirmanos...")
        confirmar=int(input("""¿Estás seguro de depositar esa cantidad de dinero?"
                                 1. Sí
                                 2. No
                                 3. Cancelar """))
        if (confirmar==1):
          self.money=self.money + self.deposito
          print("Deposito exitoso")
          print("Acabas de depositar $", self.deposito, " a tu cuenta")
        elif (confirmar==2):
          self.money=self.money - self.deposito
          print("Deposito cancelado") 
        else:
          print("BYE")
          self.verificar()
          
    def avance(self):
      self.avance = int(input("Préstamo rápido ¿Qué cantidad necesitas?"))
      self.money = self.money + self.avance
      recibito=int(input("""¿Estás seguro de gastar papel imprimiendo tu recibo?"
                                 1. Sí
                                 2. No
                                 """))
      if recibito == 1:
        print("Recibo impreso :/")
      elif recibito == 2:
        print("Saliendo...")
      else:
        print("Solo se acepta el 1 o 2") 
      self.verificar()

    def donar(self):
      self.donar = int(input("¿Cuánto desea donar a 'Cajerito Rayo MCQueen' para que mejore su servicio?"))
      while self.cajero==0:
        if self.donar > self.money:
          print("Lo siento, no tienes el suficiente dinero para donar ¡Inténtalo otra vez!")
          self.donar = int(input("Cuánto desea donar a 'Cajerito Rayo MCQueen para que mejore su servicio?"))
        elif self.donar<= self.money:
            self.money=self.money-self.donar
            self.verificar()

      

    def salir(self):
        print("Muchas gracias por preferirnos, nos vemos luego :)")
        

dinerito = Cajerito()
dinerito.inicio()
dinerito.numeritos()
