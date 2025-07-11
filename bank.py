# bank management system - python 

d = {}

class bank:
    def create(self,index):
        name = input("enter name :")
        balance = int(input("enter balance :"))
        
        d[index] = {"Name":name,"balance":balance}
        print("ACCOUNT CREATE SUCCESSFULLY")
        print("your account number is :",index)
        
    def withdrow(self):
        acc_no = int(input("enter account no. :"))
        for i,j in d.items():
            if i == acc_no:
                for k,v in j.items():
                    if k == "balance":
                        amount = int(input("Enter amount to withdrow"))
                        a = v - amount
                        d[acc_no] = {"balance":a}
                        print("your current balance :",a)
        
    def deposite(self):
        acc_no = int(input("enter account no. :"))
        for i,j in d.items():
            if i == acc_no:
                for k,v in j.items():
                    if k == "balance":
                        amount = int(input("Enter amount to deposite"))
                        a = v + amount
                        d[acc_no] = {"balance":a}
                        print("your current balance :",a)
                        
    def view(self):
        for i,j in d.items():
            print("account nomber :", i)
            for k,v in j.items():
                print(k,":",v)
            print("-----------------")
    
obj = bank()
index = 1

while True:
    menu = """
        1) create account
        2) withdrow account
        3) deposite account
        4) view account
        5) exit
    """
    print(menu)
    
    choice = int(input("Enter your choice :"))
    if choice == 1:
        try:
            obj.create(index)
            index+=1
        except:
            print("some error")
    elif choice == 2:
        obj.withdrow()
    elif choice == 3:
        obj.deposite()
    elif choice == 4:
        obj.view()
    else:
        print("Thank you")