class BankAccount:
    def __init__(self,name,password,balance):
        self.name = name
        self.password = password
        self.balance = balance
    
    def deposit(self,amount,password):
        if password != self.password:
            return "Wrong Credentials Try Again"
        
        if amount <= 0:
            return "Can't take in this value"
        
        self.balance += amount
        
    def withdraw(self,amount,password):
        if password != self.password:
            return "Wrong Credentials Try Again"
        
        if amount <= 0:
            return "Can't withdraw this value"
        
        self.balance -= amount
        return f"{amount} withdrawn. Current Balance {self.balance}"
    
    def showAccount(self,password):
        if password != self.password:
            return "Wrong Credentials Try Again"
        return(f"""
                Name:{self.name}
                Balance:{self.balance}
                Password:{self.password}
              """)
    def changepwd(self,password,new_password):
        if password != self.password:
            return "Wrong Credentials Try Again"
        self.password = new_password
        return "Password changed!"
    


didi = BankAccount("David","23jumpy",100)
didi.deposit(200,"23jumpy")
print(didi.showAccount("23jumpy"))
