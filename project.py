import colorama
from colorama import Fore, Back, Style
import time
from datetime import datetime

# Autoreset the Background.
colorama.init(autoreset=True)


class Expense:
    """Initialize Expense object

        Attributes:
        category (str): Category of the expense.
        amount (str): Cost of the expense in CAD.
        overview (str): A summary of the expense.
        date (str): Date and time of the expense in the format '%Y/%m/%d %H:%M:%S'."""
    
    def __init__(self, category, amount, overview):
        self.category = category
        self.amount = amount
        self.overview = overview
        self.date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


class ExpenseManager:
    """Initialize an ExpenseManager object"""
    def __init__(self):
        self.expanseList = []


    """Add an expense to the manager
    
        Args:
            category: Category of the expense
            amount:   Cost of the expense
            overview: A summary of the expense.
            
        Methods:
        add_expense(category, amount, overview): Add an expense to the manager.
        update_expense(category_to_update, choice, new_value): Update expenses if necessary.
        view_by_category(category): View expenses based on category.
        view_all_expenses(): View all expenses.
        delete_expense(category_to_remove): Delete a certain expense."""
    
    def add_expense(self, category, amount, overview):
        valid_categories = ["Entertainment", "Shopping", "Education", "Food & Drinks", "Home & Utility", "Family", "Health & Wellbeing", "Travel"]
        if category not in valid_categories:
            raise ValueError(f"Invalid category: {category}. Please choose a valid category.")
        expense = Expense(category, amount, overview)
        self.expanseList.append(expense)

    """Update the expenses if necessary
    
        Args:
            category_to_update: Takes the category that user want to update
            choice:             The type of information to update (1. Category, 2. Amount, 3. Overview)
            new_value:          Updated value of the choosen information."""
    
    def update_expense(self, category_to_update, choice, new_value):
        while True:
            # The flag is set to false
            category_found = False
            for expense in self.expanseList:
                if expense.category == category_to_update:
                    # After finding the category the flag value will be changed to True
                    category_found = True
                    if choice == 1:
                        expense.category = new_value
                    elif choice == 2:
                        expense.amount = new_value
                    elif choice == 3:
                        expense.overview = new_value
                    else: # Any value other than (1-3)
                        print(f"Invalid choice: {choice}. Please enter a valid choice.")
            # If the user enter unknown category        
            if not category_found:
                raise AssertionError
            else:
                break

    """User can view expenses based on category

        Args:
            category: Category of the expense to view"""
    
    def view_by_category(self, category):
        print(
            f'\n{"Category":^15}{"Amount(CAD)":^15}{"Dates":^20}{"Overview":^35}'
        )
        print("-" * 90)
        for expense in self.expanseList:
            if expense.category == category:
                print(
                    f"{Fore.BLACK}{Back.YELLOW}{Style.BRIGHT}{expense.category:^15}{str(expense.amount):^12}{expense.date:^28}{expense.overview:^50}"
                )

    """User also have the option to view all category at once"""

    def view_all_expenses(self):
        print(
            f'{Fore.YELLOW}{Style.BRIGHT}\n{"Category":^15}{"Amount(CAD)":^15}{"Dates":^24}{"Overview":^39}'
        )
        print("-" * 120)
        for expense in self.expanseList:
            print(
                f"{Fore.BLACK}{Back.YELLOW}{Style.BRIGHT}{expense.category:^15}{str(expense.amount):^12}{expense.date:^28}{expense.overview:^50}"
            )
            print()

    """User can delete a certain expense.

        Args:
            category_to_remove: Category of the expense to be deleted."""
    def delete_expense(self, category_to_remove):
        # Creates a list to store the deleted expense
        deleted_expenses = [expense for expense in self.expanseList if expense.category == category_to_remove]
        # Removes the desired deleted expense from the self.expenseList 
        self.expanseList = [expense for expense in self.expanseList if expense.category != category_to_remove]
        return deleted_expenses
        

def menu():
    """Instance of ExpenseManager class."""
    expense_manager = ExpenseManager()

    while True:
        title = f"MENU"
        subtitle = (
            f"--------------------------------------------------------------------"
        )
        print(f"{Fore.MAGENTA}{Style.BRIGHT} {title:>34}")
        print(f"{Fore.CYAN}{Style.BRIGHT} {subtitle:>37}")
        menu_option = int(input(
            Fore.LIGHTBLUE_EX
            + Style.BRIGHT
            + "\nIf you want to\n1.Add\n2.Update\n3.View\n4.Delete?\nPress 0 to exit. "
        ))
        time.sleep(1)
        if menu_option == 0:
            break

        if menu_option == 1:
            print()
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Choose your preferred category")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "1.Entertainment")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "2.Shopping")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "3.Food & Drinks")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "4.Home & Utility")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "5.Family")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "6.Health & Wellbeing")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "7.Travel")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "8.Education")
            category = input(
                Fore.LIGHTCYAN_EX
                + Style.BRIGHT
                + "Enter the corresponding category: "
            )
            amount = input(
                Fore.LIGHTWHITE_EX + Style.BRIGHT + "\nEnter Amount(CAD): "
            )
            overview = input(
                Fore.LIGHTWHITE_EX + Style.BRIGHT + "Enter Overview: "
            )
            expense_manager.add_expense(category, amount, overview)
            time.sleep(1)

        if menu_option == 2:
            category_to_update = input(
                Fore.GREEN
                + Style.BRIGHT
                + "Enter the category to update: " 
            )
            choice = int(
                input(
                    Fore.LIGHTGREEN_EX
                    + Style.BRIGHT
                    + "Enter the number to update (1. Category, 2. Amount(CAD), 3. Overview): "
                )
            )
            time.sleep(2)
            new_value = input(
                Fore.LIGHTGREEN_EX
                + Style.BRIGHT
                + "Enter the new value: "
            )
            expense_manager.update_expense(
                category_to_update, choice, new_value
            )
            time.sleep(1)

        if menu_option == 3:
            view_option = input(
                Fore.YELLOW + Style.BRIGHT + "Do you want to view all(v) or category wise(c)? "
            )
            # To view all items
            if view_option.lower() == "v":
                expense_manager.view_all_expenses()
                time.sleep(8)
            # Views the items by category
            elif view_option.lower() == "c":
                category = input(
                    Fore.LIGHTCYAN_EX
                    + Style.BRIGHT
                    + "\nEnter your preferred category(name): "
                )
                expense_manager.view_by_category(category)
                time.sleep(8)

        if menu_option == 4:
            category_to_remove = input(
                Fore.LIGHTRED_EX
                + Style.BRIGHT
                + "Enter the category to be removed: "
            )
            expense_manager.delete_expense(category_to_remove)
            time.sleep(1)
        if int(menu_option) > 5 or int(menu_option) < 0:
            print(
                Fore.RED + Style.NORMAL + "Invalid option. Please choose a number between 1 and 4."
            )

        time.sleep(1)

if __name__ == "__main__":
    menu()
