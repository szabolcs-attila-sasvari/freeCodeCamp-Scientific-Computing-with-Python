# Define the commonly used symbols as global variables
space_char = ' '
minus_char = '-'
o_char = 'o'
star_char = '*'


# Category class
class Category:
    def __init__(self, given_type):
        self.ledger = []
        self.balance = 0
        self.type = given_type

    def __str__(self):
        one_side_stars = int((30 - len(self.type)) / 2)
        total_amount = 0
        printing = f"{star_char * one_side_stars}{self.type}{star_char * one_side_stars}\n"
        for item in self.ledger:
            current_amount = f"{item['amount']:.2f}"
            if 23 < len(item['description']):
                printing += f"{item['description'][0:23]}{space_char * int(30 - len(item['description'][0:23]) - len(current_amount))}{item['amount']:.2f}\n"
            else:
                printing += f"{item['description']}{space_char * int(30 - len(item['description']) - len(current_amount))}{item['amount']:.2f}\n"
            total_amount += item['amount']
        printing += f"Total: {total_amount}"
        return printing

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": float(-amount), "description": description})
            self.balance += -amount
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, obj):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {obj.type}")
            obj.deposit(amount, f"Transfer from {self.type}")
            return True

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True


# Create spend chart function
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    withdraws = []
    percentages = []
    total_amount_of_withdraws = 0

    for i in range(0, len(categories)):
        current_amount = 0
        for item in categories[i].ledger:
            if item["amount"] < 0:
                current_amount += abs(item["amount"])
        withdraws.append(current_amount)
        total_amount_of_withdraws += current_amount

    for i in range(0, len(withdraws)):
        current_percentage = int(f"{(withdraws[i] / total_amount_of_withdraws) * 100:.0f}") - (int(f"{(withdraws[i] / total_amount_of_withdraws) * 100:.0f}") % 10)
        percentages.append(current_percentage)

    for i in range(100, -10, -10):
        chart += f"{space_char * (len(str(100)) - len(str(i)))}{i}| "
        for j in range(0, len(percentages)):
            if i <= percentages[j]:
                chart += f"{o_char}  "
            else:
                chart += f"{space_char * 3}"
        chart += '\n'
    chart += f"{space_char * 4}{minus_char * (len(categories) * 3 + 1)}\n"

    longest_category = 0
    for i in range(0, len(categories)):
        if longest_category <= len(categories[i].type):
            longest_category = len(categories[i].type)

    for i in range(0, longest_category):
        for j in range(0, len(categories)):
            if i < len(categories[j].type):
                if j == 0:
                    chart += f"{space_char * 5}{categories[j].type[i]}{space_char * 2}"
                else:
                    chart += f"{categories[j].type[i]}{space_char * 2}"
            else:
                if j == 0:
                    chart += f"{space_char * 5}{space_char * 3}"
                else:
                    chart += f"{space_char * 3}"
        if i != longest_category - 1:
            chart += '\n'
            
    return chart
