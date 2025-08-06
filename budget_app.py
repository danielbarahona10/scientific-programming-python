class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        lines = []
        izq = int((30 - len(self.name))/2)
        der = 30 - len(self.name) - izq
        lines.append(f"{'*'*izq}{self.name}{'*'*der}")
        for o in self.ledger:
            spaces = ' '*max(0,23 - len(o['description']))
            amount = "{:.2f}".format(o['amount'])
            lines.append(f"{o['description'][:23]}{spaces}{' '*(7-len(str(amount)))}{amount}")
        lines.append(f"Total: {self.get_balance()}")
        return "\n".join(lines)

    def deposit(self, amount, description=""):
        deposit_object = {}
        deposit_object['amount'] = amount
        deposit_object['description'] = description
        self.ledger.append(deposit_object)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        withdraw_object = {}
        withdraw_object['amount'] = -amount
        withdraw_object['description'] = description
        self.ledger.append(withdraw_object)
        return True

    def get_balance(self):
        balance = 0
        for o in self.ledger:
            balance += o['amount']
        return balance

    def transfer(self, amount, destination_budget_category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {destination_budget_category.name}')
        destination_budget_category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    lines = []
    withdrawals = []
    for category in categories:
        for o in category.ledger:
            if o['amount'] < 0:
                withdrawals.append(-o['amount'])
    category_percentage = 50
    lines.append(f'Percentage spent by category')
    for n in range(10,-1,-1):
        label = str(n*10) 
        line = ' '*(3-len(label)) + label + '| '
        for withdrawal in withdrawals:
            o_category = 'o' if (withdrawal/sum(withdrawals)*100) >= n*10 else ' '
            line += o_category + '  '
        lines.append(f"{line}")
    lines.append(' '*4 + '-'*3*len(categories) + '-')
    max_len = max(len(category.name) for category in categories)
    categories_names = []
    for category in categories:
         categories_names.append(category.name)
    for i in range(len(categories_names)):
        categories_names[i] = categories_names[i] + ' '*(max_len-len(categories_names[i]))
    for l in range(max_len):
        line = ' '*5
        for category_name in categories_names:
            line += category_name[l] + '  '
        lines.append(f"{line}")
    return "\n".join(lines)


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
# print(food)

auto = Category('Auto')

categories = [food, clothing, auto]
print(create_spend_chart(categories))