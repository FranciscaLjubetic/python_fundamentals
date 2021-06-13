class User:
    def __init__(self, name, email):
        self.nombre = name
        self.correo = email
        self.accountbalance = 0

    def make_deposit(self, amount):
        self.accountbalance += amount
        print (f"'Su deposito por'+{amount}+'pesos, ha sido cargado exitosamente a su cuenta. Su nuevo saldo es '+{self.accountbalance}+'pesos.'")

    def make_withdrawal(self, cash):
        self.accountbalance -= cash
        if cash > self.accountbalance:
            print (f"Este giro ha sido cargado a su línea de sobregiro.")
        else:
            print(f"{self.nombre}+', su giro por'+{cash}+'pesos, ha resultado exitoso. Su nuevo saldo es '+{self.accountbalance}+'pesos.'")

    def display_user_balance(self):
        print(f"{self.nombre}+'tiene en su cuenta'+{self.accountbalance}+'pesos.'")

    def transfer_money(self, otheruser, trans):
        self.accountbalance -= trans
        otheruser.accountbalance += trans
        if trans > self.accountbalance:
            print (f"Esta transferencia ha hecho uso de su línea de sobregiro.")
        else:
            print(f"{self.nombre}+'ha transferido'+{trans}+'pesos, a'+{otheruser}")

Pedro = User('Pedro', 'chino@gmail.com')
Juan = User('Juan', 'hjhh@gmail.com')

Pedro.make_deposit(200)

Pedro.make_withdrawal(500)

Soyla = User('Soyla', 'xoromiyultakesae@hotmail.com')

Soyla.make_deposit(2000)
Soyla.transfer_money(Soyla, Pedro, 1000)

