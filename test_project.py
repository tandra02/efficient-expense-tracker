from project import ExpenseManager
import pytest
def main():
    test_add_expense()
    test_update_expanse()
    test_view_all_expanse()
    test_view_by_category()
    test_delete_expanse()

def test_add_expense():
    # Create an instance of ExpenseManager
    expense_manager = ExpenseManager()
    expense_manager.add_expense("Entertainment", "$900", "went to disney world, had a blast.")
    assert len(expense_manager.expanseList) == 1
    expense_manager.add_expense("Shopping", "$90.85", "bought my mom a gold ear ring and bangals")
    assert len(expense_manager.expanseList) == 2
    expense_manager.add_expense("Education", "$31,416", "paid all the tution fees and im free of debt")
    assert len(expense_manager.expanseList) == 3
    # Adding an invalid expense (should raise a ValueError)
    with pytest.raises(ValueError, match="Invalid category: Crops. Please choose a valid category."):
        expense_manager.add_expense("Crops", "$100", "bought seeds")

def test_update_expanse():
    expense_manager = ExpenseManager()
    # Add information to the ExpanseManager
    expense_manager.add_expense("Travel", "$275", "cost of villa in philipines.")
    # Update the information
    expense_manager.update_expense("Travel", 3, "food and drinks and living cost for 3 days.")
    # # Retrieve the updated expense from the ExpenseManager
    update_expanse = expense_manager.expanseList[0]
    assert update_expanse.overview == "food and drinks and living cost for 3 days."
    expense_manager.add_expense("Family","$12,677", "Buying everyone something from my first earnings.")
    expense_manager.update_expense("Family",2, "$70,455") #( category_to_update, choice, new_value)
    update_expanse = expense_manager.expanseList[1]
    assert update_expanse.amount == "$70,455"
    
    # Adding an invalid choice(should raise a AssertionError)
    with pytest.raises(AssertionError):
        expense_manager.update_expense("Emergency", 2, "$275")
    
def test_view_all_expanse():
    expense_manager = ExpenseManager()
    expense_manager.add_expense("Health & Wellbeing","$14,987","Dental cost")
    expense_manager.view_all_expenses()

def test_view_by_category():
    expense_manager = ExpenseManager()
    expense_manager.add_expense("Health & Wellbeing","$14,987","Dental cost")
    expense_manager.view_by_category("Health & Wellbeing")

def test_delete_expanse():
    expense_manager = ExpenseManager()
    expense_manager.add_expense("Travel","$275","cost of something")
    expense_manager.delete_expense("Travel")

if __name__ == "__main__":
    main()
