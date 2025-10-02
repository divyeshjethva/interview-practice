
def fun(my):
    def sub():
        print('First')
        my()
        print('Second')
    return sub
    
@fun
def my():
    print("Hello")

my()
