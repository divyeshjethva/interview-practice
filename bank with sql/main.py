# bank management system - with sql database
from connection import *

d = {}

class bank:
    def create(self):
        name = input("enter name :")
        balance = int(input("enter balance :"))
        
        cursor.execute(f"insert into users (name,balance) values ('{name}',{balance})")
        connection.commit()
        
        cursor.execute(f"select id from where name={name}")
        b = cursor.fetchone()
        
        print("ACCOUNT CREATE SUCCESSFULLY")
        print("your account number is :",b)
        
    def withdrow(self):
        acc_no = int(input("enter account no. :"))
        cursor.execute(f"select * from users where id={acc_no}")
        b = cursor.fetchone()
        connection.commit()
        
        if b:
            amount = int(input("Enter amount"))
            print(b[0])
            print(b[1])
            c = b[2] - amount
            cursor.execute(f"update users set balance={c} where id={acc_no}")
            connection.commit()
            print("your current amount",c)
        else:
            print("user not found")
        connection.commit()
        
        # for i,j in d.items():
        #     if i == acc_no:
        #         for k,v in j.items():
        #             if k == "balance":
        #                 amount = int(input("Enter amount to withdrow"))
        #                 a = v - amount
        #                 d[acc_no] = {"balance":a}
        #                 print("your current balance :",a)
        
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
            obj.create()
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