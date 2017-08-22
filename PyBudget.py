import sys

class Application:
    def __init__(self):
        """Initializes the program along with the entries variable."""

        self.entries = []
        self.main()

    def main(self):
        """Asks the user what kind of item they would like to add to the analysis,
        when the user is done, the calculate function is called."""

        budget_item = input('Add Income or Expense(enter f to finish)? [-/+]: ')
        if budget_item =='+':
            self.prompt('income')
        elif budget_item =='-':
            self.prompt('expense')
        else:
            self.calculate()

    def prompt(self, item_type):
        """Asks for user input depending on the item_type (Income or Expense), until
        the user is done entering items."""

        while True:
            value = int(input('Enter %s amount (numbers only): ' % item_type))
            label = input('Enter %s name: ' % item_type)
            self.entries.append({
                'value': value if item_type == 'income' else -value,
                'label': label
            })
            more = input('Enter %s? [y/n]: ' % item_type)
            if more == 'n':
                break
        self.main()

    def calculate(self):
        """Takes all values in self.entries and calculates the sum, displays
        the appropriate response in relation to the sum. Either calls the
        reset function or the close program function depending on user input."""

        balance = sum(entry['value'] for entry in self.entries)
        if balance < 0:
            print('\nYou are in the negative, you have a deficit of: ' + '$' + str(balance))
        if balance == 0:
            print('\nYou have broken even, you are spending exactly as much as you make.')
        if balance> 0:
            print('\nYou are in the positive, you have a surplus of ' + '$' + str(balance))
        another = input('\nWould you like to run another analysis? [y/n]: ')
        if another == 'y':
            self.reset_program()
        else:
            self.close_program()

    def reset_program(self):
        """Clears self.entries and calls self.main()"""

        del self.entries[0:]
        self.main()

    def close_program(self):
        """Exits the program."""

        print('\nExiting Program.')
        sys.exit(0)


if __name__ == '__main__':
    Application()
