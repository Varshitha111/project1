class user:
    name=""
    def show_user(self):
        pass
    
class wallet:
    balance=0
    def show_balance(self):
        pass
class PaymentAPP(user,wallet):
    app_name=""
    def show_details(self):
        pass
obj=PaymentAPP()
obj.show_details()