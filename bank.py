# bank management system - python 

d = {}

class bank:
    def create(self):
        pass
    def withdrow(self):
        pass
    def deposite(self):
        pass
    
obj = bank()

while True:
    menu = """
        1) create account
        2) withdrow account
        3) deposite account
        4) exit
    """
    print(menu)
    
    choice = int(input("Enter your choice :"))
    if choice == 1:
        obj.create()
    elif choice == 2:
        obj.withdrow()
    elif choice == 3:
        obj.deposite()
    else:
        print("Thank you")