# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("-" * 87)
    print("Welcome to the bank. Please provide the following information for your savings account: ")
    print("-" * 87)
    savings_balance = float(input("Savings Account Balance: "))
    savings_interest= float(input("Savings Account Interest Rate: "))
    savings_maturity = int(input("Savings Account Maturity (Months): "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated savings account balance is ${updated_savings_balance:,.2f}, and your interest earned is ${interest_earned:,.2f}.")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("-" * 67)
    print("Next, please provide the following information for your CD account: ")
    print("-" * 67)
    cd_balance = float(input("CD Account Balance: "))
    cd_interest= float(input("CD Account Interest Rate: "))
    cd_maturity = int(input("CD Account Maturity (Months): "))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated CD account balance is ${updated_cd_balance:,.2f}, and your interest earned is ${interest_earned:,.2f}.")
if __name__ == "__main__":
    # Call the main function.
    main()
