#Expense Tracker - Installment 5: the menu comes alive
#Author: King Arthur R. Ambo
#Description: interactive expense tracker that allows user to record expenses, calculate the subtotal, tax, and grand total, and evaluate their budget status while displayting the exact remaining or exess amount.

# --- header ---

print("="* 40)
print("\t    EXPENSE TRACKER")
print("       Know where your money goes.")
print("="* 40)

# --- variable initialization ---

subtotal = 0
count = 0
amount1 = 0
amount2 = 0
tax_percent = 0
budget = 0

# --- user input module 0: Name, Tax Rate, and Budget ---

name = input("\nWhat is your name? ")
tax_percent = int(input("Tax rate? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}! ")

# --- text main menu ---

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t")
print("\t[4] Exit\t\t\t")

#--- option module: for menu selection ---

while True:
    option = (input("Choose 1-4: "))

# --- option module 1: Add an expense ---

    if option == "1":

        # --- user input module 1: for expenses and amounts ---

        amount1 =float(input("Amount? "))
        count += 1

        # --- decision making Module 0:  for expense amount ---

        if amount1 > 200: 
            print("Huge expense - are you sure?")
        elif amount1 >= 100:
            print("Big expense.")
        elif amount1 >= 50:
            print("Moderate expense.")
        else:
            print("Small expense.")

        # --- user input module 2: for expenses and amounts ---

        amount2 = float(input("Amount? "))
        count += 1

        # --- decision making Module 1: for expense amount ---

        if amount2 > 200: 
            print("Huge expense - are you sure?")
        elif amount2 >= 100:
            print("Big expense.")
        elif amount2 >= 50:
            print("Moderate expense.")
        else:
            print("Small expense.")

        # --- Data processing ---   

        subtotal = amount1 + amount2

        # --- decision making Module 3: for subtotal ---
        if subtotal > 100: 
            print("Two big expenses in a row - slow down!")

# --- option module 2: View all expenses (coming soon) ---

    elif option == "2":
                print("Coming soon: the tracker can't remember each item yet!")

# --- option module 3: Show total spent ---

    elif option == "3":
        # --- Data processing ---

        average = subtotal / 2
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total

        # --- summary ---

        print(f"Expenses: \t\t\t\t{count:.2f}")
        print(f"Subtotal: \t\t\t\t${subtotal:.2f}")
        print(f"Average: \t\t\t\t${average:.2f}") 
        print(f"Tax({tax_percent}%): \t\t\t\t${tax:.2f}")
        print(f"Grand Total: \t\t\t\t${total:.2f}")

        # --- Decision making Module 4: for budget ---

        if total > budget:
            print(f"Over Budget: by \t\t\t${total - budget:.2f}")
        elif total >= (0.9 * budget):
            print(f"Careful: only \t\t\t\t${left:.2f}")
        else: 
            print(f"Within Budget \t\t\t\t${left:.2f}") 

# --- option module 4: Exit ---    
    elif option == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: King Arthur R. Ambo | Installment 5")
        print("=" * 40)
        exit()
    else:
    ## --- invalid option  ---
        print("Please choose 1, 2, 3, or 4.")