# Mutable Functions
def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(100)
withdraw(25)
withdraw(25)
withdraw(60)
withdraw(15)

# Mutable Functions without nonlocal
def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

withdraw = make_withdraw_list(100)
withdraw(25)

# Multiple Accounts
stan = make_withdraw(100)
kevin = make_withdraw(10000000)
stan(10) # Stan gets McDonalds
kevin(1000) # Kevin treats the 61A staff to dinner
stan(2000) # Stan wants to build a PC
kevin(2000) # Kevin lends Stan money
