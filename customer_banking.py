# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

def is_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False
    
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input("\n Enter the saving account balance: ")

    savings_interest = input("\n Enter the saving interest rate: ")

    savings_maturity = input("\n Enter the maturity period: ")

    if is_float(savings_balance) and is_float(savings_interest) and savings_maturity.isdigit():
        # Call the create_savings_account function and pass the variables from the user.
        updated_savings_balance, interest_earned = create_savings_account(float(savings_balance), float(savings_interest), int(savings_maturity))

        # Print out the interest earned and updated savings account balance with interest earned for the given months.
        # ADD YOUR CODE HERE
        print(f"\n Your total balance ${ format(updated_savings_balance,',.2f') } and interest earn will be ${ format(interest_earned,',.2f') } ")
    else:
        print("\n Error Invalid input. Please try again")
             

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("\n Enter the CD account balance: ")

    cd_interest = input("\n Enter the CD interest rate: ")

    cd_maturity = input("\n Enter the maturity period: ")


    if is_float(cd_balance) and is_float(cd_interest) and cd_maturity.isdigit():
        # Call the create_cd_account function and pass the variables from the user.
        updated_cd_balance, interest_earned_cd = create_cd_account(float(cd_balance), float(cd_interest), int(cd_maturity))

        # Print out the interest earned and updated CD account balance with interest earned for the given months.
        # ADD YOUR CODE HERE
        print(f"\n Your total balance ${ format(updated_cd_balance,',.2f') } and interest earn will be ${ format(interest_earned_cd,',.2f') }")
    else:
        print("\n Error Invalid input")

if __name__ == "__main__":
    # Call the main function.
    main()

