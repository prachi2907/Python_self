class atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        print(id(self))
        self.menu()

    def menu():
        user_input = input('''
                         Which Operration do you like to perform:
                           1.Enter 1 to create pin
                           2.Enter 2 to deposite 
                           3.Enter 3 to withdraw
                           4.Enter 4 to check balance
                           5.Enter 5 to Exit       ''')   
        if user_input=="1":
            print("pin created") 
        
 